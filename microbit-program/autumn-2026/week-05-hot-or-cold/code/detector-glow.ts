let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    led.setBrightness(Math.map(strength, -95, -42, 5, 255))
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
})
