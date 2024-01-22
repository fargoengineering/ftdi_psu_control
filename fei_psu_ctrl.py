from pyftdi.i2c import I2cController

class PMBus():
    # Instantiate an I2C controller

    # Configure the first interface (IF/1) of the FTDI device as an I2C master
    def __init__(self):
        self.i2c = I2cController()
        # self.i2c.configure('ftdi://ftdi:232h:FT6AP51K/1')
        self.i2c.configure('ftdi://ftdi:232h:1/1')
        self.slave = self.i2c.get_port(0x00)

    def connect_to_slave(self,adr):
    # Get a port to an I2C slave device
        self.slave = self.i2c.get_port(adr)

    def set_power(self,state):
        if state:
            data_to_send = [0x01, 0x80]     # PSU ON
            try:
                self.slave.write(data_to_send)
            except Exception as e:
                print(e)
                self.i2c.terminate()
        else:
            data_to_send = [0x01, 0x40]     # PSU OFF
            try:
                self.slave.write(data_to_send)
            except Exception as e:
                print(e)
                self.i2c.terminate()
                
    def set_vout(self,val):
        hex_bytes = self.convert_to_hex_little_endian(val)
        
        # Write Protect Off(0x10)
        data_to_send = [0x10, 0x00]
        self.slave.write(data_to_send)

        # Send PassWord (0xE2)
        data_to_send = [0xE2,0x55,0x73,0x65,0x72]
        self.slave.write(data_to_send)
        
        # VOUT Selection
        data_to_send = [0xDA, 0x01]
        self.slave.write(data_to_send)
        
        # VOUT Program
        data_to_send = [0x21,hex_bytes[1],hex_bytes[0]]
        self.slave.write(data_to_send)
        
        # Save State
        data_to_send = [0x15]
        self.slave.write(data_to_send)
    def set_iout(self,val):
        pass
    
    def get_vout(self):
        pass
    
    def get_iout(self):
        pass
    
    def convert_to_hex_little_endian(self, value):
        integer_part = int(value)
        fractional_part = int((value - integer_part) * 255)
        return (integer_part & 0xFF, fractional_part & 0xFF)

# Example usage
if __name__ == '__main__':
    
    pm = PMBus()
    
    pm.connect_to_slave(0x5F)
    
    # pm.set_power(True)
    
    pm.set_vout(8.7)