def game_loop():
    option = game_menu()
    if option == '1':
        questions = read_questions()
        result = ask_questions(questions)
        display_result(result)
    elif option == '2':
        add_a_question()
    elif option == '3':
        return
    else:
        print "This is not a valid option!"
    game_loop()

def game_menu():
    menu = "Enter 1 to play\n" + \
        "Enter 2 to Add a Question\n" + \
        "Enter 3 to Exit\n"
    return raw_input(menu)


def write_question(question,answer):
    with open('questions.txt','a')as f:
        f.writelines([question + '\n', answer + '\n'])

def add_a_question():
    question_text=raw_input("Enter a question:\n")
    answer_text=raw_input("Enter the answer:\n")
    write_question(question_text,answer_text)

def read_questions():
    questions, answers = [], []
    with open('questions.txt') as f:
        for i, line in enumerate(f):
            if i % 2 != 0:
                answers.append(line.strip())
            else:
                questions.append(line.strip())
    return zip(questions, answers)



def ask_questions(questions, get_answer=raw_input):
    questions = read_questions()
    score = 0
    total = len(questions)
    for question, answer in questions:
        guess = get_answer(question)
        if guess == answer:
            score += 1
    #print 'You got %s out of %s questions right' % (score, total)
    return score, total




def display_result(result):
    print"You scored %s out of %s"%(result[0],result[1])

game_loop()










