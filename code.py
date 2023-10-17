import serial

portserie = serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=2); ## for linux
## portserie = serial.Serial("COM3",baudrate=9600,timeout=2); for windows

file = open("potentiometer_values",'a')
for i in range(1,13):
    esp_data = portserie.readline().decode('ascii')
    print(esp_data)
    file.write(esp_data)


file.close()

