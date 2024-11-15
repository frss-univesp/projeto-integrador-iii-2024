import pandas as pd
import pymongo
import os

client = pymongo.MongoClient('mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['proj_integrador_ii']
collection = db['cbo']

csv_file_path = r"C:\Users\francisr\dados_extraidos\CBO2002 - Ocupacao.csv"

if os.path.exists(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path, header=0, encoding='latin1', sep=';', decimal=',')        
        print(f"Arquivo CSV '{csv_file_path}' lido com sucesso!")
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

        data_dicts = df.to_dict(orient='records')

        if data_dicts:
            collection.insert_many(data_dicts)
            print(f"{len(data_dicts)} documentos inseridos no MongoDB com sucesso.")
        
        os.remove(csv_file_path)
        print(f"Arquivo CSV '{csv_file_path}' excluído com sucesso.")

    except Exception as e:
        print(f"Erro ao processar o arquivo CSV '{csv_file_path}': {e}")
else:
    print(f"Arquivo CSV '{csv_file_path}' não encontrado.")
