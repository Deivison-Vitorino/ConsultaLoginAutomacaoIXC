# Automação de Gerenciamento de Clientes Super W Baixa Mogiana

![Super W Baixa Mogiana](./logo/Logotipo.png){ width=200px }

Este projeto foi desenvolvido para gerenciar clientes baseados em dados recebidos de uma planilha contendo logins, potência de sinal e portas associadas na OLT do provedor Super W Baixa Mogiana. A automação tem como objetivo principal duas funcionalidades:

1. **Identificação de Problemas de Potência de Sinal:**
   - Monitora a potência de sinal de cada cliente para identificar desvios do padrão pré-estabelecido.
   - Agendamento preventivo de visitas técnicas para clientes com potência fora do padrão, garantindo manutenção proativa.

2. **Análise de Capacidade de Portas da OLT:**
   - Analisa quantos logins estão associados a cada porta da OLT.
   - Facilita a identificação de portas sobrecarregadas ou subutilizadas, auxiliando em decisões de remanejamento de CTO e manutenção preventiva.

## Funcionamento

A automação é implementada em Python e utiliza Selenium para automatizar consultas no sistema web IXC Soft.
Os principais componentes do projeto são:

- **digitacao.py:** 
   Módulo para simulação de entrada de dados.
  
- **ixc_automacao.py:** 
   Módulo principal que contém a lógica da automação para gerar uma nova planilha adicionando nome e endereço do cliente correspondente ao login pesquisado.
  
- **manipulador_excel.py:** 
   Utilizado para leitura e processamento da planilha `clientes_porta.xlsx`. Commit vasio por posssuir informações sensiveis. Para uso basta colar as informações a serem pesquisadas na colunas corrrespondentes ou readaptar o arquivo ou o código.
  
- **main.py:** 
   Ponto de entrada do programa que carrega as configurações e inicia a automação.

## Instruções de Uso

Para utilizar este projeto, siga as etapas abaixo:

1. **Configuração Inicial:**
   - Clone este repositório em sua máquina local.

2. **Instalação de Dependências:**
   - Certifique-se de ter Python instalado em sua máquina. Recomenda-se utilizar Python 3.x.
   - Instale as bibliotecas necessárias executando o comando:
  
     ```
     pip install openpyxl
     pip install selenium
     ```

3. **Configuração das Credenciais:**
   - Edite o arquivo `config.json` e insira as credenciais necessárias para acesso ao sistema web.

4. **Execução:**
   - Execute o arquivo `main.py` para iniciar a automação:

     ```
     python main.py
     ```
   
5. ## Monitoramento e Análise

Este projeto foi desenvolvido para permitir ao usuário analisar a planilha dos clientes da Super W Baixa Mogiana, verificando a quantidade de clientes por porta na OLT e a potência de sinal associada a cada um. Inicialmente, a planilha continha apenas informações básicas como login, potência e porta.

Após a execução da automação, uma nova planilha foi gerada incluindo o nome e endereço dos clientes. Isso possibilita uma análise mais detalhada para verificar quais clientes estavam com sinal dentro dos padrões aceitáveis. Nos casos identificados um desvio, o usuário agendou uma visita técnica de forma preventiva, melhorando assim a experiência do cliente.

Além disso, o projeto pode ser facilmente adaptado por usuários do sistema web que possuam uma planilha com características semelhantes ou quaisquer usuários que necessitam de automação com planilhas em excel. Isso permite que outros usuários aproveitem a estrutura existente para agilizar o trabalho de análise e gestão em seus próprios contextos.


**Nota:** 
Certifique-se de manter as credenciais e dados sensíveis (como `config.json`) seguros e não os comite em repositórios públicos.

---

Este README fornece uma visão geral clara e intuitiva sobre o funcionamento da automação desenvolvida, incluindo instruções detalhadas sobre como configurar, instalar as dependências necessárias e utilizar o projeto.
