# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def insert_estoque():
    print("olá")
    estoque_dict = {}
    print("Entre com os produtos no estoque. Quando estiver satisfeito escreva 'pare'")
    while True:
        produto = input("Insira produto: ").strip().lower()
        if produto == "pare":
            break
        quantidade = input("Insira quantidade: ")
        if quantidade == "pare":
            break
        estoque_dict[produto] = quantidade

    print()
    for produto, quant in estoque_dict.items():
        print(f"{produto.title()}: {quantidade}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi")
    insert_estoque()