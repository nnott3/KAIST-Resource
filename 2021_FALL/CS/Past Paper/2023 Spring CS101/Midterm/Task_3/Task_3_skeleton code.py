import cs1robots
from commands import *

# ----------------------------------------
# Do not modify here!
_world = cs1robots._world
hubo = None
score = 0
turns = 0
high_score = 0
# -----------------------------------------


def drop_new_number():
    # Call generate_new_number() function and get three return values.
    #   The first value shows the avenue of the designated location.
    #   The second value shows the street of the designated location.
    #   The third value shows the number of beepers.
    # Move to designated location.
    # Call hubo.drop_number_tile(number) to drop number tile.
    # Return hubo to the location (avenue = 1, street = 5, orientation = "S")
    ####################### IMPLEMENT HERE #######################
    pass
    ####################### IMPLEMENT HERE #######################


def restart_game():
    # Re-initialize score, turns to zero.
    # Call reset_game() function.
    # Return hubo to the location (avenue = 1, street = 5, orientation = "S")
    # Call drop_new_number() function two times.
    ####################### IMPLEMENT HERE #######################
    pass
    ####################### IMPLEMENT HERE #######################


def on_dead():
    # Print the Message "Game Over..."
    # If the value of high score is less than current score, change the high score to current score, and print
    #   "!! New High Score !!"
    # Print the game result message "Score S, Turns T, High Score H"
    #  (in this message, S is the value of score, T is the value of turns, H is the value of high score")
    # Repeat this loop,
    # └ Ask user input printing "Press Enter to restart..."
    # └ If the user input is empty string, '',
    #    call restart_game(), then quit this function using return
    ####################### IMPLEMENT HERE #######################
    pass
    ####################### IMPLEMENT HERE #######################


def hubo_action():
    # Repeat this loop,
    # └ Ask user input printing
    #   "[Score S, Turns T] Move (w,a,s,d) or exit (x)? "
    #   (in this message, S is the value of score, T is the value of turns)
    #  Then call the correspondent function below.
    #   'w' → move_north(hubo)
    #   'a' → move_west(hubo)
    #   's' → move_south(hubo)
    #   'd' → move_east(hubo)
    #   'x' → return
    # └ Increase score and turns only if the first return value of move_xx() is True.
    # └ Call drop_new_number() only if the first return value of move_xx() is True.
    # └ Call is_dead() function and get the return value.
    #    If the return value is True, call on_dead() function.
    ####################### IMPLEMENT HERE #######################
    pass
    ####################### IMPLEMENT HERE #######################


# ----------------------------------------
# Do not modify here!!
if __name__ == "__main__":
    if _world == None:
        create_world(4, 5)
        hubo = Robot(avenue=1, street=5, orientation='S')

    restart_game()
    hubo_action()
# ----------------------------------------
