import socket
import time

# Configuration
FILE_PATH = "2-sample-signal-100hz.txt"
UDP_ADDR = "192.168.1.100"  # Change to your server's IP
UDP_PORT = 5005  # Change to your server's port
FREQUENCY_HZ = 100
INTERVAL = 1.0 / FREQUENCY_HZ


# Convert float to bytes (MicroPython doesn't have struct module by default)
def float_to_bytes(value):
    return bytearray(str(value), "utf-8")


# Initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    with open(FILE_PATH, "r") as file:
        for line in file:
            try:
                value = float(line.strip())
                data = float_to_bytes(value)
                packet = bytearray([0]) + data  # Prepend data type byte
                sock.sendto(packet, (UDP_ADDR, UDP_PORT))
                print("Sent EKG sensor data:", value)
            except ValueError:
                print("Invalid line, skipping:", line.strip())

            time.sleep(INTERVAL)

    # Send termination packet
    sock.sendto(bytearray([3, 9]), (UDP_ADDR, UDP_PORT))
    print("Sent termination signal")
except OSError as e:
    print("Error accessing file:", e)
finally:
    sock.close()
