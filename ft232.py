import usb
import usb.util
from pyftdi.ftdi import Ftdi

dev = usb.core.find(idVendor=0x0403, idProduct=0x6014)
print(dev)

Ftdi().open_from_url('ftdi:///?')