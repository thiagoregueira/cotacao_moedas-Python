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
    "USD": "public\\us.png",
    "BRL": "public\\br.png",
    "BRLT": "public\\br.png",
    "EUR": "public\\eu.png",
    "GBP": "public\\gb.png",
    "CAD": "public\\ca.png",
    "AUD": "public\\au.png",
    "ARS": "public\\ar.png",
    "JPY": "public\\jp.png",
    "CHF": "public\\ch.png",
    "CNY": "public\\cn.png",
    "ILS": "public\\il.png",
    "BTC": "public\\bit.png",
    "ETH": "public\\eth.png",
    "XRP": "public\\xrp.png",
    "LTC": "public\\ltc.png",
    "DKK": "public\\dk.png",
    "HKD": "public\\hk.png",
    "MXN": "public\\mx.png",
    "NOK": "public\\no.png",
    "NZD": "public\\nz.png",
    "PLN": "public\\pl.png",
    "SAR": "public\\sa.png",
    "SEK": "public\\se.png",
    "THB": "public\\th.png",
    "TRY": "public\\tr.png",
    "TWD": "public\\tw.png",
    "VEF": "public\\ve.png",
    "ZAR": "public\\za.png",
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
    with st.container(border=True):
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