import random

def load_jokes():
    """Returns a list of programming-related jokes"""
    return [
        {
            "setup": "Why do Python programmers wear glasses?",
            "punchline": "Because they can't C#!"
        },
        {
            "setup": "How many programmers does it take to change a light bulb?",
            "punchline": "None. It's a hardware problem!"
        },
        {
            "setup": "What did the Python say when it was feeling slow?",
            "punchline": "I think I need to do some list comprehension!"
        },
        {
            "setup": "Why don't programmers like nature?",
            "punchline": "It has too many bugs!"
        },
        {
            "setup": "What's a snake's favorite programming paradigm?",
            "punchline": "Object-Hisssss-oriented programming!"
        },
        {
            "setup": "Why did the programmer quit his job?",
            "punchline": "Because he didn't get arrays!"
        },
        {
            "setup": "What do you call a Python programmer who's lost their pet snake?",
            "punchline": "Someone with a missing import!"
        },
        {
            "setup": "Why was the math book sad?",
            "punchline": "Because it had too many problems!"
        },
        {
            "setup": "What does a Python programmer wear to stay warm?",
            "punchline": "A tuple neck sweater!"
        },
        {
            "setup": "Why do programmers always mix up Halloween and Christmas?",
            "punchline": "Because Oct 31 == Dec 25!"
        }
    ]

def display_joke(joke):
    """Prints a joke with a small delay for better timing"""
    import time
    
    print("\n🎭 Here's your programming joke: \n")
    print(f"Q: {joke['setup']}")
    time.sleep(2)  # Pause for dramatic effect
    print(f"A: {joke['punchline']}")
    print("\n" + "="*40 + "\n")

def main():
    """Main program function"""
    print("Welcome to the Python Joke Generator! 🐍")
    print("Loading jokes from our totally-not-binary humor database...")
    
    jokes = load_jokes()
    
    while True:
        display_joke(random.choice(jokes))
        
        # Ask if user wants another joke
        answer = input("Would you like another joke? (y/n): ").lower()
        if answer != 'y':
            print("\nGoodbye! Remember: There are only 10 types of people... 😉\n")
            break

if __name__ == "__main__":
    main()