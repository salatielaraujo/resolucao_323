import streamlit as st

st.title("Classificação de Empreendimentos de Irrigação")


# Perguntas para determinar o método de irrigação
st.subheader("Métodos de irrigação:")
metodos = {
    "1- Superficial com barragens": "1",
    "2- Superficial com açudes": "2",
    "3- Superficial sem uso de reservatório": "3",
    "4- Aspersão ou localizado com barragens": "4",
    "5- Aspersão ou localizado com açudes": "5",
    "6- Aspersão ou localizado sem reservatório": "6",
    "7- Barragem para irrigação": "7",
    "8- Açude para irrigação": "8"
}

metodo_selecionado = st.selectbox("Qual é o método de irrigação utilizado?", list(metodos.keys()))

metodo = metodos[metodo_selecionado]

if metodo in ["1", "2", "3", "4", "7"]:
    st.write("\nO empreendimento é considerado como de potencial poluidor 'alto'")
else:
    st.write("\nO empreendimento é considerado como de potencial poluidor 'baixo'")

area = None
# Pergunta sobre a área irrigada ou área da bacia de acumulação
if metodo in ["1", "2", "3"]:
    st.write("\nA medida de porte é área irrigada e a unidade de medida é 'hectares'")
    area = st.number_input("Qual é a área irrigada em hectares?", min_value=0.0, step=0.1)
elif metodo in ["4", "5", "7", "8"]:
    st.write("\nA medida de porte é área da bacia de acumulação e a unidade de medida é 'hectares'")
    area = st.number_input("Qual é a área da bacia de acumulação em hectares?", min_value=0.0, step=0.1)
else:
    st.write("Atividade isenta.")

# Determinação da classificação do porte com base nas respostas
if area is not None:
    if metodo in ["1", "2", "3"]:  
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
    elif metodo == "4":  
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
    elif metodo == "5":  
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
    elif metodo == "6":  
        st.write("\nA atividade é isenta.")
    elif metodo == "7":  
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
    elif metodo == "8":  
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
    if metodo in ["1", "2", "3"]:  
        if area > 1000:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    elif metodo == "4":  
        if area > 50:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    elif metodo == "7":  
        if area > 200:
            st.write("\nClassificação: Passível de EIA/RIMA")
        else:
            st.write("\nClassificação: Licenciamento trifásico")
    else:
        st.write("\nMétodo de irrigação inválido.")

