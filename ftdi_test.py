# Added by Dylan 12/15/2023
from pyftdi.i2c import I2cController

# Create an instance of the I2C controller
i2c = I2cController()

# Configure the FTDI interface for the C232HM cable
i2c.configure('ftdi://ftdi:232h:FT6AP51K/1')

# Replace 0x1A with the I2C slave address of your device
slave_address = 0x5F

# Open a connection to the specified slave
slave = i2c.get_port(slave_address)

# Replace these bytes with the data you want to send
data_to_send = [0x01, 0x40]

# Write data to the I2C slave
try:
    slave.write(data_to_send)
except Exception as e:
    print(e)
    i2c.terminate()
# Optional: Read data back from the slave
# data_read = slave.read(3)  # Read 3 bytes of data

# Close the I2C connection
i2c.terminate()