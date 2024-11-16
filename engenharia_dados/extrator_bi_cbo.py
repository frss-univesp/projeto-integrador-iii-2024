import pymongo
import pandas as pd

client = pymongo.MongoClient('mongodb+srv://pi2_writer:74ZMHoV9iSZtMrfr@cluster0.tz7tehv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['proj_integrador_ii']
collection = db['cbo']

cursor = collection.find({}, {"_id": 0})

data = list(cursor)
df_cbo = pd.DataFrame(data)
df_cbo
