import random
import pandas as pd

data = pd.read_csv('DB.csv')

def export():
    tmp = random.randrange(0, len(data))
    print('{')
    for i in range(2, len(data.columns) - 2):
        print('  "' + data.columns[i] + '": ' + str(data.iloc[tmp][i]) + ',')
    i += 1
    print('  "' + data.columns[i] + '": ' + str(data.iloc[tmp][i]))
    print('}')
    i += 1
    print('Result: ' + data.columns[i] + '\t' + str(data.iloc[tmp][i]))

def export2():
    tmp = random.randrange(0, len(data))
    print('{', end='')
    for i in range(2, len(data.columns) - 2):
        print('"' + data.columns[i] + '": ' + str(data.iloc[tmp][i]) + ', ', end='')
    i += 1
    print('"' + data.columns[i] + '": ' + str(data.iloc[tmp][i]), end='')
    print('}')
    i += 1
    print('Result: ' + data.columns[i] + '\t' + str(data.iloc[tmp][i]))

export2()