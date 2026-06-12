import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_time():
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time_now}")

def get_date():
    date_today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {date_today}")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_wikipedia(topic):
    try:
        speak(f"Searching Wikipedia for {topic}")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find that.")

def open_website(site):
    websites = {
        "google"   : "https://www.google.com",
        "youtube"  : "https://www.youtube.com",
        "github"   : "https://www.github.com",
        "linkedin" : "https://www.linkedin.com",
    }
    for name, url in websites.items():
        if name in site:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return
    speak("Sorry, I don't know that website.")

def process_command(command):
    command = command.lower()

    if any(w in command for w in ["hello", "hi", "hey"]):
        speak("Hello! I am Jarvis. How can I help you?")

    elif "time" in command:
        get_time()

    elif "date" in command or "today" in command:
        get_date()

    elif "wikipedia" in command:
        topic = input("Search topic: ")
        search_wikipedia(topic)

    elif "open" in command:
        site = input("Which website? ")
        open_website(site)

    elif any(w in command for w in ["search", "google", "find"]):
        query = input("Search query: ")
        search_web(query)

    elif any(w in command for w in ["who are you", "your name"]):
        speak("I am Jarvis, your Python voice assistant!")

    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs!")

    elif any(w in command for w in ["exit", "quit", "bye"]):
        speak("Goodbye! Have a great day!")
        return False

    else:
        speak(f"Sorry, I didn't understand that.")

    return True

def main():
    print("=" * 45)
    print("   🤖 JARVIS - Voice Assistant")
    print("   Oasis Infobyte - Project 1")
    print("=" * 45)

    speak("Hello! I am Jarvis, your voice assistant!")

    running = True
    while running:
        print("\n" + "-" * 35)
        command = input("You: ")
        running = process_command(command)

if __name__ == "__main__":
    main()