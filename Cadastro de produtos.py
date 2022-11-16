def CadastrarProd (dicionario):

    QuantosCad = int(input("\nDeseja cadastrar quantos produtos? "))
    print("\n")

    for i in range (QuantosCad):
        chave = input("Digite o {}º produto: ".format(i+1))
        dicionario[chave] = float(input("Digite o valor: "))
        print()

    Continuar = input("\nDeseja continuar cadastrando? (Sim=1 / Não=2)")
    
    while Continuar != "1" and Continuar != "2":

        print("\nValor inválido, Tente novamente.")
        Continuar = input("Deseja cadastrar outro produto? (Sim=1 / Não=2)")

    while Continuar == "1":

        chave = input("Digite um produto: ")
        dicionario[chave] = float(input("Digite um valor: "))
        Continuar = "3"
        while Continuar != "1" and Continuar != "2":
            Continuar = input("\nDeseja continuar cadastrando? (Sim=1 / Não=2)")

    return dicionario

def AlterarProd (dicionario):

    chave = input("Digite o produto que deseja alterar: ")

    if chave in dicionario.keys():
        dicionario[chave] = float(input("Digite o novo valor: "))
        print()
    else:
        print("Produto inexistente na lista!")

    Continuar = input("\nDeseja alterar outro produto? (Sim=1 / Não=2)")
    
    while Continuar != "1" and Continuar != "2":

        print("\nValor inválido, Tente novamente.")
        Continuar = input("Deseja alterar outro produto? (Sim=1 / Não=2)")

    while Continuar == "1":

        chave = input("Digite o produto que deseja alterar: ")

        if chave in dicionario.keys():
            dicionario[chave] = float(input("Digite o novo valor: "))

        else:
            print("Produto inexistente na lista!")

        Continuar = "3"
        while Continuar != "1" and Continuar != "2":
            Continuar = input("\nDeseja continuar? (Sim=1 / Não=2)")

    return dicionario

def PesquisarProd (dicionario):

    produto = input("\nQual produto deseja pesquisar? ")

    if produto in dicionario.keys():
        print("O valor do(a) {} é: R$ {}".format(produto, dicionario.get(produto)))
    else:
        print("Produto inexistente na lista!")

    Continuar = input("\nDeseja pesquisar outro produto? (Sim=1 / Não=2)")

    while Continuar != "1" and Continuar != "2":

        print("\nValor inválido, Tente novamente.")
        Continuar = input("Deseja pesquisar outro produto? (Sim=1 / Não=2)")

    while Continuar == "1":

        produto = input("\nQual produto deseja pesquisar? ")
        if produto in dicionario.keys():
            print("O valor do(a) {} é: R$ {}".format(produto, dicionario.get(produto)))
        else:
            print("Produto inexistente na lista!")
        Continuar = input("\nDeseja pesquisar outro produto? (Sim=1 / Não=2)")

def RemoverProd (dicionario):

    produto = input("\nQual produto deseja remover? ")

    if produto in dicionario.keys():
        dicionario.pop(produto)
        print("O(a) {} foi removido(a) da lista".format(produto))
    else:
        print("Produto inexistente na lista!")

    Continuar = input("\nDeseja remover outro produto? (Sim=1 / Não=2)")

    while Continuar != "1" and Continuar != "2":

        print("\nValor inválido, Tente novamente.")
        Continuar = input("Deseja remover outro produto? (Sim=1 / Não=2)")

    while Continuar == "1":

        produto = input("\nQual produto deseja remover? ")
        if produto in dicionario.keys():
            dicionario.pop(produto)
            print("O(a) {} foi removido(a) da lista".format(produto))
        else:
            print("Produto inexistente na lista!")
        Continuar = input("\nDeseja remover outro produto? (Sim=1 / Não=2)")

def ImprimirProd (dicionario):

    Lista = dicionario.items()
    print("\nLista de produtos: \n")
    for k,v in Lista:
        print ("{} - R$ {}".format(k,v))

    print("\n")

    encerrar = "0"

    while encerrar != "1":
        encerrar = input('Digite "1" para encerrar: ')

produtos = {}

input('\nSeja bem vindo a nosso sistema, aqui você poderar cadastrar produtos diversos. Digite "Enter" para continuar ')
print()

CadastrarProd (produtos)
encerrar = "0"

while encerrar != "5":

    print("\n")
    print("-"*50)
    print("Menu de tarefas:")
    print("-"*50, "\n")

    print("1 = Cadastrar um novo produto")
    print("2 = Alterar preço de um produto existente")
    print("3 = Pesquisar valor de um produto")
    print("4 = Remover um produto")
    print("5 = Ver lista de produtos")
    print("6 = Encerrar programa")

    print("\n")
    print("-"*50)

    tarefa = input("Qual tarefa deseja executar? ")
    print("-"*50)

    if tarefa == "1":
        CadastrarProd(produtos)

    if tarefa == "2":
        AlterarProd(produtos)

    elif tarefa == "3":
        PesquisarProd(produtos)
    
    elif tarefa == "4":
        RemoverProd(produtos)
    
    elif tarefa == "5":
        ImprimirProd(produtos)

    elif tarefa == "6":
        encerrar = "6"

    else:
        print("Valor inválido tente novamente")