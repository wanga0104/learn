time = int(input('需要转换的秒数：'))
day = time//86400
hour = time//3600-day*24
min = time//60-day*24*60-hour*60
sec = time-day*86400-hour*3600-min*60
print(time,'秒可以转化为：',day,'天',hour,'小时',min,'分钟',sec,'秒',sep='')
print(f'{time}秒可以转化为：{day}天{hour}小时{min}分钟{sec}秒')
print('%d秒可以转化为：%d天%d小时%d分钟%d秒'%(time,day,hour,min,sec))
print('{}秒可以转化为：{}天{}小时{}分钟{}秒'.format(time,day,hour,min,sec))