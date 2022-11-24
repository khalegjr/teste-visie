from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "168.637.122-53": {
        "nome": "Alberto Vieira",
        "rg": "25.507.105-2",
        "cpf": "168.637.122-53",
        "data_nascmimento": "1997-07-01",
        "data_admissao": get_timestamp(),
        "função": "",
    },
    "877.733.889-89": {
        "nome": "Alexandre Teixeira",
        "rg": "79.474.888-8",
        "cpf": "877.733.889-89",
        "data_nascmimento": "1982-08-16",
        "data_admissao": get_timestamp(),
        "função": "",
    },
    "766.370.920-96": {
        "nome": "Ana Carolina Souza",
        "rg": "52.565.667-8",
        "cpf": "766.370.920-96",
        "data_nascmimento": "1982-03-19",
        "data_admissao": get_timestamp(),
        "função": "",
    },
}


def read_all():
    return list(PEOPLE.values())
