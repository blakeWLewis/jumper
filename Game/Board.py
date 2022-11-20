
sky = "   - - - - -  "

parachute = [
        "      ___      ",
        "     /___\     ",
        "     \   /     ",
        "      \ /      "]

live_jumper = "       0       \n      /|\      \n      / \      "
dead_jumper = "       x       \n      /|\      \n      / \      "
ground = "\n   ^^^^^^^^^  "


class Board:

    def printJumper(self, removes):
        # print(sky)

        for s in range(0, removes):
            print("")

        for row in range(removes, len(parachute)):
            print(parachute[row]) 
        
        if(removes == len(parachute)):
            print(dead_jumper)
        else:
            print(live_jumper)
        
        print(ground)
