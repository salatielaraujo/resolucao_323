import streamlit as st

st.title("Classificação de Empreendimentos de Irrigação - V 1.3")

# Perguntas para determinar o método de irrigação

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

metodo_selecionado = st.selectbox("Qual é o método de irrigação utilizado?", ["Selecione um método"] + list(metodos.keys()))

if metodo_selecionado != "Selecione um método":
    metodo = metodos[metodo_selecionado]

    if metodo in ["1", "2", "3", "4", "7"]:
        potencial_poluidor = 'alto'
    else:
        potencial_poluidor = 'baixo'

    area = None
    # Pergunta sobre a área irrigada ou área da bacia de acumulação
    if metodo in ["1", "2", "3"]:
        medida_porte = 'área irrigada'
        area = st.number_input("Qual é a área irrigada em hectares?", min_value=0.0, step=0.1)
    elif metodo in ["4", "5", "7", "8"]:
        medida_porte = 'área da bacia de acumulação ou área alagada'
        area = st.number_input("Qual é a área da bacia de acumulação em hectares?", min_value=0.0, step=0.1)
    else:
        st.write("Atividade isenta.")

    # Determinação da classificação do porte com base nas respostas
    if area is not None and area > 0:
        if metodo in ["1", "2", "3"]:  
            if area <= 50:
                porte = "Mínimo"
                st.write("\nO impacto é local e a competência do licenciamento é municipal.")
            elif 50 < area <= 100:
                porte = "Pequeno"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 100 < area <= 500:
                porte = "Médio"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 500 < area <= 1000:
                porte = "Grande"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
            else:
                porte = "Excepcional"
                st.write("\nEIA/RIMA necessário.")
        elif metodo == "4":  
            if area <= 10:
                porte = "Mínimo"
                st.write("\nO impacto é local e a competência do licenciamento é municipal.")
            elif 10 < area <= 25:
                porte = "Pequeno"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 25 <= area <= 50:
                porte = "Médio"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
            elif 50 <= area <= 200:
                porte = "Grande"
                st.write("\nEIA/RIMA necessário.")
            else:
                porte = "Excepcional"
                st.write("\nEIA/RIMA necessário.")
        elif metodo == "5":  
            if area <= 5:
                porte = "A atividade é isenta."
            elif 5 < area <= 10:
                porte = "Mínimo"
                st.write("\nO impacto é local e a competência do licenciamento é municipal.")
            elif 10 < area <= 25:
                porte = "Pequeno"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 25 < area <= 100:
                porte = "Médio"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
            elif 100 < area <= 200:
                porte = "Grande"
                st.write("\nEIA/RIMA necessário.")
            else:
                porte = "Excepcional"
                st.write("\nEIA/RIMA necessário.")
        elif metodo == "6":  
            porte = "A atividade é isenta."
        elif metodo == "7":  
            if area <= 10:
                porte = "Mínimo"
                st.write("\nO impacto é local e a competência do licenciamento é municipal.")
            elif 10 < area <= 25:
                porte = "Pequeno"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 25 < area <= 50:
                porte = "Médio"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
            elif 50 <= area <= 200:
                porte = "Grande"
                st.write("\nEIA/RIMA necessário.")
            else:
                porte = "Excepcional"
                st.write("\nEIA/RIMA necessário.")
        elif metodo == "8":  
            if area <= 5:
                porte = "Atividade é isenta."
            elif 5 < area <= 10:
                porte = "Mínimo"
                st.write("\nO impacto é local e a competência do licenciamento é municipal.")
            elif 10 < area <= 25:
                porte = "Pequeno"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo I")
            elif 25 < area <= 100:
                porte = "Médio"
                st.write("\nO projeto de licenciamento será apresentado conforme o Anexo II")
            elif 100 < area <= 200:
                porte = "Grande"
                st.write("\nEIA/RIMA necessário.")
            else:
                porte = "Excepcional"
                st.write("\nEIA/RIMA necessário.")
                
    # Determinação da classificação com base nas respostas
    if area is not None and area > 0:
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

    st.write("\nPorte: "+porte)
    st.write("\nO empreendimento é considerado como de potencial poluidor '"+potencial_poluidor+"'")
    st.write("\nA medida de porte é '"+medida_porte+"' e a unidade de medida é 'hectares'")
