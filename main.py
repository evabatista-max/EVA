basic.show_leds("""
    # . # # #
    . # # # #
    # . # # #
    . # # # #
    # . # # #
    """)
music.play(music.string_playable("D B F C5 C - C5 A ", 120),
    music.PlaybackMode.UNTIL_DONE)
basic.show_string("HII , DO YOU KNOW")
music.play(music.string_playable("- B - B - D - - ", 120),
    music.PlaybackMode.UNTIL_DONE)
basic.show_string("WHO I AM?")
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.HAPPY)
music.play(music.string_playable("C5 B A G B C A D ", 120),
    music.PlaybackMode.UNTIL_DONE)
basic.show_string("MILLIE BOBBIE BROWN")
basic.show_icon(IconNames.NO)
basic.show_icon(IconNames.TORTOISE)
music.play(music.tone_playable(262, music.beat(BeatFraction.SIXTEENTH)),
    music.PlaybackMode.UNTIL_DONE)
basic.show_leds("""
    # . . . #
    . . . # .
    . # . . .
    . . . . .
    # . . # .
    """)
while False:
    basic.show_string("I LOVE SKZ")
basic.show_string("BYE ?")