#eliza.py
#En verkligt simpel version av ett Eliza-liknande program
#1) Önskar användaren välkommen
#2) Upprepar följande i all oändlighet
# 2.1) Väntar på att användaren "säger" något
# 2.2) Svarar på ett sätt som verkar intelligent
# Svaret väljs alltid slumpmässigt ur en samling uttryck som vi lagrat i en
# lista. På detta sätt får vi användaren att tro
#att Eliza faktiskt är smart. Eller så inte :)
import string
import random
import loggning
positiva = [
    "Berätta mer",
    "Jag förstår...",
    "Ahaa...",
    "Jag lyssnar..."
]

NEGATIVE_WORDS = [
    "nej",
    "aldrig",
    "inte",
]

NEGATIVE_RESPONSES = [
    "Inte det?",
    "Är du helt säker?",
    "Är det sant",
    "Varför inte",
]

FAMILY_WORDS = [
    "mamma",
    "pappa",
    "bror",
    "syster",
    "kusin",
    "mormor",
    "morfar"
]
FAMILY_RESPONSES = [
    "Är din bror likadan?",
    "Hur får det dig att känna?",
    "Hur mår din mor?",
    "Har du barn?"
]

EXIT_PHRASES = [
    "Tack och godnatt!",
    "OK, that does it!",
    "Sluta!",
    "Hejs Svejs"
]

PRONOMEN = {
    "jag": "du",
    "min": "din",
    "mitt": "ditt",
    "mig": "dig",
    "mina": "dina"
}

def get_opposite_pronoun(pronoun: str) -> str:
    for key, value in PRONOMEN.items():
        if key == pronoun:
            return value
        if value == pronoun:
            return key
    return None
def print_and_log(message: str) -> None:
    print(message)
    loggning.log(message)
    
def main():
    print ("**************************************************")
    print ()
    print (" Välkommen till Elizas mottagning ")
    print ()
    print ("**************************************************")
    print ()
    print ('(Du kan sluta när som helst genom att svara "Hejs svejs")')
    print ()
    print ('Berätta för mig om dina problem...')
    # Fortsätt diskussionen i all oändlighet
    while True:
    # Vänta på att användaren matar in något
        text = input("\n> ")
        text = text.lower()
        if text.strip().lower() in EXIT_PHRASES:
            break
        
        reply = response(text)
        print_and_log(reply)
        
    print ('Tack för besöket. Betala in 150 EUR på mitt konto.')


def response(input: str) -> str:
    SPECIAL_CHARS = "!:?;.,"
    last_special_char = None
    clean_input = ""
    for i, char in enumerate(input):
        if i == len(input) - 1:
            if char in SPECIAL_CHARS:
                last_special_char = char
                break
            else:
                clean_input += char
        else:
            clean_input += char
    
    # Dela upp användarens mening i en lista av ord
    urspr_ord = clean_input.split()
    # Skapa en ny lista som innehåller samma ord (en kopia)
    nya_ord = urspr_ord[ : ]
    # Gå igenom alla ord, ett åt gången. Om ordet är i första person, så byt ut det till
    # motsvarande ord i andra person
    for i in range(len(urspr_ord)):
        new_pronoun = get_opposite_pronoun(urspr_ord[i])
        if new_pronoun is not None:
            nya_ord[i] = new_pronoun
            
    for word in nya_ord:
        if word.lower() in NEGATIVE_WORDS:
            return random.choice(NEGATIVE_RESPONSES)      
            
    for word in nya_ord:
        if word.lower() in FAMILY_WORDS:
            return random.choice(FAMILY_RESPONSES)      
    if nya_ord == urspr_ord:
        
        return random.choice(positiva)
    else:
        output = " ".join(nya_ord)
        if last_special_char is not None:
            output += last_special_char
        return output
    
    
if __name__ == '__main__':
    main()

