from flask import Flask, request, jsonify
from pynput.keyboard import Controller, Key
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyperclip
import datetime

app = Flask(__name__)
keyboard = Controller()

from pycaw.pycaw import AudioUtilities

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

la = "Idle"

@app.route("/macro", methods=["POST"])
def macro():
    global la
    action = request.json.get("action")

    if action == "prev":
        keyboard.tap(Key.media_previous)
        la = "Previous"

    elif action == "play":
        keyboard.tap(Key.media_play_pause)
        la = "Play/Pause"

    elif action == "next":
        keyboard.tap(Key.media_next)
        la = "Next"

    elif action == "copy":
        keyboard.press(Key.ctrl); keyboard.press('c')
        keyboard.release('c'); keyboard.release(Key.ctrl)
        la = "Copied: " + pyperclip.paste()[:15]

    elif action == "paste":
        keyboard.press(Key.ctrl); keyboard.press('v')
        keyboard.release('v'); keyboard.release(Key.ctrl)
        la = "Pasted"

    elif action == "backspace":
        keyboard.tap(Key.backspace)
        la = "Deleted"

    elif action == "vol_up":
        volume.SetMasterVolumeLevelScalar(
            min(volume.GetMasterVolumeLevelScalar() + 0.05, 1.0), None)
        la = "Volume +"

    elif action == "vol_down":
        volume.SetMasterVolumeLevelScalar(
            max(volume.GetMasterVolumeLevelScalar() - 0.05, 0.0), None)
        la = "Volume -"

    return jsonify({"status": "ok"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "volume": int(volume.GetMasterVolumeLevelScalar() * 100),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "last": la
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)