import os
from sys import platform
width = 80


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


def formatted_title(title):
    title = f' {title} '
    while len(title) < width:
        if len(title) % 2 == 0:
            title = '*' + title
        else:
            title = title + '*'
    return title


def formatted_choices(menu, contents):
    for item in contents:
        menu.append(f'* {item[0]} - {item[1]}' + ' ' * int(width - 6 - len(item[0]) - len(item[1])) + '*')
    return menu


def formatted_stats(menu, stats):
    """will show stats in a way that matches menu formatting"""
    pass


def choice_menu(title, contents):
    clear_terminal()
    menu = [formatted_title(title)]
    menu = formatted_choices(menu, contents)
    menu.append('*' * width)
    for line in menu:
        print(line)
    return input('Enter selection: ')

