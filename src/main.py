import os
import socket
import subprocess
import serial.tools.list_ports


def show_menu():
    print("\nPOS Diagnostic Toolkit")
    print("1 - List Serial Ports")
    print("2 - Test Serial Connection")
    print("3 - Ping Device")
    print("4 - Test TCP Port")
    print("5 - System Info")
    print("0 - Exit")


def list_serial():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p.device, "-", p.description)


def test_serial():
    import serial
    port = input("Enter COM port: ")

    try:
        ser = serial.Serial(port, 9600, timeout=2)
        print("Connection opened")
        ser.write(b'TEST\n')
        data = ser.readline()
        print("Response:", data)
        ser.close()
    except Exception as e:
        print("Error:", e)


def ping_device():
    ip = input("Enter IP: ")
    subprocess.call(["ping", ip])


def tcp_test():
    ip = input("IP: ")
    port = int(input("Port: "))

    try:
        s = socket.create_connection((ip, port), timeout=3)
        print("Port OPEN")
        s.close()
    except:
        print("Port CLOSED")


def system_info():
    os.system("ipconfig")


while True:
    show_menu()
    choice = input("Select option: ")

    if choice == "1":
        list_serial()
    elif choice == "2":
        test_serial()
    elif choice == "3":
        ping_device()
    elif choice == "4":
        tcp_test()
    elif choice == "5":
        system_info()
    elif choice == "0":
        break
