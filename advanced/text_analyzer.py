import os
os.system("clear")

with open('ipsum.txt', 'r') as ipsum:
    text = ipsum.read()

# first tip
def text_analyzer(text):
    chars = []
    count = []
    for letter in text:
        if not letter in chars:
            chars.append(letter)
            count.append(1)
        else:
            index = chars.index(letter)
            count[index] += 1
    result = {}
    for item in range(len(chars)):
        result[chars[item]] = count[item]
    return result

print(text_analyzer(text), "\n")
# second tip

def text_analyzer_middle_level(text):
    chars = set()
    for item in text:
        chars.add(item)
    chars = list(chars)
    count = [text.count(item) for item in chars]
    result = {}
    for item in range(len(chars)):
        result[chars[item]] = count[item]
    return result

print(text_analyzer_middle_level(text), "\n")

def text_analyzer_senior_level(text):
    chars = list({ item for item in text })
    count = [text.count(item) for item in chars]
    result = {}
    for item in range(len(chars)):
        result[chars[item]] = count[item]
    return result

print(text_analyzer_senior_level(text), "\n")

def text_analyzer_specialist_level(text):
    return { letter: text.count(letter) for letter in set(text) }

print(text_analyzer_specialist_level(text), "\n")
