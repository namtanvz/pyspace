from datetime import datetime
from playsound import playsound

alarm_time = input('HH:MM:SS\n')
alarm_h = alarm_time[0:2]
alarm_m = alarm_time[3:5]
alarm_s = alarm_time[6:8]
alarm_p = alarm_time[9:11].upper()

while True:
    now = datetime.now()
    current_h = now.strftime('%I')
    current_m = now.strftime('%M')
    current_s = now.strftime('%S')
    current_p = now.strftime('%p')

    if(alarm_p==current_p):
        if(alarm_h==current_h):
            if(alarm_m==current_m):
                if(alarm_s==current_s):
                    print('Get up')
                    playsound('audio.mp3')
                    break