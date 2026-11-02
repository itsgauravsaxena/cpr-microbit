input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.EighthNote)
    tick = 0
    for (let index = 0; index <= song.length - 1; index++) {
        radio.sendNumber(song[index])
        if (helper) {
            music.ringTone(song[index])
        }
        for (let index2 = 0; index2 < lengths[index]; index2++) {
            if (tick % 4 == 0) {
                radio.sendNumber(1)
            } else if (tick % 2 == 0) {
                radio.sendNumber(2)
            }
            tick += 1
            basic.pause(eighth)
        }
        music.rest(1)
    }
    music.stopAllSounds()
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(99)
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function () {
    helper = !(helper)
    if (helper) {
        basic.showString("H")
    } else {
        basic.clearScreen()
    }
})
let tick = 0
let helper = false
let eighth = 0
let lengths: number[] = []
let song: number[] = []
song = [262, 294, 330, 262, 262, 294, 330, 262, 330, 349, 392, 330, 349, 392, 392, 440, 392, 349, 330, 262, 392, 440, 392, 349, 330, 262, 262, 196, 262, 262, 196, 262]
lengths = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 4, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 4, 2, 2, 4]
eighth = 200
radio.setGroup(9)
basic.showIcon(IconNames.EighthNote)
