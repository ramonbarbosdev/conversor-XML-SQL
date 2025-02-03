import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=PM_MATASAOJOAO_CONTAB;"
    "UID=user;"
    "PWD=123;"
)

def obter_conexao():
    while True:
        try:
            conn = pyodbc.connect(connection_string, timeout=10)
            print("Conexão bem-sucedida!")
            return conn
        except pyodbc.Error as e:
            print(f"Erro ao conectar: {e}. Tentando novamente em 5 segundos...")
            time.sleep(5);
