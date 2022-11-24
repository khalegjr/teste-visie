from datetime import datetime

from flask import abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d"))


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


def create(person):
    nome = person.get("nome")
    rg = person.get("rg")
    cpf = person.get("cpf")
    data_nascimento = person.get("data_nascimento")
    data_admissao = person.get("data_admissao")
    funcao = person.get("funcao", "")

    if cpf and cpf not in PEOPLE:
        PEOPLE[cpf] = {
            "nome": nome,
            "rg": rg,
            "cpf": cpf,
            "data_nascmimento": data_nascimento,
            "data_admissao": data_admissao,
            "função": funcao,
        }
        return PEOPLE[cpf], 201
    else:
        abort(
            406,
            f"Person with cpf number {cpf} already exists",
        )


def read_one(cpf):
    if cpf in PEOPLE:
        return PEOPLE[cpf]
    else:
        abort(
            404, f"Person with cpf number {cpf} not found"
        )
