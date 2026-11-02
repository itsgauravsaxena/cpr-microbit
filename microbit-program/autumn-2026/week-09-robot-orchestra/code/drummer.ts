function bow () {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P13, 1)
    servos.P2.setAngle(140)
    music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
    basic.pause(500)
    servos.P2.setAngle(90)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P13, 1)
        servos.P1.setAngle(armDown)
        music.playTone(98, 120)
        servos.P1.setAngle(90)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P13, 0)
        lastPlayed = input.runningTime()
    } else if (receivedNumber == 2) {
        servos.P2.setAngle(75)
        music.playTone(2093, 30)
        basic.pause(60)
        servos.P2.setAngle(90)
        lastPlayed = input.runningTime()
    } else if (receivedNumber == 99) {
        bow()
    }
})
input.onButtonPressed(Button.A, function () {
    lastPlayed = input.runningTime() + 10000
    basic.showString("DRUM")
    for (let index = 0; index < 8; index++) {
        servos.P1.setAngle(armDown)
        music.playTone(98, 80)
        servos.P1.setAngle(90)
        basic.pause(80)
    }
    music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Happy)
    lastPlayed = input.runningTime()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    lastPlayed = input.runningTime() + 10000
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.InBackground)
    for (let index = 0; index < 4; index++) {
        servos.P1.setAngle(70)
        basic.pause(150)
        servos.P1.setAngle(110)
        basic.pause(150)
    }
    servos.P1.setAngle(90)
    lastPlayed = input.runningTime()
})
input.onSound(DetectedSound.Loud, function () {
    if (input.runningTime() - lastPlayed > 3000) {
        bow()
    }
})
let lastPlayed = 0
let armDown = 0
armDown = 60
radio.setGroup(9)
servos.P1.setAngle(90)
servos.P2.setAngle(90)
basic.showIcon(IconNames.Happy)
