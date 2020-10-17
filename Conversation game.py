finish = False
score = 0
print("Please respond with simple words in your answer")
print("If you want to finish, type finish")
print("If you want a hint, type hint")
questions = ["hi, how are you?", "how was school today?", "can you help me with my homework?", "I feel that you should help me more - maybe give me the answer?"]
while finish == False:
    for i in range(len(questions)):
        print(questions[i])
        response = input("What do you respond: ")
        if "good" in response or "no" in response:
            score += 3
        elif "ok" in response or "I don't know" in response or "maybe" in response:
            score += 2
        elif "bad" in response or "awful" in response or "yes" in response:
            score += 1
        elif "finish" == response.lower():
            finish = True
            break
        elif "hint" == response.lower():
             print("Think positive, but also think about what is best for you")
print("Score: ", score) 
