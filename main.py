import speech_recognition as sr
import webbrowser
import asyncio
import edge_tts
import music_library
import requests
import asyncio
import edge_tts
import pygame
import io
from groq import Groq

recognizer = sr.Recognizer()
newsapi = "ecf681f277b141ba975722db669321a5"

pygame.mixer.init()

async def speak_async(text):
    communicate = edge_tts.Communicate(text, "en-IN-PrabhatNeural")

    audio_stream = io.BytesIO()

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_stream.write(chunk["data"])

    audio_stream.seek(0)

    pygame.mixer.music.load(audio_stream, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

def speak(text):
    asyncio.run(speak_async(text))


def aiProcess(command):
    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful virtual assistant named nexus skilled in task like Alexa and Google Cloud."
        },
        {
            "role": "user",
            "content": command,
        }
    ],

    model="llama-3.3-70b-versatile"
    )

# Print the completion returned by the LLM.
    return chat_completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        speak("Fetching latest news")

        r = requests.get(
            f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey={newsapi}"
        )

        if r.status_code == 200:
            news_json = r.json()
            articles = news_json.get('articles', [])

            if not articles:
                speak("No news found")
            else:
                for article in articles[:5]:
                    print(article['title'])
                    speak(article['title'])
        else:
            speak("Failed to fetch news")

    else:
        # let AI model handle the request
        aiProcess(c)
        output = aiProcess(c)
        speak(output)




if __name__ == "__main__":
    speak("Initializing nexus....")
    while True:
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)

            word = r.recognize_google(audio)

            if (word.lower() == "nexus"):
                speak("Ya")

                with sr.Microphone() as source:
                    print("nexus Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))