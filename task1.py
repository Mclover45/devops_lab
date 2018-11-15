from configparser import ConfigParser
import datetime
import psutil
import time
parser = ConfigParser()
parser.read('config.txt')
Interval = (parser.get('some', 'Interval'))
Cheker = 1


def Writer():
    global Cheker
    file = open('testfile.txt', "a")
    file.write("SNAPSHOT ")
    file.write(str(Cheker))
    file.write(" Date: ")
    file.write(str(datetime.datetime.utcnow()))
    file.write(" disk_usage MB ")
    file.write(str(DU.used / 1000000))
    file.write(" VM MB ")
    file.write(str(VM.used / 1000000))
    file.write(" CpuLoad % ")
    file.write(str(CpuLoad))
    file.write(" IO inform ")
    file.write(" bytes_sent ")
    file.write(str(IOinform.bytes_sent))
    file.write(" bytes_recv ")
    file.write(str(IOinform.bytes_recv))
    file.write("\n")
    file.close()
    Cheker += 1
while True:
    DU = psutil.disk_usage("/")
    VM = psutil.virtual_memory()
    CpuLoad = psutil.cpu_percent(interval=1)
    IOinform = psutil.net_io_counters()
    time.sleep(int(Interval))  # in seconds
    Writer()
