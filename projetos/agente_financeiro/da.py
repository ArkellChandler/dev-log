import google.generativeai as genai

genai.configure(api_key="AIzaSyBgLA8RUK9d6nR8eY-DTi3GwYG-OIRHpIc")

3. Listar os modelos disponíveis
Crie um trecho de código para listar os modelos e ver quais estão ativos:

python
models = genai.list_models()

for m in models:
    print(m.name, m.supported_generation_methods)

    4. Usar um modelo válido
    Depois de ver a lista, escolha um modelo que suporte generateContent.
    Por exemplo, se aparecer gemini-1.0-pro, use assim:
    
    python
    model = genai.GenerativeModel("gemini-1.0-pro")
    response = model.generate_content("Olá mundo")
    print(response.text)


    import streamlit as st
    import google.generativeai as genai
    
    genai.configure(api_key="AIzaSyBgLA8RUK9d6nR8eY-DTi3GwYG-OIRHpIc")
    
    st.title("Teste com Gemini")
    
    # Botão para listar modelos
    if st.button("Listar modelos"):
        models = genai.list_models()
        for m in models:
            st.write(m.name, m.supported_generation_methods)
    
    # Entrada de texto
    prompt = st.text_input("Digite seu prompt:")
    
    if st.button("Gerar resposta"):
        model = genai.GenerativeModel("gemini-1.0-pro")  # troque pelo modelo válido
        response = model.generate_content(prompt)
        st.write(response.text)
