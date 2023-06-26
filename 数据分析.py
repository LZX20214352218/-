import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

data=pd.read_csv('train_period.txt', header=None, sep=' ')
print(data[1].value_counts())
data[1].value_counts().plot(kind="bar")