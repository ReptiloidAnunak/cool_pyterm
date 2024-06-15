from colorama import Back, Fore, Style, init
# init(autoreset=True)


def terminal_set_color_block(name_function: str,
                        set_all_str_color=True):
    if set_all_str_color:
        init(autoreset=False)
        name_function = Back.YELLOW + Fore.BLACK + name_function + Style.RESET_ALL
    else:
        name_function = Back.YELLOW + Fore.BLACK + name_function
    print(name_function)


terminal_set_color_block('adb', set_all_str_color=False)
print("111")
print("ddd")