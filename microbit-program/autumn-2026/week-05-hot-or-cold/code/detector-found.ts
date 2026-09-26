let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
basic.forever(function () {
    if (strength > -48) {
        basic.showIcon(IconNames.Yes)
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        basic.pause(1500)
    } else {
        led.plotBarGraph(Math.map(strength, -95, -48, 0, 100), 100)
        basic.pause(100)
    }
})
