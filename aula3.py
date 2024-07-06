import pandas as pd
import time

start = time.time()

path = '/home/edgar/Documents/Aula/BS Faturamento - ZSD090/'
base = pd.read_csv(f'{path}24.01.Janeiro.csv')
colunas = ['Número OV', 'Data OV', 'Nota Fiscal', 'Faturamento', 'Data Fat.', 'UF', 'Cidade', 'CanDist',
           'Desc. CanalDist.', 'GrpMerc', 'Grupo Mercadoria', 'DenomGrpMat',
           'Equipe Vendas', 'Centro', 'Material', 'Desc. Material', 'UnMed',
           'QtdFat', 'Peso Unit.', 'Un.Peso', 'Vlr s/Pont.', 'Inco.1']


def funcao_string_numero(string):
    return float(string.replace('.', '').replace(',', '.'))


def convert_numeros(base, coluna):
    try:
        base[coluna] = base[coluna].astype(float)
        return
    except:
        pass
    try:
        base[coluna] = base[coluna].apply(funcao_string_numero)
        return
    except:
        pass


for coluna in base.columns:
    convert_numeros(base, coluna)

base['peso_bruto'] = base['QtdFat'] * base['Peso Unit.']

end = time.time()
print('rodou em', end-start)








