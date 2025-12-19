#from gpiozero import LED
from time import sleep

# MOCK PINS FOR SIMULATION
class LED:
    def __init__(self, pin):
        self.pin = pin

    def on(self):
        print(f"[SIMULATION] LED on pin {self.pin} is ON")

    def off(self):
        print(f"[SIMULATION] LED on pin {self.pin} is OFF")


#LED PATTERNS
def blink(led, on_time, off_time):
        led.on()
        sleep(on_time)
        led.off()
        sleep(off_time)


def blink_slow(led):
    blink(led, 1, 1)
    
def blink_fast(led):
    blink(led, 0.2, 0.2)

def heartbeat(led):
    blink(led, 0.2, 0.2)
    sleep(0.4)
    

def sos(led):
    for i in range(3):
        blink_fast(led) # S three short blinks

    sleep(0.6)
    for i in range(3):
        blink(led, 0.6, 1) # O three medium blinks
    sleep(0.6)

    for i in range(3):
        blink_fast(led) # S three short blinks
    sleep(0.6)

test_pattern = "heartbeat"  # Options: "blink_slow", "blink_fast", "heartbeat", "sos"

def main():
    led = LED(17)  # GPIO pin 17
    counter = 0
    try:
        while counter <= 5:
            counter += 1
            print(f"Executing pattern: {test_pattern}")

            if test_pattern =="blink_slow":
                blink_slow(led)

            elif test_pattern =="blink_fast":
                blink_fast(led)

            elif test_pattern == "heartbeat":
                heartbeat(led)
            elif test_pattern == "sos":
                print("Sending SOS Signal")
                sos(led)
            print(counter)

            

    except KeyboardInterrupt:
        print("Program Termination")
        led.off()



if __name__ == "__main__":
    main()

