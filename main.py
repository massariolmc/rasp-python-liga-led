import RPi.GPIO as gpio
import time


class AcendeLed():
    def __init__(self):
        #Desabilita os warnings
        gpio.setwarnings(False)
        gpio.cleanup()
        self.define_pins()

    def define_pins(self):
        self.leds = {
                'led1': 3,
                'led2' : 5
            }
        self.define_setup(**self.leds)

    def define_setup(self,**kwargs):
        gpio.setmode(gpio.BOARD)
        for nome_pins,valor_pins in kwargs.items():
            gpio.setup(valor_pins,gpio.OUT)

    def piscar_led(self):
        for k,v in self.leds.items():
            gpio.output(v,gpio.LOW)
            time.sleep(1)
            gpio.output(v,gpio.HIGH)

if __name__ == '__main__':
    exe = AcendeLed()
    try:
       while True:
           exe.piscar_led()
    except Exception as e:
        print(e)
    finally:
        #Desfaz as configurações dos pinos
        gpio.cleanup()
