def new_game():

    print("\nWelcome to a Trivia Game! (With a huge Metallica emphasis)\n")

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "When was metallica formed?: ": "C",
 "What was metallica's first album titled?: ": "C",
 "What song caused a meltdown in the Metal scene due to its use of Acoustic guitars?: ": "C",
 "What company did Lars file a lawsuit against in 2000?: ": "D",
 "What is Kirk, the guitarist's, last name?: " : "C",
 "Why was St. Anger panned by, pretty much, everybody?: ": "D",
 "Who was Metallica's original guitarist?: ": "A",
 "What band was formed as a result of a major fallout between former guitarist Dave Mustane and Metallica?: ": "B",
 "Who did Metallica collaborate with in early 2010's?: ": "B",
 "The creator of this trivia game has a favorite metallica album, what is it? ": "A"
}

options = [["A. 1983", "B. 1982", "C. 1981", "D. 1980"],
          ["A. Metalacolypse", "B. Master of Puppets", "C. Kill em' All", "D. Peace Sels"],
          ["A. Metal Militia", "B. Fuel", "C. Fade To Black", "D. Bleeding Me"],
          ["A. Spotify", "B. Apple Music", "C. Limewire", "D. Napster"],
          ["A. Hamlet", "B. Ham", "C. Hammett", "D. Hammet"],
          ["A. Snare Drums." "B. No solo's","C. Band turmoil", "D. Both A & B"],
          ["A. Dave Mustane", "B. Kirk Hammett", "C. Zakk Wylde", "D. Jimmy Paige"],
          ["A. Iron Maiden", "B. Megadeth", "C. Anthrax", "D. Trivium"],
          ["A. Ozzy", "B. Lou Reed", "C. Jimmy Buffett", "D. Sum-41"],
          ["A. ...And Justice for all", "B. The Black Album", "C. St. Anger", "D. Garage Inc."]]

new_game()

while play_again():
    new_game()

print("Thanks for playing. ")
