# digitacao_lenta.py

import time
from selenium.webdriver.remote.webelement import WebElement

def digitacao(elemento: WebElement, texto: str, delay: float = 0.1):
    """
    Envia caracteres para um elemento um por um com um atraso especificado entre cada caractere.

    :paramentro elemento: O WebElement para enviar os caracteres.
    :paramentro texto: O texto a ser enviado para o elemento.
    :paramentro delay: O atraso entre cada caractere em segundos.
    """
    
    for letra in texto:
        elemento.send_keys(letra)
        time.sleep(delay)
