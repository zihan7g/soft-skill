import sys
import serial
import serial.tools.list_ports

port_found = False
port_names = []
ports = []  
       
for device in serial.tools.list_ports.comports():
    if "Arduino Mega 2560" in device.description:
        try:
            port_names.append(device.name or device.device)
            ports.append(serial.Serial(port_names[-1]));
            port_found = True;
        except serial.serialutil.SerialException:
            port_names.pop()
            if __name__ == '__main__':
                print("ARDUINO PORT BUSY: ", device.name or device.device, " (SKIPPING)")
            continue
        
if not port_found:
    if __name__ == '__main__':
        print("NO ARDUINO MEGAS CONNECTED.")
        exit(1)
    else:
        raise Exception("NO ARDUINO MEGAS CONNECTED.")


def arduinos_found():
    return port_names
    
def turn_on():
    for port in ports:
        port.write(b'1');
        
def turn_off():
    for port in ports:
        port.write(b'0');
                
if __name__ == '__main__':
        print("ARDUINO MEGAS FOUND: ", port_names)
        
        if len(sys.argv) == 2:
            if sys.argv[1] == "1":
                turn_on()
                print("RELAY ACIVATED.")
            elif sys.argv[1] == "0":
                turn_off()
                print("RELAY DE-ACTIVATED.")
                
        for port in ports:
            port.close()
        exit(0)