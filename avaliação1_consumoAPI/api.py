import requests

def GotNominhos(sobrenome):
    url = "https://thronesapi.com/api/v2/Characters"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        personagens_com_sobrenome = [personagem for personagem in dados if personagem['lastName'] == sobrenome]
        
        if personagens_com_sobrenome:
            print(f"Personagens com o sobrenome '{sobrenome}':")
            for personagem in personagens_com_sobrenome:
                print(f"- {personagem['fullName']}")
        else:
            print("Personagem nao encotrado, VOCE DIGITOU CORRETAMENTE??")
    else:
        print("Erro.")

# Exemplo de uso
sobrenome = input("Digite um sobrenome (lembre-se de usar LETRAS MAIUSCULAS no inicio) --> ")
GotNominhos(sobrenome)
