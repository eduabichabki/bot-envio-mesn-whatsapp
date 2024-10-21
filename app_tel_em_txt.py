import webbrowser
import pyautogui
import pyperclip
from time import sleep

def escrever_mensagem(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")

telefones = []

with open("telefones.txt", "r") as arquivo:
    for linha in arquivo:
        telefones.append(linha.split("\n")[0])
    print(telefones)

for telefone in telefones:
    link = f"https://wa.me/{telefone}"
    webbrowser.open_new_tab(link)
    sleep(5)

    #Pressionar "Iniciar a conversa"
    pyautogui.leftClick(1513,392, duration=1)
    sleep(5)

    #Pressionar pra utilizar o whatsapp web
    pyautogui.leftClick(1509,451, duration=1)
    sleep(30)

    #Pressionar no local pra escrever a mensagem
    pyautogui.leftClick(1842,968, duration=1)
    sleep(5)

    #Escrever a mensagem
    escrever_mensagem("Ola, como voce esta")
    sleep(5)

    #Pressionar enter
    pyautogui.press("enter")