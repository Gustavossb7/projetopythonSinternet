import time
import random
import string
import math
from selenium import webdriver
import pyautogui
import pyperclip
from socket import gethostbyname, create_connection
import string
from random import randint
import subprocess
import socket
from datetime import datetime
import requests
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

moeda = 'USDT'
moeda2 = 'PAXG'
moeda3 = 'ETH'
base = "BRL"


def random_letter():
    alphabet = list(string.ascii_letters)
    return alphabet[randint(0, 50)]


senha1 = '0codigoNietzsche'
autenticacao1 = 3301


def leiaSenha(msg):
    ok = False
    while True:
        senha = str(input(msg))
        if senha == senha1:
            ok = True
        else:
            print('ERRO! Digite a senha válida')
        if ok:
            break
    return senha


def leiaAutenticacao(msg):
    ok = False
    while True:
        autenticacao = int(input(msg))
        if autenticacao == autenticacao1:
            ok = True
        else:
            print('ERRO! Digite a autenticação válida')
        if ok:
            break
    return autenticacao


def leiaOpcao(msg):
    ok = False
    while True:
        opcao = int(input(msg))
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
            ok = True
        else:
            print('ERRO! Digite uma opção válida')
        if ok:
            break
    return opcao


def leiaCriptografia(msg):
    ok = False
    while True:
        criptografar = str(input(msg))
        if criptografar == 'sim' or criptografar == 'nao' or criptografar == 'não':
            ok = True
        else:
            print('ERRO! Digite uma opção válida')
        if ok:
            break
    return criptografar


def leiaNcarteira(msg):
    ok = False
    while True:
        ncarteira = int(input(msg))
        if ncarteira == 1 or ncarteira == 2 or ncarteira == 3 or ncarteira == 4 or ncarteira == 5 or ncarteira == 6 or ncarteira == 7 or ncarteira == 8:
            ok = True
        else:
            print('ERRO! Digite uma opção válida')
        if ok:
            break
    return ncarteira


def criptografia(msg):
    tradutor = ""
    for letra in msg:
        if letra in "Aa":
            tradutor = tradutor + "H"
        elif letra in "Bb":
            tradutor = tradutor + "H"
        elif letra in "Cc":
            tradutor = tradutor + "?"
        elif letra in "Dd":
            tradutor = tradutor + "/"
        elif letra in "Ee":
            tradutor = tradutor + "z"
        elif letra in "Ff":
            tradutor = tradutor + "g"
        elif letra in "Gg":
            tradutor = tradutor + "A"
        elif letra in "Hh":
            tradutor = tradutor + "L"
        elif letra in "Ii":
            tradutor = tradutor + "<H>"
        elif letra in "Jj":
            tradutor = tradutor + "-"
        elif letra in "Kk":
            tradutor = tradutor + "´"
        elif letra in "Ll":
            tradutor = tradutor + "J"
        elif letra in "Mm":
            tradutor = tradutor + "j"
        elif letra in "Nn":
            tradutor = tradutor + "wW"
        elif letra in "Oo":
            tradutor = tradutor + "9!"
        elif letra in "Pp":
            tradutor = tradutor + "P"
        elif letra in "Qq":
            tradutor = tradutor + "r"
        elif letra in "Rr":
            tradutor = tradutor + "r"
        elif letra in "Ss":
            tradutor = tradutor + "r"
        elif letra in "Tt":
            tradutor = tradutor + "ah"
        elif letra in "Uu":
            tradutor = tradutor + "["
        elif letra in "Vv":
            tradutor = tradutor + "+"
        elif letra in "Ww":
            tradutor = tradutor + "ll"
        elif letra in "Xx":
            tradutor = tradutor + "D"
        elif letra in "Yy":
            tradutor = tradutor + "Y"
        elif letra in "Zz":
            tradutor = tradutor + "i"
        elif letra in "1":
            tradutor = tradutor + "gI-"
        elif letra in "2":
            tradutor = tradutor + "Ç"
        elif letra in "3":
            tradutor = tradutor + "]"
        elif letra in "4":
            tradutor = tradutor + "1"
        elif letra in "5":
            tradutor = tradutor + "_"
        elif letra in "6":
            tradutor = tradutor + ":)"
        elif letra in "7":
            tradutor = tradutor + ":("
        elif letra in "8":
            tradutor = tradutor + ":):"
        elif letra in "9":
            tradutor = tradutor + "^"
        else:
            tradutor = tradutor + letra
    return tradutor


def conectadoInternet():
    tentativas = 0
    servidorRemoto = 'www.google.com.br'

    while tentativas < 3:
        if tentativas == 1:
            servidorRemoto = 'www.lds.org'
        elif tentativas == 2:
            servidorRemoto = 'www.msn.com'

        try:
            host = gethostbyname(servidorRemoto)
            s = create_connection((host, 80), 2)
            return True
        except:
            tentativas += 1

    return False


laco = True
laco1 = True
laco2 = True

print('')
print('Access Matheus')
print('')
senha = leiaSenha('Digite sua senha: ')
time.sleep(1.1)
print('')
print('Credencial verificada com sucesso.')
time.sleep(0.8)
print('')
print('')
print('')
print('Estabelecendo conexão com o servidor.')
time.sleep(4.1)
print('')


print('')
print('')
print('Por favor autentique o canal.')
time.sleep(1.1)
print('')
print('')
autenticacao = leiaAutenticacao('Digite sua autenticação: ')
print('')
print('Etapa de verificação credencial e autenticação concluida com sucesso.')
print('')
print('')
print("Acess", socket.gethostname(), "   ", datetime.now(), "imported")
print('')
print('')
print('Bem vindo Matheus')
print('')

saldo1 = float(314.51265865185)  # paxg
saldo2 = float(331.79469940991)  # paxg
saldo3 = float(369.67412551236)  # paxg
saldo4 = float(366.35878201318)  # paxg
saldo5 = float(546_228.49662)  # USDT
saldo6 = float(484_625.37828)  # USDT

while laco2 == True:
        print('')
        print('')
        opcao = leiaOpcao('Digite o número da opção que deseja: ')

        # automação rede
        if opcao == 1:
                    print("")
                    print("")
                    print("Informações de rede: ")
                    print("")
                    print("")
                    time.sleep(2)
                    print("O sistema possui ID de rede classe dhcp e IPv6 permitidas para o adaptador ")
                    print("")
                    print('''
                                Possuimos uma rede padrão que exibe apenas o endereço IP, a máscara de sub-rede e
                                o gateway padrão para cada adaptador limitado ao TCP/IP.
                                Para Release e Renew, se nenhum nome de adaptador for especificado,
                                as concessões de endereços IP para todos os adaptadores limitados
                                ao TCP/IP serão liberadas ou renovadas.
    
                                Para Setclassid e Setclassid6, se nenhuma ClassId for especificada, ClassId
                                será removida.''')
                    print("")
                    # pyautogui.press("win")
                    # pyautogui.write('cmd')
                    # pyautogui.press("enter")
                    # time.sleep(1)
                    # pyperclip.copy('ipconfig')
                    # time.sleep(1)
                    # comando = pyperclip.paste()
                    # pyautogui.write(comando)
                    # pyautogui.press("enter")
                    # pyautogui.press("f11")
                    # time.sleep(2)
                    # pyautogui.leftClick(x=473, y=437)
                    # pyautogui.keyDown('shift')
                    # pyautogui.leftClick(x=7, y=71)
                    # pyautogui.keyUp('shift')
                    # pyautogui.hotkey('ctrl', 'c')
                    # textoRede = pyperclip.paste()
                    # time.sleep(5)
                    #
                    # pyautogui.click(x=117, y=476)
                    # pyperclip.copy('netsh wlan show drivers')
                    # time.sleep(1)
                    # comando2 = pyperclip.paste()
                    # pyautogui.write(comando2)
                    # pyautogui.press("enter")
                    # time.sleep(3)
                    # pyautogui.leftClick(x=1, y=471)
                    # pyautogui.keyDown('shift')
                    # pyautogui.leftClick(x=628, y=1017)
                    # pyautogui.keyUp('shift')
                    # pyautogui.hotkey('ctrl', 'c')
                    # textoRede2 = pyperclip.paste()
                    # pyautogui.press("f11")
                    # time.sleep(1)
                    # pyautogui.click(x=868, y=1065)
                    # time.sleep(1)
                    # pyautogui.click(x=800, y=990)

                    time.sleep(2)
                    print('Carregando automações...')
                    print('')
                    print('')
                    print('')
                    print('')
                    time.sleep(3)

                    # -*- coding: utf-8 -*-
                    subprocess.run(["ipconfig"])
                    print('')
                    print('')
                    print('')
                    print('')
                    time.sleep(3)
                    print('')
                    print('')
                    print('')
                    subprocess.call("netsh wlan show drivers")

                    # print(textoRede)
                    # print('')
                    # print('')
                    # print('')
                    # print('')
                    # print('')
                    # print('')
                    # time.sleep(3)
                    # print(textoRede2)

                    print('')
                    print('')
                    print('')
                    print('')
                    time.sleep(3)
                    print(' ')
                    print(' ')
                    # print('A rede não possui segurança a nível de criptografia de ponta a ponta. ')
                    print(' ')

                    criptografar = leiaCriptografia(
                        'Deseja criptografar a conexão do programa, assim criando um a canal seguro? ')

                    if criptografar == 'sim'.upper().lower():
                        print('')
                        print(' ')
                        time.sleep(2.4)
                        print('''
                                                JDxK4ZlvptmPYmK3LmYd3QoSFXpHI4FBYOQJ2GBG7LrBz4lOODYq291W7lSnraA-dXOO
                                                u1JjP8Lsusb5jP6NyYkUFDlCBCs4Rixcx2IKhOB88opiTEBQHyTfNf2XDjDORLlaFjOlLaxr2nxnQ
                                                juydnq0zRsmF0m83JqQbNkcUmPTwzuVxVQ5MXnHoyjtRlxk0eR3OmKwtmG_Re5q9BYPpZQ7mepTZp
                                                DJ6fkJMfqYdtS_n_RH43E3Bw_LM3K90qOR''')
                    print(' ')

                    if criptografar == 'não'.upper().lower():
                        print('')
                        print("Não foi possível fazer o login")

                    if criptografar == 'nao'.upper().lower():
                        print('')
                        print("Não foi possível fazer o login")

        # carteiras
        if opcao == 2:
            print('''	Carteiras dísponíveis:
                    Carteira R1
                    Carteira R2
                    Carteira R3
                    Carteira R4
                    Carteira I1
                    Carteira FTX''')
            print(' ')
            opcao1 = leiaCriptografia('Deseja inspecionar o circuito interno? ')
            time.sleep(1.5)
            if opcao1 == 'não'.upper().lower() or opcao1 == 'nao'.upper().lower():
                print('')
            if opcao1 == 'sim'.upper().lower():

                print('')
                ncarteira = leiaNcarteira('Digite o número da carteira: ')
                time.sleep(1.4)
                print('')

                total = float(17_152_726.82)
                # real1 = float(2_543_484.38)
                # real2 = float(2_702_452.1563)
                # real3 = float(2_861_419.9302)
                # real4 = float(3_020_387.7041)
                # real5 = float(2_622_968.26)
                # real6 = float(2_305_032.72)

                real1 = float(saldo1 * 8745.92)
                real2 = float(saldo2 * 8745.92)
                real3 = float(saldo3 * 8745.92)
                real4 = float(saldo4 * 8745.92)
                real5 = float(saldo5 * 5.10)
                real6 = float(saldo6 * 5.10)

                la1 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))
                la2 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))
                la3 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))

                na1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na5 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na6 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na7 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
                na8 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

                ID1 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
                ID2 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
                ID3 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
                ID4 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
                ID5 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
                ID6 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)

                ta1 = random.choice([11, 12, 13, 14, 15])

                ta2 = random.choice([11, 12, 13, 14, 15])

                ta3 = 40 - (ta1 + ta2)

                al1 = round((100 * real1) / total, 3)
                al2 = round((100 * real2) / total, 3)
                al3 = round((100 * real3) / total, 3)
                al4 = round((100 * real4) / total, 3)
                al5 = round((100 * real5) / total, 3)
                al6 = round((100 * real6) / total, 3)

                if ncarteira == 1:
                    print(
                        'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                            saldo1, al1))
                    print('')
                    print('')
                    print('')
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")

                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R1                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo1, al1))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo1, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2=taxa*10
                        taxaPaxg = random.choice(
                            [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845, 0.000451243811,
                             0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272, 0.007470163288])

                        taxaPaxg2 = random.choice(
                            [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641, 0.026274362743,
                             0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062, 0.037388547043])

                        taxaUsdt = random.choice(
                            [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988, 1.39284, 8.85470,
                             13.39448])

                        taxaUsdt2 = random.choice(
                            [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639, 27.45124,
                             49.73885,
                             67.16942])
                        print('')
                        if destino == 5 or destino == 6:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8,
                                                                       la2, la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg2))

                            if confirmar == 'sim'.upper().lower().strip():
                                saldo1 = saldo1 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = (saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = (saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = (saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = (saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1
                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))

                        else:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo1 = saldo1 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = (saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = (saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = (saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = (saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                time.sleep(1.5)
                                print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                time.sleep(1.5)
                                print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                time.sleep(1.5)
                                print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                time.sleep(1.5)
                                cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))


                    else:
                        print('Processo Finalizado')

                if ncarteira == 2:
                    print(
                        'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                            saldo2, al2))
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")

                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R2                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo2, al2))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo2, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                        print('')
                        print('')
                    print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2 = taxa * 10
                        taxaPaxg = random.choice(
                            [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845, 0.000451243811,
                             0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272, 0.007470163288])

                        taxaPaxg2 = random.choice(
                            [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641, 0.026274362743,
                             0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062, 0.037388547043])

                        taxaUsdt = random.choice(
                            [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988, 1.39284, 8.85470,
                             13.39448])

                        taxaUsdt2 = random.choice(
                            [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639, 27.45124,
                             49.73885,
                             67.16942])
                        print('')
                        if destino == 5 or destino == 6:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8,
                                                                       la2, la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg2))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo2 = saldo2 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))

                        else:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo2 = saldo2 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))

                    else:
                        print('Processo Finalizado')

                if ncarteira == 3:
                    print(
                        'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                            saldo3, al3))
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")

                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R3                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo3, al3))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo3, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                        print('')
                        print('')
                    print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2 = taxa * 10
                        taxaPaxg = random.choice(
                            [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845, 0.000451243811,
                             0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272, 0.007470163288])

                        taxaPaxg2 = random.choice(
                            [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641, 0.026274362743,
                             0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062, 0.037388547043])

                        taxaUsdt = random.choice(
                            [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988, 1.39284, 8.85470,
                             13.39448])

                        taxaUsdt2 = random.choice(
                            [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639, 27.45124,
                             49.73885,
                             67.16942])
                        print('')
                        if destino == 5 or destino == 6:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8,
                                                                       la2, la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg2))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo3 = saldo3 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                        else:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo3 = saldo3 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                            if destino == 1:
                                print(
                                    'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                            if destino == 2:
                                print(
                                    'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                            if destino == 3:
                                print(
                                    'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                            if destino == 4:
                                print(
                                    'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                            if destino == 5:
                                print(
                                    'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                            if destino == 6:
                                print(
                                    'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                        saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                    else:
                        print('Processo Finalizado')

                if ncarteira == 4:
                    print(
                        'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                            saldo4, al4))
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")

                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R4                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo4, al4))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo4, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                        print('')
                        print('')
                    print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2 = taxa * 10
                        taxaPaxg = random.choice(
                            [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845, 0.000451243811,
                             0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272, 0.007470163288])

                        taxaPaxg2 = random.choice(
                            [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641, 0.026274362743,
                             0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062, 0.037388547043])
                        print('')
                        if destino == 5 or destino == 6:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8,
                                                                       la2, la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} PAXG.
                                    Digite sim, para confirmar:'''.format(taxaPaxg2))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo4 = saldo4 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                        else:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8,
                                                                       la2, la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo4 = saldo4 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + valor - taxaPaxg
                                    real1 = float(saldo1 * 9097.38)
                                    al1 = round((100 * real1) / total, 3)
                                if destino == 2:
                                    saldo2 = saldo2 + valor - taxaPaxg
                                    real2 = float(saldo2 * 9097.38)
                                    al2 = round((100 * real2) / total, 3)
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaPaxg
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaPaxg
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                if destino == 5:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 6:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                    if destino == 1:
                                        print(
                                            'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                                    if destino == 2:
                                        print(
                                            'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                                    if destino == 3:
                                        print(
                                            'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                                    if destino == 4:
                                        print(
                                            'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                                    if destino == 5:
                                        print(
                                            'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                                    if destino == 6:
                                        print(
                                            'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
                                                la3))
                    else:
                        print('Processo Finalizado')

                if ncarteira == 5:
                    print(
                        'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%'.format(
                            saldo5, al5))
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira I1                      Tipo: Intermediaria')
                        print('')
                        time.sleep(0.5)
                        print('Criptomoeda: Theter (USDT)       Quantidade: {}    AL: {}% '.format(saldo5, al5))
                        print('                                           R${}'.format(
                            round(cotacaoUSDTbinance * saldo5, 1)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                    print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2 = taxa * 10
                        taxaUsdt = random.choice(
                            [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988, 1.39284, 8.85470,
                             13.39448])

                        taxaUsdt2 = random.choice(
                            [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639, 27.45124,
                             49.73885,
                             67.16942])
                        print('')
                        if destino == 1 or destino == 2 or destino == 3 or destino == 4:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} USDT.
                                    Digite sim, para confirmar:'''.format(taxaUsdt2))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo5 = saldo5 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + (valor * 1794) - taxaUsdt2
                                    real1 = (saldo1 * 5.07)
                                    saldo1 = round(saldo1, 5)
                                    al1 = round((100 * real1) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 2:
                                    saldo2 = saldo2 + (valor * 1794) - taxaUsdt2
                                    real2 = (saldo2 * 5.07)
                                    saldo2 = round(saldo2, 3)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaUsdt2
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaUsdt2
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 5:
                                    saldo5 = saldo5 + valor - taxaUsdt
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                if destino == 6:
                                    saldo6 = saldo6 + valor - taxaUsdt
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))

                        else:

                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} USDT.
                                    Digite sim, para confirmar:'''.format(taxaUsdt))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo5 = saldo5 - valor
                                if destino == 1:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 2:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaUsdt
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaUsdt
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 5:
                                    saldo5 = saldo5 + valor - taxaUsdt
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                if destino == 6:
                                    saldo6 = saldo6 + valor - taxaUsdt
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                    else:
                        print('Processo Finalizado')

                if ncarteira == 6:
                    print(
                        'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%'.format(
                            saldo6, al6))
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print("R$", cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print("R$", cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print("")
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira FTX                      Tipo: Corretora')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Theter (USDT)   Quantidade: {}    AL: {}% '.format(saldo6, al6))
                        print('                                       R${}'.format(
                            round(cotacaoUSDTbinance * saldo6, 1)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                        print('')
                        print('')
                    print('')
                    transfer = str(input('Deseja movimentar o circuito interno? '))
                    print('')
                    if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                        print('')
                    if transfer == 'sim'.upper().lower():
                        print('')
                        valor = float(input('Quantifique a tranferencia: '))
                        print('')
                        destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
                        time.sleep(1.4)
                        # taxa = random.choice(
                        # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                        # 	 0.001904,
                        # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                        # 	 0.001856])
                        # taxa2 = taxa * 10
                        taxaUsdt = random.choice(
                            [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988, 1.39284, 8.85470,
                             13.39448])

                        taxaUsdt2 = random.choice(
                            [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639, 27.45124,
                             49.73885,
                             67.16942])
                        print('')
                        if destino == 1 or destino == 2 or destino == 3 or destino == 4:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                        O valor de taxa de é {} USDT.
                                        Digite sim, para confirmar:'''.format(taxaUsdt2))

                            if confirmar == 'sim'.upper().lower().strip():
                                saldo6 = saldo6 - valor
                                if destino == 1:
                                    saldo1 = saldo1 + (valor * 1794) - taxaUsdt2
                                    real1 = (saldo1 * 5.07)
                                    saldo1 = round(saldo1, 5)
                                    al1 = round((100 * real1) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 2:
                                    saldo2 = saldo2 + (valor * 1794) - taxaUsdt2
                                    real2 = (saldo2 * 5.07)
                                    saldo2 = round(saldo2, 5)
                                    al2 = round((100 * real2) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaUsdt2
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaUsdt
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 5:
                                    saldo5 = saldo5 + valor - taxaUsdt
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                if destino == 6:
                                    saldo6 = saldo6 + valor - taxaUsdt
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                        else:
                            print(
                                '''	
                                ERC-20 Transaction: Tax pending.
                                Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5, na6, na7,
                                                                       na8, la2,
                                                                       la3))
                            time.sleep(3)
                            confirmar = leiaCriptografia('''
                                    O valor de taxa de é {} USDT.
                                    Digite sim, para confirmar:'''.format(taxaUsdt))
                            if confirmar == 'sim'.upper().lower().strip():
                                saldo6 = saldo6 - valor
                                if destino == 1:
                                    saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                    for c in range(1, 20):
                                        cont = 0
                                        while cont < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont = cont + 1
                                if destino == 2:
                                    saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)
                                    for c in range(1, 20):
                                        cont1 = 0
                                        while cont1 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)

                                            cont1 = cont1 + 1
                                if destino == 3:
                                    saldo3 = saldo3 + valor - taxaUsdt
                                    real3 = float(saldo3 * 9097.38)
                                    al3 = round((100 * real3) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 4:
                                    saldo4 = saldo4 + valor - taxaUsdt
                                    real4 = float(saldo4 * 9097.38)
                                    al4 = round((100 * real4) / total, 3)
                                    for c in range(1, 60):
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                              ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
                                        time.sleep(1.5)
                                if destino == 5:
                                    saldo5 = saldo5 + valor - taxaUsdt
                                    real5 = (saldo5 * 5.07)
                                    saldo5 = round(saldo5, 5)
                                    al5 = round((100 * real5) / total, 3)
                                if destino == 6:
                                    saldo6 = saldo6 + valor - taxaUsdt
                                    real6 = (saldo6 * 5.07)
                                    saldo6 = round(saldo6, 5)
                                    al6 = round((100 * real6) / total, 3)

                                for c in range(1, ta1):
                                    cont2 = 0
                                    while cont2 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont2 = cont2 + 1
                                for c in range(1, ta2):
                                    cont3 = 0
                                    while cont3 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont3 = cont3 + 1
                                for c in range(1, ta3):
                                    cont4 = 0
                                    while cont4 < 1:
                                        x1 = (random_letter())
                                        x2 = (random_letter())
                                        x3 = (random_letter())
                                        x4 = (random_letter())
                                        x5 = (random_letter())
                                        x6 = (random_letter())
                                        x7 = (random_letter())

                                        a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)

                                        cont4 = cont4 + 1
                                        time.sleep(1.5)
                                cont5 = 0
                                while cont5 < 1:
                                    x1 = (random_letter())
                                    x2 = (random_letter())
                                    x3 = (random_letter())
                                    x4 = (random_letter())
                                    x5 = (random_letter())
                                    x6 = (random_letter())
                                    x7 = (random_letter())

                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                    time.sleep(1.5)
                                    cont5 = cont5 + 1

                                if destino == 1:
                                    print(
                                        'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 2:
                                    print(
                                        'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 3:
                                    print(
                                        'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 4:
                                    print(
                                        'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 5:
                                    print(
                                        'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                                if destino == 6:
                                    print(
                                        'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                            saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
                    else:
                        print('Processo Finalizado')

                if ncarteira == 7:
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira R1                      Tipo: Reserva')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo1, al1))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    time.sleep(1.6)
                    print('')
                    print('')
                    print('')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira R2                      Tipo: Reserva')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo2, al2))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    time.sleep(1.6)
                    print('')
                    print('')
                    print('')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira R3                      Tipo: Reserva')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo3, al3))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    time.sleep(1.6)
                    print('')
                    print('')
                    print('')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira R4                      Tipo: Reserva')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo4, al4))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    time.sleep(1.6)
                    print('')
                    print('')
                    print('')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira I1                      Tipo: Intermediaria')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Theter (USDT)       Quantidade: {}    AL: {}% '.format(saldo5, al5))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    time.sleep(1.6)
                    print('')
                    print('')
                    print('')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('Carteira FTX                      Tipo: Corretora')
                    time.sleep(0.5)
                    print('')
                    print('Criptomoeda: Theter (USDT)   Quantidade: {}    AL: {}% '.format(saldo6, al6))
                    time.sleep(0.8)
                    print('')
                    print('Status: Chaves ativas sob gerenciamento')
                    print(
                        '------------------------------------------------------------------------------------')
                    print('')
                    print('')
                    print('')
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoUSDTbinance = resposta["price"]
                        cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                        cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)
                        print(cotacaoUSDTbinance)

                        simbolo2 = moeda2 + moeda

                        url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                        requisicao2 = requests.get(url2)
                        resposta2 = requisicao2.json()

                        cotacaoPAXGbinance = resposta2["price"]
                        cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                        cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                        cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)
                        print(cotacaoPAXGbinance)

                        # até aqui

                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                        time.sleep(4)
                        print("")
                        print("")
                        print("")
                        print("A aplicação está consultando as cotações atuais...")
                        print("")
                        options = webdriver.ChromeOptions()
                        options.add_experimental_option('excludeSwitches', ['enable-logging'])

                        print("")
                        navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                        print("")
                        print("")
                        cotacaoUSDT = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoUSDT = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hUSDT = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print(precoUSDT.text)
                        print(cotacaoUSDTbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                              volume24hUSDT.text)
                        print("")
                        print("")
                        print("")

                        print('------------------------------')
                        print("")
                        print("")

                        navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                        cotacaoPAXG = navegador.find_element("xpath",
                                                             '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        precoPAXG = navegador.find_element("xpath",
                                                           '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        marketcapPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                           '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        volume24hPAXG = navegador.find_element("xpath",
                                                               '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                        print('Preço de PAX Gold (PAXG)')
                        print(cotacaoPAXGbinance)
                        print("")
                        print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                              '           ',
                              volume24hPAXG.text)
                        print("")
                        print("")
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R1                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo1, al1))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo1, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        time.sleep(1.6)
                        print('')
                        print('')
                        print('')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R2                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo2, al2))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo2, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        time.sleep(1.6)
                        print('')
                        print('')
                        print('')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R3                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo3, al3))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo3, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        time.sleep(1.6)
                        print('')
                        print('')
                        print('')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira R4                      Tipo: Reserva')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(saldo4, al4))
                        print('                                           R${}'.format(
                            round(cotacaoPAXGbinance * saldo4, 2)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        time.sleep(1.6)
                        print('')
                        print('')
                        print('')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira I1                      Tipo: Intermediaria')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Theter (USDT)       Quantidade: {}    AL: {}% '.format(saldo5, al5))
                        print('                                           R${}'.format(
                            round(cotacaoUSDTbinance * saldo5, 1)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        time.sleep(1.6)
                        print('')
                        print('')
                        print('')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira FTX                      Tipo: Corretora')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Theter (USDT)   Quantidade: {}    AL: {}% '.format(saldo6, al6))
                        print('                                       R${}'.format(
                            round(cotacaoUSDTbinance * saldo6, 1)))
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')
                        print('')
                        print('')
                        print('')
                    print(' ')
                    opcao1 = leiaCriptografia('Deseja inspecionar o circuito interno? ')
                    time.sleep(1.5)
                    if opcao1 == 'não'.upper().lower() or opcao1 == 'nao'.upper().lower():
                        print('')
                    if opcao1 == 'sim'.upper().lower():
                        print('')
                        ncarteira = leiaNcarteira('Digite o número da carteira: ')
                        time.sleep(1.4)
                        print('')
                        if ncarteira == 1:
                            print(
                                'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                                    saldo1, al1))
                            print('')
                            print('')
                            print('')
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")

                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira R1                      Tipo: Reserva')
                                time.sleep(0.5)
                                print('')
                                print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(
                                    saldo1, al1))
                                print('                                           R${}'.format(
                                    round(cotacaoPAXGbinance * saldo1, 2)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2=taxa*10
                                taxaPaxg = random.choice(
                                    [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845,
                                     0.000451243811,
                                     0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272,
                                     0.007470163288])

                                taxaPaxg2 = random.choice(
                                    [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641,
                                     0.026274362743,
                                     0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062,
                                     0.037388547043])

                                taxaUsdt = random.choice(
                                    [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988,
                                     1.39284, 8.85470,
                                     13.39448])

                                taxaUsdt2 = random.choice(
                                    [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639,
                                     27.45124,
                                     49.73885,
                                     67.16942])
                                print('')
                                if destino == 5 or destino == 6:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8,
                                                                               la2, la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg2))

                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo1 = saldo1 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = (saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = (saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = (saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = (saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1
                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))

                                else:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo1 = saldo1 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = (saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = (saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = (saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = (saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                        time.sleep(1.5)
                                        cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))


                            else:
                                print('Processo Finalizado')

                        if ncarteira == 2:
                            print(
                                'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                                    saldo2, al2))
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")

                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira R2                      Tipo: Reserva')
                                time.sleep(0.5)
                                print('')
                                print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(
                                    saldo2, al2))
                                print('                                           R${}'.format(
                                    round(cotacaoPAXGbinance * saldo2, 2)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                                print('')
                                print('')
                            print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2 = taxa * 10
                                taxaPaxg = random.choice(
                                    [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845,
                                     0.000451243811,
                                     0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272,
                                     0.007470163288])

                                taxaPaxg2 = random.choice(
                                    [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641,
                                     0.026274362743,
                                     0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062,
                                     0.037388547043])

                                taxaUsdt = random.choice(
                                    [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988,
                                     1.39284, 8.85470,
                                     13.39448])

                                taxaUsdt2 = random.choice(
                                    [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639,
                                     27.45124,
                                     49.73885,
                                     67.16942])
                                print('')
                                if destino == 5 or destino == 6:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8,
                                                                               la2, la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg2))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo2 = saldo2 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))

                                else:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo2 = saldo2 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))

                            else:
                                print('Processo Finalizado')

                        if ncarteira == 3:
                            print(
                                'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                                    saldo3, al3))
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")

                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira R3                      Tipo: Reserva')
                                time.sleep(0.5)
                                print('')
                                print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(
                                    saldo3, al3))
                                print('                                           R${}'.format(
                                    round(cotacaoPAXGbinance * saldo3, 2)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                                print('')
                                print('')
                            print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2 = taxa * 10
                                taxaPaxg = random.choice(
                                    [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845,
                                     0.000451243811,
                                     0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272,
                                     0.007470163288])

                                taxaPaxg2 = random.choice(
                                    [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641,
                                     0.026274362743,
                                     0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062,
                                     0.037388547043])

                                taxaUsdt = random.choice(
                                    [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988,
                                     1.39284, 8.85470,
                                     13.39448])

                                taxaUsdt2 = random.choice(
                                    [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639,
                                     27.45124,
                                     49.73885,
                                     67.16942])
                                print('')
                                if destino == 5 or destino == 6:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8,
                                                                               la2, la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg2))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo3 = saldo3 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                else:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                                    O valor de taxa de é {} PAXG.
                                                    Digite sim, para confirmar:'''.format(taxaPaxg))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo3 = saldo3 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                    if destino == 1:
                                        print(
                                            'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                                    if destino == 2:
                                        print(
                                            'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                                    if destino == 3:
                                        print(
                                            'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                                    if destino == 4:
                                        print(
                                            'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                                    if destino == 5:
                                        print(
                                            'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                                    if destino == 6:
                                        print(
                                            'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8,
                                                la2, la3))
                            else:
                                print('Processo Finalizado')

                        if ncarteira == 4:
                            print(
                                'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
                                    saldo4, al4))
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")

                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira R4                      Tipo: Reserva')
                                time.sleep(0.5)
                                print('')
                                print('Criptomoeda: Paxos Gold (PAXG)   Quantidade: {}    AL: {}% '.format(
                                    saldo4, al4))
                                print('                                           R${}'.format(
                                    round(cotacaoPAXGbinance * saldo4, 2)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                                print('')
                                print('')
                            print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2 = taxa * 10
                                taxaPaxg = random.choice(
                                    [0.00098869808, 0.000860438248, 0.000332286556, 0.000229802845,
                                     0.000451243811,
                                     0.000223358254, 0.001666435356, 0.00192716402, 0.005312830272,
                                     0.007470163288])

                                taxaPaxg2 = random.choice(
                                    [0.014144054453, 0.017594981639, 0.019175284100, 0.025124769641,
                                     0.026274362743,
                                     0.021119023841, 0.022372391771, 0.039284750228, 0.030672705062,
                                     0.037388547043])
                                print('')
                                if destino == 5 or destino == 6:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8,
                                                                               la2, la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} PAXG.
                                            Digite sim, para confirmar:'''.format(taxaPaxg2))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo4 = saldo4 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                else:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8,
                                                                               la2, la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                                    O valor de taxa de é {} PAXG.
                                                    Digite sim, para confirmar:'''.format(taxaPaxg))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo4 = saldo4 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + valor - taxaPaxg
                                            real1 = float(saldo1 * 9097.38)
                                            al1 = round((100 * real1) / total, 3)
                                        if destino == 2:
                                            saldo2 = saldo2 + valor - taxaPaxg
                                            real2 = float(saldo2 * 9097.38)
                                            al2 = round((100 * real2) / total, 3)
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaPaxg
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaPaxg
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                        if destino == 5:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 6:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                            if destino == 1:
                                                print(
                                                    'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                                            if destino == 2:
                                                print(
                                                    'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                                            if destino == 3:
                                                print(
                                                    'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                                            if destino == 4:
                                                print(
                                                    'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                                            if destino == 5:
                                                print(
                                                    'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                                            if destino == 6:
                                                print(
                                                    'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                        saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                        na8, la2, la3))
                            else:
                                print('Processo Finalizado')

                        if ncarteira == 5:
                            print(
                                'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%'.format(
                                    saldo5, al5))
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira I1                      Tipo: Intermediaria')
                                print('')
                                time.sleep(0.5)
                                print('Criptomoeda: Theter (USDT)       Quantidade: {}    AL: {}% '.format(
                                    saldo5, al5))
                                print('                                           R${}'.format(
                                    round(cotacaoUSDTbinance * saldo5, 1)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                            print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2 = taxa * 10
                                taxaUsdt = random.choice(
                                    [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988,
                                     1.39284, 8.85470,
                                     13.39448])

                                taxaUsdt2 = random.choice(
                                    [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639,
                                     27.45124,
                                     49.73885,
                                     67.16942])
                                print('')
                                if destino == 1 or destino == 2 or destino == 3 or destino == 4:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} USDT.
                                            Digite sim, para confirmar:'''.format(taxaUsdt2))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo5 = saldo5 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + (valor * 1794) - taxaUsdt2
                                            real1 = (saldo1 * 5.07)
                                            saldo1 = round(saldo1, 5)
                                            al1 = round((100 * real1) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 2:
                                            saldo2 = saldo2 + (valor * 1794) - taxaUsdt2
                                            real2 = (saldo2 * 5.07)
                                            saldo2 = round(saldo2, 3)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaUsdt2
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaUsdt2
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 5:
                                            saldo5 = saldo5 + valor - taxaUsdt
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                        if destino == 6:
                                            saldo6 = saldo6 + valor - taxaUsdt
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))

                                else:

                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} USDT.
                                            Digite sim, para confirmar:'''.format(taxaUsdt))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo5 = saldo5 - valor
                                        if destino == 1:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 2:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaUsdt
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaUsdt
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 5:
                                            saldo5 = saldo5 + valor - taxaUsdt
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                        if destino == 6:
                                            saldo6 = saldo6 + valor - taxaUsdt
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                            else:
                                print('Processo Finalizado')

                        if ncarteira == 6:
                            print(
                                'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%'.format(
                                    saldo6, al6))
                            desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                            if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                                print('')
                            if desejaConsultar == 'sim'.upper().lower():
                                print('')
                                print('Consultando...')
                                time.sleep(5)
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                                navegador = webdriver.Chrome(options=options)

                                print("")
                                print("")

                                # mudei aqui

                                simbolo = moeda + base

                                url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                                requisicao = requests.get(url)
                                resposta = requisicao.json()

                                cotacaoUSDTbinance = resposta["price"]
                                cotacaoUSDTbinance = float(cotacaoUSDTbinance)
                                cotacaoUSDTbinance = round(cotacaoUSDTbinance, 1)

                                simbolo2 = moeda2 + moeda

                                url2 = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo2}"

                                requisicao2 = requests.get(url2)
                                resposta2 = requisicao2.json()

                                cotacaoPAXGbinance = resposta2["price"]
                                cotacaoPAXGbinance = float(cotacaoPAXGbinance)
                                cotacaoPAXGbinance = cotacaoPAXGbinance * cotacaoUSDTbinance
                                cotacaoPAXGbinance = round(cotacaoPAXGbinance, 2)

                                # até aqui

                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")
                                time.sleep(4)
                                print("")
                                print("")
                                print("")
                                print("A aplicação está consultando as cotações atuais...")
                                print("")
                                options = webdriver.ChromeOptions()
                                options.add_experimental_option('excludeSwitches', ['enable-logging'])

                                print("")
                                navegador.get("https://coinmarketcap.com/pt-br/currencies/tether/")

                                print("")
                                print("")
                                cotacaoUSDT = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoUSDT = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapUSDT = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hUSDT = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print(precoUSDT.text)
                                print("R$", cotacaoUSDTbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapUSDT.text, '     ', fullydilutedmarketcapUSDT.text, '     ',
                                      volume24hUSDT.text)
                                print("")
                                print("")
                                print("")

                                print('------------------------------')
                                print("")
                                print("")

                                navegador.get("https://coinmarketcap.com/currencies/pax-gold/")
                                cotacaoPAXG = navegador.find_element("xpath",
                                                                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                                precoPAXG = navegador.find_element("xpath",
                                                                   '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                                marketcapPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                                fullydilutedmarketcapPAXG = navegador.find_element("xpath",
                                                                                   '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                                volume24hPAXG = navegador.find_element("xpath",
                                                                       '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')

                                print('Preço de PAX Gold (PAXG)')
                                print("R$", cotacaoPAXGbinance)
                                print("")
                                print("Market Cap", '         ', "Fully Diluted Market Cap", '     ',
                                      "Volume 24h")
                                print(marketcapPAXG.text, '             ', fullydilutedmarketcapPAXG.text,
                                      '           ',
                                      volume24hPAXG.text)
                                print("")
                                print("")
                                print("")
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('Carteira FTX                      Tipo: Corretora')
                                time.sleep(0.5)
                                print('')
                                print(
                                    'Criptomoeda: Theter (USDT)   Quantidade: {}    AL: {}% '.format(saldo6,
                                                                                                     al6))
                                print('                                       R${}'.format(
                                    round(cotacaoUSDTbinance * saldo6, 1)))
                                time.sleep(0.8)
                                print('')
                                print('Status: Chaves ativas sob gerenciamento')
                                print(
                                    '------------------------------------------------------------------------------------')
                                print('')
                                print('')
                                print('')
                            print('')
                            transfer = str(input('Deseja movimentar o circuito interno? '))
                            print('')
                            if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
                                print('')
                            if transfer == 'sim'.upper().lower():
                                print('')
                                valor = float(input('Quantifique a tranferencia: '))
                                print('')
                                destino = leiaNcarteira(
                                    'Qual a carteira de destino? (digite o número da carteira): ')
                                time.sleep(1.4)
                                # taxa = random.choice(
                                # 	[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
                                # 	 0.001904,
                                # 	 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
                                # 	 0.001856])
                                # taxa2 = taxa * 10
                                taxaUsdt = random.choice(
                                    [1.77289, 3.86556, 4.29802, 11.11901, 7.01632, 9.144054, 6.00988,
                                     1.39284, 8.85470,
                                     13.39448])

                                taxaUsdt2 = random.choice(
                                    [25.41013, 36.41005, 63.033228, 32.902384, 40.40544, 55.07471, 61.91639,
                                     27.45124,
                                     49.73885,
                                     67.16942])
                                print('')
                                if destino == 1 or destino == 2 or destino == 3 or destino == 4:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        Conversão será feita automaticamente via protocolo crosschain (1 INCH NETWORK).
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                                O valor de taxa de é {} USDT.
                                                Digite sim, para confirmar:'''.format(taxaUsdt2))

                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo6 = saldo6 - valor
                                        if destino == 1:
                                            saldo1 = saldo1 + (valor * 1794) - taxaUsdt2
                                            real1 = (saldo1 * 5.07)
                                            saldo1 = round(saldo1, 5)
                                            al1 = round((100 * real1) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 2:
                                            saldo2 = saldo2 + (valor * 1794) - taxaUsdt2
                                            real2 = (saldo2 * 5.07)
                                            saldo2 = round(saldo2, 5)
                                            al2 = round((100 * real2) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaUsdt2
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaUsdt
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 5:
                                            saldo5 = saldo5 + valor - taxaUsdt
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                        if destino == 6:
                                            saldo6 = saldo6 + valor - taxaUsdt
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                else:
                                    print(
                                        '''	
                                        ERC-20 Transaction: Tax pending.
                                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                                        ID: {}{}{}{}{}{}{}{}{}-{}{} '''.format(na1, na2, na3, la1, na4, na5,
                                                                               na6, na7, na8, la2,
                                                                               la3))
                                    time.sleep(3)
                                    confirmar = leiaCriptografia('''
                                            O valor de taxa de é {} USDT.
                                            Digite sim, para confirmar:'''.format(taxaUsdt))
                                    if confirmar == 'sim'.upper().lower().strip():
                                        saldo6 = saldo6 - valor
                                        if destino == 1:
                                            saldo5 = saldo5 + (valor * 1794) - taxaPaxg2
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                            for c in range(1, 20):
                                                cont = 0
                                                while cont < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont = cont + 1
                                        if destino == 2:
                                            saldo6 = saldo6 + (valor * 1794) - taxaPaxg2
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)
                                            for c in range(1, 20):
                                                cont1 = 0
                                                while cont1 < 1:
                                                    x1 = (random_letter())
                                                    x2 = (random_letter())
                                                    x3 = (random_letter())
                                                    x4 = (random_letter())
                                                    x5 = (random_letter())
                                                    x6 = (random_letter())
                                                    x7 = (random_letter())

                                                    a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)
                                                    print(
                                                        'Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                        a)
                                                    time.sleep(1.5)

                                                    cont1 = cont1 + 1
                                        if destino == 3:
                                            saldo3 = saldo3 + valor - taxaUsdt
                                            real3 = float(saldo3 * 9097.38)
                                            al3 = round((100 * real3) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 4:
                                            saldo4 = saldo4 + valor - taxaUsdt
                                            real4 = float(saldo4 * 9097.38)
                                            al4 = round((100 * real4) / total, 3)
                                            for c in range(1, 60):
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
                                                      ''.join(random.SystemRandom().choices(
                                                          string.ascii_letters, k=7)))
                                                time.sleep(1.5)
                                        if destino == 5:
                                            saldo5 = saldo5 + valor - taxaUsdt
                                            real5 = (saldo5 * 5.07)
                                            saldo5 = round(saldo5, 5)
                                            al5 = round((100 * real5) / total, 3)
                                        if destino == 6:
                                            saldo6 = saldo6 + valor - taxaUsdt
                                            real6 = (saldo6 * 5.07)
                                            saldo6 = round(saldo6, 5)
                                            al6 = round((100 * real6) / total, 3)

                                        for c in range(1, ta1):
                                            cont2 = 0
                                            while cont2 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (0/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont2 = cont2 + 1
                                        for c in range(1, ta2):
                                            cont3 = 0
                                            while cont3 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (1/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont3 = cont3 + 1
                                        for c in range(1, ta3):
                                            cont4 = 0
                                            while cont4 < 1:
                                                x1 = (random_letter())
                                                x2 = (random_letter())
                                                x3 = (random_letter())
                                                x4 = (random_letter())
                                                x5 = (random_letter())
                                                x6 = (random_letter())
                                                x7 = (random_letter())

                                                a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)
                                                print('Confirmação de rede pendende (2/3):  PROTOCOLO -', a)
                                                time.sleep(1.5)

                                                cont4 = cont4 + 1
                                                time.sleep(1.5)
                                        cont5 = 0
                                        while cont5 < 1:
                                            x1 = (random_letter())
                                            x2 = (random_letter())
                                            x3 = (random_letter())
                                            x4 = (random_letter())
                                            x5 = (random_letter())
                                            x6 = (random_letter())
                                            x7 = (random_letter())

                                            a = (x1 + x2 + x3 + x4 + x5 + x6 + x7)

                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            print('Confirmação de rede pendende (3/3):  PROTOCOLO -', a)
                                            time.sleep(1.5)
                                            cont5 = cont5 + 1

                                        if destino == 1:
                                            print(
                                                'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 2:
                                            print(
                                                'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 3:
                                            print(
                                                'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 4:
                                            print(
                                                'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 5:
                                            print(
                                                'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                                        if destino == 6:
                                            print(
                                                'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
                                                    saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7,
                                                    na8, la2, la3))
                            else:
                                print('Processo Finalizado')

                if ncarteira == 8:
                    print(
                        'Criptomoeda: Ethereum (ETH), Quantidade: 1.969,56 , Status: Chaves ativas sob gerenciamento')
                    print('')
                    print('')
                    print('')
                    desejaConsultar = leiaCriptografia("Deseja consultar as cotações?")
                    if desejaConsultar == 'não'.upper().lower() or desejaConsultar == 'nao'.upper().lower():
                        print('')
                    if desejaConsultar == 'sim'.upper().lower():
                        print('')
                        print('Consultando...')
                        time.sleep(5)
                        # options = webdriver.ChromeOptions()
                        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        # navegador = webdriver.Chrome(options=options)

                        print("")
                        print("")

                        # mudei aqui

                        simbolo = moeda3 + base

                        url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

                        requisicao = requests.get(url)
                        resposta = requisicao.json()

                        cotacaoEthbinance = resposta["price"]
                        cotacaoEthbinance = float(cotacaoEthbinance)



                        # até aqui

                        # navegador.get("https://coinmarketcap.com/pt-br/currencies/ethereum/")
                        # time.sleep(4)
                        # print("")
                        # print("")
                        # print("")
                        # print("A aplicação está consultando as cotações atuais...")
                        # print("")
                        # options = webdriver.ChromeOptions()
                        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
                        #
                        # print("")
                        #
                        # print("")
                        # print("")
                        # cotacaoEth = navegador.find_element("xpath",
                        #                                      '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
                        # precoEth = navegador.find_element("xpath",
                        #                                    '// *[ @ id = "__next"] / div / div[1] / div[2] / div / div[1] / div[2] / div / div[2] / h1')
                        # marketcapEth = navegador.find_element("xpath",
                        #                                        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div')
                        # fullydilutedmarketcapEth = navegador.find_element("xpath",
                        #                                                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div[2]/div')
                        # volume24hEth = navegador.find_element("xpath",
                        #                                        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/div')
                        #
                        # print(precoEth.text)
                        # print("R$", cotacaoEthbinance)
                        # print("")
                        # print("Market Cap", '         ', "Fully Diluted Market Cap", '     ', "Volume 24h")
                        # print(marketcapEth.text, '     ', fullydilutedmarketcapEth.text, '     ',
                        #       volume24hEth.text)
                        # print("")
                        # print("")
                        # print("")

                        #print('------------------------------')
                        print("")
                        print("")

                        print(
                            '------------------------------------------------------------------------------------')
                        print('Carteira M        ')
                        time.sleep(0.5)
                        print('')
                        print('Criptomoeda: Ethereum (ETH), Quantidade: 1.969,56')
                        print('                                         R$14.916.826,96')
                        time.sleep(0.8)
                        print('')
                        print('Status: Chaves ativas sob gerenciamento')
                        print(
                            '------------------------------------------------------------------------------------')

        # informações criptografia
        if opcao == 3:
            print("")
            print("Informações de criptografia: ")
            print("")
            print("")
            print("")
            print("")
            print(
                "O sistema possui capacidade de encriptografamento de padrão Advanced Encryption Standard (AES) ")
            print("")
            print('''
                Possuimos uma criptografia assimétrica que possui HASHs de segurança, 
                e uma cifra de fluxo (stream cipher), pois é um dos melhores e mais 
                seguros protocolos de criptografia e é utilizado em incontáveis aplicações.''')
            print("")
            print("")
            print('''
                A tecnologia utilizada na criptografia são protocolos Secure Socket Layer (SSL),
                hoje conhecido como Transport Layer Security (TLS), 
                Derivada do DES, a criptografia 3DES (ou Triplo DES).''')
            print("")
            print("")
            criptousuario = str(input("Digite uma mensagem que gostaria que fosse encriptografada: "))
            print("")
            print("Sua mensagem encriptografada ficou: ")
            print("")
            print(criptografia(criptousuario))
            print("")

        # informações protocolo de segurança
        if opcao == 4:
            print("")
            print("Informações Protodolo de segurança: ")
            print("")
            print("")
            print("")
            print("")
            print(
                '''O sistema possui segurança de encriptografamento de padrão Advanced Encryption Standard (AES), 
        ID de rede classe dhcp, IPv6 permitidas para o adaptador com conexão segura e protocolos de segurança WEP e WPA''')
            print("")
            print('''
                Wired Equivalent Privacy  (Privacidade equivalente aos fios) WEP é um sistema de criptografia adotado pelo padrão IEEE 802.11. 
                Ele utiliza uma senha compartilhada para criptografar os dados e funciona de forma estática. 
                Além de fornecer apenas um controle de acesso e de privacidade de dados na rede sem fio.
                        ''')
            print("")
            print("")
            print('''
                Wi-fi Protected Access  (Wi-Fi de acesso protegido) Também é conhecido como TKIP (Temporal Key Integrity Protocol). 
                O recurso surgiu em 2003 para aumentar a segurança do protocolo WEP. O WPA2 é considerada a versão final o WPA. 
                A principal diferença entre o WPA e o WPA2 é a forma com a qual ele criptografa os dados. 
                Enquanto o WPA utiliza o TKIP como algoritmo de criptografia, o WPA2 utiliza o algoritmo AES (Advanced Encryption Standard). 
                O algoritmo AES é consideravelmente mais pesado que o TKIP. 
                Por conta disso, as placas mais antigas não suportam o WPA2, nem com um firmware atualizado.
                O AES é o padrão de criptografia utilizado''')
            print("")
            print("")

        # Log out
        if opcao == 5:
            time.sleep(2)
            print("Desconectando da rede...")
            time.sleep(4)
            print('')
            print('')
            print("Fazendo checagem de segurança...")
            time.sleep(4)
            print('')
            print('')
            print('')
            print("Fazendo Log out...")
            time.sleep(4)
            print('')
            print('3')
            time.sleep(3)
            time.sleep(3)
            print('')
            print('2')
            time.sleep(3)
            print('')
            print('1')
            time.sleep(1.5)
            print('')
            print("Log out feito com sucesso.")

            shutdown = input("Deseja desligar o computador? ")
            if shutdown == 'sim':
                os.system("shutdown /s /t 1")
            else:
                laco2 = False
                print('')