import win32com.client

speaker = win32com.client.Dispatch('SAPI.spVoice')

# while 1:
#     print('enter any word you want it to speak loud by computer\nif you want to exit press ctrl + z\n')
#     s = input()
#     speaker.speak(s)


name_list = ['shivi', 'tiwari', 'raanu', 'pradeep', 'raam'];

for i in name_list:
    ans = f'shoutout to {i}'
    speaker.speak(ans);
