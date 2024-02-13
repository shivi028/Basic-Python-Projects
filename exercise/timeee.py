# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

H = int(input('enter the hour\n'));

if(H>=0 and H<12):
    print('morning')

elif(H>=12 and H<17):
    print('afternoon')

elif(H>=17 and H<19):
    print('evening')
    
elif(H>=19 and H<24):
    print('night')

 

