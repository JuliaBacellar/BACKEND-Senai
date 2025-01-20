#x = 1 
#x2 = 2 

#soma = x + x2
#print(soma)


#<-----EXERCICIO  1 ---> 
##num1 = float(input("escreva aqui o numero que quiser"))
##num2 = float(input("escreva aqui o numero que quiser"))

##soma = num1 + num2
##print(soma)



##ano_nascimento = float(input("digite aqui a sua data de nascimento:"))
#nome = input('digite aqui o seu nome:')

#idade_usuario = 2025 - ano_nascimento

#print(f"a sua idade é{idade_usuario}") 


#recebe 5 notas de alunos e verifica  se a media for maior ou igual 
# a 5 aprovado,se a media for entre 2.5 e 5 recuperação se a media e
# é menor que 2.5 reprovado

 
# aluno1 = float(input("escreva aqui a nota do primeiro aluno"))
# aluno2 = float(input("escreva aqui a nota do segundo aluno"))
# aluno3 = float(input("escreva aqui a nota do terceiro aluno"))
# aluno4 = float(input("escreva aqui a nota do quarto  aluno"))
# aluno5 = float(input("escreva aqui a nota do quinto  aluno"))

# if aluno1 >= 5:
#     print("aprovado")
# elif aluno1 > 2.5 and aluno1< 5:
#     print ("recuperação")
# else:
#     print("reprovado")

# if aluno2 >= 5:
#     print("aprovado")
# elif aluno2 > 2.5 and aluno2< 5:
#     print ("recuperação")
# else:
#     print("reprovado")

# if aluno3 >= 5:
#     print("aprovado")
# elif aluno3 > 2.5 and aluno3< 5:
#     print ("recuperação")
# else:
#     print("reprovado")

# if aluno4 >= 5:
#     print("aprovado")
# elif aluno4 > 2.5 and aluno4< 5:
#     print ("recuperação")
# else:
#     print("reprovado")

# if aluno5 >= 5:
#     print("aprovado")
# elif aluno5 > 2.5 and aluno5< 5:
#     print ("recuperação")
# else:
#     print("reprovado")

#<--- laços de repetição --> atençaõ identação 
# numero = int(input("escreva um número inteiro positivo:"))


# for i in range(numero):
#     print(i)
    
#programa que solicite numeros ate usuario digitar um numero negativo
#e verifique qual dos numeros digitados é o maior

# numeros = int(input("digite aqui numeros"))

# while numeros > 0:
#     print(numeros)
#     if numeros < 0:
#         print("escreva aqui os números somente positivos")
#     else:
#         print("somente positivos")

#<-- funções --> 

#crie uma função inverter_string(S) que inverte a string S#
#sem usar a ténica de slicing(sem usar s[::-1] use um laço de repetição
#para resolver 
##utilizando um laço de repetição que itera sobre cada um,range que percorre sobre
# toda a string 
    def inverter_string(s):
    resultado = ""  
    for i in range(len(s) - 1, -1, -1):  
    return resultado


s = "julia"
print(inverter_string(s))  


##crie uma função contar_caracteres(s) que  recebe uma string s e retorna um dicio
#nario com a contagem de cada caractere que aparece na string .exemplo
#contar_caracteres("banana") deve retornar{'b':1, 'a':3, 'n':2}.

def contar_caracteres(s):
    contagem = {}
    for char in s:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem



#def abc(X):
    #print(X[1])
   # print("OLA")
   # print(X)
 
#abc("oieeeeeee")

 

