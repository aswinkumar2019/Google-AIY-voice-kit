import logging
from gpiozero import Buzzer
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
    assistant = aiy.assistant.grpc.get_assistant()
    text = None
    bz1=Buzzer(PIN_A)
    bz2=Buzzer(PIN_B)
    bz3=Buzzer(PIN_C)
    bz1.on()
    bz2.on()
    bz3.on()
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    button = aiy.voicehat.get_button()
    status_ui.status('ready')
    with aiy.audio.get_recorder():
           while True:
                print('Press the button and speak')
                button.wait_for_press()
                print('Listening...')
                text, audio = assistant.recognize()
                print(text)
                if text == 'red': 
                    bz1.off()
                    bz2.on()
                    bz3.on()
                    print('RED')
                elif text == 'violet' or text == 'purple':
                    bz1.off()
                    bz2.off()
                    bz3.on()
                elif text == 'blue':
                    bz1.on()
                    bz2.off()
                    bz3.on()
                else:
                    aiy.audio.say("I cant understand")

if __name__ == '__main__':
        main()

