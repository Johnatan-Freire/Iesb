menu = 0            #Váriavel utilizada no menu na função Main
list = []           #Lista onde vão ser guardados os contatos

#Função que cadastra um contato na lista
def cadastra():

    #Inicia um dicionário
    dicionario = {}

    #Leitura dos dados e atribui no dicionário o dado
    print("Qual é o nome?")
    nome = input()
    dicionario['nome'] = nome

    print("Qual é o telefone?")
    telefone = input()
    dicionario['telefone'] = telefone

    print("Qual é o E-mail?")
    email = input()
    dicionario['email'] = email

    print("Qual é o instagram?")
    instagram = input()
    dicionario['instagram'] = instagram

    print("Qual é o twitter?")
    twitter = input()
    dicionario['twitter'] = twitter

    print(dicionario)
    
    #Coloca o dicionário na lista
    list.append(dicionario);
    print(list)

#Função que busca e exibe as informações de um contato que o usuário define
def busca():

    print("Qual o nome da pessoa que deseja buscar?")
    nomeBusca = input()

    #Percorremos a lista de dicionários utilizando o nome
    #Verifico cada nome em cada dicionário se corresponde com a variável nomeBusca que lemos
    #Se corresponder, a lista é exibida
    for i in range(len(list)):
        if(nomeBusca == list[i]['nome']):
            print(list[i])

#Função que deleta pelo nome um contato da agenda
def deleta():
    print("Qual o nome da pessoa que deseja deletar as informações?")
    nomeDeleta = input()

    #Código busca na lista o nome do usuário
    for i in range(len(list)):            
        if(nomeDeleta == list[i]['nome']):
            list.pop(i)     #Comando para remover o elemento de índice i da lista
            break           #Para de correr a lista depois de item ser removido

    print(list)

#Função que permite alterar os dados de um contato cadastrado
def altera():
    
    #Leitura do nome da pessoa que desejamos alterar
    print("Qual o nome da pessoa que deseja alterar?")
    nomeAltera = input()

    #Nesse trecho de código, vai ser digitado uma das opções com todas as letras
    #Não deve ser escrito outra coisa aqui alem das opções dadas
    print("O que você deseja alterar?")
    print("Digite uma das palavras abaixo para escolher o que quer que seja alterado:")
    print("nome")
    print("telefone")
    print("email")
    print("instagram")
    print("twitter")
    menuAltera = input()
    
    print("Agora digite a informação nova:")
    alteracao = input()

    #Percorremos a lista e o dicionário que o nome corresponder, alteramos a informação do usuário
    for i in range(len(list)):
        if(nomeAltera == list[i]['nome']):
            list[i][menuAltera] = alteracao
            break                       #Para de percorrer a lista após o fim
    
    print(list) 

#Função que permite o cadastro de vários contatos de uma vez, sendo o número definido pelo usuário
def insereVarios():

    print("Quantos contatos você deseja inserir?")
    qtdContatos = int(input())

    #Esse código é igual o de cadastro, porém temos um for que vai de 0 até a quantidade que você digitou, repetindo o código quantas vezes você desejar
    for i in range(0,qtdContatos):
        dicionario = {}

        print("Qual é o nome?")
        nome = input()
        dicionario['nome'] = nome

        print("Qual é o telefone?")
        telefone = input()
        dicionario['telefone'] = telefone

        print("Qual é o E-mail?")
        email = input()
        dicionario['email'] = email

        print("Qual é o instagram?")
        instagram = input()
        dicionario['instagram'] = instagram

        print("Qual é o twitter?")
        twitter = input()
        dicionario['twitter'] = twitter

        print(dicionario)
        list.append(dicionario);
        print(list)

#Função que exibe um relatório com todos os contatos cadastrados na agenda até então
def relatorio():

    #Só percorremos a lista e printamos as informações
    print("Nome      Telefone      Email      Instagram      Twitter")
    for i in range(len(list)):
        print(list[i])

#Função que exibe os dados da lista de dicionários com virgula, apenas percorrendo e acessando
def salvaComVirgula():

    #Também a lista é percorrída e salvamos o dado com as virgulas
    for i in range(len(list)):
        print(list[i]['nome'],",",list[i]['telefone'],",",list[i]['email'],",",list[i]['instagram'],",",list[i]['twitter'])


#Aqui é a parte principal do programa, temos um input que vamos digitar um numero inteiro de 1 a 8, e temos as opções exibidas
#Quando digitamos um número everificado a variavel nos if's e ele executa a função correspondente ao texto
while menu != 8:
    menu = int(input("Escolha uma das opções:\nDigite 1 para inserir um novo contato \nDigite 2 para consultar um contato a partir do nome \nDigite 3 para remover um contato a partir do nome\nDigite 4 para alterar os dados de um contato já cadastrado\nDigite 5 Para inserir 2 ou mais contatos\nDigite 6 para gerar o relatório\nDigite 7 para salvar as informações com virgula\nDigite 8 para sair\n"))

    #Menu com as ações
    if menu == 1:
        cadastra()

    if menu == 2:
        busca()

    if menu == 3:
        deleta()

    if menu == 4:
        altera()

    if menu == 5:
        insereVarios()

    if menu == 6:
        relatorio()

    if menu == 7:
        salvaComVirgula()

    if menu == 8:
        print("Até mais!\n")

