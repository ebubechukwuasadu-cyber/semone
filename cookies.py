from gtts import gTTS

text = """
Cookies are delicious little treats made from flour, sugar, butter, and creativity.
Some are crunchy, some are soft, and some are filled with chocolate chips.
No matter the type, cookies always bring joy.
"""

tts = gTTS(text=text, lang="en")
tts.save("cookies.mp3")

print("Created cookies.mp3!")
