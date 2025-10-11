print("--" * 10)
print("SUPERMERCADO")
print("--" * 10)

T1 = T2 = M = 0
p = " "
cont = 0

while True:
    
    produto = str ( input("Qual o nome do produto:"))
    valor = float ( input("Qual o valor do produto:"))
    T1 += valor
    cont += 1

    if cont == 1:
        M = valor
        p = produto
    
    else:
        if valor < M:
            M = valor
            p = produto
 
    r = " "
    
    while r not in "SN":

        r = str ( input("Deseja continuar [S/N]:")).strip().upper()[0]

    if valor > 1000:
        T2 += 1
   
    if valor < M:
        M = valor
        p = produto

    if r == "N":
        break
   
print(f"O TOTAL DA COMPRA É DE: {T1}")
print(F"O TOTAL DE PRODUTOS COM VALOR A CIMA DE 1000 REAIS É DE:{T2}")
print(f"O produto mais barato é {p} e ele custa {M}")

