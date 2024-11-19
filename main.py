import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print("""
    🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 
    ╔═══════════════════════════════════╗
    ║     The Pirate Translator         ║
    ║        By Order of the Cap'n      ║
    ╚═══════════════════════════════════╝
    🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 🏴‍☠️ 
    """)

def print_ship():
    print("""
                |    |    |
               )_)  )_)  )_)
              )___))___))___)\
             )____)____)_____)\\
           _____|____|____|____\\\__
    ---------\                   /---------
      ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
        ^^^^      ^^^^     ^^^    ^^
             ^^^^      ^^^
    """)

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
            'everyone': "all hands",
            'look': "spy",
            'throw': "heave",
            'theft': "plunder",
            'steal': "pillage",
            'victory': "conquest"
        }

    def text_to_pirate(self, text):
        words = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text).split()
        pirate_words = []
        
        i = 0
        while i < len(words):
            if i < len(words) - 1:
                phrase = words[i] + ' ' + words[i + 1]
                if phrase in self.pirate_dict:
                    pirate_words.append(self.pirate_dict[phrase])
                    i += 2
                    continue
            
            if words[i] in self.pirate_dict:
                pirate_words.append(self.pirate_dict[words[i]])
            else:
                pirate_words.append(words[i])
            i += 1
        
        pirate_text = ' '.join(pirate_words)
        return self._add_pirate_flourishes(pirate_text)

    def _add_pirate_flourishes(self, text):
        flourishes = [
            " Arr!",
            " Yarr!",
            " Yo ho ho!",
            " Shiver me timbers!",
            " Avast ye!"
        ]
        return text + random.choice(flourishes)

def main():
    translator = PirateTranslator()
    
    while True:
        clear_screen()
        print_title()
        print_ship()
        
        print("\n⚓ Choose yer path, sailor:")
        print("1. ⚔️  Translate to Pirate Speak")
        print("2. 📜 View Pirate Dictionary")
        print("3. 👑 Famous Pirates")
        print("4. 💾 Save Last Translation")
        print("5. 🚪 Abandon Ship (Exit)")
        
        choice = input("\nEnter yer choice (1-5): ")
        
        if choice == '1':
            text = input("\nEnter yer text to translate: ")
            print("\n🦜 Pirate Translation:")
            pirate_text = translator.text_to_pirate(text)
            print("➜", pirate_text)
            last_original = text
            last_translation = pirate_text
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            print("\n📚 Pirate Dictionary:")
            for normal, pirate in sorted(translator.pirate_dict.items()):
                print(f"{normal:15} ➜ {pirate}")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            print("\n👑 Famous Pirates Throughout History:")
            famous_pirates = [
                "Blackbeard (Edward Teach) - The most notorious pirate of all time",
                "Anne Bonny - One of the most famous female pirates",
                "Bartholomew Roberts - The most successful pirate of the Golden Age",
                "Calico Jack - Known for his distinctive flag design",
                "Captain Henry Morgan - Famous privateer turned pirate",
                "Mary Read - Disguised herself as a male pirate",
                "William Kidd - Started as a privateer, ended as a pirate",
                "Cheng I Sao - Most successful pirate in Chinese history",
                "Sir Francis Drake - Famous privateer for Queen Elizabeth I",
                "Jean Lafitte - The Gentleman Pirate"
            ]
            for pirate in famous_pirates:
                print(f"• {pirate}")
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            try:
                save_translation_to_file(last_original, last_translation)
                print("\n💾 Translation saved to 'pirate_translations.txt'!")
            except NameError:
                print("\n❌ No translation to save! Translate something first!")
            input("\nPress Enter to continue...")
        
        elif choice == '5':
            clear_screen()
            print("""
                 ⛵ Fair winds and following seas! ⛵
                        See ye later, matey!
            """)
            break
        
        else:
            print("Blimey! That's not a valid choice, ye scallywag!")
            input("Press Enter to try again...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nYe be jumping ship! Fair winds, matey! 🏴‍☠️")

