import pandas as pd
import json
from main import carregar_df
from relatorio_individual import relatorio

def metricas(df):

    df_validos = relatorio(df)

    qtd_por_area = df_validos.groupby("area")["nome"].count().to_dict()

    media_salarial_por_area = df_validos.groupby("area")['salario'].mean().round(2).to_dict()

    bonus_total_geral = df_validos["bonus_final"].sum()

    top3_bonus = (
        df_validos.nlargest(3, "bonus_final")[["nome", "bonus_final"]].to_dict(orient = "records")
    )

    kpis = {
        "quantidade_funcionarios_por_area" : qtd_por_area,
        "media_salarial_por_area"          : media_salarial_por_area,
        "bonus_total_geral"                : bonus_total_geral,
        "top3_funcionarios_maior_bonus"    : top3_bonus 
    }

    with open("kpis.json", "w", encoding = "utf-8") as f:
        json.dump(kpis, f, indent = 4, ensure_ascii = False)

        print("Arquivo kpis.json gerado com sucesso")

if __name__ == "__main__":
    df = carregar_df()
    metricas(df)