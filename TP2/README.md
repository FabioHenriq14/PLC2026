# TPC 2

**Nome:** Fábio Henrique Alves dos Santos  
**Número de Aluno:** A109300  

<img src="..\pfp.jpeg" width="250">

---

## Conversor (Markdown -> HTML) para listas com marcadores e listas numeradas

```
    import re

    def md_para_html(texto):
        saida = []
        lista = None  # None, 'ul' ou 'ol'

        for linha in texto.split('\n'):
            if re.match(r'^\d+\. ', linha):
                tipo = 'ol'
                item = re.sub(r'^\d+\. ', '', linha)
            elif re.match(r'^[-*] ', linha):
                tipo = 'ul'
                item = linha[2:]
            else:
                tipo = None

            if tipo != lista:
                if lista:
                    saida.append(f'</{lista}>')
                if tipo:
                    saida.append(f'<{tipo}>')
                lista = tipo

            if tipo:
                saida.append(f'<li>{item}</li>')
            else:
                saida.append(linha)

        if lista:
            saida.append(f'</{lista}>')

        return '\n'.join(saida)


    if __name__ == '__main__':
        exemplo = """Frutas:
    - Maçã
    - Banana
    Passos:
    1. Lavar
    2. Cortar
    3. Comer"""
        print(md_para_html(exemplo))
```