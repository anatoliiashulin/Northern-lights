import pandas as pd

def make_file(url = 'https://www-app3.gfz-potsdam.de/kp_index/Kp_ap_since_1932.txt', path = 'data/update/data_update.csv'):
    '''обновляет базу данных'''
    df = pd.read_csv(url, skiprows=30, header=None)
    df = df.loc[:,0].str.split(expand=True) 
    df['datetime'] = df[0] + '.' + df[1] + '.' + df[2] + ' ' + df[3].apply(lambda x: x[:2]) + ':00:00'
    df.index = df['datetime']
    df = df[7].copy()
    df.rename('kp', inplace=True)
    df = df.astype('float')
    df.to_csv(path)

if __name__ == '__main__':
    make_file()