def ajuda(com):
    help(com)
    

comando = ''
while True:
    print("=== CENTRAL DE AJUDA ===")
    print("-- 'fim' para finalizar")
    comando = str(input("Digite o comando que procura > ")).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
print("=== FIM DO PROGRAMA ===")
