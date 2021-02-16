import time
import board
import digitalio
import busio
import usb_midi

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

button = digitalio.DigitalInOut(board.GP28)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Set USB MIDI up on channel 0
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

while True:
    if (button.value):
        midi.send(NoteOn(36, 100))
    else:
        midi.send(NoteOff(36, 0))

