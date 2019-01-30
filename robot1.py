import logging
from gpiozero import Servo
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
from time import sleep
from aiy.pins import (PIN_A, PIN_B, PIN_C, PIN_D)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

def main():
    text = None
    servo1 = Servo(PIN_A)
    servo2 = Servo(PIN_B)
    servo3 = Servo(PIN_C)
    servo4 = Servo(PIN_D)
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    with aiy.audio.get_recorder():
            status_ui.status('ready')
            while True:
                print('Press the button and speak')
                button.wait_for_press()
                status_ui.status('listening')
                print('Listening...')
                text, audio = assistant.recognize()
                if text.find('Melody')>=0 or text.find('melody')>=0:
                  aiy.audio.say("Ok,let me dance slower for a melody song")
                  x=0
                  y=1
                  q=0
                  w=1
                  for z in range(0,3):
                    while(x<=0.89 and y>=-0.89):
                        x=x+0.3
                        y=y-0.3
                        sleep(0.2)
                        print(x)
                        servo1.value=x
                        servo2.value=y
                    while(q<=0.89 and w>=-0.89):
                        q=q+0.3
                        w=w-0.3
                        sleep(0.2)
                        print(x)
                        servo3.value=q
                        servo4.value=w
                    while(x>=-0.89 and y<=0.89):
                        x=x-0.3
                        y=y+0.3
                        sleep(0.2)
                        print(x)
                        servo1.value=x
                        servo2.value=y
                    while(q>=-0.89 and w<=0.89):
                        q=q-0.3
                        w=w+0.3
                        sleep(0.2)
                        print(x)
                        servo3.value=q
                        servo4.value=w
                  servo1.value=0
                  servo2.value=0
                  servo3.value=0
                  servo4.value=0
                elif text.find('low')>=0 or text.find("Low")>=0:
                  aiy.audio.say("Really do you want me to make it slower?")
                  sleep(1)
                  aiy.audio.say("ok,It may look like break dance,dont make fun of me")
                  x=0
                  y=1
                  q=0
                  w=1
                  for z in range(0,3):
                    while(x<=0.89 and y>=-0.89):
                        x=x+0.1
                        y=y-0.1
                        sleep(0.25)
                        print(x)
                        servo1.value=x
                        servo2.value=y
                    while(q<=0.89 and w>=-0.89):
                        q=q+0.1
                        w=w-0.1
                        sleep(0.25)
                        print(x)
                        servo3.value=q
                        servo4.value=w
                    while(x>=-0.89 and y<=0.89):
                        x=x-0.1
                        y=y+0.1
                        sleep(0.25)
                        print(x)
                        servo1.value=x
                        servo2.value=y
                    while(q>=-0.89 and w<=0.89):
                        q=q-0.1
                        w=w+0.1
                        sleep(0.25)
                        print(x)
                        servo3.value=q
                        servo4.value=w
                  servo1.value=0
                  servo2.value=0
                  servo3.value=0
                  servo4.value=0

                elif text.find('Surya')>=0 or text.find('surya')>=0:
                  aiy.audio.say("Let me dance faster like singam surya")
                  for a in range(0,5):
                    servo1.value=1
                    servo2.value=-1
                    sleep(1)
                    servo1.value=-1
                    servo2.value=1
                    sleep(1)
                  servo1.value=0
                  servo2.value=0
                  servo3.value=0
                  servo4.value=0
                elif text.find('high')>=0 or text.find('High')>=0 or text.find("hi")>=0 or text.find("Hi")>=0:
                 aiy.audio.say("Ok,Let me make it faster")
                 for s in range(0,10): 
                  servo1.value=1
                  servo2.value=-1
                  sleep(0.2)
                  servo1.value=-1
                  servo2.value=1
                  sleep(0.2)
                 servo1.value=0
                 servo2.value=0
                 servo3.value=0
                 servo4.value=0

if __name__ == '__main__':
        main()

