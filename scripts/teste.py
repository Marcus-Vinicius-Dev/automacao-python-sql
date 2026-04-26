import winreg

# COMANDO 1 - HKEY_CLASSES_ROOT (HKCR)
# Associações de arquivos, extensões e CLSID
print("=== HKCR - Primeiras 5 subpastas ===")
chave1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "")
for i in range(5):
    nome = winreg.EnumKey(chave1, i)
    print(f"  📁 {nome}")
winreg.CloseKey(chave1)

# COMANDO 2 - HKEY_CURRENT_USER (HKCU)
# Configurações do usuário atual (mais seguro de explorar)
print("\n=== HKCU - Subpastas iniciais ===")
chave2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "")
for i in range(5):
    nome = winreg.EnumKey(chave2, i)
    print(f"  📁 {nome}")
winreg.CloseKey(chave2)

# COMANDO 3 - HKEY_LOCAL_MACHINE (HKLM)
# Configurações do sistema (cuidado: gigante!)
print("\n=== HKLM - Subpastas iniciais ===")
chave3 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "")
for i in range(5):
    nome = winreg.EnumKey(chave3, i)
    print(f"  📁 {nome}")
winreg.CloseKey(chave3)

# COMANDO 4 - HKEY_USERS (HKU)
# Perfis de todos usuários da máquina
print("\n=== HKU - Subpastas (SIDs dos usuários) ===")
chave4 = winreg.OpenKey(winreg.HKEY_USERS, "")
for i in range(5):
    nome = winreg.EnumKey(chave4, i)
    print(f"  👤 {nome}")
winreg.CloseKey(chave4)

# COMANDO 5 - HKEY_CURRENT_CONFIG (HKCC)
# Perfil de hardware atual
print("\n=== HKCC - Subpastas ===")
chave5 = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, "")
for i in range(5):
    try:
        nome = winreg.EnumKey(chave5, i)
        print(f"  🔧 {nome}")
    except:
        break
winreg.CloseKey(chave5)