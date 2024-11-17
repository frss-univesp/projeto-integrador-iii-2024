import random
import pymongo
import datetime
from faker import Faker

client = pymongo.MongoClient(r"mongodb+srv://secret:secret@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["proj_integrador_ii"]
collection = db["perm_trabalho"]

fake = Faker()

def generate_random_date():
    current_year = datetime.datetime.now().year
    start_date = datetime.datetime(current_year, 1, 1)
    end_date = datetime.datetime(current_year, 12, 31)
    return fake.date_time_between(start_date=start_date, end_date=end_date)

def get_next_id():
    qt_docs = collection.count_documents({})

    if qt_docs > 0:

        result = collection.aggregate([
            {'$group': {'_id': None, 'max_value': {'$max': '$_id'}}}
        ])
        max_value = int(result.next()['max_value'])

    else:
        max_value = 0

    return max_value

def generate_document(id):
    locais = [
        "Caldeira", "Torre de Destilação", "Forno", "Trocador de Calor",
        "Tanque de Armazenamento", "Compressor", "Casa de Máquinas"
    ]
    
    descr_ativ = [
        "Pintura", "Soldagem", "Lixamento", "Inspeção", "Desativação", "Limpeza"
    ]
    
    dt_execucao = generate_random_date()
    dt_conclusao = generate_random_date()
    while dt_conclusao > dt_execucao:
        dt_conclusao = generate_random_date()
    
    document = {
        "_id": id,
        "local": random.choice(locais),
        "dt_execucao": dt_execucao.isoformat(),
        "dt_conclusao": dt_conclusao.isoformat(),
        "dt_prorrog": "",
        "descr_ativ": random.choice(descr_ativ),
        "nm_solicte": "FRSS",
        "area_solicte": "Destilação",
        "ferram_utilz": "Outros",
        "doc_ctrl_risc": "Outros",
        "apontamento": "",
    }
    
    for i in range(1, 20):
        document[f"chk_item{i}"] = random.choice([True, False])
    
    for i in range(13, 20):
        document[f"form_ctrl_{i}"] = ""
    
    document.update({
        "med_adic_ctrl": "",
        "epi_1": "",
        "epi_2": "",
        "epi_3": "",
        "epi_4": "",
        "epi_5": "",
        "outros_epi": "",
        "epc_1": "",
        "epc_2": "",
        "epc_3": "",
        "epc_4": "",
        "epc_5": "",
        "outros_epc": "",
        "nm_aprovador": None,
        "cargo_aprovador": None,
        "dt_aprovacao": None,
        "nm_exec_1": None,
        "cargo_exec_1": None,
        "nm_exec_2": None,
        "cargo_exec_2": None,
        "nm_exec_3": None,
        "cargo_exec_3": None
    })
    
    return document

def insert_documents():
    documents = []

    new_id = get_next_id()
    
    for x in range(1127):
        id = new_id + x + 1
        documents.append(generate_document(id))
    
    collection.insert_many(documents)
    print("Documentos inseridos com sucesso!")

insert_documents()

client.close()
