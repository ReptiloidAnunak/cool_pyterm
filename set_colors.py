import shutil
from colorama import Back, Fore, Style, init


def center_multiline_text(text, fore_color=Fore.WHITE, back_color=Back.BLACK):
    """
    Center-aligns the given multiline text within the terminal width.
    """
    # Определяем ширину консоли
    width = shutil.get_terminal_size().columns

    # Разбиваем текст на строки
    text_lines = text.split('\n')

    # Создаем список для центрированных строк
    centered_lines = []

    # Центрируем каждую строку
    for line in text_lines:
        if len(line) >= width:
            centered_lines.append(line)
        else:
            padding = (width - len(line))
            centered_line = ' ' * padding + line + ' ' * padding
            centered_lines.append(centered_line)

    # Выводим каждую центрированную строку с заданными цветами
    for line in centered_lines:
        colored_text = f"{back_color}{fore_color}{line}{Style.RESET_ALL}"
        print(colored_text)


def terminal_set_style_block(text: str = None,
                             bold: bool = False,
                             text_color=None,
                             back_color=None,
                             set_back_after: bool = True,
                             location='l'):

    if not text:
        print('Set the function`s text arg')
        exit()

    if location == 'c':
        padding = ' ' * 50

        if '\n' in text:
            lines_lst = text.split('\n')
            lines_formated = []
            for line in lines_lst:
                line = padding + line + ' ' * 200
                lines_formated.append(line)

            text = '\n'.join(lines_formated)

        else:
            text = padding + text + ' ' * 50
            # Формируем центрированный текст с пробелами по бокам
            text = text
    if set_back_after:
        init(autoreset=False)
        text = back_color + text_color + text
    else:
        text = back_color + text_color + text + Style.RESET_ALL
    if bold:
        text = Style.BRIGHT + text
    return text

print(


terminal_set_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak',
                         bold=True,
                         text_color=Fore.BLACK,
                         back_color=Back.WHITE,
                         set_back_after=False,
                         location='c'),


terminal_set_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak\n',
                         bold=False,
                         text_color=Fore.WHITE,
                         back_color=Back.BLACK,
                         set_back_after=False,
                         location=''),

terminal_set_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak\n',
                         bold=False,
                         text_color=Fore.RED,
                         back_color=Back.BLACK,
                         set_back_after=True,
                         location=''),
terminal_set_style_block(text='\nCOOL PYTERM\ncreated by ReptiloidAnunak',
                         bold=False,
                         text_color=Fore.LIGHTRED_EX,
                         back_color=Back.GREEN,
                         set_back_after=True,
                         location='')
)