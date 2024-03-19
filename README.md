# Projeto de Cotação de Moedas
Este projeto é uma aplicação web desenvolvida com Streamlit para consultar a cotação de moedas.
Pode ser acessado através do endereço: `https://cotacaomoedas.streamlit.app/`

## Estrutura do Projeto
~~~
.gitignore
.streamlit/
    config.toml
cotacao.py
requirements.txt
style.css
~~~

## Arquivos Principais
- `cotacao.py:` Este é o arquivo principal do projeto, onde a aplicação Streamlit é criada e a API é consultada para obter as cotações das moedas.
- `requirements.txt:` Este arquivo contém todas as dependências necessárias para executar o projeto.
- `style.css:` Este arquivo contém os estilos CSS usados na aplicação.

## Como Executar o Projeto
1. Clone o repositório.
2. Instale as dependências usando pip:
~~~python
 pip install -r requirements.txt
~~~
3. Execute o arquivo `cotacao.py`:
~~~python
streamlit run cotacao.py
~~~

## Dependências
Este projeto usa várias bibliotecas Python, incluindo:

- **Streamlit** para a criação da aplicação web.
- **Requests** para fazer chamadas à API.
- **Streamlit Modal** para criar modais na aplicação.
