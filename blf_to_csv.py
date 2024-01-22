import can #pip3 install python-can
import csv

filename = "test.blf"
log = can.BLFReader("test.blf")
log = list(log)

log_output = []

for msg in log:
    msg = str(msg)
    #log_output.append([msg[18:26],msg[38:40],msg[40:42],msg[46],msg[62],msg[67:90]])
    msg1 = msg.replace(";", "")
    msg2 = msg1.replace('"', '')
    log_output.append(msg2)

with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f,delimiter=' ', quotechar='\"', quoting=csv.QUOTE_NONE)
    writer.writerows(log_output)