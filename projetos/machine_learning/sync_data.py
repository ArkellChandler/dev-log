import mysql.connector
import pandas as pd
import os

# Caminhos baseados no seu ambiente Windows 11
BASE_DIR = r'C:\Users\User\dev-log\machine_learning'
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
JSON_OUTPUT = os.path.join(ASSETS_DIR, 'data_sync.json')

def processar_etl():
    try:
        # 1. Conexão SQL (XAMPP)
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="", 
            database="db_integracao"
        )
        
        # 2. Extração com Pandas
        df = pd.read_sql("SELECT * FROM vendas_origem", conn)
        
        # 3. Transformação Simples (ETL)
        df['valor_taxado'] = (df['valor'] * 1.10).round(2)
        df['data_venda'] = df['data_venda'].astype(str) # Garante que a data vire texto para o JSON

        # 4. Carga (Cria a pasta assets se não existir)
        if not os.path.exists(ASSETS_DIR):
            os.makedirs(ASSETS_DIR)
            
        df.to_json(JSON_OUTPUT, orient='records', indent=4)
        
        print(f"✅ Sucesso! Dados salvos em: {JSON_OUTPUT}")
        conn.close()

    except Exception as e:
        print(f"❌ Erro na integração: {e}")

if __name__ == "__main__":
    processar_etl()
