# -*- coding: utf-8 -*-
"""
AUTOMATIZADOR DE VERIFICAÇÃO DO BD CONTAGEH
Marcus - DGERD/Secretaria da Educação SP
"""

import pyodbc
import pandas as pd
from datetime import datetime
import os
import json

# Configuração do banco (ALTERE PARA SEUS DADOS REAIS)
SERVER = r'Vinicius\MSSQLSERVER01'   # Ex: 'MSSQLSERVER' ou 'localhost'
DATABASE = 'CONTAGEH'
DRIVER = '{SQL Server}'

# String de conexão
CONN_STR = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'

def testar_conexao():
    """Testa se o BD está online e acessível"""
    try:
        conn = pyodbc.connect(CONN_STR, timeout=5)
        conn.close()
        return True, "BD ONLINE"
    except Exception as e:
        return False, f"BD OFFLINE - Erro: {str(e)}"

def listar_tabelas():
    """Retorna lista de todas tabelas do BD CONTAGEH"""
    try:
        conn = pyodbc.connect(CONN_STR)
        query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
        ORDER BY TABLE_NAME
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Erro ao listar tabelas: {e}")
        return pd.DataFrame()

def gerar_relatorio_completo():
    """Gera relatório completo do BD e salva em arquivo"""
    print("="*60)
    print(f"RELATORIO DO BD CONTAGEH - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)
    
    # Verificar conexão
    status, msg = testar_conexao()
    print(f"\n[STATUS] {msg}")
    
    if not status:
        print("Nao foi possivel gerar relatorio completo")
        return
    
    # Listar tabelas
    print("\n[TABELAS ENCONTRADAS]")
    df_tabelas = listar_tabelas()
    if not df_tabelas.empty:
        print(f"Total: {len(df_tabelas)} tabelas")
    
    # Salvar relatorio
    os.makedirs('logs', exist_ok=True)
    nome_arquivo = f"logs/relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump({'data': datetime.now().isoformat(), 'status': status}, f)
    
    print(f"\nRelatorio salvo em: {nome_arquivo}")
    print("="*60)

if __name__ == "__main__":
    print("INICIANDO AUTOMATIZADOR DO CONTAGEH\n")
    gerar_relatorio_completo()