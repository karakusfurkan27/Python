import random

emoji_dict = {
    "cat": "🐱", "dog": "🐶", "sun": "☀️", "star": "⭐", 
    "moon": "🌙", "wizard": "🧙", "robot": "🤖", "alien": "👽",
    "love": "❤️", "fire": "🔥", "earth": "🌎", "sky": "🌌"
}

def text_to_emoji(text):
    words = text.split()
    transformed_text = []
    for word in words:
        transformed_text.append(emoji_dict.get(word.lower(), word))
    return " ".join(transformed_text)

text = "The wizard and the alien found a new planet under the moon and stars."
print(text_to_emoji(text))
