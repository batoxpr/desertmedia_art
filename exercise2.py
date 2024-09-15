import time
import board
import neopixel

# Initialize the on-board Neopixel
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)

# Color definitions
PINK = (255, 102, 255)  # Calm, soft pink
RED = (255, 0, 0)       # Peak heart rate, deep red

# Function to blink the light for a given number of times and delay
def blink_color(color, blink_times, delay):
    for _ in range(blink_times):
        pixels.fill(color) # Turn the light on
        time.sleep(delay)  # Wait for a bit
        pixels.fill((0, 0, 0))  # Turn the light off
        time.sleep(delay)  # Wait for a bit more

# Loop to repeat the heart rate animation
while True:
    # Stage 1: Slow heart rate, pink blinking
    blink_color(PINK, 5, 0.8)  # Slow bpm at rest

    # Gradually increase the blinking speed and transition to red
    for i in range(5):
        # Transition from pink to red
        r = PINK[0] + (RED[0] - PINK[0]) * i // 5
        g = PINK[1] + (RED[1] - PINK[1]) * i // 5
        b = PINK[2] + (RED[2] - PINK[2]) * i // 5
        pixels.fill((r, g, b))
        time.sleep(0.05)  # Short color change delay

        # Increase blink speed
        blink_color((r, g, b), 5, 0.5 - (i * 0.1))  # Faster blinks

    # Stage 2: Fast, red blinking at peak heart rate
    blink_color(RED, 10, 0.1)  # Peak bpm, fast blinks

    # Stage 3: Hold solid red for 5 seconds (peak heart rate reached)
    pixels.fill(RED)
    time.sleep(5)
