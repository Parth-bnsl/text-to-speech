from gtts import gTTS
import os

input_txt = 'Insert any text you prefer'
language = 'en'
convertfn = gTTS(text=mytext, lang=language, slow=False)
convertfn.save("name.mp3")
