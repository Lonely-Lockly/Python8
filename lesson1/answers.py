def get_answer(question, delimeter=' '):
    question = question.lower()
    answers = {"привет": "И тебе привет!", "как_ты": "Лучше всех", "пока": "Увидимся"}
    dialogue = answers.get(question)    
    return dialogue.lower()

question = input()

print(get_answer(question))