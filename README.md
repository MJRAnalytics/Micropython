# Micropython
Repository for Micropython breadboard projects on the Raspberry Pi Pico and the ESP32.

---

### Micro Game of Life
A MicroPython implementation of Conway's Game of Life, designed to run on an ESP32 and display on a 128x64 yellow and blue OLED screen. The grid is drawn in the blue portion of the screen, and the yellow portion displays the time and generation count. The seed for the game is randomly generated based on potentiometer values.

**Features:**
  - Random seed generation using potentiometers.
  - Displays elapsed time and generation in the yellow zone.
  - Conway’s Game of Life simulation in the blue zone.
  - Button and toggle switch input for starting the game and controlling the simulation.

**Components Used:**
  - ESP32
  - 128x64 yellow and blue OLED display
  - Potentiometers, button, toggle switch

**Purpose:**
  - Demonstrates a simple yet interactive implementation of Conway’s Game of Life on a MicroPython platform with a small OLED display.

---

### RFID Music Player
Plays a tune on a WS2812 buzzer using a Raspberry Pi Pico. The song pattern is saved on an RFID tag, so each scan plays a portion of the song off of each tag.

**Features:**
  - Plays portions of a song based on RFID tag scans.

**Components Used:**
  - Raspberry Pi Pico
  - RFID reader and tags
  - WS2812 buzzer

**Purpose:**
  - A simple project to demonstrate playing sound through a WS2812 buzzer, triggered by RFID tag scans.

---

### Raspberry Pi Pico Thermometer and Humidity Sensor
This program reads from a DHT11 temperature/humidity sensor and a temperature sensor, providing the temperature in Fahrenheit and the relative humidity, displayed on an LCD1602 screen every 2 seconds.

**Features:**
  - Displays temperature in Fahrenheit and relative humidity on an LCD screen.
  - Updates every 2 seconds.

**Components Used:**
  - Raspberry Pi Pico
  - DHT11 temperature/humidity sensor
  - LCD1602 screen

**Purpose:**
  - A practical project for displaying environmental data with an LCD screen and sensors.

---

### uConfig - Custom Configuration Parser
uConfig is a custom configuration parser written in MicroPython that provides functionality similar to the `configparser` library in CPython. It reads a configuration file and stores the values in a dictionary.

**Features:**
  - Reads and stores configuration values in a dictionary format.
  - Handles multiple sections and key-value pairs in the config file.

**Components Used:**
  - Pure MicroPython code

**Purpose:**
  - A simple solution for reading configuration files in MicroPython, without needing to use JSON.

---

### MicroDiscordApi
MicroDiscordApi is a Discord API wrapper for the ESP32 that allows posting to a Discord server. It was inspired by parts of the official API and based on a project I found on the 'awesome-micropython' repository.

**Features:**
  - Allows the ESP32 to send data to a Discord server.

**Components Used:**
  - ESP32

**Purpose:**
  - A Discord API wrapper for the ESP32 that facilitates posting to Discord servers from microcontrollers.
