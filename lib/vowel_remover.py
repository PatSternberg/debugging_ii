# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.text


new_text = 'aeiou'
new_text_length = len(new_text)
vowels = ["a", "e", "i", "o", "u"]
i = 0
while i < new_text_length:
    if new_text[-1].lower() in vowels:
        new_text = new_text[:i] + new_text[i+1:]
    i += 1
print(new_text)

