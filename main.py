import pandas as pd


def carregar_df():
    df = pd.read_csv("formulario.csv")

    CONSTANTE_BONUS = 1000

    df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
    df['bonus_percentual'] = pd.to_numeric(df['bonus_percentual'], errors='coerce')

    df['bonus_final'] = CONSTANTE_BONUS + df['salario'] * df['bonus_percentual']
    return df

