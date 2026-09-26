let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    pins.analogWritePin(AnalogPin.P0, Math.map(strength, -95, -42, 0, 1023))
    basic.pause(100)
})
