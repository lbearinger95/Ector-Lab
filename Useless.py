from machine import Pin,PWM
from myservo import Servo
from time import sleep 
import time 
from machine import I2C, Pin
from I2C_LCD import I2CLcd
buzzer = PWM(Pin(6)) #Speaker is usually 4 but buzzer is 


notes = {"C0": 16,
    "C#0": 17,
    "D0": 18,
    "D#0": 19,
    "E0": 20,
    "F0": 21,
    "F#0": 23,
    "G0": 24,
    "G#0": 26,
    "A0": 27,
    "A#0": 29,
    "B0": 31,
    "C1": 33,
    "C#1": 35,
    "D1": 37,
    "D#1": 39,
    "E1": 41,
    "F1": 44,
    "F#1": 46,
    "G1": 49,
    "G#1": 52,
    "A1": 55,
    "A#1": 58,
    "B1": 62,
    "C2": 65,
    "C#2": 69,
    "D2": 73,
    "D#2": 78,
    "E2": 82,
    "F2": 87,
    "F#2": 92,
    "G2": 98,
    "G#2": 104,
    "A2": 110,
    "A#2": 117,
    "B2": 123,
    "C3": 131,
    "C#3": 139,
    "D3": 147,
    "D#3": 156,
    "E3": 165,
    "F3": 175,
    "F#3": 185,
    "G3": 196,
    "G#3": 208,
    "A3": 220,
    "A#3": 233,
    "B3": 247,
    "C4": 262,
    "C#4": 277,
    "D4": 294,
    "D#4": 311,
    "E4": 330,
    "F4": 349,
    "F#4": 370,
    "G4": 392,
    "G#4": 415,
    "A4": 440,
    "A#4": 466,
    "B4": 494,
    "C5": 523,
    "C#5": 554,
    "D5": 587,
    "D#5": 622,
    "E5": 659,
    "F5": 698,
    "F#5": 740,
    "G5": 784,
    "G#5": 831,
    "A5": 880,
    "A#5": 932,
    "B5": 988,
    "C6": 1047,
    "C#6": 1109,
    "D6": 1175,
    "D#6": 1244,
    "E6": 1318,
    "F6": 1397,
    "F#6": 1480,
    "G6": 1568,
    "G#6": 1661,
    "A6": 1760,
    "A#6": 1864,
    "B6": 1975,
    "C7": 2093,
    "C#7": 2217,
    "D7": 2349,
    "D#7": 2489,
    "E7": 2637,
    "F7": 2794,
    "F#7": 2960,
    "G7": 3136,
    "G#7": 3322,
    "A7": 3520,
    "A#7": 3729,
    "B7": 3951,
    "C8": 4186,
}

#Plays the song or whatever you want
def play_mario_theme(notes, buzzer):
    buzzer.duty_u16(1000) 
    buzzer.freq(532)
    sleep(0)
    mario_theme_simplified = ["E6", "E4", "G4", "C4", "E4", "G4", "G4"]

    for note in mario_theme_simplified:
        if note in notes:
            frequency = notes[note]
            buzzer.duty_u16(512)
            buzzer.freq(int(frequency))
            sleep(0.3)
            buzzer.duty_u16(0)
            sleep(0.5)




def getDistance():
    Trig = Pin(19, Pin.OUT, 0)
    Echo = Pin(18, Pin.IN, 0)

    distance = 0
    soundVelocity = 340
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    stoptime = time.ticks_ms() 
    
    while not Echo.value():
        StartTime = time.ticks_ms()
        minusTime = time.ticks_diff(StartTime, stoptime) 
        if minusTime > 100:
            return 0 
    
        pass
    pingStart = time.ticks_us()
    
    while Echo.value():
        pass
    pingStop = time.ticks_us()
    distanceTime = time.ticks_diff(pingStop, pingStart) // 2
    distance = int(soundVelocity * distanceTime // 10000)
    return distance

#Uses the function getDistance to get  the distance in sonar 
def sonarplay(): 
    time.sleep(2)
    while True:
        time.sleep_ms(500)
        distance = getDistance()
        print("Distance: ", distance, "cm")

#Sets up the lcd 
def lcdplay():
    i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
    devices = i2c.scan()

    try:
        if devices != []:
            lcd = I2CLcd(i2c, devices[0], 2, 16)
            lcd.move_to(0, 0)
            lcd.putstr("Hello Students")
            count = 0
            while True:
                lcd.move_to(0, 1)
                lcd.putstr("Counter:%d" %(count))
                time.sleep(1)
                count += 1
        else:
            print("No address found")
    except:
        pass

def ledplay():
    pwm = PWM(Pin(22))
    pwm.freq(10000)

    try:
        while True:
    #Range of pwm 16 bits (0-65535)
            for i in range(0, 65535):
                pwm.duty_u16(i)
                time.sleep_us(100)
            for i in range(65535, 0, -1):
                pwm.duty_u16(i)
                time.sleep_us(100)
    except:
    #turn pwm off
        pwm.deinit()

# Function to control the LED based on sonar distance
def control_led(distance):
    led_pin = Pin(22, Pin.OUT)

    if distance > 20:
        led_pin.on()  # Turn on the LED
    else:
        led_pin.off()  # Turn off the LED


def distance_led_play():
    while True:
        distance = getDistance()
        print("Distance:", distance, "cm")
        control_led(distance)
        sleep(0.5)  # Adjust the delay as needed


def servoplay(): 
    servo=Servo(20)
    time.sleep_ms(1000)
    switchpin = 11
    Switch=Pin(switchpin,Pin.IN,Pin.PULL_UP)

    while True:  
        switchvalue = Switch.value()
        print(switchvalue)
        if switchvalue == 1: 
            servo.ServoAngle(0)
            time.sleep_ms(10)
        elif switchvalue == 0: 
            servo.ServoAngle(180)
            time.sleep_ms(10)    
        else:
            servo.deinit()

servoplay()
