import os
import time

def InicializarBancosDeDados ():
    ARQUIVO_BD = "DbCompras.txt"
    if not os.path.exists(ARQUIVO_BD):
        with open (ARQUIVO_BD, "w", encoding = "utf-8") as db:
            pass
        for numeros in range(4):
            print(f"Aguarde, Criando Banco de dados{"." * numeros}")
            time.sleep (1)
            limpar_tela()
    else: 
        for numeros in range(4):
            print(f"Aguarde, Inicializando Banco de dados{"." * numeros}")
            time.sleep (0.5)
            limpar_tela()

def texto_cafe_da_firma ():
    print ('''BEM VINDO AO SISTEMA DE COMPRAS DO CAFÉ DA EXPERT!
senha matheus 123
senha jhan 456
senha nick 789
LISTA DE USUÁRIOS:

-> MATHEUS

-> JHANPIERRI
       
-> NICK''')

def ascii_cafe ():
    print ('''
 ______     ______     ______   ______        _____     ______   
/\  ___\   /\  __ \   /\  ___\ /\  ___\      /\  __-.  /\  __ \  
\ \ \____  \ \  __ \  \ \  __\ \ \  __\      \ \ \/\ \ \ \  __ \ 
 \ \_____\  \ \_\ \_\  \ \_\    \ \_____\     \ \____-  \ \_\ \_\

                                                    
 ______   __     ______     __    __     ______                  
/\  ___\ /\ \   /\  == \   /\ "-./  \   /\  __ \                 
\ \  __\ \ \ \  \ \  __<   \ \ \-./\ \  \ \  __ \                
 \ \_\    \ \_\  \ \_\ \_\  \ \_\ \ \_\  \ \_\ \_\               
  \/_/     \/_/   \/_/ /_/   \/_/  \/_/   \/_/\/_/               
''')
    
def ascii_anotar ():
    print ('''
    _    _   _  ___ _____  _    ____       _                             
   / \  | \ | |/ _ \_   _|/ \  |  _ \     / \                            
  / _ \ |  \| | | | || | / _ \ | |_) |   / _ \                           
 / ___ \| |\  | |_| || |/ ___ \|  _ <   / ___ \                          
/_/  _\_\_| \_|\___/ |_/_/ _ \_\_| \_\_/_/_  \_\ __ ____  ____      _    
|  \/  |_ _| \ | | | | |  / \     / ___/ _ \|  \/  |  _ \|  _ \    / \   
| |\/| || ||  \| | |_| | / _ \   | |  | | | | |\/| | |_) | |_) |  / _ \  
| |  | || || |\  |  _  |/ ___ \  | |__| |_| | |  | |  __/|  _ <  / ___ \ 
|_|  |_|___|_| \_|_| |_/_/   \_\  \____\___/|_|  |_|_|   |_| \_\/_/   \_\
''')

def ascii_relatorio():
    print ('''
 _____  ______ _            _______ ____  _____  _____ ____  
|  __ \|  ____| |        /\|__   __/ __ \|  __ \|_   _/ __ \ 
| |__) | |__  | |       /  \  | | | |  | | |__) | | || |  | |
|  _  /|  __| | |      / /\ \ | | | |  | |  _  /  | || |  | |
| | \ \| |____| |____ / ____ \| | | |__| | | \ \ _| || |__| |
|_|__\_\______|______/_/    \_\_|  \____/|_|  \_\_____\____/ 
|  __ \|  ____|                                              
| |  | | |__                                                 
| |  | |  __|                                                
| |__| | |____                                               
|_____/|______|_  __ _____  _____             _____          
 / ____/ __ \|  \/  |  __ \|  __ \     /\    / ____|         
| |   | |  | | \  / | |__) | |__) |   /  \  | (___           
| |   | |  | | |\/| |  ___/|  _  /   / /\ \  \___ \          
| |___| |__| | |  | | |    | | \ \  / ____ \ ____) |         
 \_____\____/|_|  |_|_|    |_|  \_\/_/    \_\_____/          
''')
    
def erro_de_caractere ():
    print ("POR FAVOR, DIGITE O NÚMERO DA OPÇÃO QUE DESEJA.")
    time.sleep (2)
    limpar_tela ()

def aguarde (segundos):
    time.sleep (segundos)

def mensagem_aguarde ():
    time.sleep (0.5)
    for contagem_numeros in range (1,4):
        limpar_tela ()
        print (f"AGUARDE{"." * contagem_numeros}")
        time.sleep (1)
        limpar_tela ()
    time.sleep (1)

def limpar_tela ():
    os.system("cls")