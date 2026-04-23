# Lista instâncias e mostra qual está conectada
import pyodbc
import winreg

# ===== PARTE 1: winreg lê instâncias do PC =====
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Microsoft SQL Server")
instances, _ = winreg.QueryValueEx(key, "InstalledInstances")

print("\nINSTANCIAS INSTALADAS")
for instance in instances:
    print(instance)

# ===== PARTE 2: pyodbc conecta e mostra qual você usou =====
SERVIDOR_DGERD = "Vinicius\\MSSQLSERVER01" # ← VARIÁVEL SERVIDOR_DGERD, MUDE O NOME DO SERVIDOR

conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={SERVIDOR_DGERD};" # ← USA A VARIÁVEL, não escreve o nome
    "Database=master;"
    "Trusted_Connection=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT @@SERVERNAME AS InstanciaAtual")
    atual = cursor.fetchone()[0]
    print(f"\nINSTANCIA CONECTADA\n{atual}")
    conn.close()
except Exception as e:
    print(f"\nErro na conexão: {e}")