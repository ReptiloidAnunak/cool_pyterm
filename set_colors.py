import shutil
from colorama import Back, Fore, Style, init

from style.colorama_colours import get_background_color_for_terminal, \
    get_text_color_for_terminal


def center_multiline_text(text, fore_color=Fore.WHITE, back_color=Back.BLACK):
    """
    Center-aligns the given multiline text within the terminal width.
    """

    width = shutil.get_terminal_size().columns
    text = text
    text_lines = text.split('\n')

    centered_lines = []

    for line in text_lines:
        if len(line) >= width:
            centered_lines.append(line)
        else:
            padding = (width - len(line))
            centered_line = ' ' * padding + line + ' ' * padding
            centered_lines.append(centered_line)

    for line in centered_lines:
        colored_text = f"{back_color}{fore_color}{line}{Style.RESET_ALL}"
        print(colored_text)


def terminal_set_print_style_block(text: str = None,
                                   bold: bool = False,
                                   text_color: str = None,
                                   back_color: str = None,
                                   set_back_after: bool = True,
                                   location: str ='l'):

    if not text:
        print('Set the function`s text arg')
        return


    text_color_code = get_text_color_for_terminal(text_color) if text_color else ""
    back_color_code = get_background_color_for_terminal(back_color) if back_color else ""

    width = shutil.get_terminal_size().columns
    if location == 'c':
        padding = ' ' * 90

        if '\n' in text:
            lines_lst = text.split('\n')
            lines_formated = []
            for line in lines_lst:
                line = padding + line + ' ' * 200
                lines_formated.append(line)

            text = '\n'.join(lines_formated)
        else:
            text = padding + text + ' ' * 200

    if bold:
        text = Style.BRIGHT + text

    if set_back_after:
        text = back_color_code + text_color_code + text + Style.RESET_ALL
    else:
        text = back_color_code + text_color_code + text

    print(text)


#
terminal_set_print_style_block(text='ARGENTINA',
                               bold=True, text_color='BLACK',
                               back_color='BLUE', set_back_after=1,
                               location='c')

terminal_set_print_style_block(text='COOL PYTERM\ncreated by ReptiloidAnunak', bold=1,
                               text_color='LIGHTYELLOW', back_color='lightwhite', set_back_after=1, location='c'),

terminal_set_print_style_block(text='VIVA LA LIBERTAD, CARAJO!',
                               bold=True, text_color='BLACK',
                               back_color='BLUE', set_back_after=1,
                               location='c')

    # terminal_set_print_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak\n', bold=False, text_color=Fore.RED,
    #                                back_color=Back.BLACK, set_back_after=True, location=''),
    # terminal_set_print_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak', bold=False,
    #                                text_color=Fore.LIGHTRED_EX, back_color=Back.GREEN, set_back_after=True, location='')
# )
