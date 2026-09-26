let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    music.playTone(Note.C5, 40)
    basic.pause(Math.map(strength, -95, -42, 700, 60))
})
