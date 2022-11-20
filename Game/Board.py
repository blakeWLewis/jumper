

parachute = [
        "      ___      ",
        "     /___\     ",
        "     \   /     ",
        "      \ /      "]

live_jumper = "       0       \n      /|\      \n      / \      "
dead_jumper = "       x       \n      /|\      \n      / \      "
ground = "\n   ^^^^^^^^^  "



class Board:
    """This is the board class. 

    This class manages the printing of the board and removing any parts of the parachute that are not supposed to show up

    Attributes: 
        parachute: a list of the lines of the parachute that need to be printed
        live_jumper: what gets printed if the jumper is alive
        dead_jumper: what gets printted if the jumper is dead
        ground: the ground is what gets printed at the bottom of the board 

    """


    def printJumper(self, removes):
        """prints the jumper
        
        Args:
            removes: the numer of lines that need to be removed from the parachute
        """

        for s in range(0, removes):
            print("")

        for row in range(removes, len(parachute)):
            print(parachute[row]) 
        
        if(removes == len(parachute)):
            print(dead_jumper)
        else:
            print(live_jumper)
        
        print(ground)
