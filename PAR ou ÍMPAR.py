from random import randint

v = 0

while True:

    p = int ( input("Digite um número:"))
    c = randint(0, 10)
    t = p + c
   

    e = ' '

    while e not in 'PpIi':

        e = str( input ("ímpar ou Par: ")).strip().upper()[0]

    print (f"Você jogou {p} e o computador jogou {c}, total de: {t}")

    if e == 'P':
        if t % 2 == 0:
            print ("Você ganhou")
            v += 1
        else:
            print("Você perdeu")
            break

    elif e == 'I':
        if t % 2 == 1:
            print ("Você ganhou")
            v += 1
        
        else:
            print("Você perdeu")
            break
    
    print("Vamos jogar novamente...")

print(f"Você ganhou {v}")