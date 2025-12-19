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
    print("[PATTERN] Heartbeat")
    blink(led, 0.2, 0.2)
    blink(led, 0.2, 0.5)
    

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

choices = input("Choose LED pattern (blink slow, blink fast, heartbeat, sos): ").lower()
PATTERNS = {
    "blink slow": ("Slow Blink", blink_slow),
    "blink fast": ("Fast Blink", blink_fast),
    "heartbeat": ("Heartbeat", heartbeat),
    "sos": ("SOS Signal", sos),
}

def main():
    led = LED(17)  # GPIO pin 17
    counter = 0
    
    name, pattern_func = PATTERNS.get(choices, (None, None))

    if pattern_func is None:
        print("Invalid choice... Exiting")
        return
    
    try:
        while counter <= 5:
            counter += 1
            print(f"Executing Pattern: {name} (Iteration {counter})")
            pattern_func(led)

    except KeyboardInterrupt:
        print("Program Termination")
        led.off()

if __name__ == "__main__":
    main()

