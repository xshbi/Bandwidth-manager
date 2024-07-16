import time
import psutil
import tkinter as tk

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_sent + last_received


def update_network_activity_label():
    global last_received, last_sent, last_total  # Declare the variables as global

    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_sent + bytes_received

    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    activity_label.config(
        text=f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total"
    )

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    root.after(
        1000, update_network_activity_label
    )  # Schedule the update after 1000 milliseconds (1 second)


# Create the main window
root = tk.Tk()
root.title("Network Activity Monitor")

# Create a label to display network activity
activity_label = tk.Label(root, text="")
activity_label.pack()

# Start monitoring the network activity
update_network_activity_label()

# Start the main event loop
root.mainloop()
