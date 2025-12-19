
## from gpiozero import LED
from time import sleep

#MOCK PINS FOR SIMULATION
class LED:
    def __init__(self, pin):
        self.pin = pin

        def on(self):
            print(f"[SIMULATION] LED on pin {self.pin} is ON")

        def off(self):
            print(f"[SIMULATION] LED on pin {self.pin} is OFF")


# MOCK PINS FOR SIMULATION
class LED:
    def __init__(self, pin):
        self.pin = pin

    def on(self):
        print(f"[SIMULATION] LED on pin {self.pin} is ON")

    def off(self):
        print(f"[SIMULATION] LED on pin {self.pin} is OFF")


def main():
    led = LED(17)  # GPIO pin 17

    try:
        while True:
            led.on()
            print("LED IS NOW ON")
            sleep(1)

            led.off()
            print("LED IS NOW OFF")
            sleep(1)

    except KeyboardInterrupt:
        print("Program Termination")
        led.off()



if __name__ == "__main__":
    main()

