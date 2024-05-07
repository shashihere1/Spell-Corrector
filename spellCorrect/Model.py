from textblob import TextBlob

class SpellCheckerModule:
    def __init__(self):
        pass

    def correct_spell(self, text):
        blob = TextBlob(text)
        corrected_text = blob.correct()
        return str(corrected_text)


if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello. I love maschines. apppple"
    print(obj.correct_spell(message))
