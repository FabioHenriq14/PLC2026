# TPC 3

**Nome:** Fábio Henrique Alves dos Santos  
**Número de Aluno:** A109300  

<img src="..\pfp.jpeg" width="250">

---

## Analisador Léxico

Neste TPC, foi construído um analisador léxico para uma linguagem de query, em que seu conteúdo é quebrado em tokens que seguem o seguinte padrão:

- O caráter '#' marca o início de um comentário que se prolonga até ao fim da linha e deve ser ignorado;
- O caráter '?' marca o início de um identificador de uma variável que se prolonga até ao primeiro caráter não alfanumérico;
- O caráter '@' marca o início de um identificador de língua que terá mais 2 carateres;
- Qualquer sequência entre aspas é um valor do tipo string;
- As outras sequências de alfanuméricos são identificadores de conceitos;
- Os carateres '{}.' são delimitadores;
- 'LIMIT' é uma palavra reservada;
- '1000' é um valor numérico


Para resolver o exercício proposto, eu dividi o problema em 3 etapas:

1) Definir a expressão regular geral que apanhará todos os padrões desejados seguindo uma ordem predefinida. Isso permite que tokens não sejam categorizados mais de uma vez, porque ao satisfazer um dos grupos, nenhum posterior é mais avaliado para este. Grupos de captura nomeados foram usados para identificar estes padrões, que serão usados nos próximos passos.

2) Armazenar e categorizar os tokens. Para isso foi usado um dicionário composto por pares {nome do grupo: lista de matches}.

3) Por fim, resta percorrer o texto contido no documento e, para cada match devolvido pelo iterador, extrair a categoria usando `.lastgroup`, que indica onde a correspondência será inserida no dicionário, e o conteúdo do match usando `.group()`, que será o valor adicionado. Por fim, o dicionário é percorrido e o seu conteúdo é apresentado no STDOUT.