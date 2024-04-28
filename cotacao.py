import streamlit as st
import requests
import json
from streamlit_modal import Modal
import datetime
import streamlit.components.v1 as components


def consulta_api():
    url = "https://economia.awesomeapi.com.br/last/"
    moedas = [
        "USD-BRL",
        "USD-BRLT",
        "EUR-BRL",
        "GBP-BRL",
        "CAD-BRL",
        "AUD-BRL",
        "ARS-BRL",
        "JPY-BRL",
        "CHF-BRL",
        "CNY-BRL",
        "ILS-BRL",
        "BTC-BRL",
        "ETH-BRL",
        "XRP-BRL",
        "LTC-BRL",
        "DKK-BRL",
        "HKD-BRL",
        "MXN-BRL",
        "NOK-BRL",
        "NZD-BRL",
        "PLN-BRL",
        "SAR-BRL",
        "SEK-BRL",
        "THB-BRL",
        "TRY-BRL",
        "TWD-BRL",
        "VEF-BRL",
        "ZAR-BRL",
    ]
    moedas = ",".join(moedas)
    url = url + moedas
    response = requests.get(url)
    moedas = json.loads(response.text)
    return moedas


bandeiras = {
    "USD": "https://www.crwflags.com/fotw/images/u/us.gif",
    "BRL": "https://www.crwflags.com/fotw/images/b/br1.gif",
    "BRLT": "https://www.crwflags.com/fotw/images/b/br1.gif",
    "EUR": "https://www.crwflags.com/fotw/images/e/eu-eun.gif",
    "GBP": "https://www.crwflags.com/fotw/images/g/gb.gif",
    "CAD": "https://www.crwflags.com/fotw/images/c/ca.gif",
    "AUD": "https://www.crwflags.com/fotw/images/a/au.gif",
    "ARS": "https://www.crwflags.com/fotw/images/a/ar.gif",
    "JPY": "https://www.crwflags.com/fotw/images/j/jp.gif",
    "CHF": "https://www.crwflags.com/fotw/images/c/ch.gif",
    "CNY": "https://www.crwflags.com/fotw/images/c/cn.gif",
    "ILS": "https://www.crwflags.com/fotw/images/i/il.gif",
    "BTC": "https://user-images.githubusercontent.com/14335913/44107307-5a5ddc14-9fcd-11e8-870e-9ba9a46c8ebc.jpg",
    "ETH": "https://i.pinimg.com/564x/69/86/72/69867268bb36524c836b87b35b55c72a.jpg",
    "XRP": "https://cdn.freelogovectors.net/wp-content/uploads/2023/01/xrp-logo-freelogovectors.net_.png",
    "LTC": "https://i.pinimg.com/564x/8b/05/aa/8b05aa6e125f6022310d899bfe0cc698.jpg",
    "DKK": "https://www.crwflags.com/fotw/images/d/dk.gif",
    "HKD": "https://www.crwflags.com/fotw/images/h/hk.gif",
    "MXN": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Flag_of_Mexico_%281893-1916%29.svg",
    "NOK": "https://www.crwflags.com/fotw/images/n/no.gif",
    "NZD": "https://www.crwflags.com/fotw/images/n/nz.gif",
    "PLN": "https://www.crwflags.com/fotw/images/p/pl.gif",
    "SAR": "https://www.crwflags.com/fotw/images/s/sa.gif",
    "SEK": "https://www.crwflags.com/fotw/images/s/se.gif",
    "THB": "https://www.crwflags.com/fotw/images/t/th.gif",
    "TRY": "https://www.crwflags.com/fotw/images/t/tr.gif",
    "TWD": "https://www.crwflags.com/fotw/images/t/tw.gif",
    "VEF": "https://www.crwflags.com/fotw/images/v/ve.gif",
    "ZAR": "https://www.crwflags.com/fotw/images/z/za.gif",
}

st.set_page_config(
    page_title="Cotação de Moedas",
    page_icon=":moneybag:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    """,
    unsafe_allow_html=True,
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


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

st.write("")
st.write("")
st.write("")


columns = st.columns(5)

index = 0


for currency, details in consulta_api().items():
    with st.container():
        with columns[index]:

            col1, col2 = st.columns([0.5, 2])
            col1.image(bandeiras[currency[:3]], width=50)
            col2.image(bandeiras[currency[3:]], width=50)

            st.markdown(
                f"""
                            <div class="card">
                                <h5 class="card-title" style="text-align: center;">{currency[:3]} - {currency[3:]}</h5>
                                <span class="badge bg-primary" style="text-align: center;">{details['name']}</span>
                                <p style="text-align: center;"><strong>Preço de Compra:</strong> R$ {float(details['bid']):.2f}</p>
                                <p style="text-align: center;"><strong>Preço de Venda:</strong> R$ {float(details['ask']):.2f}</p>
                            </div>
                        """,
                unsafe_allow_html=True,
            )

            open_modal = st.button("Detalhes", key=f"button-{currency}")
            modal = Modal(
                title="Detalhes do par de moedas",
                key=f"modal-{currency}",
                padding=0,
                max_width=600,
            )

            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write(
                        f"""<h1 class="badge bg-primary" style="text-align: center;"><strong>{details['name']}</strong></h1>""",
                        unsafe_allow_html=True,
                    )
                    create_date = datetime.datetime.strptime(
                        details["create_date"], "%Y-%m-%d %H:%M:%S"
                    )
                    formatted_date = create_date.strftime("%d/%m/%Y - %H:%M:%S")

                    html_string = f"""
                        <div class="card-modal" id="modal">
                            <div class="card-header">
                            </div>
                            <div class="card-body">
                                <p style="text-align: center;"><strong>Preço Máximo:</strong> R$ {float(details['high']):.2f}</p>
                                <p style="text-align: center;"><strong>Preço Mínimo:</strong> R$ {float(details['low']):.2f}</p>
                                <p style="text-align: center;"><strong>Variação:</strong> R$ {float(details['varBid']):.2f}</p>
                                <p style="text-align: center;"><strong>Porcentagem de Variação:</strong> {float(details['pctChange']):.2f}%</p>
                                <p style="text-align: center;"><strong>Preço de Compra:</strong> R$ {float(details['bid']):.2f}</p>
                                <p style="text-align: center;"><strong>Preço de Venda:</strong> R$ {float(details['ask']):.2f}</p>
                                <p style="text-align: center;"><strong>Última atualização:</strong> {formatted_date}</p>
                            </div>
                        </div>
                    """

                    components.html(html_string, height=300, width=500, scrolling=True)

        index = (index + 1) % 5
