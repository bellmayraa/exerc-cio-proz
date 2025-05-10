#Atividade 5
lado1 = int(input("Digite o comprimento do lado1 do triangulo"))
lado2 = int(input("Digite o comprimento do lado2 do triangulo"))
lado3 = int(input("Digite o comprimento do lado3 do triangulo"))

if lado1 == lado2 == lado3:
    print("O lado1 é equilatero")
elif  lado1 == lado2 == lado3:
    print("O lado2 é escaleno")
else: 
    print("O lado3 é isósceles")    
