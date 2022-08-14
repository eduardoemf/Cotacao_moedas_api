import pyodbc
import pandas as pd

credenciais = pd.read_csv('credenciais//credenciais.txt', sep=";")

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = tcp:localhost,1433 # to login in linux ubuntu
server = 'tcp:localhost,1433'
database = 'db_projeto_cotacao_online'
username = credenciais['user'][0] 
password = credenciais['senha'][0]
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print('Conexão realizada com sucesso!')