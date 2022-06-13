
maiores = 0
homens = 0
mulheresmenores = 0

while True:
    idade = int(input("digite a idade: "))
    while idade <= 0:
        idade = int(input("idade invalida, digite novamente: "))
    sexo = str(input("digite o sexo dessa pessoa: ")).strip().lower()
    while sexo != 'masculino' and sexo!=  'feminino':
        sexo = str(input("sexo inválido. Digite novamente: ")).strip().lower()
    if idade >= 18: 
        maiores += 1
    if sexo == 'masculino':
        homens += 1
    if sexo == 'feminino' and idade < 20:
        mulheresmenores += 1
    resposta = str(input("quer continuar? ")).strip().lower()
    if resposta == 'nao':
        break

print("===== Cadastro Concluído =====")
print(f"Maiores de idade: {maiores}\nHomens Cadastrados: {homens}\nMulheres com menos de 20 anos: {mulheresmenores}")