# passo 1:abrir o navegador 
# 
# entrar no site "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

# pyautogui.write() -> escreve um texto
# pyautogui.press() -> clicar com o mouse
# pyautogui.click() -> apertar uma tecla
# pyautogui.hotkey() -> apertar um atalho (ctrl,c)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=541, y=512)
time.sleep(0.5)
pyautogui.click(x=646, y=39)

# passo 2: fazer login
time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=542, y=402)
pyautogui.write("marceloyanjj@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.press("enter")
# quero dar uma pausa de 2 segundos
time.sleep(2)

# passo 3: importar banco de dados
# pip install pandas
tabela = pandas.read_csv("C:\projetos\projetoPython\python.powerup/produtos.csv")

time.sleep(0.3)
# passo 4: cadastrar um produto
 

linha = 0

for linha in tabela.index:

    pyautogui.click(x=586, y=297)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.scroll(5000)


# passo 5 repetir o processo de cadastro até acabar os produtos
 