import datetime as dt
import os
import time
import vlc



##now_time = dt.datetime.now()
mins=int(input('Введите кол-во минут до сигнала: '))
secs=int(input('Введите кол-во секунд до сигнала: '))
time_before_alarm = dt.time(0, mins, secs)
time.sleep(time_before_alarm.second)

sound_fname = (r'C:\Users\lysvm\PythonApps\Alarm_Clock\Sound_19482.mp3')
playing = vlc.MediaPlayer(sound_fname)
playing.play()
