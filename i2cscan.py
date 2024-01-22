from pyftdi.i2c import I2cController, I2cNackError

def scan_i2c_devices(bus_num=0):
    try:
        # Create an I2C controller
        controller = I2cController()

        # Open the I2C connection
        controller.configure('ftdi://ftdi:232h:FT6AP51K/1')

        # Scan for I2C devices
        found_devices = []
        for address in range(128):
            try:
                # Try to read 1 byte from the device at the given address
                controller.write(address, bytes([0x00]))
                found_devices.append(address)
            except I2cNackError:
                pass

        if found_devices:
            print("Found I2C devices:")
            for device in found_devices:
                print(f"Device at address 0x{device:02X}")
        else:
            print("No I2C devices found on the bus.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the I2C connection
        controller.close()

if __name__ == "__main__":
    # Change the bus_num if needed (0 is the default bus)
    scan_i2c_devices(bus_num=0)
