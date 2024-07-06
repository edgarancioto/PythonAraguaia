from os import listdir
import pandas as pd
import time

# capturando o inicio da execução em milissegundos
start = time.time()

# função que cria o arquivo local consolidado
def cria_consolidado(path, files):
    bases = []
    # para cada arquivo da pasta
    for file in files:
        # tente
        try:
            # ler o arquivo como excel, filtrando apenas a coluna 'Sheet1'
            df = pd.read_excel(path + file, 'Sheet1')
            # atribuindo o nome do arquivo ao conjunto de dados lidos
            df['name'] = file
            # adiciona na lista de arquivos
            bases.append(df)
        except ValueError as e:
            # tratamento/exibição de erros
            print(file, e)

    # concatenando os arquivos lidos em um único dataframe
    base_final = pd.concat(bases)
    # transformando e salvando o dataframe em csv na mesma pasta
    base_final.to_csv(f'{path}consolidado.csv')
    # retornando o dataframe criado
    return base_final

# pasta com os arquivos
path = '/home/edgar/Documents/Aula/BS Faturamento - ZSD090/xlsx/'

# lista de arquivos da pasta
files = listdir(path)

# verifica se o arquivo consolidado já existe entre os arquivos da pasta
if 'consolidado.csv' in files:
    # leitura do arquivo consolidado em dataframe
    print('consolidado')
    df = pd.read_csv(path + 'consolidado.csv')
else:
    # chamada da função de criação do arquivo consolidado
    print('criação')
    df = cria_consolidado(path, files)

# captura do tempo final da execução
end = time.time()
print(end-start)


#   filtrando a série de dados com valores não nulos
#   df[coluna][~df[coluna].isna()].count()
#   série escolhida: df[coluna]
#   valores nulos da série: df[coluna].isna() --> negando com ~ -- transformando em valores não nulos
#   filtrando a série com a condição anterior df[coluna]['condição']
#   contagem sobre o resultado do filtro df[coluna]['condição'].count()


for coluna in df.columns:
    print(coluna, df[coluna][~df[coluna].isna()].count())

print('')
