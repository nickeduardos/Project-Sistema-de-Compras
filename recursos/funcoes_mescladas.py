from recursos.funcoes_unicas import *
from datetime import datetime

ARQUIVO_BD = "DbCompras.txt"
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

def menu():
    '''Inicia o menu principal'''
    rodando = True
    while rodando:
        limpar_tela()
        InicializarBancosDeDados()

        aguarde (1)

        limpar_tela ()

        ascii_cafe()

        aguarde(2)

        texto_cafe_da_firma()

        print ()

        LoopUser = True
        while LoopUser:
            try:
                user = str ( input ("DIGITE O SEU USUÁRIO: "))
                passw = int( input ("DIGITE A SUA SENHA: "))
                aguarde (1)

                if user == "MATHEUS" and passw == 123:
                    LoopUser = False
                    return "MATHEUS"
                
                elif user == "JHANPIERRI" and passw == 456:
                    LoopUser = False
                    return "JHANPIERRI"

                elif user == "NICK" and passw == 789:
                    LoopUser = False
                    return "NICK"
                
                else:
                    print ("USUÁRIO OU SENHA INCORRETO")
                    aguarde (3)
                    limpar_tela()
                    aguarde (1)
                    ascii_cafe()
                    texto_cafe_da_firma()
                    print ()
                    LoopUser = True

            except ValueError:
                aguarde (2)
                print ()
                print ("USUÁRIO OU SENHA INCORRETO")
                aguarde (2)
                limpar_tela ()  
                aguarde (1)
                ascii_cafe ()
                texto_cafe_da_firma ()

def menu_matheus():
    '''Puxa o menu do usuario chamado matheus'''
    print ()
    user = "MATHEUS"
    aguarde (1)
    limpar_tela ()
    aguarde(1)

    while int:
        try:
            EscolhaMenuUser = int (input (f'''BEM VINDO AO SISTEMA DE COMPRAS DO CAFÉ DA EXPERT, {user}!
                                            
[1] ANOTAR A MINHA COMPRA
[2] RELAÇÃO DE COMPRAS DA EQUIPE
[3] SAIR

DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA ESCOLHER: '''))
            break
        except ValueError:
            print ("ERRO! Por Favor, Digite o Número da Opção que Deseja.")
            aguarde (3)
            limpar_tela()

    if EscolhaMenuUser == 1:
        limpar_tela ()

        ascii_anotar ()

        print ()

        aguarde (2)

        rodando_primeiro = True
        rodando_segundo = True
        while rodando_primeiro:
            while rodando_segundo:
                try:
                    compra_usuario_anotar = int (input ('''LISTA DE PRODUTOS:
                                                            
[1] PÃO
                                                                
[2] NATA                                                

[3] AMBOS (PÃO E NATA)

[4] VOLTAR PARA O MENU PRINCIPAL
                                                                                    
DIGITE O NÚMERO DO PRODUTO QUE VOCÊ COMPROU: '''))
                    rodando_segundo = False
                except ValueError:
                        print ("POR FAVOR, DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA.")
                        aguarde (2)
                        limpar_tela ()
                        aguarde (1)
                        ascii_anotar ()
                
            limpar_tela()

            try:
                if compra_usuario_anotar == 1:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Pao\n")
                    print (f"COMPRA DE 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 2:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write(f"{data_atual} | {user} | Nata\n")
                    print (f"COMPRA DE 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 3:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Ambos (Pao e Nata)\n")
                    print (f"COMPRA DE 1 PÃO E 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 4:
                    limpar_tela()
                    tem_certeza = int (input ("Você realmente deseja voltar para o menu principal? [1] Sim [2] Não: "))
                    if tem_certeza == 1:
                        return

                    elif tem_certeza == 2:
                        aguarde (1)
                        rodando_primeiro = True
                        rodando_segundo = True
                        limpar_tela ()

                    else:
                        print ("Por Favor, Digite uma Opção Válida!")                    

                else:
                    print ("Por Favor, Digite uma Opção Válida!")
                    aguarde (3)
                    limpar_tela()
                    rodando_primeiro = True
                    rodando_segundo = True
                    
            except ValueError:
                print ("Por Favor, Digite uma Opção Válida")

    elif EscolhaMenuUser == 2:
        limpar_tela()
        exibir_relatorio()

    elif EscolhaMenuUser == 3:
        while int:
            try:
                tem_certeza = int (input ("\nVocê realmente deseja sair do programa? [1] Sim [2] Não: "))
                break
            except ValueError:
                print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
                aguarde (2)

        if tem_certeza == 1:
            limpar_tela()
            print ('''SAINDO
OBRIGADO POR UTILIZAR O SISTEMA!''')
            aguarde (3)
            quit()

        elif tem_certeza == 2:
            return False
                
        else:
            print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
    
    else:
        print ("ERRO! POR FAVOR, DIGITE UMA OPÇÃO VÁLIDA.")
        aguarde (3)
        limpar_tela()

def menu_jhanpierri():
    '''Puxa o menu do usuario chamado jhan'''
    print ()
    user = "JHANPIERRI"
    aguarde (1)
    limpar_tela ()
    aguarde(1)

    while int:
        try:
            EscolhaMenuUser = int (input (f'''BEM VINDO AO SISTEMA DE COMPRAS DO CAFÉ DA EXPERT, {user}!
                                            
[1] ANOTAR A MINHA COMPRA
[2] RELAÇÃO DE COMPRAS DA EQUIPE
[3] SAIR

DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA ESCOLHER: '''))
            break
        except ValueError:
            print ("ERRO! Por Favor, Digite o Número da Opção que Deseja.")
            aguarde (3)
            limpar_tela()

    if EscolhaMenuUser == 1:
        limpar_tela ()

        ascii_anotar ()

        print ()

        aguarde (2)

        rodando_primeiro = True
        rodando_segundo = True
        while rodando_primeiro:
            while rodando_segundo:
                try:
                    compra_usuario_anotar = int (input ('''LISTA DE PRODUTOS:
                                                            
[1] PÃO
                                                                
[2] NATA                                                

[3] AMBOS (PÃO E NATA)

[4] VOLTAR PARA O MENU PRINCIPAL
                                                                                    
DIGITE O NÚMERO DO PRODUTO QUE VOCÊ COMPROU: '''))
                    rodando_segundo = False
                except ValueError:
                        print ("POR FAVOR, DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA.")
                        aguarde (2)
                        limpar_tela ()
                        aguarde (1)
                        ascii_anotar ()
                
            limpar_tela()

            try:
                if compra_usuario_anotar == 1:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Pao\n")
                    print (f"COMPRA DE 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 2:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write(f"{data_atual} | {user} | Nata\n")
                    print (f"COMPRA DE 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 3:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Ambos (Pao e Nata)\n")
                    print (f"COMPRA DE 1 PÃO E 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 4:
                    limpar_tela()
                    tem_certeza = int (input ("Você realmente deseja voltar para o menu principal? [1] Sim [2] Não: "))
                    if tem_certeza == 1:
                        return

                    elif tem_certeza == 2:
                        aguarde (1)
                        rodando_primeiro = True
                        rodando_segundo = True
                        limpar_tela ()

                    else:
                        print ("Por Favor, Digite uma Opção Válida!")                    

                else:
                    print ("Por Favor, Digite uma Opção Válida!")
                    aguarde (3)
                    limpar_tela()
                    rodando_primeiro = True
                    rodando_segundo = True
                    
            except ValueError:
                print ("Por Favor, Digite uma Opção Válida")

    elif EscolhaMenuUser == 2:
        limpar_tela()
        exibir_relatorio()

    elif EscolhaMenuUser == 3:
        while int:
            try:
                tem_certeza = int (input ("\nVocê realmente deseja sair do programa? [1] Sim [2] Não: "))
                break
            except ValueError:
                print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
                aguarde (2)

        if tem_certeza == 1:
            limpar_tela()
            print ('''SAINDO
OBRIGADO POR UTILIZAR O SISTEMA!''')
            aguarde (3)
            quit()

        elif tem_certeza == 2:
            return False
                
        else:
            print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
    
    else:
        print ("ERRO! POR FAVOR, DIGITE UMA OPÇÃO VÁLIDA.")
        aguarde (3)
        limpar_tela()

def menu_nick():
    '''Puxa o menu do usuario chamado matheus'''
    print ()
    user = "NICK"
    aguarde (1)
    limpar_tela ()
    aguarde(1)

    while int:
        try:
            EscolhaMenuUser = int (input (f'''BEM VINDO AO SISTEMA DE COMPRAS DO CAFÉ DA EXPERT, {user}!
                                            
[1] ANOTAR A MINHA COMPRA
[2] RELAÇÃO DE COMPRAS DA EQUIPE
[3] SAIR

DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA ESCOLHER: '''))
            break
        except ValueError:
            print ("ERRO! Por Favor, Digite o Número da Opção que Deseja.")
            aguarde (3)
            limpar_tela()

    if EscolhaMenuUser == 1:
        limpar_tela ()

        ascii_anotar ()

        print ()

        aguarde (2)

        rodando_primeiro = True
        rodando_segundo = True
        while rodando_primeiro:
            while rodando_segundo:
                try:
                    compra_usuario_anotar = int (input ('''LISTA DE PRODUTOS:
                                                            
[1] PÃO
                                                                
[2] NATA                                                

[3] AMBOS (PÃO E NATA)

[4] VOLTAR PARA O MENU PRINCIPAL
                                                                                    
DIGITE O NÚMERO DO PRODUTO QUE VOCÊ COMPROU: '''))
                    rodando_segundo = False
                except ValueError:
                        print ("POR FAVOR, DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA.")
                        aguarde (2)
                        limpar_tela ()
                        aguarde (1)
                        ascii_anotar ()
                
            limpar_tela()

            try:
                if compra_usuario_anotar == 1:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Pao\n")
                    print (f"COMPRA DE 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 2:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write(f"{data_atual} | {user} | Nata\n")
                    print (f"COMPRA DE 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 3:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Ambos (Pao e Nata)\n")
                    print (f"COMPRA DE 1 PÃO E 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (3)
                    return

                elif compra_usuario_anotar == 4:
                    limpar_tela()
                    tem_certeza = int (input ("Você realmente deseja voltar para o menu principal? [1] Sim [2] Não: "))
                    if tem_certeza == 1:
                        return

                    elif tem_certeza == 2:
                        aguarde (1)
                        rodando_primeiro = True
                        rodando_segundo = True
                        limpar_tela ()

                    else:
                        print ("Por Favor, Digite uma Opção Válida!")                    

                else:
                    print ("Por Favor, Digite uma Opção Válida!")
                    aguarde (3)
                    limpar_tela()
                    rodando_primeiro = True
                    rodando_segundo = True
                    
            except ValueError:
                print ("Por Favor, Digite uma Opção Válida")

    elif EscolhaMenuUser == 2:
        limpar_tela()
        exibir_relatorio()

    elif EscolhaMenuUser == 3:
        while int:
            try:
                tem_certeza = int (input ("\nVocê realmente deseja sair do programa? [1] Sim [2] Não: "))
                break
            except ValueError:
                print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
                aguarde (2)

        if tem_certeza == 1:
            limpar_tela()
            print ('''SAINDO
OBRIGADO POR UTILIZAR O SISTEMA!''')
            aguarde (3)
            quit()

        elif tem_certeza == 2:
            return False
                
        else:
            print ("ERRO. Por favor, Digite [1] para SIM ou [2] para NÃO.")
    
    else:
        print ("ERRO! POR FAVOR, DIGITE UMA OPÇÃO VÁLIDA.")
        aguarde (3)
        limpar_tela()

def exibir_relatorio():
    '''Exibe o relatorio de compras de toda a equipe'''
    rodando = True
    while rodando:
        ascii_relatorio()

        if not os.path.exists(ARQUIVO_BD) or os.stat (ARQUIVO_BD).st_size == 0:
            print ("NENHUMA COMPRA REGISTRADA ATÉ O MOMENTO")
            aguarde(2)
            return
        
        print ((f"{'DATA':<16} | {'FUNCIONÁRIO'} | {'PRODUTO':<15}"))
        print ("-" * 60)
        
        with open (ARQUIVO_BD, "r") as db:
            for linha in db:
                if linha.strip:
                    data, funcionario, produto = [item.strip() for item in linha.split("|")]
                    print (f"{data:<15} | {funcionario:<11} | {produto:<15}")
        
        print ("-" * 60)
        print ()
        while int:
            try:
                voltar = int(input ("Digite [1] para voltar para o menu principal: "))
                break
            except ValueError:
                print ("ERRO. POR FAVOR, DIGITE APENAS NÚMEROS!\n")
                aguarde(3)

        if voltar == 1:
            rodando = False

        else:
            print ("ERRO. POR FAVOR, SE QUISER VOLTAR DIGITE [1]")
            aguarde(3)