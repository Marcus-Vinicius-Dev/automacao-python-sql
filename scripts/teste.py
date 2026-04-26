import winreg

print("=== TODOS PROGRAMAS INSTALADOS (COMPLETO) ===\n")

def listar_programas(reg_key, caminho):
    programas = []
    try:
        chave = winreg.OpenKey(reg_key, caminho)
        for i in range(500):
            try:
                subkey_name = winreg.EnumKey(chave, i)
                subchave = winreg.OpenKey(chave, subkey_name)
                try:
                    nome = winreg.QueryValueEx(subchave, "DisplayName")[0]
                    if nome and nome not in programas:
                        programas.append(nome)
                except:
                    pass
                winreg.CloseKey(subchave)
            except:
                break
        winreg.CloseKey(chave)
    except:
        pass
    return programas

# Lista de locais onde programas podem estar registrados
locais = [
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
]

todos_programas = []

for reg_key, caminho in locais:
    todos_programas.extend(listar_programas(reg_key, caminho))

# Remove duplicatas e ordena
todos_programas = sorted(set(todos_programas))

for p in todos_programas:
    print(f"📦 {p}")

print(f"\n✅ Total: {len(todos_programas)} programas instalados")