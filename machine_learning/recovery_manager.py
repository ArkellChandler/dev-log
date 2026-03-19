import os
import json
import pandas as pd
import mysql.connector
from datetime import datetime

# Configurações
BASE_DIR = r'C:\Users\User\dev-log\machine_learning'
PATH_JSON = os.path.join(BASE_DIR, 'assets', 'data_sync.json')
PATH_BACKUP = os.path.join(BASE_DIR, 'assets', 'backup_recovery.csv')

def log_status(mensagem):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {mensagem}")

def recuperar_dados():
    log_status("Iniciando Verificação de Integridade...")

    # TENTATIVA 1: Tentar conexão com SQL (Fonte Primária)
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_integracao")
        if conn.is_connected():
            log_status("Fonte Primária (SQL) Online. Atualizando Backup...")
            df = pd.read_sql("SELECT * FROM vendas_origem", conn)
            df.to_csv(PATH_BACKUP, index=False) # Cria um backup em CSV (segurança extra)
            conn.close()
            return "SQL_OK"
    except Exception as e:
        log_status(f"⚠️ Alerta: Fonte Primária (SQL) Offline! Motivo: {e}")

    # TENTATIVA 2: Recuperar via JSON (Ponte de Integração)
    if os.path.exists(PATH_JSON):
        log_status("Recuperando via Cache JSON...")
        return "JSON_RECOVERED"

    # TENTATIVA 3: Recuperar via CSV de Emergência
    if os.path.exists(PATH_BACKUP):
        log_status("Recuperando via Backup CSV Crítico...")
        df_backup = pd.read_csv(PATH_BACKUP)
        # Reconstrói o JSON para que o Dashboard volte a funcionar
        df_backup.to_json(PATH_JSON, orient='records', indent=4)
        log_status("✅ Sistema restaurado via Backup CSV.")
        return "BACKUP_RESTORED"

    log_status("❌ ERRO CRÍTICO: Nenhuma fonte de dados disponível.")
    return "CRITICAL_FAILURE"

if __name__ == "__main__":
    status = recuperar_dados()
    print(f"\nStatus Final da Plataforma: {status}")
