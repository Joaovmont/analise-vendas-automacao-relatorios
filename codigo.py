import pandas as pd
import os
import yagmail

lista_cidades = ["BH", "DF", "Manaus", "Rio", "Salvador", "SP"]

faturamentos = {}

for cidade in lista_cidades:
    vendas_df = pd.read_excel(f"Loja {cidade}.xlsx")
    faturamento_cidade = sum(vendas_df["Vendas"])
    faturamentos[cidade] = faturamento_cidade

ranking_df = pd.DataFrame.from_dict(
    faturamentos,
    orient="index",
    columns=["Vendas"]
)

ranking_df = ranking_df.sort_values(
    by="Vendas",
    ascending=False
)

ranking_df = ranking_df.map("R${:,.2f}".format)

mensagem = f"""
Prezados,

Segue em anexo o ranking das lojas:

{ranking_df.to_string().replace(" ", ".")}

Att,
João.
"""

usuario = yagmail.SMTP(
    os.getenv("EMAIL"),
    os.getenv("EMAIL_SENHA")
)

usuario.send(
    to="jvmmcode@gmail.com",
    subject="Ranking das lojas",
    contents=mensagem
)
