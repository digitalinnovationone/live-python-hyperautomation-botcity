## Descrição do Projeto

Será desenvolvido um projeto de robô que faz operações em uma página Web e em um aplicativo Desktop utilizando Python. Essa automação abre o site FlowGPT, usa um prompt para gerar informações de produtos, extrai e faz um tratamento dos dados, e registra em um aplicativo de ERP desktop.

Durante a live, será demonstrado como ganhar produtividade no desenvolvimento da automação usando Visão Computacional e trabalhando com os IDs dos elementos.

Além disso, serão apresentados os principais conceitos envolvidos na gestão e orquestração dos bots, e como paralelizar automações em background.

Por fim, serão discutidos conceitos e ferramentas relacionadas a Hiperautomação com Python e open source, e dicas para os profissionais que buscam se aperfeiçoar na área de hiperautomação.

LINK DA LIVE: https://www.youtube.com/watch?v=aiWkNlqxMqw

## Tecnologias utilizadas no Projeto

#### Linguagens:
- Python

#### Conceitos e abordagens:
- IA Generativa / LLMs (FlowGPT/ChatGPT), RPA, Hiperautomação, Visão Computacional, Automação Web/Desktop, Orquestração, Runner desktop e Runner background, Paralelismo

#### Frameworks / Bibliotecas:
- pandas: http://pandas.pydata.org/pandas-docs/stable/
- BotCity Framework Web: https://github.com/botcity-dev/botcity-framework-web-python
- BotCity Framework Core: https://github.com/botcity-dev/botcity-framework-core-python
- BotCity Maestro SDK: https://github.com/botcity-dev/botcity-maestro-sdk-python

Todas as dependências utilizadas no código estão listadas no arquivo `requirements.txt`. Para que todas as dependências sejam instaladas, basta executar o seguinte comando dentro da pasta do projeto:

```
pip install --upgrade -r requirements.txt
```

## Outras tecnologias complementares:

- Site FlowGPT - utilizado para gerar os dados dos produtos: https://flowgpt.com/chat
- Fakturama - software desktop utilizado para realizar o cadastro dos produtos: https://www.fakturama.info
- BotCity Maestro - plataforma de orquestração da BotCity utilizado para gerenciar as execuções da automação: https://developers.botcity.dev

## Links úteis

As bibliotecas e funcionalidades utilizadas durante o código estão disponíveis na documentação da BotCity: https://documentation.botcity.dev.

Na documentação você irá encontrar os guias completos sobre: 
- [Setup e configuração do ambiente](https://documentation.botcity.dev/getting-started/prerequisites/)
- [Instalação do BotCity Studio SDK](https://documentation.botcity.dev/getting-started/botcity-studio-sdk/)
- [Desenvolvimento de um primeiro bot utilizando Python](https://documentation.botcity.dev/tutorials/python-automations/web/)
- [Orquestração e gerenciamento das automações através do BotCity Maestro](https://documentation.botcity.dev/maestro/)
