import random
import numpy

MAX_N = 25
DEFAULT_N = 6
WIKTIONARY_IP = "https://en.wiktionary.org/wiki/Appendix:Toki_Pona/"

array_dice = [
    ["li", "la", "e", "a", "o", "seme"] , #gramatical particles (o que estas sean "gratis")
    ["en", "pi", "anu", "tenpo", "kin", "taso"], #conjunctions
    ["mi", "sina", "ona", "ni", "kulupu", "ijo"], #subjects
    ["jan", "meli", "tonsi", "mije", "mama", "monsuta"], #people
    ["kepeken", "lon", "sama", "tan", "tawa", "nanpa"], #prepositions
    ["kama", "ken", "open", "pini", "wile", "sona"], #preverbs
    ["jo", "pali", "pilin", "olin", "moli", "lape"], #verbs
    ["pana", "awen", "lukin", "toki", "moku", "musi"], #verbs
    ["alasa", "unpa", "utala", "kokosila", "pakala", "lanpan"], #verbs
    ["kon", "ko", "telo", "sijelo", "kalama", "kiwen"], #states
    ["wawa", "suwi", "lili", "suli", "pona", "ike"], #adjectives
    ["seli", "lete", "ante", "sin", "epiku", "weka"], #adjectives
    ["len", "linja", "palisa", "poki", "kipisi", "lupa"], #things
    ["namako", "ilo", "tomo", "leko", "jaki", "esun"], #things
    ["kasi", "kili", "mun", "suno", "soko", "pan"],
    ["ma", "pu", "ku", "lipu", "nasin", "nena"],
    ["sike", "nasa", "mani", "supa", "jasima", "sewi"],
    ["misikeke", "nimi", "n", "mu", "meso", "sitelen"],
    ["ala", "wan", "tu", "mute", "ale", ""], #numbers
    ["kule", "walo", "pimeja", "laso", "jelo", "loje"], #colors
    ["anpa", "insa", "monsi", "sinpin", "poka", "selo"], #position
    ["pipi", "kala", "waso", "soweli", "akesi", "kijetesantakalu"], #animals
    ["luka", "kute", "oko", "lawa", "noka", "uta"] #body parts
]
# KU SULI: kijetesantakalu epiku kipisi leko tonsi ku kokosila monsuta misikeke n lanpan meso jasima
# a kin
# sin namako
# lukin oko

def show_dice():
    dice_text = ""
    for i, value_i in enumerate(array_dice):
        dice_text += "🎲" + str(i) + ": "
        for value_j in value_i:
            dice_text += value_j + " "
        dice_text += "\n"
    return dice_text

def roll_dice(args, help_command_text):
    n = DEFAULT_N #standard number of dice
    if len(args) > 0: #arguments
        n = try_parse_N(args[0])
        if n == 0: #error in N
            return f"The first argument (if any) has to be an integer between 1 and {MAX_N}"
        if len(args) > n + 1: #too many args
            return f"Too many arguments! The specified number of dice is {n}. "\
                f"After that, you can specify a maximum of {n} dice between 0 and {len(array_dice) - 1} if you want. "\
                    f"Type /{help_command_text} to see some examples."
        if not try_parse_args(args): #wrong args
            return f"Wrong arguments! The specified number of dice is {n}. "\
                f"After that, you can specify a maximum of {n} dice between 0 and {len(array_dice) - 1} if you want. "\
                    f"Type /{help_command_text} to see some examples."
    # roll dice    
    used_dice = numpy.full(len(array_dice), False)
    roll_text = "Dice roll successful!\n\n"
    for i in range(n):
        die = 0
        if len(args) >= i + 2:
            die = int(args[i + 1])
        else:
            not_used_dice = [i for i, value in enumerate(used_dice) if value == False]
            # print(not_used_dice)
            if len(not_used_dice) > 0:
                die = random.choice(not_used_dice) #no repetitions
            else:
                die = random.randint(0, len(array_dice) - 1) #can repeat if no more dice are available
        choice = random.choice(array_dice[die])
        roll_text += "🎲" + str(die) + " -> " + f'<a href="{WIKTIONARY_IP}{choice}">{choice}</a>' + "\n"
        used_dice[die] = True

    return roll_text

def try_parse_N(string):
    try:
        n = int(string)
        return n if n > 0 and n <= MAX_N else 0
    except Exception:
        return 0

def try_parse_args(args):
    try:
        i = 1
        while i < len(args):
            number = int(args[i])
            if number < 0 or number >= len(array_dice):
                return False
            i += 1
        return True
    except Exception:
        return False
