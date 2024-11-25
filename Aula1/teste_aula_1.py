#0. importar os recursos
import time
import pyautogui
import pandas as pd

#1. Abrir Navegador
pyautogui.press("win")
pyautogui.write("opera.exe")
pyautogui.press("enter")
time.sleep(2)

#2. Entrar no Link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#3. Fazer o Login
pyautogui.press("tab")
#pyautogui.click(x=732, y=395)
pyautogui.write("Gostosão42069@ifba.com")
pyautogui.press("tab")
pyautogui.write("AmogatinhosS2")
pyautogui.press("enter")
time.sleep(2)

#4. Base de Produtos
tabela = pd.read_csv("produtos.csv")

#5. Preencher as informações dos Produtos
for linha in tabela.index:
    codigo = pyautogui.locateOnScreen('Codigo_do_produto.png')
    pyautogui.click(codigo)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(69420) # hehe