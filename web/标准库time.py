import time



# print(time.asctime())#国外的时间显示
# print(time.time())#时间戳
# print(time.localtime())#获取当前时间
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#获取自定格式时间



#获取两天前的时间
now_timestamp =time.time()
two_day_before =now_timestamp-60*60*24*2
time_tuple =time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple))