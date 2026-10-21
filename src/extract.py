import requests 

def consulting_series_sgs(cod_serie, i_date, f_date):
    base_url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{cod_serie}/dados"
    parameters = {
        "formato": "json",
        "dataInicial": i_date,
        "dataFinal": f_date
    }

    response = requests.get(base_url, params=parameters, timeout=10)

    if response.status_code == 404 and "Value(s) not found" in response.text:
        return []

    response.raise_for_status()

    return response.json()

