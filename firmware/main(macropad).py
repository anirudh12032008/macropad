import network
import urequests
import utime
from machine import Pin, I2C
import sh1106


# why should I tell you thissss! go fill yours 
# SSID = 
# PASSWORD = 
# SERVER = 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    utime.sleep(1)

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
display = sh1106.SH1106_I2C(128, 64, i2c)

buttons = [
    Pin(2, Pin.IN, Pin.PULL_UP),
    Pin(3, Pin.IN, Pin.PULL_UP),
    Pin(4, Pin.IN, Pin.PULL_UP),
    Pin(5, Pin.IN, Pin.PULL_UP),
    Pin(6, Pin.IN, Pin.PULL_UP),
    Pin(7, Pin.IN, Pin.PULL_UP),
]

clk = Pin(14, Pin.IN, Pin.PULL_UP)
dt = Pin(15, Pin.IN, Pin.PULL_UP)
last = clk.value()


msg = "Idle"


def send(action):
    global msg
    r = urequests.post(SERVER + "/macro", json={"action": action})
    r.close()
    msg = action
  

def stat():
    r = urequests.get(SERVER + "/status")
    data = r.json()
    r.close()
    return data

def upstat(data):
    display.fill(0)
    display.text("Time: " + data["time"], 0, 0)
    display.text("Vol: " + str(data["volume"]) + "%", 0, 15)
    display.text("Last:", 0, 30)
    display.text(data["last"][:18], 0, 45)
    display.show()


while True:

    curr = clk.value()
    if curr != last:
        if dt.value() != curr:
            send("vol up")
        else:
            send("vol down")
    last = curr

    for i, btn in enumerate(buttons):
        if btn.value() == 0:
            if i == 0:
                send("prev")
            elif i == 1:
                send("play")
            elif i == 2:
                send("next")
            elif i == 3:
                send("copy")
            elif i == 4:
                send("paste")
            elif i == 5:
                send("backspace")
            utime.sleep(0.3)

    status = stat()
    if status:
        upstat(status)

    utime.sleep(1)