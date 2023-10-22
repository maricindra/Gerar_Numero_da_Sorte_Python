#OBJETIVO: GERAR NUMEROS DA SORTE - Detalhes em Read
# Uso da biblioteca Random.
import random 

# Introdução para o usuário.
print("\n Olá, Seja bem vindo \n") 

# Entrada de dados do tipo inteiro e especifico para o sistema não ter erros.
quantidade = int(input("Escolha, quantos número da sorte você quer? "))

# Mostrar as escolhas do usuário, facilitam os desenvolvedores e os usuários.
print(f"\nOk, então {quantidade} numeros\n") 

# Oferecer um mundo de opções ao usuário, mas especificando e organizando no sistema.
entre = int(input("Você quer que esses números sejam entre o valor "))
ate = int(input("ate o "))

# Guiar sempre o usuário com as escolhas realizadas.
print(f"\nGerando numeros aleatorios entre {entre} e {ate}")                

# Gerar o solicitado:
for i in range (quantidade):
    numero_aleatorio = random.randint(entre,ate)
    print (numero_aleatorio)


#--------------------- total de 10 linhas------------
# Não foi preferivel usar o while, pois o codigo ficaria grande,
# mas Caso fosse usar o While, seria:
# a = 0
# while a < quantidade:
#    numero_aleatorio = random.randint(entre,entrefim)
#    print(numero_aleatorio)
#    a = a + 1
