import re

expressao_geral = re.compile(
    r"(?P<identificador_variavel>\?\w+)|"
    r"(?P<identificador_lingua>@\w{2})|"
    r"(?P<String>\"[^\"]*\")|"
    r"(?P<reservada>\bLIMIT\b)|"
    r"(?P<numerico>\d+)|"
    r"(?P<identificadores_conceito>[\w:]+)|"
    r"(?P<delimitadores>[{}\.])"
)

token_dict = {
    "identificador_variavel": [],
    "identificador_lingua": [],
    "String": [],
    "identificadores_conceito": [],
    "reservada": [],
    "numerico": [],
    "delimitadores": []
}

with open("TP3\\entrada.txt", "r") as arquivo:
    text = arquivo.read()

    for token in expressao_geral.finditer(text):
        categoria = token.lastgroup
        token_dict[categoria].append(token.group())

    for item in token_dict:
        print(f"{item}: {token_dict[item]}")
