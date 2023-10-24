import pandas as pd

def make_features(
        data,
        lag_end=8, 
        rolling_mean_size=7, 
        lag_start=1,
        real_features='kp', 
        date_cut='2022.12.31',
        train_test=True):
    '''Добавляет столбцу календарные признаки, скользящее среднее и значения 
    за предыдущие дни'''

    # календарные признаки 
    data['dayofweek'] = data.index.dayofweek
    data['hour'] = data.index.hour
    data['month'] = data.index.month

    # значения за предыдущие дни
    for lag in range(lag_start, lag_end+1):
        data['lag_{}'.format(lag)] = data[real_features].shift(lag)

    # добавляем скользящее среднее 
    data['rolling_mean'] = data[real_features].rolling(rolling_mean_size, closed='left').mean()

    # удаляем пропуски из-за лага
    data.dropna(axis=0, inplace=True)

    # разбивка датасета на тренировочную и тестовую выборку 
    features_train = data.loc[:date_cut].drop([real_features], axis=1)
    target_train = data.loc[:date_cut][real_features]
    features_test = data.loc[date_cut:].drop([real_features], axis=1)
    target_test = data.loc[date_cut:][real_features]

    if train_test:
        return features_train, features_test, target_train, target_test
    else:
        return data


if __name__ == '__main__':
    df = pd.read_csv('data/data_update.csv', index_col=0)
    df.index = pd.to_datetime(df.index)
    features_train, features_test, target_train, target_test = make_features(df)
    features_train.to_csv('data/processed/features_train.csv')
    features_test.to_csv('data/processed/features_test.csv')
    target_train.to_csv('data/processed/target_train.csv')
    target_test.to_csv('data/processed/target_test.csv')