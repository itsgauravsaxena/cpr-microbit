let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    led.plotBarGraph(Math.map(strength, -95, -42, 0, 100), 100)
    basic.pause(100)
})
