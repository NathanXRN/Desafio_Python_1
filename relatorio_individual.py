import pandas as pd
from main import carregar_df

def relatorio(df):
    lista_rel = []

    for idx, row in df.iterrows():
        
        if pd.isna(row['nome']) or str(row['nome']).strip() == "":
            continue  
        
        if any(char.isdigit() for char in str(row['nome'])):
            continue  
        
        if row['salario'] < 0:
            continue 
        
        if row['area'] not in ['Vendas', 'TI', 'Financeiro', 'RH', 'Operações']:
            continue  
        try:
            if pd.isna(row['bonus_percentual']):
                continue
            bonus = float(row['bonus_percentual'])
            if bonus < 0 or bonus > 1:
                continue 
        except(ValueError, TypeError):
            continue

        lista_rel.append([
            row['nome'],
            row['area'],
            row['salario'],
            row['bonus_percentual'],
            row['bonus_final']
        ])
    
    if lista_rel:
        df_lista_rel = pd.DataFrame(lista_rel, columns=['nome', 'area', 'salario', 'bonus_percentual', 'bonus_final'])
        
        df_lista_rel['salario'] = pd.to_numeric(df_lista_rel['salario'], errors='coerce')
        df_lista_rel['bonus_percentual'] = pd.to_numeric(df_lista_rel['bonus_percentual'], errors='coerce')
        df_lista_rel['bonus_final'] = pd.to_numeric(df_lista_rel['bonus_final'], errors='coerce')
        
        df_lista_rel.to_csv("relatorio_individual.csv", index=False, encoding="utf-8-sig")
        print(f"Arquivo relatorio_individual.csv gerado com {len(df_lista_rel)} registros válidos!")
        return df_lista_rel
    else:
        print("Nenhum registro válido encontrado")

        df_vazio = pd.DataFrame(columns=['nome', 'area', 'salario', 'bonus_percentual', 'bonus_final'])
        df_vazio['salario'] = df_vazio['salario'].astype('float64')
        df_vazio['bonus_percentual'] = df_vazio['bonus_percentual'].astype('float64')
        df_vazio['calculo_bonus_final'] = df_vazio['bonus_final'].astype('float64')
        return df_vazio

if __name__ == "__main__":
    df = carregar_df()
    relatorio(df)