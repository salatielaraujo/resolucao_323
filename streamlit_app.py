import streamlit as st

st.title("Classificação de Empreendimentos de Irrigação")

# Perguntas para determinar o método de irrigação
st.subheader("Métodos de irrigação:")
metodos = [
    "Superficial com barragens",
    "Superficial com açudes",
    "Superficial sem uso de reservatório",
    "Aspersão ou localizado com barragens",
    "Aspersão ou localizado com açudes",
    "Aspersão ou localizado sem reservatório",
    "Barragem para irrigação",
    "Açude para irrigação"
]

metodo_selecionado = st.selectbox("Qual é o método de irrigação utilizado?", metodos)

if metodo_selecionado in metodos[:5]:
    st.write("\nO empreendimento é considerado como de potencial poluidor 'alto'")
else:
    st.write("\nO empreendimento é considerado como de potencial poluidor 'baixo'")

area = None
# Pergunta sobre a área irrigada ou área da bacia de acumulação
if metodo_selecionado in metodos[:3]:
    st.subheader("\nA medida de porte é área irrigada e a unidade de medida é 'hectares'")
    area = st.number_input("Qual é a área irrigada em hectares?", min_value=0.0, step=0.1)
elif metodo_selecionado in metodos[3:]:
    st.subheader("\nA medida de porte é área da bacia de acumulação e a unidade de medida é 'hectares'")
    area = st.number_input("Qual é a área da bacia de acumulação em hectares?", min_value=0.0, step=0.1)
else:
    st.write("Atividade isenta.")

# Determinação da classificação do porte com base nas respostas
if area is not None:
    if metodo_selecionado in metodos[:3]:  
        if area <= 50:
            st.write("\nPorte: Mínimo")
            st.write("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 50 < area <= 100:
            st.write("\nPorte: Pequeno")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 100 < area <= 500:
            st.write("\nPorte: Médio")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 500 < area <= 1000:
            st.write("\nPorte: Grande")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        else:
            st.write("\nPorte: Excepcional")
            st.write("\nEIA/RIMA necessário.")
    elif metodo_selecionado == metodos[3]:  
        if area <= 10:
            st.write("\nPorte: Mínimo")
            st.write("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10 < area <= 25:
            st.write("\nPorte: Pequeno")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25 <= area <= 50:
            st.write("\nPorte: Médio")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 50 <= area <= 200:
            st.write("\nPorte: Grande")
            st.write("\nEIA/RIMA necessário.")
        else:
            st.write("\nPorte: Excepcional")
            st.write("\nEIA/RIMA necessário.")
    elif metodo_selecionado == metodos[4]:  
        if area <= 5:
            st.write("\nA atividade é isenta.")
        elif 5 < area <= 10:
            st.write("\nPorte: Mínimo")
            st.write("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10 < area <= 25:
            st.write("\nPorte: Pequeno")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25 < area <= 100:
            st.write("\nPorte: Médio")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 100 < area <= 200:
            st.write("\nPorte: Grande")
            st.write("\nEIA/RIMA necessário.")
        else:
            st.write("\nPorte: Excepcional")
            st.write("\nEIA/RIMA necessário.")
    elif metodo_selecionado == metodos[5]:  
        st.write("\nA atividade é isenta.")
    elif metodo_selecionado == metodos[6]:  
        if area <= 10:
            st.write("\nPorte: Mínimo")
            st.write("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10 < area <= 25:
            st.write("\nPorte: Pequeno")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25 < area <= 50:
            st.write("\nPorte: Médio")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 50 <= area <= 200:
            st.write("\nPorte: Grande")
            st.write("\nEIA/RIMA necessário.")
        else:
            st.write("\nPorte: Excepcional")
            st.write("\nEIA/RIMA necessário.")
    elif metodo_selecionado == metodos[7]:  
        if area <= 5:
            st.write("\nAtividade é isenta.")
        elif 5 < area <= 10:
            st.write("\nPorte: Mínimo")
            st.write("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10 < area <= 25:
            st.write("\nPorte: Pequeno")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25 < area <= 100:
            st.write("\nPorte: Médio")
            st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 100 < area <= 200:
            st.write("\nPorte: Grande")
            st.write("\nEIA/RIMA necessário.")
        else:
            st.write("\nPorte: Excepcional")
            st.write("\nEIA/RIMA necessário.")
            
# Determinação da classificação com base nas respostas
if area is not None:
    if metodo_selecionado in metodos[:3]:  
        if area > 1000:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    elif metodo_selecionado == metodos[3]:  
        if area > 50:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    elif metodo_selecionado == metodos[6]:  
        if area > 200:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    else:
        st.write("\nMétodo de irrigação inválido.")
