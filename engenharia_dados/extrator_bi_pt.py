import pandas as pd
from pymongo import MongoClient

def conectar_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def extrair_dados_mongodb(uri, db_name, collection_name):
    collection = conectar_mongodb(uri, db_name, collection_name)
    documentos = collection.find()
    lista_documentos = list(documentos)
    df = pd.DataFrame(lista_documentos)
    
    if '_id' in df.columns:
        df.drop('_id', axis=1, inplace=True)

    renomear_campos = {
        'local': 'Local de Execução',
        'dt_execucao': 'Data de Execução',
        'dt_conclusao': 'Data de Conclusão',
        'chk_item1': 'Queda de material ou trabalho em altura',
        'chk_item2': 'Movimentação de veículos',
        'chk_item3': 'Fogo ou explosivos',
        'chk_item4': 'Atmosfera explosiva',
        'chk_item5': 'Oxidantes',
        'chk_item6': 'Tóxicos ou infectantes',
        'chk_item7': 'Corrosivos',
        'chk_item8': 'Energias perigosas',
        'chk_item9': 'Asfixiantes',
        'chk_item10': 'Espaços confinados',
        'chk_item11': 'Içamento de cargas',
        'chk_item12': 'Escavação, perfuração e riscos estruturais',
        'chk_item13': 'Avaliação de impacto de atividades simultâneas',
        'chk_item14': 'Isolamento da área',
        'chk_item15': 'Isolamento dos dispositivos de segurança contra incêndio',
        'chk_item16': 'Preparação do equipamento (drenagem, purga)',
        'chk_item17': 'Remoção de materiais não essenciais para o trabalho',
        'chk_item18': 'Requerimentos de supervisão em caso de trabalho realizado por um trabalhador',
        'chk_item19': 'Requerimentos de emergência'
    }
    
    df = df[[col for col in renomear_campos.keys() if col in df.columns]]
    df.rename(columns=renomear_campos, inplace=True)

    return df

uri = "mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_name = "proj_integrador_ii"
collection_name = "perm_trabalho"

df = extrair_dados_mongodb(uri, db_name, collection_name)
df