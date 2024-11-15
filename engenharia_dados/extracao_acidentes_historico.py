import zipfile
import os
import requests
import pandas as pd
import re
import pymongo
import unicodedata
from pymongo import MongoClient

client = MongoClient('mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['proj_integrador_ii']
collection = db['historico_acidente']


def gerar_links(ano_inicial, mes_inicial, ano_final, mes_final):
    links = []    
    ano = ano_inicial
    mes = mes_inicial

    while (ano < ano_final) or (ano == ano_final and mes <= mes_final):
        mes_formatado = f"{mes:02}"
        link = f'https://armazenamento-dadosabertos.s3.sa-east-1.amazonaws.com/PDA_2023_2025/Grupos_de_dados/Comunica%C3%A7%C3%B5es+de+Acidente+de+Trabalho+%E2%80%93+CAT/D.SDA.PDA.005.CAT.{ano}{mes_formatado}.ZIP'
        links.append(link)
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1

    return links


def remover_acentos(texto):
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('ascii')


def json_serializer(obj):
    if isinstance(obj, pd.Timestamp):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, float) and (pd.isna(obj)):
        return None
    raise TypeError(f"Tipo {type(obj)} não serializável")


ano_inicial = 2023
mes_inicial = 6
ano_final = 2024
mes_final = 9

urls = gerar_links(ano_inicial, mes_inicial, ano_final, mes_final)

for url in urls:
    arquivo_zip = url.split("/")[-1]
    
    response = requests.get(url)
    with open(arquivo_zip, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall('dados_extraidos')

    arquivos_csv = [f for f in os.listdir('dados_extraidos') if f.upper().endswith('.CSV')]

    for file in arquivos_csv:
        file_path = os.path.join('dados_extraidos', file)

        try:
            df = pd.read_csv(file_path, header=0, encoding='latin1', sep=';', decimal=',')
            df = df[['Data Acidente',  'CBO', 'CID-10', 'CNAE2.0 Empregador',
                     'Indica Óbito Acidente', 'Sexo', 'Tipo do Acidente',
                     'UF Munic. Empregador', 'Data Nascimento']]

            df = df.loc[:, ~df.columns.str.contains('^unnamed', case=False)]
            df.columns = [remover_acentos(col).strip() for col in df.columns]
            df.columns = [re.sub(r'[^a-zA-Z0-9 ]', '', col) for col in df.columns]  
            df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            data_dicts = df.to_dict(orient='records')

            if data_dicts:
                collection.insert_many(data_dicts)
                print(f"{len(data_dicts)} documentos inseridos no database.")

            df = None
            data_dicts = None
            os.remove(file_path)
            print(f"Arquivo CSV {file} excluído com sucesso.")

        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {e}")

    os.remove(arquivo_zip)
    print(f"Arquivo ZIP {arquivo_zip} excluído com sucesso.")
