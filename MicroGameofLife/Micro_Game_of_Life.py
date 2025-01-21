import ssd1306
from machine import Pin, SoftI2C, ADC
import time
import urandom  # For pseudo randomness

# Initialize I2C for OLED
i2c = SoftI2C(scl=Pin(35), sda=Pin(33))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize peripherals
toggle_switch = Pin(10, Pin.IN, Pin.PULL_UP)  # Toggle switch
potentiometer_1 = ADC(Pin(7))  # Potentiometer 1
potentiometer_2 = ADC(Pin(3))  # Potentiometer 2
button_1 = Pin(11, Pin.IN, Pin.PULL_UP)  # Button 1 with pull-up

# Configure ADC attenuation for potentiometers
potentiometer_1.atten(ADC.ATTN_11DB)    # 0-3.6V range
potentiometer_2.atten(ADC.ATTN_11DB)

# Game grid setup
WIDTH, HEIGHT = 128, 64  # Screen resolution
CELL_SIZE = 4            # Size of each cell in pixels
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = (HEIGHT - 16) // CELL_SIZE  # Leave 10px for the yellow area

# Create a 2D grid (0 = dead, 1 = alive)
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
next_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Display a startup message
def startup_message():
    oled.fill(0)
    oled.text("Micro", 20, 20)
    oled.text("Game of Life", 10, 40)
    oled.show()

# Generate a random seed based on potentiometers
def generate_random_seed():
    random_factor_1 = potentiometer_1.read() // 256  # Scale to 0-15
    random_factor_2 = potentiometer_2.read() // 256  # Scale to 0-15
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = urandom.getrandbits(1) if urandom.getrandbits(4) < (random_factor_1 + random_factor_2) else 0
    draw_grid(0, 0)

# Draw the grid and the time/step information
def draw_grid(elapsed_time, step):
    oled.fill(0)  # Clear the screen
    
    # Display time and step count in the yellow portion (top 10 pixels)
    oled.text(f"Time: {elapsed_time}s", 0, 0)
    oled.text(f"T: {step}", 80, 0)
    
    # Draw the grid in the blue portion
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                oled.fill_rect(x * CELL_SIZE, (y * CELL_SIZE) + 16, CELL_SIZE, CELL_SIZE, 1)
    
    oled.show()

# Count the number of alive neighbors around a cell
def count_neighbors(x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
            count += grid[ny][nx]
    return count

# Update the grid according to the Game of Life rules
def update_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            alive_neighbors = count_neighbors(x, y)
            if grid[y][x] == 1:  # Alive cell
                next_grid[y][x] = 1 if 2 <= alive_neighbors <= 3 else 0
            else:  # Dead cell
                next_grid[y][x] = 1 if alive_neighbors == 3 else 0
    # Swap grids
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = next_grid[y][x]

# Main loop
def main():
    startup_message()
    
    # Wait for the toggle switch to be turned on
    while toggle_switch.value() == 0:
        time.sleep(0.1)  # Check periodically

    # Toggle switch is ON: allow setting a random seed
    while toggle_switch.value() == 1:
        generate_random_seed()
        oled.text("Press Button", 10, 55)
        oled.show()
        
        # Check if the button is pressed
        if button_1.value() == 0:  # Button pressed
            time.sleep(0.2)  # Debounce delay
            while button_1.value() == 0:
                pass  # Wait for button release

            # Start the simulation
            start_time = time.ticks_ms()  # Record start time
            step = 0  # Generation counter

            while toggle_switch.value() == 1:  # Stop if toggle is turned off
                current_time = time.ticks_ms()  # Current time in milliseconds
                elapsed_time = time.ticks_diff(current_time, start_time) // 1000  # Elapsed time in seconds

                # Display elapsed time and generation on the yellow portion
                draw_grid(elapsed_time, step)  # Pass elapsed time and step to draw_grid()
                update_grid()
                step += 1  # Increment generation count
                time.sleep(0.1)  # Animation speed

        time.sleep(0.1)  # Small delay to avoid rapid polling

    # If toggle switch is turned off, restart the program
    main()

# Run the program
try:
    main()
except KeyboardInterrupt:
    print("Program stopped.")
