
import pymongo
import pandas as pd

client = pymongo.MongoClient('mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['proj_integrador_ii']
collection = db['historico_acidente']

cursor = collection.find({}, {"_id": 0})

data = list(cursor)
df_historico_acidente = pd.DataFrame(data)
df_historico_acidente
