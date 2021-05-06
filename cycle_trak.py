from os import system
from sys import platform


def check_files():
    # check to see if the files are in the same location as this
    pass


def main():
    selection = ''
    choices = [['R', 'Rides'], ['S', 'Statistics'], ['L', 'Locations'], ['A', 'About/Settings'], ['Q', 'Quit']]
    while selection.upper() != 'Q':
        selection = formatted_menu('CYCLETRAK', choices)
        if selection.upper() == 'R':
            rides()
        elif selection.upper() == 'S':
            statistics()
        elif selection.upper() == 'L':
            locations()
        elif selection.upper() == 'A':
            about()
        elif selection.upper() == 'Q':
            pass
        else:
            input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def rides():
    selection = ''
    choices = [['N', 'Log New Ride'], ['V', 'View/Edit Rides'], ['B', 'Back']]
    while selection.upper() != 'B':
        selection = formatted_menu('RIDES', choices)
        if selection.upper() == 'N':
            pass
        elif selection.upper() == 'V':
            pass
        elif selection.upper() == 'B':
            pass
        else:
            input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def statistics():
    selection = ''
    choices = [['W', 'Week view'], ['M', 'Month view'], ['Y', 'Year view'], ['A', 'All-time view'], ['B', 'Back']]
    while selection.upper() != 'B':
        selection = formatted_menu('STATISTICS', choices)
        if selection.upper() == 'W':
            pass
        elif selection.upper() == 'M':
            pass
        elif selection.upper() == 'Y':
            pass
        elif selection.upper() == 'A':
            pass
        elif selection.upper() == 'B':
            pass
        else:
            input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def locations():
    selection = ''
    choices = [['N', 'New location'], ['V', 'View/edit locations'], ['P', 'Print locations'], ['B', 'Back']]
    while selection.upper() != 'B':
        selection = formatted_menu('STATISTICS', choices)
        if selection.upper() == 'N':
            pass
        elif selection.upper() == 'V':
            pass
        elif selection.upper() == 'P':
            pass
        elif selection.upper() == 'B':
            pass
        else:
            input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def about():
    selection = ''
    choices = [['A', 'About'], ['U', 'User Information'], ['G', 'Set/Edit Goals'], ['B', 'Back']]
    while selection.upper() != 'B':
        selection = formatted_menu('STATISTICS', choices)
        if selection.upper() == 'A':
            pass
        elif selection.upper() == 'U':
            pass
        elif selection.upper() == 'G':
            pass
        elif selection.upper() == 'B':
            pass
        else:
            input('ERROR: ENTER A VALID RESPONSE. Press enter to continue.')


def clear_terminal():
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        system('clear')
    elif platform == 'win32':
        system('cls')


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


def input_menu(title, contents):
    print(title)
    print(contents)


intro_page()
main()
exit_page()
