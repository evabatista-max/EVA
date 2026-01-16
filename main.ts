basic.showLeds(`
    # . # # #
    . # # # #
    # . # # #
    . # # # #
    # . # # #
    `)
music.play(music.stringPlayable("D B F C5 C - C5 A ", 120), music.PlaybackMode.UntilDone)
basic.showString("HII , DO YOU KNOW")
music.play(music.stringPlayable("- B - B - D - - ", 120), music.PlaybackMode.UntilDone)
basic.showString("WHO I AM?")
basic.showIcon(IconNames.Heart)
basic.showIcon(IconNames.Happy)
music.play(music.stringPlayable("C5 B A G B C A D ", 120), music.PlaybackMode.UntilDone)
basic.showString("MILLIE BOBBIE BROWN")
basic.showIcon(IconNames.No)
basic.showIcon(IconNames.Tortoise)
music.play(music.tonePlayable(262, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
basic.showLeds(`
    # . . . #
    . . . # .
    . # . . .
    . . . . .
    # . . # .
    `)
while (false) {
    basic.showString("I LOVE SKZ")
}
basic.showString("BYE ?")
