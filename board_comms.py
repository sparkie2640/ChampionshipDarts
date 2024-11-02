import serial
import yaml
import logging
import sys, time

# Setup logging
# if os.path.isfile ("DartBoard.log") :
    # os.remove ("DartBoard.log")
logging.basicConfig(filename='DartBoard.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Start of application")

# Read config
try:
    with open ("config.yaml", 'r') as ymlconfig:
        cfg = yaml.load(ymlconfig, Loader=yaml.BaseLoader)
except:
    logging.error("No configuration file found!")
    sys.exit("ERROR: No configuration file found!")

if cfg:
    # General variables from Config
    serialport_dart = cfg['general'] ['serial_dart']
    serialbaud_dart = cfg['general'] ['baud_dart']
    serialport_led = cfg['general'] ['serial_led']
    serialbaud_led = cfg['general'] ['baud_led']
    # Serial configuration
    ser_dart = serial.Serial()
    ser_dart.port = serialport_dart
    ser_dart.baudrate = serialbaud_dart
    #ser_dart.timeout = 1
    ser_led = serial.Serial()
    ser_led.port = serialport_led
    ser_led.baudrate = serialbaud_led
    #ser_led.timeout = 1

# Open dartboard port
try:
    ser_dart.open()
    logging.info("Serial communication to dartboard started")
except(serial.serialutil.SerialException):
    logging.error("Serial communication with dartboard not possible!")
    sys.exit("ERROR: Serial communication with dartboard not possible!")

try:
    ser_led.open()
    logging.info("Serial communication to LED board started")
except(serial.serialutil.SerialException):
    logging.error("Serial communication with LED board not possible!")
    sys.exit("ERROR: Serial communication with LED board not possible!")
   
"""
Possible commands to send to button LEDS

UP_ON
UP_OFF
UP_BLINK
DOWN_ON
DOWN_OFF
DOWN_BLINK
LEFT_ON
LEFT_OFF
LEFT_BLINK
RIGHT_ON
RIGHT_OFF
RIGHT_BLINK
ENTER_ON
ENTER_OFF
ENTER_BLINK
"""

matrix_dict = {
    '15,4': 'D20', '15,3': 'O20', '15,2': 'T20', '15,1': 'I20',
    '10,4': 'D19', '10,3': 'O19', '10,2': 'T19', '10,1': 'I19',
    '14,8': 'D18', '14,7': 'O18', '14,6': 'T18', '14,5': 'I18',
    '9,8': 'D17', '9,7': 'O17', '9,6': 'T17', '9,5': 'I17',
    '8,4': 'D16', '8,3': 'O16', '8,2': 'T16', '8,1': 'I16',
    '7,8': 'D15', '7,7': 'O15', '7,6': 'T15', '7,5': 'I15',
    '11,4': 'D14', '11,3': 'O14', '11,2': 'T14', '11,1': 'I14',
    '12,8': 'D13', '12,7': 'O13', '12,6': 'T13', '12,5': 'I13',
    '13,4': 'D12', '13,3': 'O12', '13,2': 'T12', '13,1': 'I12',
    '6,4': 'D11', '6,3': 'O11', '6,2': 'T11', '6,1': 'I11',
    '6,8': 'D10', '6,7': 'O10', '6,6': 'T10', '6,5': 'I10',
    '12,4': 'D9', '12,3': 'O9', '12,2': 'T9', '12,1': 'I9',
    '7,4': 'D8', '7,3': 'O8', '7,2': 'T8', '7,1': 'I8',
    '9,4': 'D7', '9,3': 'O7', '9,2': 'T7', '9,1': 'I7',
    '11,8': 'D6', '11,7': 'O6', '11,6': 'T6', '11,5': 'I6',
    '14,4': 'D5', '14,3': 'O5', '14,2': 'T5', '14,1': 'I5',
    '13,8': 'D4', '13,7': 'O4', '13,6': 'T4', '13,5': 'I4',
    '10,8': 'D3', '10,7': 'O3', '10,6': 'T3', '10,5': 'I3',
    '8,8': 'D2', '8,7': 'O2', '8,6': 'T2', '8,5': 'I2',
    '15,8': 'D1', '15,7': 'O1', '15,6': 'T1', '15,5': 'I1',
    '5,2': 'SB', '5,1': 'DB',
    '3,0': 'UP',
    '1,0': 'DOWN',
    '4,0': 'LEFT',
    '2,0': 'RIGHT',
    '0,0': 'ENTER',
    'VIB': 'VIB',
    'ENTER_ON': 'ENTER_ON'
}

def read_serial():
    string = ser_dart.readline()
    if string:
        string = string[:-2]
        string = string.decode()
        ser_led.write(matrix_dict[string].encode())
        clear_buffer = ser_led.readline()
        if clear_buffer:
            return string
    else:
        return None

def read_serial_end_turn():
    string = ser_dart.readline()
    if string:
        string = string[:-2]
        string = string.decode()
        string = matrix_dict[string]
        if string == "ENTER" or string == "RIGHT":
            return string
    else:
        return None
    
def write_serial_led(_input):
    string = _input
    if string:
        ser_led.write(string.encode())
        clear_buffer = ser_led.readline()
        if clear_buffer:
            return
        
def read_board(_end = False):
    while True:
        if _end == True:
            string = read_serial_end_turn()
            if string:
                return string
        else:
            string = read_serial() 
            if string:
                string = matrix_dict[string].encode()
                string = string.decode('utf-8')
                return string