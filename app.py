import random

def text_add():
    with open('bot.txt','a') as bot:
        text = input('Введите фразу: ')
        bot.write(f"{text}\n")
        print(f"Вы добавили фразу: {text}!")
        
    
def text_random():
    with open('bot.txt') as bot:
        phrases = bot.readlines()
        print(f"бот отвечает: {random.choice(phrases)}")


text_add()
text_random()