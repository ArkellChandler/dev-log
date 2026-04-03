import streamlit as st
import sys
import os

# Adiciona src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
import agent

st.set_page_config(page_title="Agente Financeiro IA", page_icon="💰")

st.title("💰 Agente Financeiro Inteligente")
st.markdown("---")

api_key = st.sidebar.text_input("Gemini API Key", type="password")

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
                response = agent.get_financial_advice(prompt, api_key)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Erro na comunicação: {e}")

st.sidebar.markdown("---")
st.sidebar.info("Agente focado em planejamento, metas e controle de gastos.")
