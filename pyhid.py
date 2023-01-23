#import serial
#import serial.tools.list_ports_windows as lpw
#import serial.tools.list_ports as lp
import hid
vid = 0x046d	# Change it for your device
pid = 0xc534	# Change it for your device
#HID\VID_045E&PID_028E&IG_00 # Witte controller
vid= 0x045E
pid= 0x028E
#HID\VID_046D&PID_C216 #logitech dinges
vid = 0x046D
pid = 0xC216


with hid.Device(vid, pid) as h:
    print(f'Device manufacturer: {h.manufacturer}')
    print(f'Product: {h.product}')
    print(f'Serial Number: {h.serial}')

for d in hid.enumerate():
    print(d['vendor_id'],d['product_id'],d['product_string'])

gamepad = hid.Device() #make an instance of a class
gamepad.open(vid=0x046d,pid=0xc216)
gamepad.set_nonblocking=True