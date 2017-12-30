import sys
from sys import exit
from time import sleep


class Scene (object):

    def enter(self):
        exit(1)


class End(Scene):
    def enter(self):
        print "\n\tThese shouting high pitched voices remain in your ears. Ouch!"
        exit()


class Start(Scene):
    def enter(self):
        print """
        ,--.   ,--.,------.,--.    ,-----. ,-----. ,--.   ,--.,------.
        |  |   |  ||  .---'|  |   '  .--./'  .-.  '|   `.'   ||  .---'
        |  |.'.|  ||  `--, |  |   |  |    |  | |  ||  |'.'|  ||  `--,
        |   ,'.   ||  `---.|  '--.'  '--_''  '-'  '|  |   |  ||  `---.
        '--'   '--'`------'`-----' `-----' `-----' `--'   `--'`------'
           ,--------. ,-----.   ,--------.,--.   ,--.  ,---.  ,--.
           '--.  .--''  .-.  '  '--.  .--'|  |   |  | /  O  \ |  |
              |  |   |  | |  |     |  |   |  '---'  ||  .-.  ||  |
              |  |   '  '-'  '     |  |   |  |   |  ||  | |  ||  |
              `--'    `-----'      `--'   '--'   '--'`--' `--'`--'
        ,--. ,--.  ,---.  ,------.   ,---.   ,-----. ,--. ,--.,------.
        |  .'   / /  O  \ |  .--. ' /  O  \ '  .-.  '|  .'  / |  .---'
        |  .   ' |  .-.  ||  '--'.'|  .-.  ||  | |  ||  .   ' |  `--,
        |  |\   \|  | |  ||  |\  \ |  | |  |'  '-'  '|  |\   \|  `---.
        `--' '--'`--' `--'`--' '--'`--' `--' `-----' `--' '--'`------'
                         ,-----.   ,---.   ,------.   
                         |  .---| /   O  \ |  .--. ' 
                         |  .--'.|  .--.  ||  '--'.'
                         |  .---||  |  |  ||  |\  \ 
                         `-----' `--'  `--'`--' '--'"""


        startwords= """
You want to go out with your friends to have some cocktails at Sausalitos bar.
The barkeeper is having a good night. Free drinks for you! What was planned
as "some drinks in a bar ended at the Kiez. Oh no. After Halo, Mondoo Rotation
you had a break at Hesburger. After a blackout you find yourself infront
a karaoke bar called Thai Oase.
First, you need to get through the bouncer.
        Bouncer: How many drinks did you had?\n"""
        for char in startwords:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

        choice = raw_input("\tYour answer: ")
        if choice == "0":
            print "\tBouncer: You're a bad liar."
            return 'end'
        elif choice == "1":
            print "\tBouncer: That's a good start. Come in!"
            return 'bar1'
        else:
            print "\tBouncer: Business is tough, just enter anyway."
            return 'bar1'


class Bar(Scene):
    def enter(self):
        print "\nYou've entered the 'Thai Oase'. An Austrian guy is singing DJ Oetzi Hits. Ugh!"
        print "Your friends also wrote your name on the singers list. Fill in the missing lyrics!"
        print "\n\tI bin so schoen. I bin so toll. I bin der Anton aus Tirol."
        print "\n\tMeine giganschlanken Wadln san a Wahnsinn fuer die Madln."
        print "\n\tMei Figur a _______ Natur!"

        choice = raw_input("\n\tType in the missing lyrics: ")

        if choice == "Wunder der" or choice == "Wunder dar":
            print "\nAnton, Anton, Anton! That's right! You must be a secret fan."
            return 'bar2'

        else:
            print "\nOh no, try again!"

            choice = raw_input("Type in the missing lyrics: ")

            if choice == "Wunder der" or choice == "Wunder dar":
                print "\nWell finally! Relieved you're tumbling to the bar."
                return 'bar2'

            else:
                print "'Boo boo' everyone. Even your friends. You're the worst Karaoke singer."
                return 'end'


class Counter(Scene):
    def enter(self):
        print "\nYou're now at the bar again. Do you want to buy another drink?"
        option = raw_input("You: ")

        if option == "yes" or option == "Yes" or option == "y":
            return 'strange'

        elif option == "no" or option == "No" or option == "n":
            print "\nMerlin would have chosen more drinks. Merlin is wise wizard."
            return 'strange'

        else:
            print "\nThe bar woman is giving a sign to the bouncer ans shout some Thai words."
            print "You have to go now, you cannot camp the bar not spending money"
            print "You run home and ditch your friends. They are still waiting for your next performance."
            return 'end'


class StrangerThings(Scene):
    def enter(self):
        startwords= """
At the counter a horde of old semesters want to talk to you. In broken English they say::
You are the DJ Oetzi fan. Here get a Freigetraenk! You should really sing again.
We like unsere German artists very much. Such 'ne beautiful language. But not only the
Buben also our Madls are 'klasse'. Helene Fischer is our favorite one.
    These oldtimers force you to group sing their idol Helene's songs."""
        for char in startwords:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        return 'another_song'


class AnotherSong(Scene):
    def enter(self):
        print "\n\n\tAtemlos durch die Nacht. \n\tSpuer' was Liebe mit uns macht."
        print "\tAtemlos, schwindelfrei, _______ fuer uns zwei"

        choice = raw_input("\n\tType in the missing lyrics: ")

        if choice == "grosses Kino":
            print "\n\tYou ended as professional karaoke guide in the local retirement home"
            print "\tLucky you, get some donuts and caffeine-free coffee"
            return 'success'

        else:
            print "\nYou displeased the regular guests of the bar."
            print "\nThe bouncer accompanies you through the exit and a ban for tonight."
            return 'end'


class Success(Scene):

    def enter(self):
        print "\n\tWow. I hate this job. Well..."
        exit()

class Engine(object):

        def __init__(self, scene_map):
            self.scene_map = scene_map

        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('success')

            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()


class Map(object):

    scenes = {
        'start': Start(),
        'bar1': Bar(),
        'bar2': Counter(),
        'strange': StrangerThings(),
        'another_song': AnotherSong(),
        'end': End(),
        'success': Success(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()