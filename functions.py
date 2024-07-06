from os import listdir
import pandas as pd

path = '/home/edgar/Documents/Aula/BS Faturamento - ZSD090/test/'

files = listdir(path)
bases = []

for file in files:
    with open(f'{path}{file}') as f:
        base = pd.read_csv(f)
        bases.append(base)

base_final = pd.concat(bases)

