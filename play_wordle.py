from letter_state import LetterState
from worlde import Wordle
from colorama import Fore
import random


def main():
    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    while wordle.can_attempt:
        x = input("\nType your guess : ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long" + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("Good job")
    else:
        print("You didn't solve it")
        print(f"The secret word was : {wordle.secret}")


def display_results(wordle: Wordle):
    print("\n Your results so far:\n ")
    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)


def convert_result_to_color(result: list[LetterState]):
    result_with_color = []

    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


def draw_border_around(lines: list[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)

    return word_set


if __name__ == "__main__":
    main()
