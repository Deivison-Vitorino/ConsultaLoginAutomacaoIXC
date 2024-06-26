# ixc_automacao.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from digitacao import digitacao
from manipulador_excel import ManipuladorExcel

class IXCAutomacao:
    def __init__(self, usuario: str, senha: str):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.manipulador_excel = ManipuladorExcel(
            'clientes_porta.xlsx', 'ClienteSinalPortaBairro.xlsx'
        )
        
    def login(self):
        """
        Faz login no sistema IXC usando as credenciais fornecidas.
        """
        self.driver.get('https://ixc.superw.com.br/login.php')
        sleep(6)
        
        # Insere credenciais e tenta fazer login
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(self.usuario)
        self.driver.find_element(By.XPATH, '//*[@id="senha"]').send_keys(self.senha)
        self.driver.find_element(By.XPATH, '//*[@id="entrar"]').click()
        sleep(2)
        
        # Verifica se aviso de usuário logado é apresentado na tela
        while True:
            try:
                # Verifica se o usuario ja está logado
                jaLogado = self.driver.find_element(By.XPATH, '//*[@id="resp"]')
                if jaLogado:
                    # Se ja está logado, clica no botão novamente para acessar o sistema
                    self.driver.find_element(By.XPATH, '//*[@id="entrar"]').click()
            except NoSuchElementException:
                # Se não está logado, continua o processo normal de login
                break
    
    def processar_clientes(self):
        """
        Processa cada login de cliente, busca os dados e os salva no arquivo Excel.
        """
        logins = self.manipulador_excel.ler_logins()

        for login, porta, potencia in logins:
            self.pesquisar_cliente(login)
            try:
                self.abrir_cadastro_cliente()
                nome, endereco = self.obter_dados_cliente()
            except NoSuchElementException:
                nome, endereco = "Não encontrado", "Não encontrado"

            self.manipulador_excel.salvar_dados_cliente(login, porta, potencia, nome, endereco)

    def pesquisar_cliente(self, login: str):
        """
        Pesquisa um cliente no sistema usando o login fornecido.
        
        :parametro login: O identificador de login do cliente.
        """
        campo_pesquisa = self.driver.find_element(
            By.XPATH, '/html/body/div[7]/div[1]/input'
            )
        campo_pesquisa.clear()
        digitacao(campo_pesquisa, login, delay=0.04)
        sleep(1)

    def abrir_cadastro_cliente(self):
        """
        Abre os detalhes do cadastro do cliente.
        """
        cadastro = self.driver.find_element(
            By.XPATH, '//li[@class="x-cmp-searchbar-registro-listMaster"]'
            )
        sleep(1)
        cadastro.click()
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, 'iframe'))
        
    def obter_dados_cliente(self):
        """
        Obtém os dados do cliente a partir do cadastro aberto.

        :return: Nome e endereço do cliente.
        """
        nome_cliente = self.driver.find_element(
            By.XPATH, '//*[@id="dados_cliente"]/article/div/div[1]/div/div[2]/div'
            )
        lista_nome = nome_cliente.text.split()
        nome = ' '.join(lista_nome[2:])

        endereco_cliente = self.driver.find_element(
            By.XPATH, '//*[@id="dados_cliente"]/article/div/div[2]/div/div[1]/div[4]'
            )
        lista_endereco = endereco_cliente.text.split()
        endereco = ' '.join(lista_endereco[2:])
        
        self.driver.switch_to.default_content()
        
        return nome, endereco
