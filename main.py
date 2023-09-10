#Exercicio 1
#Faça um programa que peça dois números e verifique (usando if e else) e imprima o maior deles  

# numero_um = int(input("Digite um número: "))
# numero_dois = int(input("Digite outro número: "))

# if numero_um > numero_dois:
#     print(f"O maior numero é o: {numero_um}")

# elif numero_dois > numero_um:
#     print(f"O maior numero é o: {numero_dois}")

# else:
#     print("Os dois números são iguais")

#exercicio 2
#Faça um programa que peça um valor e mostre na tela 
# se o valor é positivo ou negativo 
# numero_um = int(input("Digite um número: "))

# if numero_um <0:
#     print(f"O número: {numero_um} é negativo")

# else:
#     print(f"O número: {numero_um} é positivo")

#exercicio 3
# Faça um programa que verifique (usando if e else)
# se uma letra digitada é “F” ou “M”. Conforme a letra escrever:
# F – Feminino, M- Masculino, Sexo inválido.  

# sexo = input("Digite seu sexo [M]masculino, [F]feminino: ")

# if sexo =='M':
#     print("O seu sexo é Masculino")

# elif sexo == 'F':
#     print("Seu sexo é Feminino")

# else:
#     print("Sexo invalido!")

#exercicio 4
#Faça um programa que verifique (usando if e else)
# se uma letra digitada é vogal ou consoante.

# letra = input("Digite uma letra: ")

# if letra == 'a'or  letra == 'e' or letra == 'o' or letra =='u':

#         print(f"A letra {letra} é uma vogal")

# else:
#         print(f"A letra {letra} é uam cosoante")

#exercicio 5
#Faça um programa para a leitura de duas notas parciais de um aluno.  

#A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#A mensagem “Aprovado com Distinção”, se a média for igual a dez;
#A mensagem “Reprovado” se a média for menor de do que sete;

# nota_um = float(input("Digite a primeira nota: "))
# nota_dois = float(input("Digite a segunda nota: "))
# media = (nota_um + nota_dois) /2

# if media == 7:
#     print(f"Aluno aprovado com a média {media}")

# if media == 10:
#     print(f"Aluno aprovado com distinção com a média {media}")

# else:
#     print(f"Aluno repovado com a média {media}")

#exercicio 6
#Faça um programa que leia três números, 
# verifique (usando if e else), e mostre o maior deles.  

# numero_um = input("Digite um numero: ")
# numero_dois = input("Digite um segundo numero: ")
# numero_tres = input("Digite um terceiro numero: ")

# if numero_um > numero_dois and numero_um > numero_tres:
#     print(f" o numero {numero_um} é o maior número")

# elif numero_dois > numero_um and numero_dois > numero_tres:
#     print(f"O número {numero_dois} é o maior número")

# else:
#     print(f"O número {numero_tres} é o maior número")


#exercicio 7
#Faça um programa que leia três números, 
#verifique (usando if e else) e mostre o maior e o menor deles;  
# numero_um = input("Digite um numero: ")
# numero_dois = input("Digite um segundo numero: ")
# numero_tres = input("Digite um terceiro numero: ")

# if numero_um > numero_dois and numero_um > numero_tres:
#     print(f" o numero {numero_um} é o maior número")
#     if numero_um < numero_dois and numero_um < numero_tres:
#         print(f"O número {numero_um} é o menor número")
#     if numero_dois < numero_um and numero_dois < numero_tres:
#         print(f"O número {numero_dois} é o menor número")
#     if numero_tres < numero_dois and numero_tres < numero_um:
#         print(f"O número {numero_tres} é o menor número")

# elif numero_dois > numero_um and numero_dois > numero_tres:
#     print(f"O número {numero_dois} é o maior número")
#     if numero_dois < numero_um and numero_dois < numero_tres:
#         print(f"O número {numero_dois} é o menor número")
#     if numero_um < numero_dois and numero_um < numero_tres:
#         print(f"O número {numero_um} é o menor número")
#     if numero_tres < numero_dois and numero_tres < numero_um:
#         print(f"O número {numero_tres} é o menor número")

# else:
#     print(f"O número {numero_tres} é o maior número")
#     if numero_tres < numero_dois and numero_tres < numero_um:
#         print(f"O número {numero_tres} é o menor número")
#     if numero_dois < numero_um and numero_dois < numero_tres:
#         print(f"O número {numero_dois} é o menor número")
#     if numero_um < numero_dois and numero_um < numero_tres:
#         print(f"O número {numero_um} é o menor número")


#exercicio 8
# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve
# comprar, sabendo que a decisão é sempre o mais barato.  

# preco_um = float(input("Digite o primeiro preço: "))
# preco_dois = float(input("Digite o segundo preço: "))
# preco_tres = float(input("Digite o terceiro preço: "))

# if preco_um < preco_dois and preco_um < preco_tres:
#     print(f"O {preco_um} é o mais barato")

# elif preco_dois < preco_tres and preco_dois < preco_tres:
#     print(f"O {preco_dois} é o mais barato")

# else:
#     print(f"O {preco_tres} é o mais barato")

#exercicio 9
# Faça um programa que leia três números e mostre-os em ordem decrescente. 
# numero_um = input("Digite o primeiro número: ") 
# numero_dois = input("Digite o segundo número: ") 
# numero_tres = input("Digite o terceiro número: ") 

# if numero_um > numero_dois and numero_dois > numero_tres:
#     print(f"lista 1 - {numero_um} {numero_dois} {numero_tres}")

# if numero_dois > numero_um and numero_um > numero_tres:
#     print(f" lista 2 - {numero_dois} {numero_um} {numero_tres}")

# if numero_tres > numero_um and numero_dois > numero_um:
#     print(f" lista 3 - {numero_tres} {numero_dois} {numero_um}")

#exercicio 10

# Faça um programa que pergunte em que turno você estuda
# Peça para digitar M-matutino ou V-vespertino ou N-noturno. 
# Imprima a mensagem “Bom dia!” ou  “Boa Noite” ou “Valor inválido”, conforme o caso.  
# while True:
#     turno = input("Digite o turno em que você estuda: [M]matutino, [V]vespertino e [N]noturno: ")

#     if turno == 'M':
#         print("Bom dia!")

#     elif turno == 'V':
#         print("Boa tarde!")

#     elif turno == 'N':
#         print("Boa noite!")

#     else:
#         print("Turno invalido")
#         break

#  Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# “Telefonou para a vítima? “
# “Esteve no local do crime?”
# “Mora perto da vítima? “
# “Devia para a vítima? “
# “Já trabalhou com a vítima? “

# pergunta_um = input("Telefonou para a vítima?: ")
# pergunta_dois = input("Esteve no local do crime?: ")
# pergunta_tres = input("Mora perto da vítima?: ")
# pergunta_quatro = input("Devia para a vítima?: ")
# pergunta_quita = input("Já trabalhou com a vítima?: ")



# contagem = 0

# if pergunta_um == 'sim':
#     contagem = contagem + 1

# if pergunta_dois == 'sim':
#     contagem = contagem + 1

# if pergunta_tres == 'sim':
#     contagem = contagem + 1                           

# if pergunta_quatro == 'sim':
#     contagem = contagem + 1

# if pergunta_quita == 'sim':
#     contagem = contagem + 1


#     if contagem == 2:
#         print("Suspeita")

#     elif contagem == 3 or contagem < 4:
#         print("cumplice")

#     elif contagem > 4:
#         print("Assassino")

#     else:
#         print("Inocente")

# Crie um programa que peça um número ao usuário e armazene ele na variável x.
# Depois peça outro número e armazene na variável y. Mostre esses números.
# Em seguida, faça com que x passe a ter o valor de y, e que y passe a ter o valor de x.

# x = input("Digite um número: ")
# y = input("Digite um outro número: ")

# print(f"Os número foram {x} e {y}")

# z = x
# x = y
# y = z
# print(f"Os números trocados são {x} e {y}")

# Para doar sangue é necessário ter entre 18 e 67 anos.
# Faça um aplicativo que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
# Use alguns dos operadores lógicos 

