items = ('Caneta Posca', 25.00, 'Caderno', 10.00, 'Estojo', 5.00, 'Cartão de Memória', 50.00, 'Memória RAM', 300.00, 'Camera de vídeo', 350.00, 'Microfone de mesa', 200.00, 'iphone', 1000.00)

print("===================== TABELA DE PREÇOS =====================")
for c in range(0, len(items), 2):
    print(f"{items[c]:.<50}R$ {items[c+1]}")