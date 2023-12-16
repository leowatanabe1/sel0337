from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura")
while True:
        id, texto = leitor.read()
        if id == 565782449781:
                GPIO.output(38, True)
                GPIO.output(40, False)
                print("Acesso liberado")
        if id != 565782449781:
                GPIO.output(38, False)
                GPIO.output(40, True)
                print("Acesso negado")
        print("ID: {}\nTexto: {}".format(id, texto))
        sleep(3)