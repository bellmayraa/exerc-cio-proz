#Atividade 10
idade = int(input("Digite sua idade"))

if idade < 12:
    classificação = "criança"
elif idade >= 12 and idade <18:
    classificação = "adolecente"
elif idade >= 18 and idade <30:
    classificação = "jovem adulto" 
else:
    classificação = "adulto"
    
print(f"classificação: {classificação}")           
    