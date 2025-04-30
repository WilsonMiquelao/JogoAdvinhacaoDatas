import json
import random

#abrindo o arquivo json
f = open("words.json", encoding="utf8")

#inserindo o conteudo do arquivo em uma variavel para manipulação
words = json.load(f)
#inserindo as chaves do dicionario, no caso a data em uma variavel para manipulação
choice_c = random.choice(list(words.keys()))

print("Ola, seja bem vindo!")
print("#################################")

#inserindo o numero de tentativas a fornecer ao usuario
n_choices = 5
#declarando a varivel para utilizar como pilha conforme acerto do usuario
win = False

#loop para mostrar ao usuário 5 chances de acertar qual é a data, até chegar 
#a pilha total de acertos
while n_choices > 0 and win is not True:
    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAAAA\n")
    print("################## \n")

    #condicional para fazer com que a entrada tenha 8 digitos utilizando o "lenght"
    #para medir a entrada conforme o usuario
    if len(answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue
    
    #condicionando para adicionar um "✅" a cada vez que o usuario escrever a entrada
    #exatamente igual a variavel choice_c que são as chaves do dicionario
    #referindo ao arquivo json{}
    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation = pontuation + 1
            else:
                check.append("💢")
        
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#######################\n")

        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue
    n_choices = n_choices - 1

if win == True:
    print("VITÓRIA!!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)