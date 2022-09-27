from time import sleep
import serial
import serial.tools.list_ports

port = ""
baud_rate = 9600

ports = serial.tools.list_ports.comports()


for i in range(len(ports)):
    print(f"({i}): {ports[i]}")

while True:
    try:
        port_num = int(input("Port: ").strip())

        port = ports[port_num][0]
        print(f"Port {port} selected.")

        break
    except:
        print("Please input a valid number.")

while True:
    try:
        baud_rate = int(input("Baud Rate: ").strip())
        break
    except:
        print("Please input a valid number.")

ser = serial.Serial(port, baud_rate, timeout=1)

# import pyautogui
#
# x, y = 0, 0

sleep(1)

while True:
    sleep(0.01)

    line = ser.readline().decode().strip()
    data = int(line)
    print(int(line))

    # signed_data = data - 512

    # if abs(signed_data) < 256:
    #    x = signed_data
    # else:
    #    y = signed_data
    #
    # pyautogui.move(x / 100, y / 100)
