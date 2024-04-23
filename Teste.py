# Praticando PY
# logica

# Teste 

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int (input("Digite um número: "))
if a and b and c  >= 0:
    print ("Multiplicação / Divisão / Adição / Divisão ")
    print (" A multiplicação dos números digitados é:", a * b * c) 
    print (" A divisão dos números digitados é: " , a / b / c)
    print (" A Adição dos números digitados é: ", a + b + c)
    print (" A subtração dos números digitados é: ", a - b - c)
elif a and b and c <= 0:
    print ("Erro, valor digitado não permitido") 
#Teste

d = 909 
e = 12**2
f = 2 - d

valor = int(input("Digite um numero:"))
if valor > 0:
    print ("Teste 1", d - 2 * 35 - 900)
elif valor < 0:
    print("Teste 2", e + d) 
elif valor == 0:
    print("Teste 3", f - d * e)

#

a = 4
b = 2
c = 4

if a > b:
 print("A é maior que B")
 b < a
 print ("B é menor que A")
 c == a
print ("C é igual á A")

# logica com entrada de dados

valor = int(input("Digite um número positivo ou negativo:"))
if valor == 0:
 print("Erro, Número digitado foi maior que o permitido!!")
elif valor > 0:
 print ("O número digitado foi positivo e multiplicado por 100 é:",valor * 100)
elif valor < 0:
 print ("O número digitado foi negativo e dividido por 5 é:", valor /5)
else:
 print("Erro!!!")
 
# calculo divisão e subtração

a = int(input("Digite um número maior que ZERO (A):"))
if a == 0:
    print ("Número invalido")
b = int(input("Digite um número menor que MIL (B):"))
if b >=1000:
    print("Número invalido")
c = int(input("Digite um número negativo (C):"))
if c >=0:
    print("Número digitado invalido")
else:
    print("A / B - C é igual a: ", a/b-c)

# calculadora 
    
    def calculate (): 
     operation 
    operation = input(''' Calculadora
       Por favor escolha
    +  para adição  
    -  para subtração
    *  para multiplicação 
    / para divisão : '''
    )

    num_1 = int(input('digite um número:'))
    num_2 = int(input('digite outro número:'))

    if operation == '+':
        print ('{} + {} ='.format(num_1,num_2))
        print (num_1 + num_2)

    elif operation == '-':
        print ('{} - {} ='.format(num_1,num_2))
        print (num_1 - num_2)

    elif operation == '/':
        print ('{} / {} ='.format(num_1,num_2))
        print (num_1 / num_2)

    elif operation == '*':
        print ('{} * {} ='.format(num_1,num_2))
        print (num_1 * num_2)
    else:
        print('Erro')

calculate()

#Creating Teste#


a1 = int(input('digite um numero'))
b1 = float(input('digite um numero'))

if a1 > 0:
        print ('',a1)
elif b1 > a1:
    print('',b1)
else:
    print('erro')

