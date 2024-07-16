import time
import psutil


last_recived = psutil.net_io_counters().bytes_recv

last_sent = psutil.net_io_counters().bytes_sent


last_total = last_sent + last_recived


while True:

    bytes_recived = psutil.net_io_counters().bytes_recv

    bytes_sent = psutil.net_io_counters().bytes_sent

    bytes_total = last_sent + last_recived

    new_received = bytes_recived - last_recived

    new_sent = bytes_recived + last_recived

    new_total = bytes_total - last_total

    mb_new_recived = new_received/ 1024 / 1024 
    mb_new_sent = new_sent / 1024  /1024
    mb_new_total = new_total /1024 /1024

    print(f"{mb_new_recived:.2f} MB recevied,{mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")

    last_recived = bytes_recived
    last_sent = bytes_sent
    last_total = bytes_total


    time.sleep(1)



