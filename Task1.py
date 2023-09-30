Questions=("What is the capital city of India? ",
           "How many states in India?",
           "Which is the cleanest city in India?",
           "How many union territories in India?",
           "Who was the first to discover India?",
           "Name of the National Bird of India.",
           "Name of the National Animal of India.",
           "Name of the National Sport of India.",
           "Name of the National Heritage Animal of India."
          )

Options = (( "a) New Delhi" , "b) Mumbai" , "c) Nagpur" , "d) Chennai"),
           ( "a) 21" , "b) 28" , "c) 29" , "d) 30"),
           ( "a) Pune", "b) Indore", "c) Mumbai", "d) Assam"),
           ( "a) 7", "b) 9", "c) 6", "d)8"),
           ( "a) Mercator", "b) Colombus", "c) Ibt Batuta", "d) Vasco the Gama"),
           ( "a) Peacock", "b) Parrot", "c) Hummingbird", "d) Eagle"),
           ( "a) Lion", "b) Cheetah", "c) Tiger", "d) Elephant"),
           ( "a) Hockey", "b) cricket", "c) footboll", "d) Kabaddi"),
           ( "a) Lion", "b) Cheetah", "c) Tiger", "d) Elephant")
            )

Answers = ("a","b","b","d","d","a","c","a","d")
Guesses=[]
score=int()
Question_no = 0


for question in Questions:
    print("----------------------")
    print(question)
    for option in Options[Question_no]:
        print(option)

    guess = input("Enter (a, b, c, d): ").lower()
    Guesses.append(guess)
    if guess == Answers[Question_no]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{Answers[Question_no]} is the correct answer")
    Question_no += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in Answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in Guesses:
    print(guess, end=" ")
print()

score = int(score / len(Questions) * 100)
print(f"Your score is: {score}%")