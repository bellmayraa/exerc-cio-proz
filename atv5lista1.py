#Atividade 5
def verificaTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo equilatero")
    elif (lado1 == lado2 and lado2 != lado3) or (lado1 != lado2 and lado2 == lado3):
        print("É um isóceles")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Triangulo escaleno")

def verificaTrianguloComRetorno(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Triangulo equilatero"
    elif (lado1 == lado2 and lado2 != lado3) or (lado1 != lado2 and lado2 == lado3):
        return "É um isóceles"
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return "Triangulo escaleno"

# Peça ao usuário os comprimentos dos três lados de um triângulo
lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o lado 2: "))
lado3 = int(input("Digite o lado 3: "))
# determine se é equilátero, isósceles ou escaleno
verificaTriangulo(lado1, lado2, lado3)
resultado = verificaTrianguloComRetorno(lado1, lado2, lado3)
print(resultado)
