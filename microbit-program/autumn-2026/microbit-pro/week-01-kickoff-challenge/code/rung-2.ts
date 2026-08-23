basic.forever(function () {
    let pitch = Math.map(input.lightLevel(), 0, 255, 200, 1200)
    music.ringTone(pitch)
})
