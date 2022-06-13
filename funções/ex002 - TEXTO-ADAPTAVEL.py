def escreva(a):
    print("-"*(len(a)+4))
    print(f"  {a}")
    print("-"*(len(a)+4))


texto = str(input("Digite qualquer coisa aqui: ")).strip().upper()
escreva(texto)
