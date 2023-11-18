import sys
import random
from googlesearch import search
from colorama import Fore, Style, init

init(autoreset=True)

def search_google(query):
    try:
        results = list(search(f"{query} programming language documentation"))
        if results:
            return results[0]
    except Exception as e:
        print(f"Error searching Google: {e}")
    return None

def print_colored(message, color=Fore.WHITE, style=Style.NORMAL):
    print(style + color + message + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_colored(f"Usage: python3 {sys.argv[0]} <text file> [amount of lines]", Fore.RED, Style.BRIGHT)
        sys.exit(1)

    with open(sys.argv[1]) as file:
        lines = file.readlines()

    amount_of_lines = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    for _ in range(amount_of_lines):
        language = random.choice(lines).strip()
        documentation_link = search_google(language)

        color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])
        
        if documentation_link:
            print_colored(f"{language}: {documentation_link}", color, Style.BRIGHT)
        else:
            print_colored(f"No documentation found for {language}", color, Style.DIM)
