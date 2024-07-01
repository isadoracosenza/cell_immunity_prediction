import pandas as pd
from sqlalchemy import create_engine
import os

connection = create_engine('mysql+pymysql://root:euamobioinfo@localhost:3306/iedb')
assay_responses = [
    ('IL-4.csv', 'IL-4 release'),
    ('IL-18.csv', 'IL-18 release'),
    ('IL-10.csv', 'IL-10 release'),
    ('IL-12.csv', 'IL-12 release'),
    ('IL-13.csv', 'IL-13 release'),
    ('IL-15.csv', 'IL-15 release'),
    ('IL-16.csv', 'IL-16 release'),
    ('IL-17.csv', 'IL-17 release'),
    ('IL-17A.csv', 'IL-17A release'),
    ('IL-17F.csv', 'IL-1F release'),
    ('IL-18.csv', 'IL-18 release'),
    ('IL-1a.csv', 'IL-1A release'),
    ('IL-1b.csv', 'IL-1B release'),
    ('IL-2.csv', 'IL-2 release'),
    ('IL-21.csv', 'IL-21 release'),
    ('IL-22.csv', 'IL-22 release'),
    ('IL-23.csv', 'IL-23 release'),
    ('IL-25.csv', 'IL-25 release'),
    ('IL-27.csv', 'IL-27 release'),
    ('IL-3.csv', 'IL-3 release'),
    ('IL-4.csv', 'IL-4 release'),
    ('IL-5.csv', 'IL-5 release'),
    ('IL-6.csv', 'IL-6 release'),
    ('IL-7.csv', 'IL-7 release'),
    ('IL-8.csv', 'IL-8 release'),
    ('IL-9.csv', 'IL-9 release'),
    ('cytotoxicity.csv', 'cytotoxicity'),
    ('IFNa.csv', 'IFNa release'),
    ('IFNb.csv', 'IFNb release'),
    ('IFNg.csv', 'IFNg release'),
    ('TNFb.csv', 'lymphotoxin A/TNFb release'),
    ('TGFb.csv', 'TGFb release'),
    ('TNF.csv', 'TNF release'),
    ('TNFa.csv', 'TNFa release'),
    ('agglutination.csv', 'agglutination'),
    ('amphiregulin_release.csv', 'amphyregulin_release'),
]

for csv_file, assay_response in assay_responses:
    sql = f"""
        SELECT 
            object.mol1_seq AS sequence,
            assay_type.response AS response,
            tcell.as_char_value AS result,
            source.accession AS source_accession,
            source.database AS source_database
        FROM tcell 
        LEFT JOIN curated_epitope
            ON tcell.curated_epitope_id = curated_epitope.curated_epitope_id
        LEFT JOIN object
            ON curated_epitope.e_object_id = object.object_id
        LEFT JOIN assay_type
            ON tcell.as_type_id = assay_type.assay_type_id
        LEFT JOIN source
            ON source.source_id = object.mol1_source_id
        WHERE response = '{assay_response}';
        """

    df = pd.read_sql(sql, connection)
    df.to_csv(os.path.join('data', 'raw/', csv_file))
    print(f'arquivo {csv_file} criado com sucesso;')



# criar listas com os diferentes outcomes
# criar um for que cria um arquivo csv para cada outcome, consultando a database