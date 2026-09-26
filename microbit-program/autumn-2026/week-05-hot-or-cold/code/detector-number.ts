let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    basic.showNumber(Math.round(Math.map(strength, -95, -42, 0, 100)))
    basic.pause(500)
})
