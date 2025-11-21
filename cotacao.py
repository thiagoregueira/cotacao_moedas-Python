import streamlit as st
import requests
import time
from streamlit_modal import Modal
import datetime
import streamlit.components.v1 as components


@st.cache_data(ttl=1800)
def consulta_api():
    url = 'https://economia.awesomeapi.com.br/last/'
    moedas = [
        'USD-BRL',
        'USD-BRLT',
        'EUR-BRL',
        'GBP-BRL',
        'CAD-BRL',
        'AUD-BRL',
        'ARS-BRL',
        'JPY-BRL',
        'CHF-BRL',
        'CNY-BRL',
        'ILS-BRL',
        'BTC-BRL',
        'ETH-BRL',
        'XRP-BRL',
        'LTC-BRL',
        'DKK-BRL',
        'HKD-BRL',
        'MXN-BRL',
        'NOK-BRL',
        'NZD-BRL',
        'PLN-BRL',
        'SAR-BRL',
        'SEK-BRL',
        'THB-BRL',
        'TRY-BRL',
        'TWD-BRL',
        'VEF-BRL',
        'ZAR-BRL',
    ]
    moedas = ','.join(moedas)
    url = url + moedas

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=15)

            if response.status_code == 200:
                data = response.json()
                if 'status' in data or ('code' in data and 'message' in data and len(data) <= 2):
                    st.error(f'A API retornou um erro: {data}')
                    return {}
                return data

            elif response.status_code == 429:
                if attempt < max_retries - 1:
                    time.sleep(2**attempt)  # Backoff exponencial
                    continue
                else:
                    st.error(
                        'Erro 429: Muitas requisições. O servidor da API bloqueou temporariamente o acesso devido ao alto tráfego (comum em ambientes compartilhados como Streamlit Cloud). Tente novamente mais tarde.'
                    )
                    return {}
            else:
                st.error(f'Erro ao conectar com a API: Status {response.status_code}')
                return {}

        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            st.error(f'Erro inesperado: {e}')
            return {}
    return {}


bandeiras = {
    'USD': 'https://www.crwflags.com/fotw/images/u/us.gif',
    'BRL': 'https://www.crwflags.com/fotw/images/b/br1.gif',
    'BRLT': 'https://www.crwflags.com/fotw/images/b/br1.gif',
    'EUR': 'https://www.crwflags.com/fotw/images/e/eu-eun.gif',
    'GBP': 'https://www.crwflags.com/fotw/images/g/gb.gif',
    'CAD': 'https://www.crwflags.com/fotw/images/c/ca.gif',
    'AUD': 'https://www.crwflags.com/fotw/images/a/au.gif',
    'ARS': 'https://www.crwflags.com/fotw/images/a/ar.gif',
    'JPY': 'https://www.crwflags.com/fotw/images/j/jp.gif',
    'CHF': 'https://www.crwflags.com/fotw/images/c/ch.gif',
    'CNY': 'https://www.crwflags.com/fotw/images/c/cn.gif',
    'ILS': 'https://www.crwflags.com/fotw/images/i/il.gif',
    'BTC': 'https://user-images.githubusercontent.com/14335913/44107307-5a5ddc14-9fcd-11e8-870e-9ba9a46c8ebc.jpg',
    'ETH': 'https://i.pinimg.com/564x/69/86/72/69867268bb36524c836b87b35b55c72a.jpg',
    'XRP': 'https://cdn.freelogovectors.net/wp-content/uploads/2023/01/xrp-logo-freelogovectors.net_.png',
    'LTC': 'https://i.pinimg.com/564x/8b/05/aa/8b05aa6e125f6022310d899bfe0cc698.jpg',
    'DKK': 'https://www.crwflags.com/fotw/images/d/dk.gif',
    'HKD': 'https://www.crwflags.com/fotw/images/h/hk.gif',
    'MXN': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Flag_of_Mexico_%281893-1916%29.svg',
    'NOK': 'https://www.crwflags.com/fotw/images/n/no.gif',
    'NZD': 'https://www.crwflags.com/fotw/images/n/nz.gif',
    'PLN': 'https://www.crwflags.com/fotw/images/p/pl.gif',
    'SAR': 'https://www.crwflags.com/fotw/images/s/sa.gif',
    'SEK': 'https://www.crwflags.com/fotw/images/s/se.gif',
    'THB': 'https://www.crwflags.com/fotw/images/t/th.gif',
    'TRY': 'https://www.crwflags.com/fotw/images/t/tr.gif',
    'TWD': 'https://www.crwflags.com/fotw/images/t/tw.gif',
    'VEF': 'https://www.crwflags.com/fotw/images/v/ve.gif',
    'ZAR': 'https://www.crwflags.com/fotw/images/z/za.gif',
}

st.set_page_config(
    page_title='Cotação de Moedas',
    page_icon=':moneybag:',
    layout='wide',
    initial_sidebar_state='collapsed',
)

st.markdown(
    """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    """,
    unsafe_allow_html=True,
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown(
    "<h1 style='text-align: center; font-size: 80px;'>Cotação de Moedas</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='text-align: center; color: white;'>Acompanhe a cotação das principais moedas do mundo em relação ao real.</h2>",
    unsafe_allow_html=True,
)

st.markdown(
    "<h4 style='text-align: center;'> Atualizado a cada 30 minutos</h4>",
    unsafe_allow_html=True,
)

st.write('')
st.write('')
st.write('')


columns = st.columns(5)

index = 0

# Imagem placeholder para bandeiras não encontradas
PLACEHOLDER_IMG = 'https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-404.png'

data = consulta_api()
if not data:
    st.warning('Não foi possível carregar as cotações no momento. Tente recarregar a página em alguns instantes.')
else:
    for currency, details in data.items():
        if not isinstance(details, dict):
            continue

        with columns[index]:
            col1, col2 = st.columns([0.5, 2])

            # Uso defensivo do dicionário de bandeiras
            bandeira_origem = bandeiras.get(currency[:3], PLACEHOLDER_IMG)
            # Para a segunda moeda, assume-se que seja os caracteres a partir do 3o,
            # mas cuidado com moedas de 4 letras como BRLT.
            # Se currency for USDBRLT (7 chars), currency[3:] é BRLT.
            bandeira_destino = bandeiras.get(currency[3:], PLACEHOLDER_IMG)

            col1.image(bandeira_origem, width=50)
            col2.image(bandeira_destino, width=50)

            st.markdown(
                f"""
                                <div class="card">
                                    <h5 class="card-title" style="text-align: center;">{currency[:3]} - {currency[3:]}</h5>
                                    <span class="badge bg-primary" style="text-align: center;">{details.get('name', 'N/A')}</span>
                                    <p style="text-align: center;"><strong>Preço de Compra:</strong> R$ {float(details.get('bid', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Preço de Venda:</strong> R$ {float(details.get('ask', 0)):.2f}</p>
                                </div>
                            """,
                unsafe_allow_html=True,
            )

            open_modal = st.button('Detalhes', key=f'button-{currency}')
            modal = Modal(
                title='Detalhes do par de moedas',
                key=f'modal-{currency}',
                padding=0,
                max_width=600,
            )

            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write(
                        f"""<h1 class="badge bg-primary" style="text-align: center;"><strong>{details.get('name', 'N/A')}</strong></h1>""",
                        unsafe_allow_html=True,
                    )
                    try:
                        create_date = datetime.datetime.strptime(details.get('create_date', ''), '%Y-%m-%d %H:%M:%S')
                        formatted_date = create_date.strftime('%d/%m/%Y - %H:%M:%S')
                    except:  # noqa: E722
                        formatted_date = 'Data indisponível'

                    html_string = f"""
                            <div class="card-modal" id="modal">
                                <div class="card-header">
                                </div>
                                <div class="card-body">
                                    <p style="text-align: center;"><strong>Preço Máximo:</strong> R$ {float(details.get('high', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Preço Mínimo:</strong> R$ {float(details.get('low', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Variação:</strong> R$ {float(details.get('varBid', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Porcentagem de Variação:</strong> {float(details.get('pctChange', 0)):.2f}%</p>
                                    <p style="text-align: center;"><strong>Preço de Compra:</strong> R$ {float(details.get('bid', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Preço de Venda:</strong> R$ {float(details.get('ask', 0)):.2f}</p>
                                    <p style="text-align: center;"><strong>Última atualização:</strong> {formatted_date}</p>
                                </div>
                            </div>
                        """

                    components.html(html_string, height=300, width=500, scrolling=True)

        index = (index + 1) % 5
