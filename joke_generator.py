import random

# list of jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the JavaScript developer sad? Because he didn't 'null' his feelings.",
    "How many programmers does it take to change a light bulb? None, it's a hardware problem!",
    "Why do Python programmers hate Java? Because they don't like to be C-ed!",
    "What is a programmer's favorite hangout place? The Foo Bar!"
]

def tell_joke():
    while True:
        print("\n" + random.choice(jokes))
        user_input = input("\n Do you want another joke? (yes/no): ").strip().lower()
        if user_input != "yes":
            print("Thank you for listening to the jokes! Have a great day!")
            break

tell_joke()
