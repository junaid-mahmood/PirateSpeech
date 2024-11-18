class PirateTranslator:
    def __init__(self):
        self.pirate_dict = {
            'hello': "ahoy",
            'hi': "yarr",
            'my': "me",
            'friend': "matey",
            'yes': "aye",
            'no': "nay",
            'is': "be",
            'are': "be",
            'the': "th'",
            'you': "ye",
            'your': "yer",
            'stop': "avast",
            'money': "doubloons",
            'food': "grub",
            'water': "grog",
            'drink': "grog",
            'wow': "blimey",
            'my god': "shiver me timbers",
            'oh my': "shiver me timbers",
            'happy': "jolly",
            'bathroom': "head",
            'restaurant': "galley",
            'friend': "matey",
            'everyone': "all hands",
            'look': "spy",
            'throw': "heave",
            'food': "grub",
            'theft': "plunder",
            'steal': "pillage",
            'victory': "conquest"
        }

    def text_to_pirate(self, text):
        # Clean the text and split into words
        words = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text).split()
        pirate_words = []
        
        i = 0
        while i < len(words):
            # Try two-word phrases first
            if i < len(words) - 1:
                phrase = words[i] + ' ' + words[i + 1]
                if phrase in self.pirate_dict:
                    pirate_words.append(self.pirate_dict[phrase])
                    i += 2
                    continue
            
            # Try single words
            if words[i] in self.pirate_dict:
                pirate_words.append(self.pirate_dict[words[i]])
            else:
                pirate_words.append(words[i])
            i += 1
        
        pirate_text = ' '.join(pirate_words)
        return self._add_pirate_flourishes(pirate_text)

    def _add_pirate_flourishes(self, text):
        from random import choice
        flourishes = [
            " Arr!",
            " Yarr!",
            " Yo ho ho!",
            " Shiver me timbers!",
            " Avast ye!"
        ]
        return text + choice(flourishes)

def main():
    translator = PirateTranslator()
    
    while True:
        print("\nAhoy! Choose yer option:")
        print("1. Text to Pirate")
        print("2. Abandon Ship (Exit)")
        
        choice = input("Enter yer choice (1-2): ")
        
        if choice == '1':
            text = input("Enter yer text: ")
            pirate_text = translator.text_to_pirate(text)
            print("Pirate speak:", pirate_text)
        
        elif choice == '2':
            print("Fair winds, ye scurvy dog!")
            break
        
        else:
            print("Blimey! That's not a valid choice!")

if __name__ == "__main__":
    main()
