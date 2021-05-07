import os
from sys import platform


# Connect to SQL here
class User:
    """There can be only one user, which holds the name and odometer"""
    def __init__(self, user_id, name, total_miles=0):
        self.user_id = user_id
        self.name = name
        self.total_miles = total_miles

    def set_odometer(self):
        # this is where the total_mileage data is collected and set
        pass


class Ride:
    """Ride logs an individual ride and collects info from that ride"""
    def __init__(self, ride_id, name, bike, location, date, time, duration, distance, odometer):
        self.ride_id = ride_id
        self.name = name
        self.bike = bike
        self.location = location
        self.date = date
        self.time = time
        self.duration = duration
        self.distance = distance
        self.odometer = odometer


class Bike:
    """Each individual bike a user can own"""
    def __init__(self, bike_id, type, year, make, model, date_bought, date_retired, odometer):
        self.bike_id = bike_id
        self.type = type
        self.year= year
        self.make = make
        self.model = model
        self.date_bought = date_bought
        self.date_retired = date_retired
        self.odometer = odometer

    def set_odometer(self):
        # this is the total_mileage data is collected and set for the bike
        pass


class Location:
    """Each location has distance and terrain type"""
    def __init__(self, location_id, name, city, distance, terrain):
        self.location_id = location_id
        self.name = name
        self.city = city
        self.distance = distance
        self.terrain = terrain


def wrong_answer():
    input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def clear_terminal():
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')


def intro_page():
    clear_terminal()
    print('********************* CYCLETRAK *********************')
    print('')
    print(' o__         __o        ,__o        __o           __o')
    print(' ,>/_       -\<,      _-\\_<,       _`\\<,_       _ \\<_')
    print("(*)`(*).....O/ O.....(*)/'(*).....(*)/ (*).....(_)/(_)")
    print()
    print('BY CHRISTIAN HALL                         VERSION 1.0')
    print('')
    input('           press ENTER to continue to app')


def exit_page():
    clear_terminal()
    print('Have a great day!')
    print('')
    print('                                          $"   *.      ')
    print('              d$$$$$$$P"                  $    J')
    print('                  ^$.                     4r  "')
    print('                  d"b                    .db')
    print('                 P   $                  e" $')
    print('        ..ec.. ."     *.              zP   $.zec..')
    print('    .^        3*b.     *.           .P" .@"4F      "4')
    print('  ."         d"  ^b.    *c        .$"  d"   $         %')
    print(' /          P      $.    "c      d"   @     3r         3')
    print('4        .eE........$r===e$$$$eeP    J       *..        b')
    print('$       $$$$$       $   4$$$$$$$     F       d$$$.      4')
    print('$       $$$$$       $   4$$$$$$$     L       *$$$"      4')
    print('4         "      ""3P ===$$$$$$"     3                  P')
    print(' *                 $       """        b                J')
    print('  ".             .P                    %.             @')
    print('    %.         z*"                      ^%.        .r"')
    print('       "*==*""                             ^"*==*""')
    print('')
    print('')
    input('press ENTER to exit')
    clear_terminal()


def formatted_menu(title, contents):
    clear_terminal()
    menu, width, title = [], 80, ' ' + title + ' '
    while len(title) < width:
        if len(title) % 2 == 0:
            title = '*' + title
        else:
            title = title + '*'
    menu.append(title)
    for line_item in contents:
        line_item = '* ' + line_item[0] + ' - ' + line_item[1]
        while len(line_item) < width - 1:
            line_item = line_item + ' '
        line_item = line_item + '*'
        menu.append(line_item)
    menu.append('*' * width)
    for line in menu:
        print(line)
    return input('Enter selection: ')


def user_menu():
    choice = ' '
    while choice.upper() != 'B':
        clear_terminal()
        user_name = 'Christian Hall' # get this from SQL
        total_mileage = 29.2 # get this from SQL
        print('********************************** USER MENU ***********************************')
        print('* Name:          ' + user_name + ' ' * (79 - 17 - len(user_name)) + '*')
        print('* Total Mileage: ' + str(total_mileage) + ' ' * (79 - 17 - len(str(total_mileage))) + '*')
        print('*' + ' ' * 78 + '*')
        print('* E - Edit User Name                                                           *')
        print('* B - Back                                                                     *')
        print('********************************************************************************')
        choice = input('Enter selection: ')
        if choice.upper() == 'E':
            # edit_user_name()
            pass
        elif choice.upper() == 'B':
            pass
        else:
            wrong_answer()


def rides_menu():
    selection = ''
    choices = [['N', 'New ride'], ['R', 'View rides'], ['S', 'View statistics'],['B', 'Back']]
    while selection.upper() != 'Q':
        selection = formatted_menu('RIDES MENU', choices)
        if selection.upper() == 'N':
            # new_ride_menu()
            pass
        elif selection.upper() == 'V':
            # view_rides_menu()
            pass
        elif selection.upper() == 'S':
            # view_statistics_menu()
            pass
        elif selection.upper() == 'B':
            pass
        else:
            wrong_answer()


def main_menu():
    selection = ''
    choices = [['U', 'User Data'], ['R', 'Rides'], ['C', 'Cycles'], ['L', 'Locations'], ['S', 'Settings'], ['Q', 'Quit']]
    while selection.upper() != 'Q':
        selection = formatted_menu('CYCLETRAK', choices)
        if selection.upper() == 'U':
            user_menu()
        elif selection.upper() == 'R':
            # rides_menu()
            pass
        elif selection.upper() == 'B':
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


intro_page()
# check for existing user
main_menu()
exit_page()
