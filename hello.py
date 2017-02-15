#!/usr/bin/python
import usb.core
import usb.util
import sys
import time

#is usb == pyusb (yes) https://github.com/walac/pyusb/blob/master/docs/tutorial.rst
# how to use libusb?

# find our device
dev = usb.core.find(idVendor=0x04d8, idProduct=0x003f)
# was it found
if dev is None:
        raise ValueError('Device not found')

# handle if device is busy
if dev.is_kernel_driver_active(0) is True:
   dev.detach_kernel_driver(0)

# set the active configuration.  No args the first config
# will become the active one
dev.set_configuration()

dev.write(1, 100, 1)

# toggle LED by sending toggle_led command
print "Toggling LED"
dev.write(1, [0x80], 0, 100)
time.sleep(1)
dev.write(1, [0x80], 0, 100)

# reading switch status
print "Reading switch status  1=not pressed,  0=pressed"
dev.write(1, [0x81], 0, 100)
ret = dev.read(0x81, 64, 0, 100)
print ret[1]

dev.reset()


####

# custom 0x82 code for reading RD4 as GPIO input
print "Reading RD4 input status"
dev.write(1, [0x82], 0, 100)
ret = dev.read(0x81, 64, 0, 100)
print ret[1]

############
VENDOR_ID=0x04d8
PRODUCT_ID=0x003f
import usb1
with usb1.USBContext() as context:
    handle = usb1.USBContext().openByVendorIDAndProductID(
        VENDOR_ID,
        PRODUCT_ID,
        skip_on_error=True,
    )
    if handle is None:
    	print "\n\n\nNO HANDLE"
        # Device not present, or user is not allowed to access device.

    with handle.claimInterface(INTERFACE):
        # Do stuff with endpoints on claimed interface.

        # handle if device is busy
		if handle.is_kernel_driver_active(0) is True:
		   handle.detach_kernel_driver(0)

		# set the active configuration.  No args the first config
		# will become the active one
		handle.set_configuration()

		# toggle LED by sending toggle_led command
		print "Toggling LED"
		handle.write(1, [0x80], 0, 100)
		time.sleep(1)
		handle.write(1, [0x80], 0, 100)

		# reading switch status
		print "Reading switch status  1=not pressed,  0=pressed"
		handle.write(1, [0x81], 0, 100)
		ret = handle.read(0x81, 64, 0, 100)
		print ret[1]

		handle.reset()
