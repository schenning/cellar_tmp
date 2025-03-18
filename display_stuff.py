from sense_hat import SenseHat
import time

sense = SenseHat()

white = (255, 255, 255)  
black = (0, 0, 0)  
red = (255, 0, 0) 


cross_pattern = [
    black, black, black, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, white, white, white, white, black, black,
    black, black, black, white, black, black, black, black,
    black, black, black, white, black, black, black, black
]

alphabet = {
    'A': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, white, white, white, white, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black
    ],
    'B': [
        black, white, white, white, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, white, white, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, white, white, white, black, black, black
    ],
    'C': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, white, black,
        black, black, white, white, white, white, black, black,
        black, black, black, black, black, black, black, black
    ],
    'D': [
        black, white, white, white, black, black, black, black,
        black, white, black, black, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, white, black, black, black,
        black, white, white, white, black, black, black, black
    ],
    'E': [
        black, white, white, white, white, white, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, white, white, white, white, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, white, white, white, white, black, black
    ],
    'F': [
        black, white, white, white, white, white, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, white, white, white, white, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black
    ],
    'G': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, white, white, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, black, white, white, white, white, black, black,
        black, black, black, black, black, black, black, black
    ],
    'H': [
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, white, white, white, white, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black
    ],
    'I': [
        black, white, white, white, white, white, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, white, white, white, white, white, black, black
    ],
    'J': [
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, white, white, white, white, black, black, black
    ],
    'K': [
        black, white, black, black, black, white, black, black,
        black, white, black, black, white, black, black, black,
        black, white, black, white, black, black, black, black,
        black, white, white, black, black, black, black, black,
        black, white, black, white, black, black, black, black,
        black, white, black, black, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, black, white, black
    ],
    'L': [
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, white, white, white, white, black, black
    ],
    'M': [
        black, white, black, black, black, black, white, black,
        black, white, white, black, black, white, white, black,
        black, white, black, white, white, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black
    ],
    'N': [
        black, white, black, black, black, black, white, black,
        black, white, white, black, black, black, white, black,
        black, white, black, white, black, black, white, black,
        black, white, black, black, white, black, white, black,
        black, white, black, black, black, white, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black
    ],
    'O': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, black, white, white, white, white, black, black
    ],
    'P': [
        black, white, white, white, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, white, white, white, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, black, black, black, black, black, black
    ],
    'Q': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, white, black, white, black,
        black, white, black, black, black, white, white, black,
        black, white, black, black, black, black, white, black,
        black, black, white, white, white, white, black, black
    ],
    'R': [
        black, white, white, white, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, white, white, white, white, black, black, black,
        black, white, black, white, black, black, black, black,
        black, white, black, black, white, black, black, black,
        black, white, black, black, black, white, black, black,
        black, white, black, black, black, black, white, black
    ],
    'S': [
        black, black, white, white, white, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, black, black,
        black, black, white, white, white, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, black, white, black, black,
        black, white, black, black, black, white, black, black,
        black, black, white, white, white, black, black, black
    ],
    'T': [
        white, white, white, white, white, white, white, white,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black
    ],
    'U': [
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, black, white, white, white, white, black, black
    ],
    'V': [
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, black, white, black, black, white, black, black,
        black, black, white, black, black, white, black, black,
        black, black, black, white, white, black, black, black,
        black, black, black, white, white, black, black, black
    ],
    'W': [
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black,
        black, white, black, white, black, white, white, black,
        black, white, black, white, black, white, white, black,
        black, white, white, black, black, white, white, black,
        black, white, black, black, black, black, white, black
    ],
    'X': [
        black, white, black, black, black, black, white, black,
        black, black, white, black, black, white, black, black,
        black, black, black, white, white, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, white, white, black, black, black,
        black, black, white, black, black, white, black, black,
        black, white, black, black, black, black, white, black,
        black, white, black, black, black, black, white, black
    ],
    'Y': [
        black, white, black, black, black, black, white, black,
        black, black, white, black, black, white, black, black,
        black, black, black, white, white, black, black, black,
        black, black, black, black, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, black, white, black, black, black, black
    ],
    'Z': [
        black, white, white, white, white, white, black, black,
        black, black, black, black, black, white, black, black,
        black, black, black, black, white, black, black, black,
        black, black, black, white, black, black, black, black,
        black, black, white, black, black, black, black, black,
        black, white, black, black, black, black, black, black,
        black, white, white, white, white, white, black, black,
        black, black, black, black, black, black, black, black
    ],
    'SW': [
    
        black, black, red, red, red, red, black, black,
        black, red, red, red, red, red, red, black,
        red, red, red, red, red, red, red, red,
        red, red, red, red, red, red, red, red,
        black, red, red, red, red, red, red, black,
        black, black, red, red, red, red, black, black,
        black, black, red, red, red, red, black, black,
        black, black, black, red, red, black, black, black
    ]
    
}

# Example usage:
# display_pattern(alphabet['A'])



while True:

    sense.set_pixels(alphabet['K'])
    time.sleep(1)
    sense.set_pixels(alphabet['R'])
    time.sleep(1)
    sense.set_pixels(alphabet['I'])
    time.sleep(1)
    sense.set_pixels(alphabet['S'])
    time.sleep(1)
    sense.set_pixels(alphabet['T'])
    time.sleep(1)
    sense.set_pixels(alphabet['I'])
    time.sleep(1)
    sense.set_pixels(alphabet['N'])
    time.sleep(1)
    sense.set_pixels(alphabet['SW'])
    time.sleep(1)
    break

sense.clear()



