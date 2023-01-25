import hid
import json

lt=0
ltp=0


def controller(vendor,product):
    with open('controllers.ori.json') as f:
        data = json.load(f)
    vid=data['vendors'][vendor]['vid']
    pid=data['vendors'][vendor]['products'][product]['pid']
    pnm=data['vendors'][vendor]['products'][product]['name']
    return int(vid,16),int(pid,16),pnm

print("currently connected Devices HID-class:")
for d in hid.enumerate():
    if d['product_string']:
        print(f"ven: {hex(d['vendor_id'])}, pro: {hex(d['product_id'])}, nme: {d['product_string']}")
    if "310" in d['product_string']:
        print("gevonden")
        if d['product_id'] == 49693:
            print(f'{ltp=}')
            ltp=1

vid,pid,name=controller(lt,ltp)
print(f'\nCurrent selection {name}\n vid: {vid} {hex(vid)}, pid: {pid} {hex(pid)}\n')
print('Connection report:')
with hid.Device(vid, pid) as h:
    print(f'Device manufacturer: {h.manufacturer}')
    print(f'Product: {h.product}')
    print(f'Serial Number: {h.serial}')

gamepad = hid.Device(vid,pid) #make an instance of a class
gamepad.set_nonblocking=True
while True:
    report = gamepad.read(80)
    if ltp==0:
        #ireport = int.from_bytes(report[0], "big")
        axes =[[report[0],#x-as Ljoy
             report[1],#y-as Ljoy
             ],[
             report[2],#x-as Rjoy
             report[3],#y-as Rjoy
             ]]
        dbut = report[4]#direction buttons
        sbut = report[5]#trigger, mode, stick buttons
        
        mode = report[6]#mode button
        unx  = report[7]#unknown (looks always high)
             
        print(axes,dbut,sbut,mode,unx)
    else:
        print(report)
    