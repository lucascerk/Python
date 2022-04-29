import classefila

tamanho = int(input("Digite o tamanho da fila: "))
f=classefila.Fila(tamanho)

opc=1
while opc != 9:
    opc = int(input("\n1 - Empilha  2 - Desempilha  3 - primeiro item da fila  4 - Exibe fila  5-empilha(remove()) 6-insere(desempilha()) \nSelecione: "))
    if opc == 1:
        if f.filaCheia():
            print("Fila cheia!")
        else:
            x = int(input("Digite o valor para adicionar a fila: "))
            f.insere(x)
            print("Inserido!")
    
    elif opc == 2:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            f.remove()
            print("Removido!")

    elif opc == 3:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            print(f.primeiro())
    
    elif opc == 4:
        if f.filaVazia():
            print("Fila vazia!")
        else:
            print("Exibindo fila:", f.getFila())
    
    elif opc == 5:
        if f.filaVazia():
            print("Pilha vazia....")
        else:
            f.insere(f.remove())
            print("Desempilhado")

    elif opc == 6:
        if f.filaVazia():
            print("Pilha vazia....")
        else:
            f.insere(f.primeiro())
            print("Sucesso")
        
    elif opc == 9:
        print("Fim!")

else:
    print("Opção inválida!")
