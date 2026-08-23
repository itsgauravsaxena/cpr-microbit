basic.forever(function () {
    let pitch = Math.map(input.lightLevel(), 0, 255, 200, 1200)
    let vol = Math.map(Math.abs(input.acceleration(Dimension.X)), 0, 1000, 0, 255)
    music.setVolume(vol)
    music.ringTone(pitch)
})
