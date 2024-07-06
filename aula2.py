import pandas as pd


def funcao_string_numero(string):
    return float(string.replace('.', '').replace(',', '.'))


path = '/home/edgar/Documents/Aula/BS Faturamento - ZSD090/'
base = pd.read_csv(f'{path}24.01.Janeiro.csv')
base['novo2'] = base['Vlr s/Pont.'].apply(lambda valor: float(valor.replace('.', '').replace(',', '.')))

novo_describe = base.groupby('Grupo Mercadoria')['novo2'].describe().sort_values(['min', 'std'], ascending=False)
novo_describe = novo_describe.reset_index()

novo_describe.to_csv(f'{path}24.01.Janeiro_resultado.csv', index=False, encoding='utf-8', float_format='%.2f', decimal=',')







