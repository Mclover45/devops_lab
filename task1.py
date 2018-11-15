from configparser import ConfigParser
import datetime
import psutil
import time


class Parser_conf(object):
    def Intervalik(kek):
        parser = ConfigParser()
        parser.read('config.txt')
        Interval = (parser.get('some', 'Interval'))
        return(Interval)


class PsutilStatus(object):
    def disk_usage(self):
        return str(psutil.disk_usage("/").used / 1024 / 1024)

    def virtual_memory(self):
        return str(psutil.virtual_memory().used / 1024 / 1024)

    def cpu_load(self):
        return str(psutil.cpu_percent(interval=1))

    def net_io_counters_1(self):
        return str(psutil.net_io_counters().bytes_sent)

    def net_io_counters_2(self):
        return str(psutil.net_io_counters().bytes_recv)


Cheker = 1


def Writer():
    global Cheker
    file = open('testfile.txt', "a")
    file.write("SNAPSHOT ")
    file.write(str(Cheker))
    file.write(" Date: ")
    file.write(str(datetime.datetime.utcnow()))
    file.write(" disk_usage MB ")
    file.write(str(State.disk_usage()))
    file.write(" VM MB ")
    file.write(str(State.virtual_memory()))
    file.write(" CpuLoad % ")
    file.write(str(State.cpu_load()))
    file.write(" IO inform ")
    file.write(" bytes_sent ")
    file.write(str(State.net_io_counters_1()))
    file.write(" bytes_recv ")
    file.write(str(State.net_io_counters_2()))
    file.write("\n")
    file.close()
    Cheker += 1


while True:
    Pareserik = Parser_conf()
    Interval = Pareserik.Intervalik()
    State = PsutilStatus()
    time.sleep(int(Interval))  # in seconds
    Writer()
