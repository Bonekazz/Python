import datetime
import time

cadastro= dict()
atual = datetime.date.today().year

cadastro['nome'] = str(input("Digite seu nome: ")).lower().strip().capitalize()
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento

while True:
    if idade < 18:
        nascimento = int(input("Idade inválida, você precisa ser maior de idade. Digite seu ano de nascimento: "))
        idade = atual - nascimento
    elif idade >= 65:
        nascimento = int(input("A pessoa cadastrada deveria estar aposentada. Digite outro ano de nascimento: "))
        idade = atual - nascimento
    else:
        break

aposentadoria = nascimento + 62
cadastro['idade'] = idade

cadastro['CTPS'] = str(input("Possui carteira de trabalho? ")).lower().strip()

while True:
    if cadastro['CTPS'] == 'sim':
        cadastro['salario'] = float(input("Digite seu salário: "))
        cadastro['ano-contrato'] = int(input("Digite o ano de sua contratação: "))
        time.sleep(1)

        print("="*50)
        print("    REGISTRO CONCLUÍDO")
        print("="*50)
        time.sleep(1)
        
        print(f"- Nome: {cadastro['nome']}")
        time.sleep(0.3)
        print(f"- Idade: {cadastro['idade']}")
        time.sleep(0.3)
        print(f"- CTPS: salário(R${cadastro['salario']}), ano de contratação({cadastro['ano-contrato']})")
        time.sleep(0.3)
        print(f"- Se aposenta em {aposentadoria} com 62 anos")
        time.sleep(1)
        print("="*50)
        break

    if cadastro['CTPS'] == 'nao':
        time.sleep(1)
        print("="*50)
        print("    REGISTRO CONCLUÍDO")
        print("="*50)
        time.sleep(1)
        
        print(f"- Nome: {cadastro['nome']}")
        time.sleep(0.3)
        print(f"- Idade: {cadastro['idade']}")
        time.sleep(0.3)
        print(f"- CTPS: Não possui")
        time.sleep(1)
        print("="*50)
        break
    else:
        cadastro['CTPS'] = str(input("Resposta inválida. Possui carteira de trabalho? ")).lower().strip()

print("FIM DO PROGRAMA...")



