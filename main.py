from recursos.funcoes_mescladas import *

#MENU PRINCIPAL
EscolhaDoUsuarioNoMenu = menu()

#MENU MATHEUS
if EscolhaDoUsuarioNoMenu == "MATHEUS":
    print ("LOGIN REALIZADO COM SUCESSO!")
    while menu_matheus:
        menu_matheus()

elif EscolhaDoUsuarioNoMenu == "JHANPIERRI":
    print ("LOGIN REALIZADO COM SUCESSO!")
    while menu_jhanpierri:
        menu_jhanpierri()

elif EscolhaDoUsuarioNoMenu == "NICK":
    print ("LOGIN REALIZADO COM SUCESSO!")
    while menu_nick:
        menu_nick()