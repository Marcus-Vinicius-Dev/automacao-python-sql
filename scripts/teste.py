import winreg

# Função recursiva para explorar o Registro (como árvore de pastas)
def explorar_registro(chave_raiz, caminho, nivel=0):
    try:
        abre_chave = winreg.OpenKey(chave_raiz, caminho)
        print("  " * nivel + f"📁 {caminho.split('\\')[-1] or caminho}")
        
        i = 0
        while True:
            try:
                # Lista subpastas (recursivamente)
                nome_subchave = winreg.EnumKey(abre_chave, i)
                novo_caminho = f"{caminho}\\{nome_subchave}" if caminho else nome_subchave
                explorar_registro(chave_raiz, novo_caminho, nivel + 1)
                i += 1
            except OSError:  # Sem mais subpastas
                break
        
        # Lista arquivos (valores)
        j = 0
        while True:
            try:
                nome_valor, dado, tipo = winreg.EnumValue(abre_chave, j)
                print("  " * (nivel + 1) + f"📄 {nome_valor} = {dado}")
                j += 1
            except OSError:  # Sem mais arquivos
                break
                
        winreg.CloseKey(abre_chave)
    except:
        pass

# Exemplo: explorar onde ficam os drivers ODBC
explorar_registro(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\ODBC")




