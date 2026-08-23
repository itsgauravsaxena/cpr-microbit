input.onGesture(Gesture.Shake, function () {
    let answers = ["YES", "NO", "MAYBE", "SOON", "NO WAY"]
    basic.showString(answers[randint(0, answers.length - 1)])
})
