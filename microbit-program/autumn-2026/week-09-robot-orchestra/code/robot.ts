function hit () {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P13, 1)
    servos.P1.setAngle(armDown)
    servos.P2.setAngle(75)
    music.playTone(myNote, 180)
    servos.P1.setAngle(90)
    servos.P2.setAngle(90)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P13, 0)
    lastPlayed = input.runningTime()
}
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
    if (receivedNumber == myNote) {
        hit()
    } else if (receivedNumber == 99) {
        bow()
    }
})
input.onButtonPressed(Button.A, function () {
    lastPlayed = input.runningTime() + 10000
    basic.showString("ROBO")
    for (let index = 0; index < 3; index++) {
        servos.P2.setAngle(60)
        pins.digitalWritePin(DigitalPin.P8, 1)
        servos.P1.setAngle(armDown)
        basic.pause(300)
        servos.P2.setAngle(120)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P13, 1)
        servos.P1.setAngle(90)
        basic.pause(300)
        pins.digitalWritePin(DigitalPin.P13, 0)
    }
    servos.P2.setAngle(90)
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
let myNote = 0
myNote = Note.C
armDown = 60
radio.setGroup(9)
servos.P1.setAngle(90)
servos.P2.setAngle(90)
basic.showIcon(IconNames.Happy)
