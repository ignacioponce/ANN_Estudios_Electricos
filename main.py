import sys

sys.path.insert(0, 'C:\ATP\LisRead')
import LISread_det
import pandas as pd
import numpy as np

path = r'C:\ATP\ATPDraw6.3\BERNAL\\'
file = 'prueba_bernal'

r = LISread_det.read_det(f'{path}{file}{1}.lis', lineSplit='\n')
chn = r['channels']  # se definen los nombres de las variables para buscar las de utilidad
col = chn[chn.index('mLONG'):]
for c in range(len(col)):
    col[c] = col[c][1:]

col = np.append(col, ['Vmax_fn_A', 'Vmax_ff_A', 'Vmax_fn_B', 'Vmax_ff_B'])
data = pd.DataFrame(columns=col)

for i in range(1, 1000):  # se recorren las 100 simulaciones
    try:
        r = LISread_det.read_det(f'{path}{file}{i}.lis',
                                 lineSplit='\n')  # se extraen los datos de una simulación en particular
        data.loc[len(data)] = [r['vmax'][:, chn.index(f'm{col[0]}')][0],
                               r['vmax'][:, chn.index(f'm{col[1]}')][0],
                               r['vmax'][:, chn.index(f'm{col[2]}')][0],
                               r['vmax'][:, chn.index(f'm{col[3]}')][0],
                               r['vmax'][:, chn.index(f'm{col[4]}')][0],
                               r['vmax'][:, chn.index(f'm{col[5]}')][0],
                               r['vmax'][:, chn.index(f'm{col[6]}')][0],
                               r['vmax'][:, chn.index(f'm{col[7]}')][0],
                               r['vmax'][:, chn.index(f'm{col[8]}')][0],
                               r['vmax'][:, chn.index(f'm{col[9]}')][0],
                               r['vmax'][:, chn.index(f'm{col[10]}')][0],
                               r['vmax'][:, chn.index(f'm{col[11]}')][0],
                               r['vmax'][:, chn.index(f'm{col[12]}')][0],
                               r['vmax'][:, chn.index(f'm{col[13]}')][0],
                               r['vmax'][:, chn.index(f'm{col[14]}')][0],
                               r['vmax'][:, chn.index(f'm{col[15]}')][0],
                               r['vmax'][:, chn.index(f'm{col[16]}')][0],
                               r['vmax'][:, chn.index(f'm{col[17]}')][0],
                               r['vmax'][:, chn.index(f'm{col[18]}')][0],
                               r['vmax'][:, chn.index(f'm{col[19]}')][0],
                               r['vmax'][:, chn.index(f'm{col[20]}')][0],
                               r['vmax'][:, chn.index(f'm{col[21]}')][0],
                               r['vmax'][:, chn.index('vLN1A-')][0],
                               r['vmax'][:, chn.index('vLN1A-')][0] * np.sqrt(3),
                               r['vmax'][:, chn.index('vLN1B-')][0],
                               r['vmax'][:, chn.index('vLN1B-')][0] * np.sqrt(3)]
    except:
        print(f'Simulación n°{i} con errores')

print(data)
