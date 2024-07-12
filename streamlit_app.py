import streamlit as st

st.title("Classificação de Empreendimentos de Irrigação - V 1.12")

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

    area = 0
    medida_porte = ""
    # Pergunta sobre a área irrigada ou área da bacia de acumulação
    if metodo in ["1", "2", "3"]:
        medida_porte = 'área irrigada'
        area = st.number_input("Qual é a área irrigada em hectares?", min_value=0, step=10, format='%d')
    elif metodo in ["4", "5", "7", "8"]:
        medida_porte = 'área da bacia de acumulação ou área alagada'
        area = st.number_input("Qual é a área da bacia de acumulação em hectares?", min_value=0, step=10, format='%d')
    else:
        st.write("Atividade isenta.")
        
    porte = ""
    impacto = ""
    # Determinação da classificação do porte com base nas respostas
    if area is not None and area > 0:
        if metodo in ["1", "2", "3"]:  
            if area <= 50:
                porte = "Mínimo"
                impacto = "O impacto é local e a competência do licenciamento é municipal."
            elif 50 < area <= 100:
                porte = "Pequeno"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 100 < area <= 500:
                porte = "Médio"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 500 < area <= 1000:
                porte = "Grande"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo II"
            else:
                porte = "Excepcional"
        elif metodo == "4":  
            if area <= 10:
                porte = "Mínimo"
                impacto = "O impacto é local e a competência do licenciamento é municipal."
            elif 10 < area <= 25:
                porte = "Pequeno"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 25 <= area <= 50:
                porte = "Médio"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo II"
            elif 50 <= area <= 200:
                porte = "Grande"
            else:
                porte = "Excepcional"
        elif metodo == "5":  
            if area <= 5:
                porte = "A atividade é isenta."
            elif 5 < area <= 10:
                porte = "Mínimo"
                impacto = "O impacto é local e a competência do licenciamento é municipal."
            elif 10 < area <= 25:
                porte = "Pequeno"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 25 < area <= 100:
                porte = "Médio"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo II"
            elif 100 < area <= 200:
                porte = "Grande"
            else:
                porte = "Excepcional"
        elif metodo == "6":  
            porte = "A atividade é isenta."
        elif metodo == "7":  
            if area <= 10:
                porte = "Mínimo"
                impacto = "O impacto é local e a competência do licenciamento é municipal."
            elif 10 < area <= 25:
                porte = "Pequeno"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 25 < area <= 50:
                porte = "Médio"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo II"
            elif 50 <= area <= 200:
                porte = "Grande"
            else:
                porte = "Excepcional"
        elif metodo == "8":  
            if area <= 5:
                porte = "Atividade é isenta."
            elif 5 < area <= 10:
                porte = "Mínimo"
                impacto = "O impacto é local e a competência do licenciamento é municipal."
            elif 10 < area <= 25:
                porte = "Pequeno"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo I"
            elif 25 < area <= 100:
                porte = "Médio"
                impacto = "O projeto de licenciamento será apresentado conforme o Anexo II"
            elif 100 < area <= 200:
                porte = "Grande"
            else:
                porte = "Excepcional"
                
    # Determinação da classificação com base nas respostas
    classificacao = ""
    if area is not None and area > 0:
        if metodo in ["1", "2", "3"]:  
            if area > 1000:
                classificacao = "Passível de EIA/RIMA"
            else:
                classificacao = "Licenciamento trifásico"
        elif metodo == "4":  
            if area > 50:
                classificacao = "Passível de EIA/RIMA"
            else:
                classificacao = "Licenciamento trifásico"
        elif metodo == "7":  
            if area > 200:
                classificacao = "Passível de EIA/RIMA"
            else:
                classificacao = "Licenciamento trifásico"
        else:
            st.write("\nMétodo de irrigação inválido.")

    st.write("\nMedida de porte...: "+medida_porte)
    if metodo != "6"
        st.write("\nUnidade de Medida.: hectares")
        st.write("\nApresentação......: "+impacto)
        st.write("\nPorte.............: "+porte)
        st.write("\nPotencial poluidor: "+potencial_poluidor)
        st.write("\nClassificação.....: "+classificacao)
