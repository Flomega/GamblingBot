import random, re, time
from colorama import init, Fore, Style

init(autoreset=True)

def gambling_advice():
    advices = [
        "Go big or go home.", "If you lose, gamble the rest too.",
        "If you lose make sure to blame the dealer.", "Go all in to make more profit.",
        "Gamble when you're emotionally unstable.", "Just listen to me and you will win.",
        "Make sure to gamble half of what you have so you can Double Down.",
        "Don't hold back and Gamble like nothing matters.",
        "Gamble Gambling Gambler, all that matters.",
        "Remember that gambling is to make money and not to entertain yourself."
    ]
    return random.choice(advices)

def decide_action(score, dealer):
    return "You should stand." if score >= 17 else ("You should hit." if score <= 11 else ("You should hit." if dealer >= 7 else "You should stand."))

def roulette_bet(): return f"You should bet on number {random.randint(0, 36)}."

def roll_dice(): return random.randint(1, 6), random.randint(1, 6)

def dice_game():
    d1, d2 = roll_dice()
    return f"You rolled {d1} and {d2}."

def slot_machine():
    s = [random.choice(["🍒", "🍋", "💎", "🔔", "7️⃣", "🍀"]) for _ in range(3)]
    print(f"{Fore.MAGENTA}🎰 Spinning...\n🌀 🌀 🌀\n     {' | '.join(s)}")
    return f"{Fore.GREEN}💰 JACKPOT!" if s[0]==s[1]==s[2] else (f"{Fore.YELLOW}🥈 Partial match." if len(set(s)) < 3 else f"{Fore.RED}💀 No match.")

def simple_calculator(expr):
    try: return f"The result of {expr} is {eval(expr)}."
    except: return "Error: Invalid calculation."

def main():
    print(f"{Fore.YELLOW}{Style.BRIGHT}🎰 Welcome to the Ultimate Gambling Terminal! 🎰")
    while True:
        text = input(
            f"\n{Fore.CYAN}Say anything that contains one of the games we offer (Blackjack - tells you what to do) (Slots - spins the slots) (Roulette - Random number to bet on) (Dice - rolls 2 dices): ").lower()

        if "exit" in text:
            print(f"{Fore.LIGHTMAGENTA_EX}🤑 Thanks for playing! Goodbye!")
            break

        if "blackjack" in text:
            try:
                parts = input("Enter your score and dealer's card (e.g., '15 10'): ").split()
                print(decide_action(int(parts[0]), int(parts[1])))
            except: print(f"{Fore.RED}⚠️ Invalid input.")
        elif "roulette" in text:
            print(roulette_bet())
        elif "dice" in text:
            print(dice_game())
        elif "slot" in text:
            print(slot_machine())
        elif m := re.search(r"\d+\s*[\+\-\*/]\s*\d+", text):
            print(simple_calculator(m.group()))
        else:
            print(f"{Fore.RED}❗ I don't understand that...")

        print(f"{Fore.LIGHTYELLOW_EX}💡 Advice: {gambling_advice()}")
        print("-" * 50)

if __name__ == "__main__":
    main()
