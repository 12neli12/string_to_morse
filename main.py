from art import ascii_art

morse_dict = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    0: "_____",
    1: ".____",
    2: "..___",
    3: "...__",
    4: "...._",
    5: ".....",
    6: "_....",
    7: "__...",
    8: "___..",
    9: "____::",
    " ": ".......",
    ",": "__..__",
    ".": "._._._",
    "?": "..__..",
    "\"": "._.._.",
    "'": ".____.",
    ":": "___...",
    "-": "_...._",
    "/": "_.._.",
    "(": "_.__.",
    ")": "_.__._"
}


def code_in_morse(text):
    characters = list(text)
    morse_code = ""
    for char in characters:
        if char in characters:
            morse_code += morse_dict[char] + " "
        else:
            return 0
    return morse_code


print(ascii_art)
user_input = input("Hello user!\n"
                   "This is a morse encoder.\n"
                   "Please enter the word you want to encode: ").lower()
print(code_in_morse(user_input))
