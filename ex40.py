#Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.
#Put the lyrics in a separate variable, then pass that variable to the class to use instead.
#See if you can hack on this and make it do more things. Don't worry if you have no idea how, just give it a try, see what happens.



class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
bombtrack=Song(["With the thoughts from a militant mind",
		"Hardline, hardline after hardline",
		"Landlords and power whores",
		"On my people they took turns",
		"Dispute the suits, I ignite",
		"And then watch 'em burn"])


people_of_the_sun=(["It's comin' back around again!",
"This is for the people of the sun!",
"It's comin' back around again! Uh!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
bombtrack.sing_me_a_song()
people_song=Song(people_of_the_sun)
people_song.sing_me_a_song()#
