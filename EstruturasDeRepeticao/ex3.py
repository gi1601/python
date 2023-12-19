homem= 0
mulher= 0
soma=0
im=0
ih=0
ig=0
for i in range(1,11):
   sexo = int(input("Qual o sexo: 1-para mulher 2-para homem"))
   idade = int(input("informe a idade: "))
   ig+=idade
   if sexo ==1:
       im+= idade
       mulher+=1
   elif sexo ==2:
       ih+= idade
       homem +=1

mediaM = im/mulher
mediaH = ih/homem
media= ig/10
print("Média mulheres: ", mediaM)
print("Média homens: ", mediaH)
print("Média geral: ", media)