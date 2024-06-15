from colorama import Fore, Back, Style, init
import shutil


init(autoreset=True)


background_colour_dict = {
    "BLACK": Back.BLACK,
    "RED": Back.RED,
    "GREEN": Back.GREEN,
    "YELLOW": Back.YELLOW,
    "BLUE": Back.BLUE,
    "MAGENTA": Back.MAGENTA,
    "CYAN": Back.CYAN,
    "WHITE": Back.WHITE,
    "RESET": Back.RESET,
    "LIGHTBLACK": Back.LIGHTBLACK_EX,
    "LIGHTRED": Back.LIGHTRED_EX,
    "LIGHTGREEN": Back.LIGHTGREEN_EX,
    "LIGHTYELLOW": Back.LIGHTYELLOW_EX,
    "LIGHTBLUE": Back.LIGHTBLUE_EX,
    "LIGHTMAGENTA": Back.LIGHTMAGENTA_EX,
    "LIGHTCYAN": Back.LIGHTCYAN_EX,
    "LIGHTWHITE": Back.LIGHTWHITE_EX
}

# Словарь цветов для текста
text_colour_dict = {
    "BLACK": Fore.BLACK,
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "BLUE": Fore.BLUE,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE,
    "RESET": Fore.RESET,
    "LIGHTBLACK": Fore.LIGHTBLACK_EX,
    "LIGHTRED": Fore.LIGHTRED_EX,
    "LIGHTGREEN": Fore.LIGHTGREEN_EX,
    "LIGHTYELLOW": Fore.LIGHTYELLOW_EX,
    "LIGHTBLUE": Fore.LIGHTBLUE_EX,
    "LIGHTMAGENTA": Fore.LIGHTMAGENTA_EX,
    "LIGHTCYAN": Fore.LIGHTCYAN_EX,
    "LIGHTWHITE": Fore.LIGHTWHITE_EX
}


def get_text_color_for_terminal(color_name: str):
    color_name = color_name.upper()
    try:
        color = text_colour_dict[color_name]
    except KeyError:
        raise ValueError(f"Invalid text color name: {color_name}")
    return color


def get_background_color_for_terminal(color_name: str):
    color_name = color_name.upper()
    try:
        color = background_colour_dict[color_name]
    except KeyError:
        raise ValueError(f"Invalid background color name: {color_name}")
    return color


