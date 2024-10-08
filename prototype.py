import digitalio
import board
import neopixel
import analogio
import time

NUM_PIXELS = 30  # NeoPixel strip length (in pixels)

# Enable the NeoPixel strip
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

# Set up NeoPixel strip
strip = neopixel.NeoPixel(board.D5, NUM_PIXELS, brightness=1, auto_write=False)

# Set up the LDR (light-dependent resistor) using an analog pin
ldr = analogio.AnalogIn(board.A0)

def set_color(color):
    """Sets the color of the entire NeoPixel strip."""
    strip.fill(color)
    strip.show()

def slow_gradient(colors, steps, delay):
    """Creates a slow gradient effect between colors."""
    for i in range(steps):
        # Interpolate between colors
        r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * (i / steps))
        g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * (i / steps))
        b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * (i / steps))
        
        # Set the strip color
        set_color((r, g, b))
        time.sleep(delay)

def get_light_intensity():
    """Reads and normalizes the light intensity from the LDR."""
    # The analog read will give values between 0 and 65535
    return ldr.value / 65535

# Main loop
while True:
    # Get light intensity from LDR
    light_intensity = get_light_intensity()

    # If light intensity is low (darker environment), show gradient of blue tones
    if light_intensity < 0.3:
        # Define the colors for the gradient (darker blue -> turquoise -> ocean blue)
        colors = [(0, 0, 100), (0, 105, 148)]  # Darker blue to ocean blue
        slow_gradient(colors, steps=100, delay=0.02)  # 100 steps for the gradient
    # If light intensity is higher (brighter environment), slowly transition to red
    else:
        # Define the colors for the gradient (blue -> red)
        colors = [(0, 255, 0), (255, 0, 0)]  # Green to red
        slow_gradient(colors, steps=100, delay=0.02)  # 100 steps for the gradient

    time.sleep(0.1)  # Short delay to avoid rapid color switching
