import win32com.client

speaker = win32com.client.Dispatch('SAPI.spVoice')

if __name__ == '__main__':
    print('WelCome to ROBOSPEAKER, Created by Shivi')
    while True:
        x = input('enter anything you want to listen: ')
        if x == 'q':
            speaker.speak('you have quit the program, ThankYou for using it')
            break
        command = f"{x}"
        speaker.speak(command)