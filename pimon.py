from neopixel import *
from gpiozero import Button
from time import sleep
import random

green = Button(4)
pink = Button(17)
yellow = Button(27)
blue = Button(22)


LED_COUNT      = 360      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 32     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


def neo(color,n):
    if color == "pink":
        for i in range(90):
            strip.setPixelColor(i,Color(20,255,147))
        strip.show()
        sleep(n)
        for i in range(90):
            strip.setPixelColor(i,Color(0,0,0))
    elif color == "green":
        for i in range(90,180):
            strip.setPixelColor(i,Color(255,0,0))
        strip.show()
        sleep(n)
        for i in range(90,180):
            strip.setPixelColor(i,Color(0,0,0))

    elif color == "blue":
        for i in range(180,270):
            strip.setPixelColor(i,Color(0,0,255))
        strip.show()
        sleep(n)
        for i in range(180,270):
            strip.setPixelColor(i,Color(0,0,0))

    elif color == "yellow":
        for i in range(270,360):
            strip.setPixelColor(i,Color(255,255,0))
        strip.show()
        sleep(n)
        for i in range(27,360):
            strip.setPixelColor(i,Color(0,0,0))

def correct(n):
    for i in range(3):
        for i in range(360):
            strip.setPixelColor(i,Color(255,0,0))
        strip.show()
        sleep(n)
        for i in range(360):
            strip.setPixelColor(i,Color(0,0,0))

def wrong(n):
    for i in range(3):
        for i in range(360):
            strip.setPixelColor(i,Color(0,255,0))
        strip.show()
        sleep(n)
        for i in range(360):
            strip.setPixelColor(i,Color(0,0,0)) 



if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    try:
        lights = ['pink','yellow','blue','green']

        while True:
            green.wait_for_press()
            for i in range(16):
                for light in lights:
                    neo(light,0.1)
            random.shuffle(lights)
            print(lights)
            sleep(1)
            player = []
            for light in lights:
                neo(light,0.3)    
            for i in range(360):
                strip.setPixelColor(i,Color(0,0,0))
                strip.show()
            while len(player) <4:
                sleep(0.4)
                if green.is_pressed:
                    player.append("green")
                    print(player)
                elif pink.is_pressed:
                    player.append("pink")
                    print(player)
                elif yellow.is_pressed:
                    player.append("yellow")
                    print(player)
                elif blue.is_pressed:
                    player.append("blue")
                    print(player)        
            for choice in player:
                neo(choice,0.5)
            if lights == player:
                print("CORRECT")
                correct(0.5)
                for i in range(360):
                    strip.setPixelColor(i,Color(0,0,0))
                strip.show()
            else:
                print("WRONG ANSWER McFLY")
                wrong(0.5)
                for i in range(360):
                    strip.setPixelColor(i,Color(0,0,0))
                strip.show()  
                    
            
    except KeyboardInterrupt:
        for i in range(360):
            strip.setPixelColor(i,Color(0,0,0))
        strip.show()
    
