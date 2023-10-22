# Uso da biblioteca Random.
import random 

# Introdução para o usuário.
print("\n Olá, Seja bem vindo \n") 

# Entrada de dados do tipo inteiro e especifico para o sistema não ter erros.
quantidade = int(input(print("Escolha quantos número da sorte você quer!\n"))) 

# Mostrar as escolhas do usuário, facilitam os desenvolvedores e os usuários.
print(f"Ok, então {quantidade} numeros") 

# Oferecer um mundo de opções ao usuário, mas especificando e organizando no sistema.
entre = int(input(print("Você quer que esses números sejam entre o valor "))) 
entrefim = int(input(print("ate o ")))

# Guiar sempre o usuário com as escolhas realizadas.
print(f" Gerando numeros aleatorios entre {entre} e {entrefim}")                

# Gerar o solicitado:
for i in range (quantidade):
    numero_aleatorio = random.randint(entre,entrefim)
    print (numero_aleatorio)



#--------------------- total de 10 linhas------------
# Não foi preferivel usar o while, pois o codigo ficaria grande,
# mas Caso fosse usar o While, seria:
# a = 0
# while a < quantidade:
#    numero_aleatorio = random.randint(entre,entrefim)
#    print(numero_aleatorio)
#    a = a + 1
