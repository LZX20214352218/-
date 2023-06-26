import json
import os

train = {}
with open('train.json', 'r') as f:
    train = json.load(f)

weather_list =  {'Cloudy': 0, 'Rainy': 1, 'Sunny': 2}
f_weather=open('train_weather.txt','w')
for item in train["annotations"]:
    label = weather_list[item['weather']]
    file_name=os.path.join(item['filename'].split('\\')[0], item['filename'].split('\\')[1])
    f_weather.write(file_name +' '+ str(label) +'\n')
f_weather.close()
print("写入train_weather.txt完成！！！")