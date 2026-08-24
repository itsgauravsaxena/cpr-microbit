let armed = false
input.onGesture(Gesture.Shake, function () {
    armed = false
    basic.showIcon(IconNames.Asleep)
    basic.pause(randint(1000, 5000))
    basic.showIcon(IconNames.Target)
    armed = true
})
input.onButtonPressed(Button.A, function () {
    if (armed) {
        armed = false
        basic.showString("A")
    }
})
input.onButtonPressed(Button.B, function () {
    if (armed) {
        armed = false
        basic.showString("B")
    }
})
