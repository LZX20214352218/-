import pandas as pd
from collections import Counter
from imblearn.over_sampling import SMOTE
import numpy as np


def upsampleing(filename):
    print(50 * '*')
    data = pd.read_csv(filename, header=None, sep=' ')
    print(data[1].value_counts())
    # 查看各个标签的样本量
    print(Counter(data[1]))
    print(50 * '*')
    # 数据均衡
    X = np.array(data[0].index.tolist()).reshape(-1, 1)
    y = data[1]
    ros = SMOTE(random_state=0)
    X_resampled, y_resampled = ros.fit_resample(X, y)
    print(Counter(y_resampled))
    print(len(y_resampled))
    print(50 * '*')
    img_list = []
    for i in range(len(X_resampled)):
        img_list.append(data.loc[X_resampled[i]][0].tolist()[0])
    dict_weather = {'0': img_list, '1': y_resampled.values}
    newdata = pd.DataFrame(dict_weather)
    print(len(newdata))
    new_filename = filename.split('.')[0] + '_imblearn' + '.txt'
    newdata.to_csv(new_filename, header=None, index=None, sep=' ')


filename = 'train_train_weather.txt'
upsampleing(filename)
filename = 'eval_train_weather.txt'
upsampleing(filename)