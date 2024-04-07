import datetime
import re
today = datetime.datetime.now()
time = ['2秒前', '今天10时', '前天', '昨天', '刚刚', '2分钟前', '3小时前', '1天前', '10天前', '1年前', '10年前']
for i in range(len(time)):
    if '今天' in time[i] or '小时' in time[i] or '分钟' in time[i]:
        time[i] = today.strftime('%Y-%m-%d')
    elif '天前' in time[i]:
        num = re.findall('(\d+)天前', time[i])[0]
        time[i] = (today - datetime.timedelta(days = int(num))).strftime('%Y-%m-%d')
    elif '昨天' in time[i]:
        time[i] = (today - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
    elif '前天' in time[i]:
        time[i] = (today - datetime.timedelta(days = 2)).strftime('%Y-%m-%d')
    elif '刚刚' in time[i]:
        time[i] = (today - datetime.timedelta(days = 0)).strftime('%Y-%m-%d') 
    elif '年前' in time[i]:
        num = re.findall('(\d+)年前', time[i])[0]
        time[i] = (today - datetime.timedelta(days = int(num) * 365)).strftime('%Y-%m-%d')
    elif '小时前' in time[i]:
        num = re.findall('(\d+)小时前', time[i])[0]
        time[i] = (today - datetime.timedelta(hours = int(num))).strftime('%Y-%m-%d')
    elif '分钟前' in time[i]:
        num = re.findall('(\d+)分钟前', time[i])[0]
        time[i] = (today - datetime.timedelta(minutes = int(num))).strftime('%Y-%m-%d')
    elif '秒前' in time[i]:
        num = re.findall('(\d+)秒前', time[i])[0]
        time[i] = (today - datetime.timedelta(seconds = int(num))).strftime('%Y-%m-%d')
print(time)
