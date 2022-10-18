import pyodbc
from azure.appconfiguration import AzureAppConfigurationClient
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:userdetailsserver.database.windows.net'
database = 'userdetails'
username = 'userdts'
password = 'Balajibala@02'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
select_stmt = "SELECT * FROM userdetails"
db = cursor.execute(select_stmt)
rows=db.fetchall()

print(rows)