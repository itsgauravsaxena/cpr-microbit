let mood = ""
basic.showIcon(IconNames.Asleep)
mood = "sleep"
input.onButtonPressed(Button.A, function () {
    mood = "fed"
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    mood = "play"
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Happy)
})
