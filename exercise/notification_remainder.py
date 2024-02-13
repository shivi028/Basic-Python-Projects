import time
from plyer import notification

if __name__ == '__main__':
    # while True:
     notification.notify(
         title = '*** Water Break ***',
         message = 'Take a break and keep yourself hydrated and make yourselg glowing.',
         app_icon = 'C:/Users/shivi/Downloads/favicon.png',
         timeout = 5
    )
     time.sleep(10)
