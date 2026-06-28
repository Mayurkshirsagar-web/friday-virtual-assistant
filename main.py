import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary
import time
from google import genai
from google.genai import types

# set up for all listening engine and speaking engine
rec = sr.Recognizer()
engine = pyttsx3.init()

# link to create Gemini API key - https://ai.google.dev/gemini-api/docs/api-key
gemini_client = genai.Client(api_key="YOUR-GEMINI-API-KEY")


# logic for speaking
def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)

# logic for getting answer from google gemini api
def ask_ai(question):
    for attempt in range(3):
        try:
            response = gemini_client.models.generate_content(
                model="gemini-2.5-flash-lite",
                config=types.GenerateContentConfig(
                    system_instruction="""
                    You are Friday, a smart voice assistant like Iron Man's AI.
                    - Keep answers short and conversational
                    - No markdown, no asterisks, no bullet points
                    - Speak in a confident, slightly formal tone
                    - If asked something personal, respond as Friday would
                    """
                ),
                contents=question
            )
            return response.text
        

        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"Server busy, retrying... (attempt {attempt+1}/3)")
                time.sleep(5)
            else:
                raise e
    return "Sorry, I'm having trouble connecting right now."


# Logic for Processing commands 
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open github" in c:
        webbrowser.open("https://github.com")
    elif "open codeforces" in c:
        webbrowser.open("https://codeforces.com")

    # logic for opening music
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # logic for reading news
    elif "news" in c:
        # link to create News API key - https://newsapi.org/
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR-NEWS-API-KEY")
        data = r.json()
        for article in data.get("articles", []):
            speak(article["title"])
    else:
        answer = ask_ai(c)
        print(f"\nFriday: {answer}\n")
        speak(answer)


# all the logic to run listen command
if __name__ == "__main__":
    speak("Initializing Friday..")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                rec.adjust_for_ambient_noise(source, duration=0.5)
                audio = rec.listen(source, timeout=2, phrase_time_limit=2)

            word = rec.recognize_google(audio)

            if "friday" in word.lower():
                speak("What's up!")
                with sr.Microphone() as source:
                    print("Friday Active...")
                    rec.adjust_for_ambient_noise(source, duration=0.5)
                    audio = rec.listen(source, timeout=5, phrase_time_limit=5)

                command = rec.recognize_google(audio)
                print(f"\nCommand: {command}\n")
                processCommand(command)

            if "deactivate" in word.lower():
                speak("Deactivating..")
                break

        except sr.WaitTimeoutError:
            print("say something bro\n")
        except sr.UnknownValueError:
            print("couldn't understand\n")
        except sr.RequestError as e:
            print(f"Google API error: {e}\n")
        except Exception as e:
            print(f"ERROR: {e}\n")