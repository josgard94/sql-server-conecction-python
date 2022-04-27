import pyodbc;

info = {
	'host':'localhost',
	'db':'barriauditorias',
	'user':'SA',
	'password':'Your-Password'
}

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+info['host']+';DATABASE='+info['db']+';UID='+info['user']+';PWD=' + info['password']);
    print("success")
    
except Exception as e:
    print("error", e)
