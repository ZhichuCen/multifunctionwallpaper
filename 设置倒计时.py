import json
import datetime

if_start = input('是否开启倒计时？（开启输入1，关闭输入2,输完按回车）')
if if_start == '1':
    title = input('请输入倒计时名称（例如：中考倒计时）\n')
    days = input('请输入剩余在校时间（例如：30）\n')
    newest_date=str(datetime.date.today())
    
    data = {
        'title':title,
        'days':days,
        'newest_date':newest_date,
        'stop':False
    }
elif if_start == '2':
    data = {}
    data['stop'] = True
with open('data.json','w') as f:
        json.dump(data,f)