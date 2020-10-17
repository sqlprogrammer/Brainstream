import random
happy = "I can't wait to see you tomorrow"
sad = "I'm not sure"
angry = "Why would you do that?!"
stressed = "Shhh I only have 5 more minutes"
shocked = "Wait what?!"
amazed = "I'm proud!"
answer = ["happy", "sad", "angry", "stressed", "shocked", "amazed"]
emoji = [happy, sad, angry, stressed, shocked, amazed]
question = random.choice(emoji)
print(question)
theiranswer = input("What emotion is this? ")
while theiranswer != answer[emoji.index(question)]:
    theiranswer = input("Try again: ")

print("Well done")

