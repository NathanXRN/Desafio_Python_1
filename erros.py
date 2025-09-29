import pandas as pd
from main import carregar_df

df = carregar_df()

def validacao_erros(df):
    erros = []

    for idx, row in df.iterrows():
        if pd.isna(row['nome']) or str(row['nome']).strip() == "":
            erros.append([idx, row['nome'], "Nome em branco!"])

        if not (pd.isna(row['nome']) or str(row['nome']).strip() == ""):
            if any(char.isdigit() for char in str(row['nome'])):
                erros.append([idx, row['nome'], "O nome contém números"])

        if pd.isna(row['salario']):
            erros.append([idx, row['nome'], "Salário não informado."])
        elif row['salario'] < 0:
            erros.append([idx, row['nome'], "Salário não pode ser menor que 0."])

        if pd.isna(row['area']) or row['area'] not in ['Vendas', 'TI', 'Financeiro', 'RH', 'Operações']:
            erros.append([idx, row['nome'], "A área não está dentro dos permitidos."])

        if pd.isna(row['bonus_percentual']):
            erros.append([idx, row['nome'], "Percentual de bônus não informado!"])
        elif row['bonus_percentual'] < 0 or row['bonus_percentual'] > 1:
            erros.append([idx, row['nome'], "Percentual não permitido"])

    if erros:
        df_erros = pd.DataFrame(erros, columns = ["linha", "nome", "motivo"])
        df_erros.to_csv("erros.csv", index = False, encoding = "utf-8-sig")
        print("Arquivo erros.csv gerado com sucesso!")

    else:
        print("Nnehum erro encontrado.")

if __name__ == '__main__':
    df = carregar_df()
    validacao_erros(df)