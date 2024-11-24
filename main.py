# Desafio 01
# Desafio referente ao módulo: Introdução ao Python


def show_menu():
    menu_entries = [
        "Adicionar contato", 
        "Visualizar lista de contatos",
        "Editar contato",
        "Marcar/desmarcar contato como favorito",
        "Visualizar lista de contatos favoritos",
        "Apagar contato",
        "Sair"
        ]
    
    print()
    for index, entry in enumerate(menu_entries, start=1):
        print(f"{index}. {entry}.")
 
    return


def get_contact():
    name = input("Digite o nome do contato:")
    number = input("Digite o número de telefone do contato:")
    email = input("Digite o email do contato:")

    contact = {"name":name, "number":number, "email":email, "favorite":False}
    return contact


def add_contact(contacts):
    try:
        contact = get_contact()
        contacts.append(contact)

    except:
        print("Erro: Dados inválidos. Cancelando operação.")
    
    return 


def show_contacts(contacts, show_all=True):
    for index, contact in enumerate(contacts, start=1):
        if show_all or contact["favorite"]:
            print(f"{index}.  {contact['name']}")
            print(f"\tTelefone: {contact['number']}")
            print(f"\tEmail:    {contact['email']}")
            fav = "Sim" if contact["favorite"] else "Não"
            print(f"\tFavorito: {fav}")
    return


def edit_contact(contacts):
    try:
        index = int(input("Digite o índice do contato para editar:")) -1
        contact = get_contact()
        contacts[index] = contact

    except:
        print("Erro: Dados inválidos. Cancelando operação.")
    
    return 


def set_favorite_contact(contacts):
    try:
        index = int(input("Digite o índice do contato para marcar/desmarcar como favorito:")) -1
        contacts[index]["favorite"] = not contacts[index]["favorite"]

    except:
        print("Erro: Dados inválidos. Cancelando operação.")
    
    return 


def delete_contact(contacts):
    try:
        index = int(input("Digite o índice do contato para apagar:")) -1
        del contacts[index]

    except:
        print("Erro: Dados inválidos. Cancelando operação.")
    
    return 


def main():
    contacts = []

    while True:
        show_menu()
        try:
            option = int(input("Digite a opção escolhida: "))

        except:
            print("Erro: Opção inválida.")

        else:
            if option == 1:
                # adicionar contato
                add_contact(contacts)

            elif option == 2:
                # visualizar contatos
                show_contacts(contacts)

            elif option == 3:
                # editar contato
                edit_contact(contacts)

            elif option == 4:
                # marcar/desmarcar favorito
                set_favorite_contact(contacts)

            elif option == 5:
                # exibir favoritos
                show_contacts(contacts, False)

            elif option == 6:
                # apagar contato
                delete_contact(contacts)
                pass

            elif option == 7:
                break

            else:
                print("Erro: Opção inválida.")
    return


main()