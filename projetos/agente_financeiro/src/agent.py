import google.generativeai as genai
import pandas as pd
import json
import os

def load_knowledge_base():
    base_path = os.path.join(os.path.dirname(__file__), '..', 'data')
    transacoes = pd.read_csv(os.path.join(base_path, 'transacoes.csv'), encoding='utf-8-sig')
    with open(os.path.join(base_path, 'perfil_investidor.json'), 'r', encoding='utf-8-sig') as f:
        perfil = json.load(f)
    with open(os.path.join(base_path, 'produtos_financeiros.json'), 'r', encoding='utf-8-sig') as f:
        produtos = json.load(f)
    return transacoes, perfil, produtos

def get_financial_advice(user_input, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    transacoes, perfil, produtos = load_knowledge_base()
    
    # Construção do Contexto para Anti-Alucinação
    context = f"""
    SISTEMA FINANCEIRO INTELIGENTE - CONTEXTO DO CLIENTE:
    Perfil: {json.dumps(perfil)}
    Transações Recentes: {transacoes.to_dict(orient='records')}
    Catálogo de Produtos: {json.dumps(produtos)}
    
    DIRETRIZES:
    Você é um agente financeiro consultivo. Sempre responda com clareza, sem jargões, usando dados da base de conhecimento. 
    Nunca invente informações. Se o cliente pedir algo fora da base (ex.: criptomoedas não listadas), responda: 
    'Essa informação não está disponível. Posso sugerir alternativas seguras.'
    """
    
    full_prompt = f"{context}\n\nCliente pergunta: {user_input}"
    response = model.generate_content(full_prompt)
    return response.text

if __name__ == "__main__":
    print("Módulo Agente carregado.")
