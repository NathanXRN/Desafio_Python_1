import pandas as pd 

df = pd.read_csv("formulario.csv")

CONSTANTE_BONUS = 1000

df['bonus_final'] = CONSTANTE_BONUS + df['salario'] * df['bonus_percentual']

erros = []

for idx, row in df.iterrows():
    if pd.isna(row['nome']) or str(row['nome']).strip() == "":
        erros.append([idx, row['nome'], "Nome em branco!"])
    elif any(char.isdigit() for char in str['nome']):
        raise ValueError("O nome contém números")
    elif df['salario'] < 0:
        raise ValueError("Salário não pode ser menor que 0!")
    elif not df['area'] in ['Vendas', 'TI', 'Financeiro','RH','Operações']:
        raise ValueError("A área não está dentro dos permitidos.")
    elif df['bonus_percentual'] < 0 and df['bonus_percentual'] > 1:
        raise ValueError("Percentual não permitido")