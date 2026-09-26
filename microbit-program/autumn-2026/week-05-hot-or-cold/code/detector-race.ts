let started = false
let startTime = 0
let strength = -128
radio.setGroup(1)
radio.onReceivedNumber(function (receivedNumber) {
    strength = radio.receivedPacket(RadioPacketProperty.SignalStrength)
})
input.onButtonPressed(Button.A, function () {
    started = true
    startTime = input.runningTime()
    basic.showIcon(IconNames.Yes)
})
basic.forever(function () {
    if (started && strength > -48) {
        started = false
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        basic.showNumber(Math.round((input.runningTime() - startTime) / 1000))
    }
    basic.pause(100)
})
