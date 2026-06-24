import os
import time
from recursos.funcoes import *
from datetime import datetime

limpar_tela()
InicializarBancosDeDados()

aguarde (1)

limpar_tela ()
alterar_cor("color a")


ascii_cafe()

aguarde(2)

texto_cafe_da_firma()

print ()

LoopUser = True
while LoopUser:
    try:
        user = str ( input ("DIGITE O SEU USUÁRIO: "))
        aguarde (0.5)
        print ()
        passw = int( input ("DIGITE A SUA SENHA: "))
        aguarde (2)
    except ValueError:
        aguarde (2)
        print ()
        print ("USUÁRIO OU SENHA INCORRETO")
        aguarde (2)
        limpar_tela ()
        aguarde (1)
        ascii_cafe ()
        texto_cafe_da_firma ()

    user = user.upper()
    print ()

    if user == "MATHEUS" and passw == 1234 :

        print ("LOGIN REALIZADO COM SUCESSO!")

        aguarde (1)
        mensagem_aguarde ()
        limpar_tela ()
        LoopUser = False
        
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
        mensagem_aguarde ()
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

            mensagem_aguarde ()

            try:
                if compra_usuario_anotar == 1:
                    # ABRIR DB, ADICIONAR UMA COMPRA DE PAO NO USUARIO MATHEUS
                    print (f'''COMPRA DE 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!
OBRIGADO POR UTILIZAR O PROGRAMA!''')
                    aguarde (5)
                elif compra_usuario_anotar == 2:
                    # compras_nata_matheus += 1
                    print (f'''COMPRA DE 1 NATA ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!
OBRIGADO POR UTILIZAR O PROGRAMA!''')
                    aguarde (5)
                elif compra_usuario_anotar == 3:
                    # compras_pao_e_nata_matheus += 1
                    print (f'''COMPRA DE 1 NATA E 1 PÃO ADICIONADA AO RELATÓRIO DE COMPRAS DE {user}!
OBRIGADO POR UTILIZAR O PROGRAMA!''')
                    aguarde (5)
                else:
                    print ("Por Favor, Digite uma Opção Válida!")
            except ValueError:
                print ("Por Favor, Digite uma Opção Válida")

                
            else:
                print ("USUÁRIO OU SENHA INCORRETO")
                aguarde (3)
                limpar_tela()
                aguarde (1)
                ascii_cafe()
                texto_cafe_da_firma()
                print ()
                LoopUser = True

ascii_cafe ()
print ()
aguarde (0.5)