
c1, c2, c3 = 0, 0, 0

while True:
    
    i = int ( input ("Digite a idade:"))
    s = " "

    while s not in "MF":
        
        s = str ( input ("Digite o sexo [M/F]:")).strip().upper()[0]
    
    if i >= 18:
       c1 += 1
    
    if s == "M":
       c2 += 1
       
    if s == "F" and i >= 20:
          c3 += 1

    r = " "
    
    while r not in "SN":

     r = str ( input ( "Deseja continua?: ")).strip().upper()[0]

    if r == "N":
       break


print(f"Total de pessoas com mais de 18 anos {c1}.")
print(f"Ao todo temos {c2} homens cadastrados")
print(f"Possuímos {c3} de mulheres com mais de 20 anos")
