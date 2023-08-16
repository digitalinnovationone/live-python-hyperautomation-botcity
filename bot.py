"""
Passos:
    - Acessar página Web do FlowGPT e iniciar chat
    - Gerar os dados no formato JSON contendo as informações de produtos aleatórios
    - Extrair os dados da página Web
    - Tratar o conteúdo que foi extraído no formato JSON e converter os dados para uma planilha do Excel utilizando pandas
    - Utilizar os dados para fazer o cadastro de todos os produtos no aplicativo desktop 'Fakturama'
"""

import pandas
from botcity.maestro import *
from botcity.core import DesktopBot
from botcity.web import WebBot, Browser, By
from botcity.web.browsers.firefox import default_options

BotMaestroSDK.RAISE_NOT_CONNECTED = False

user_dir = ""

entrada = 'Você poderia gerar no formato json com o nome "produtos" os dados de 3 produtos eletrônicos \
contendo as informações de nome, categoria, codigo, identificador, descricao, preco e quantidade?'


def coleta_dados_produtos():
    # Instanciando o WebBot
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = r"geckodriver.exe"

    # Configurando opções customizadas no navegador
    def_options = default_options(headless=bot.headless, user_data_dir=user_dir)
    bot.options = def_options

    # Acessando o site para iniciar o chat
    bot.browse("https://flowgpt.com/chat")
    bot.maximize_window()
    bot.wait(2000)

    # Encontrando elemento do input de texto para inserir a entrada
    input_text = bot.find_element(
        selector="#scrollableDiv > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > textarea:nth-child(1)", 
        by=By.CSS_SELECTOR
    )
    input_text.send_keys(entrada)

    # Clicando no botão para enviar a mensagem
    botao_enviar = bot.find_element(
        selector="#scrollableDiv > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > button:nth-child(2)",
        by=By.CSS_SELECTOR
    )
    botao_enviar.click()
    bot.wait(2000)

    # Aguarda enquanto o conteúdo está sendo gerado
    while botao_enviar.get_attribute("disabled") == "true":
        print("Aguardando os dados serem gerados...")
        bot.wait(2000)

    # Coleta os dados da página
    dados = bot.find_element("language-json", By.CLASS_NAME).get_attribute("textContent")
    print(dados)

    # Faz o tratamento dos dados que foram coletados no formato JSON
    dados = pandas.read_json(dados)
    df = pandas.json_normalize(dados["produtos"])
    
    # Converte o conteúdo para uma planilha do Excel 
    df.to_excel("produtos.xlsx", index=False)

    # Finaliza o processo Web
    bot.wait(2000)
    bot.stop_browser()

    return df


def cadastra_produtos(df: pandas.DataFrame):
    # Instanciando o DesktopBot
    bot = DesktopBot()

    # Inicia o aplicativo do Fakturama
    bot.execute(r"Fakturama.exe")

    # Validação se o aplicativo foi aberto corretamente
    if bot.find( "fakturama-logo", matching=0.97, waiting_time=60000):
        # Para cada produto do DataFrame, cadastra um novo produto no Fakturama
        for index, row in df.iterrows():
            nome = row['nome']
            categoria = row['categoria']
            codigo = row['codigo']
            identificador = row['identificador']
            descricao = row['descricao']
            preco = str(row['preco']).replace('.', ',')
            preco_custo = str(row['preco'] * 0.6).replace('.', ',')
            estoque = row['quantidade']

            if bot.find( "new_product", matching=0.97, waiting_time=10000):
                bot.click()
                bot.wait(1000)
        
            if bot.find( "item_number", matching=0.97, waiting_time=10000):
                bot.click_relative(172, 8)
                bot.kb_type(str(index))
                bot.tab()

            # Name
            bot.paste(nome)
            bot.tab()

            # Category
            bot.paste(categoria)
            bot.tab()

            # GTIN
            bot.paste(codigo)
            bot.tab()

            # Supplier code
            bot.paste(identificador)
            bot.tab()

            # Description
            bot.paste(descricao)
            bot.tab()

            # Price
            bot.control_a()
            bot.paste(preco)
            bot.tab()

            # Cost Price
            bot.control_a()
            bot.paste(preco_custo)
            bot.tab()

            # Allowance
            bot.tab()

            # VAT
            bot.tab()

            # Stock
            bot.control_a()
            bot.paste(estoque)

            # Salvando produto
            if bot.find( "save", matching=0.97, waiting_time=10000):
                bot.click()
            bot.control_w()

        # Fechando o aplicativo
        bot.wait(2000)
        bot.alt_f4()


def main():
    # Realizando integrações com a plataforma BotCity Maestro
    maestro = BotMaestroSDK().from_sys_args()
    execution = maestro.get_execution()

    maestro.alert(
        task_id=execution.task_id,
        title="Início do processo",
        message="O processo de cadastro de produtos foi iniciado!",
        alert_type=AlertType.INFO
    )

    dados_produtos = coleta_dados_produtos()
    cadastra_produtos(dados_produtos)

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Processo finalizado!"
    )


if __name__ == '__main__':
    main()
