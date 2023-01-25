from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)
else:
    print("Sphinx cannot recognize")