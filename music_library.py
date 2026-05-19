music = {
    "friday": "https://youtu.be/U6n2NcJ7rLc?si=HEvfzYhwkhbWMwtG",
    "lose my mind": "https://youtu.be/VJxppgsHjF8?si=BkMk2SBx2O6RvM7_",
    "espresso": "https://youtu.be/eVli-tstM5E?si=2BTyDEOT5gOgVdcn",
    "man": "https://youtu.be/2nP3ElUtFDU?si=Lx2HeZaH0lbXuj8h"
}



# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import music_library
# import requests

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "ecf681f277b141ba975722db669321a5"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = music_library.music[song]
#         webbrowser.open(link)
    
#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#         if r.status_code == 200:
#             # Parse the JSON response
#             news_json = r.json()
#             # Extract the articles
#             articles = news_json.get('articles', [])
#             # Print the headlines
#             for article in articles[:5]:  # Print first 5 headlines
#                 speak(article['title'])
#         else:
#             print("Failed to fetch news")


# if __name__ == "__main__":
#     speak("Initializing nexus....")
#     while True:
#         # Listen for the wake word "nexus"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
         
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=3)
#             word = r.recognize_google(audio)
#             if (word.lower() == "nexus"):
#                 speak("Ya")
#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("nexus Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)


#         except Exception as e:
#             print("Error; {0}".format(e))