import streamlit as st
import sys
import os
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError

# Adiciona src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import agent

st.set_page_config(page_title="Agente Financeiro IA", page_icon="💰")

st.title("💰 Agente Financeiro Inteligente")
st.markdown("---")

# API Key padrão e opção de substituição
default_api_key = "AIzaSyBgLA8RUK9d6nR8eY-DTi3GwYG-OIRHpIc"
api_key = st.sidebar.text_input("Gemini API Key", value=default_api_key, type="password")

# Listar modelos disponíveis
if st.sidebar.button("Listar modelos disponíveis"):
    try:
        models = agent.list_available_models(api_key)
        st.sidebar.write("Modelos encontrados:")
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                st.sidebar.text(f"✅ {m.name}")
            else:
                st.sidebar.text(f"❌ {m.name}")
    except Exception as e:
        st.sidebar.error(f"Erro ao listar modelos: {e}")

model_choice = st.sidebar.selectbox("Escolha o modelo:", [
    "models/gemini-2.0-flash", 
    "models/gemini-2.0-flash-lite", 
    "models/gemini-1.5-flash", 
    "models/gemini-1.5-pro",
    "models/gemini-2.5-flash",
    "models/gemini-2.5-pro"
])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar com suas finanças hoje?"):
    if not api_key:
        st.error("Por favor, insira sua API Key no menu lateral.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = agent.get_financial_advice(prompt, api_key, model_choice)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except ResourceExhausted:
                st.warning("⚠️ Quota excedida. Ativando modo demo.")
                demo_response = "Resposta simulada: Com base no seu perfil moderado, recomendo manter sua reserva de emergência em CDB de Liquidez Diária antes de expandir para o Fundo Multimercado Neon."
                st.markdown(demo_response)
                st.session_state.messages.append({"role": "assistant", "content": demo_response})
            except GoogleAPIError as e:
                st.error(f"Erro na API: {e}")
                demo_response = "Resposta simulada: O sistema está em modo de demonstração. Em uma situação real, eu analisaria suas transações recentes para otimizar seus gastos com Lazer."
                st.markdown(demo_response)
                st.session_state.messages.append({"role": "assistant", "content": demo_response})
            except Exception as e:
                st.error(f"Erro na comunicação: {e}")

st.sidebar.markdown("---")
st.sidebar.info("Agente focado em planejamento, metas e controle de gastos.")
