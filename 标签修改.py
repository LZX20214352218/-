import json
import os

train = {}
with open('train.json', 'r') as f:
    train = json.load(f)

period_list = {'Dawn': 0, 'Dusk': 1, 'Morning': 2, 'Afternoon': 3}
f_period=open('train_period.txt','w')
for item in train["annotations"]:
    label = period_list[item['period']]
    file_name=os.path.join(item['filename'].split('\\')[0], item['filename'].split('\\')[1])
    f_period.write(file_name +' '+ str(label) +'\n')
f_period.close()
print("写入train_period.txt完成！！！")