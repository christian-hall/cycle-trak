import database
import user
import cycle
import location
import ride
from printing import choice_menu, wrong_answer, intro_page, exit_page, error_page



def main_menu():
    selection = ''
    choices = [['U', 'User Data'], ['R', 'Rides'], ['C', 'Cycles'],
               ['L', 'Locations'], ['S', 'Settings'], ['Q', 'Quit']]
    while selection.upper() != 'Q':
        selection = choice_menu('CYCLETRAK', choices)
        if selection.upper() == 'U':
            user_menu()
        elif selection.upper() == 'R':
            # rides_menu()
            pass
        elif selection.upper() == 'C':
            # cycle_menu()
            pass
        elif selection.upper() == 'L':
            # location_menu()
            pass
        elif selection.upper() == 'S':
            # settings_menu()
            pass
        elif selection.upper() == 'Q':
            pass
        else:
            wrong_answer()
    

def user_menu():
    pass

if database.connect_to_database:
    # check for new user and generate if needed
    intro_page()
    main_menu()
    exit_page()
else:
    error_page()
