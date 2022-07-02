import pandas as pd
import sqlalchemy
database_username = 'root'
database_password = ''
database_ip       = 'localhost'
database_name     = 'madero'
database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password,
                                                      database_ip, database_name))

df = pd.read_csv('datos.csv', usecols=('codigo_postal', 'superficie_terreno', 'superficie_construccion', 'uso_construccion', 'valor_suelo', 'subsidio'))

df["valor_suelo"] = pd.to_numeric(df["valor_suelo"], errors='coerce')

df.to_sql(con=database_connection, name='terrenos', if_exists='replace')
