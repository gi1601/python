# Aluna: Giovanna Rodrigues Silva - Questão: "Impar, Par ou Roubo"

#primeiro pedi para informar todos os dados
p = int(input("Informe o escolhar do jogador 1(0-ímpar 1-par):"))
j1 = int(input("Informe o número escolhido pelo jogador 1:"))
j2 =int(input("Informe o número escolhido pelo jogador 2:"))
r =int(input("Informe a escolha do jogar 1(0-não roubar 1-roubar ):"))
a =int(input("Informe a escolha do jogar 2(0-não acusar de roubo 1-acusar de roubo ):"))

#se tiver resto é numero impar
soma= (j1+j2)%2

#coloquei as possibilidades

#roubos e acusações
if r==1 and a==0:
    print("Jogador 1 ganhou! ")
if  r == 1 and a == 1:
    print("Jogador 2 ganhou! ")
if r==0 and a==1:
    print("Jogador 1 ganhou! ")

#quando da impar, sem roubo e acusações
if p==1 and soma>0 and r==0 and a==0:
    print("Jogador 2 ganhou! ")
if p==0 and soma>0 and r==0 and a==0:
    print("Jogador 1 ganhou! ")

#quando da par, sem roubo e acusações
if p==1 and soma==0 and r==0 and a==0:
    print("Jogador 1 ganhou! ")
if p==0 and soma==0 and r==0 and a==0:
    print("Jogador 2 ganhou! ")
