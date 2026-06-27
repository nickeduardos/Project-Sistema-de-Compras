from recursos.funcoes_uteis import *
from datetime import datetime

ARQUIVO_BD = "DbCompras.txt"
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

def menu ():
    ''' INICIA O MENU PRINCIPAL '''
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

                user = user.upper()
                if user == "MATHEUS" and passw == 1234:
                    LoopUser = False
                    return "MATHEUS"
                
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
        '''PUXA O MENU DO USUÁRIO CHAMADO MATHEUS'''
        print ()
        user = "MATHEUS"

        aguarde (1)
        limpar_tela ()
        aguarde(1)
        
        while int:
            try:
                EscolhaMatheus = int (input (f'''BEM VINDO AO SISTEMA DE COMPRAS DO CAFÉ DA EXPERT, {user}!
                                            
1 -> ANOTAR A MINHA COMPRA
2 -> RELAÇÃO DE COMPRAS DA EQUIPE
3 -> SAIR

                                            
DIGITE O NÚMERO REFERENTE A OPÇÃO QUE DESEJA ESCOLHER: '''))
                break
            except ValueError:
                erro_de_caractere()
        limpar_tela()

        if EscolhaMatheus == 1:
            ascii_anotar ()

            print ()

            aguarde (2)

            while int:
                try:
                    compra_usuario_anotar = int (input ('''LISTA DE PRODUTOS:
                                                        
1 -> PÃO
                                                            
2 -> NATA                                                

3 -> AMBOS (PÃO E NATA)
                                                                                
DIGITE O NÚMERO DO PRODUTO QUE VOCÊ COMPROU: '''))
                    break
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
                    aguarde (5)
                    return True

                elif compra_usuario_anotar == 2:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write(f"{data_atual} | {user} | Nata\n")
                    print (f"COMPRA DE 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (5)
                    return True

                elif compra_usuario_anotar == 3:
                    with open (ARQUIVO_BD, "a") as db:
                        db.write (f"{data_atual} | {user} | Ambos (Pao e Nata)\n")
                    print (f"COMPRA DE 1 NATA E 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!")
                    aguarde (5)
                    return True

                else:
                    print ("Por Favor, Digite uma Opção Válida!")
            except ValueError:
                print ("Por Favor, Digite uma Opção Válida")


        if EscolhaMatheus == 3:
            print ('''SAINDO
OBRIGADO POR UTILIZAR O SISTEMA!''')
            aguarde (3)
            quit()