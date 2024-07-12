metodo = ""
print("="*120)
print("Classificação de Empreendimentos de Irrigação\n")

# Perguntas para determinar o método de irrigação
print("Métodos de irrigação: ")
print("\n1- Superficial com barragens;")
print("2- Superficial com açudes;")
print("3- Superficial sem uso de reservatório;")
print("4- Aspersão ou localizado com barragens;")
print("5- Aspersão ou localizado com açudes;")
print("6- Aspersão ou localizado sem reservatório;")
print("7- Barragem para irrigação;")
print("8- Açude para irrigação;\n")

metodo = input("Qual é o método de irrigação utilizado? ")

if metodo in ["1","2","3","4","7"]:
    print("\nO empreendimento é considerado como de potencial poluidor 'alto'")
else:
    print("\nO empreendimento é considerado como de potencial poluidor 'baixo'")

area = ""
# Pergunta sobre a área irrigada ou área da bacia de acumulação
if metodo in ["1", "2", "3"]:
    print("\nA medida de porte é área irrigada e a unidade de medida é 'hectares'\n")
    try:
        area = float(input("Qual é a área irrigada em hectares? "))
    except:
        print("Área inválida !!!")
elif metodo in ["4", "5", "7", "8"]:
    print("\nA medida de porte é área da bacia de acumulação e a unidade de medida é 'hectares'\n")
    try:
        area = float(input("Qual é a área da bacia de acumulação em hectares? "))
    except:
        print("Área inválida !!!")
else:
    print("Atividade isenta.")

# Determinação da classificação do porte com base nas respostas
if area != "":
    if metodo in ["1","2","3"]:  
        if area   <= 50:
            print("\nPorte: Mínimo")
            print("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 50   < area <= 100  :
            print("\nPorte: Pequeno")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 100  < area <= 500 :
            print("\nPorte: Médio")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 500  < area <= 1000 :
            print("\nPorte: Grande")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        else:
            print("\nPorte: Excepcional")
            print("\nEIA/RIMA necessário.")
    elif metodo in ["4"]:  
        if area   <= 10:
            print("\nPorte: Mínimo")
            print("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10  < area <= 25:
            print("\nPorte: Pequeno")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25  <= area <= 50 :
            print("\nPorte: Médio")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 50 <= area <= 200 :
            print("\nPorte: Grande")
            print("\nEIA/RIMA necessário.")
        else:
            print("\nPorte: Excepcional")
            print("\nEIA/RIMA necessário.")
    elif metodo in ["5"]:  
        if area <= 5:
            print("\nA atividade é isenta.")
        elif 5  < area <= 10  :
            print("\nPorte: Mínimo")
            print("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10  < area <= 25  :
            print("\nPorte: Pequeno")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25  < area <= 100 :
            print("\nPorte: Médio")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 100 < area <= 200 :
            print("\nPorte: Grande")
            print("\nEIA/RIMA necessário.")
        else:
            print("\nPorte: Excepcional")
            print("\nEIA/RIMA necessário.")
    elif metodo in ["6"]:  
        print("\nA atividade é isenta.")
    elif metodo in ["7"]:  
        if area <= 10:
            print("\nPorte: Mínimo")
            print("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10  < area <= 25  :
            print("\nPorte: Pequeno")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25  < area <= 50 :
            print("\nPorte: Médio")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 50 <= area <= 200 :
            print("\nPorte: Grande")
            print("\nEIA/RIMA necessário.")
        else:
            print("\nPorte: Excepcional")
            print("\nEIA/RIMA necessário.")
    elif metodo in ["8"]:  # Superficial com barragens
        if area <= 5:
            print("\nAtividade é isenta.")
        elif 5 < area <= 10:
            print("\nPorte: Mínimo")
            print("\nO impacto é local e a competência do licenciamento é municipal.")
        elif 10  < area <= 25  :
            print("\nPorte: Pequeno")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo I")
        elif 25  < area <= 100 :
            print("\nPorte: Médio")
            print("\nO projeto de licenciamento será apresentado conforme o Anexo II")
        elif 100 < area <= 200 :
            print("\nPorte: Grande")
            print("\nEIA/RIMA necessário.")
        else:
            print("\nPorte: Excepcional")
            print("\nEIA/RIMA necessário.")
            
# Determinação da classificação com base nas respostas
if area != "":
    if metodo in ["1","2","3"]:  
        if area > 1000:
            print("\nClassificação: Passível de EIA/RIMA")
        else:
            print("\nClassificação: Licenciamento trifásico")
    elif metodo == "4":  
        if area > 50:
            print("\nClassificação: Passível de EIA/RIMA")
        else:
            print("\nClassificação: Licenciamento trifásico")
    elif metodo == "7":  
        if area > 200:
            print("\nClassificação: Passível de EIA/RIMA")
        else:
            print("\nClassificação: Licenciamento trifásico")
    else:
        print("\nMétodo de irrigação inválido.")
print("\n")
print("="*120)
