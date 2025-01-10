
def questions():
    my_range = 4
    pass_range = 4
    correct_range = 0
    lists_of_questions = ["What is nearest star in our solar system?", "Who created the Theory of Relatively?"]
    lists_of_answers = ["A.) Startos", "B.) Ton A", "C.) Proxima Centauri", "D.) Collosal","A.) Thomas Edison", "B.) Albert Einstein", "C.) Nikola Tesla", "D.) Stephen Hawking"]
    lists_of_correct_answers = ["C.) Proxima Centauri", "B.) Albert Einstein"]

    for questions in lists_of_questions:
        print(questions)
        for answers in range(my_range):
            if my_range > pass_range:
               pass_range = pass_range + 1
               continue
            else:   
                print(lists_of_answers[answers])
        answer = input("Enter you answer here: ")
        for correct in lists_of_correct_answers:
            if answer != lists_of_correct_answers[correct_range]:
                print(f"Wrong! {lists_of_correct_answers[correct_range]} is the correct answer!")
                break
            else:
                print("Correct!")
                break
        correct_range = correct_range + 1
        my_range = my_range + my_range
            
questions()