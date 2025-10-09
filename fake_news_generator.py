# Fake News Headline Generator
# Author: Mugamboo

import random

# Word pools
subjects = ["Government", "Celebrity", "AI Robot", "Startup", "Politician", "Scientist", "Billionaire", "Student"]
verbs = ["launches", "bans", "discovers", "hides", "reveals", "predicts", "steals", "announces"]
objects = ["new technology", "secret project", "fake currency", "alien life", "AI model", "mystery virus", "moon base", "social app"]
places = ["in India", "at Mars", "in New York", "in Silicon Valley", "at college", "in London", "worldwide", "on the internet"]
extras = ["experts shocked", "citizens react", "officials remain silent", "goes viral", "causes chaos", "makes history", "trends globally"]

def generate_fake_headline():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    place = random.choice(places)
    extra = random.choice(extras)
    headline = f"{subject} {verb} {obj} {place}, {extra}!"
    return headline

# Generate multiple headlines
print("\n📰 Fake News Headline Generator 📰\n")
for i in range(5):
    print(f"{i+1}. {generate_fake_headline()}")
