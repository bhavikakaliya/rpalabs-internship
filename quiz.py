import time

# main class for quiz
class quiz:
    # constructor
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # method to calculate score
    def checkAnswer(self, correct):
        while(True):
            x = input("\nEnter your answer or 'pass': ")

            if x.isnumeric():
                if correct == int(x):
                    print("Correct answer!\n")
                    self.score += 10
                    break

                elif int(x) not in [1, 2, 3, 4]:
                    print("Please enter a valid choice (1, 2, 3, 4) or 'pass'.")

                else:
                    print("Wrong answer! option", correct, "is the correct answer.\n")
                    self.score -= 5
                    break

            else:
                if x.lower() == "pass":
                    print("Question skipped.\n")
                    break
                else:
                    print("Please enter a choice (1, 2, 3, 4) or 'pass'.")
        
    # 10 cycles of questions
    def questions(self):

        print("1. What is the largest country in the world?\n1. China\n2. Russia\n3. Canada\n4. India")
        self.checkAnswer(2)

        print("2. What is the smallest planet in our solar system?\n1. Mercury\n2. Mars\n3. Venus\n4. Pluto")
        self.checkAnswer(1)
    
        print("3. How many permanent teeth does a dog have?\n1. 50\n2. 40\n3. 42\n4. 45")
        self.checkAnswer(3)
    
        print("4. From what grain is the Japanese spirit Sake made?\n1. Oats\n2. Wheat\n3. Rice\n4. Barley")
        self.checkAnswer(3)

        print("5. What colour are most buses in London?\n1. Blue\n2. Red\n3. White\n4. Yellow")
        self.checkAnswer(2)
    
        print("6. Where is the smallest bone in the human body located?\n1. Ear\n2. Nose\n3. Hand\n4. Feet")
        self.checkAnswer(1)
    
        print("7. Sun rises in which direction?\n1. North\n2. South\n3. East\n4. West")
        self.checkAnswer(3)

        print("8. What is the 4th letter of the Greek alphabet?\n1. Delta\n2. Gamma\n3. Zeta\n4. Theta")
        self.checkAnswer(1)

        print("9. What country has the highest life expectancy?\n1. Canada\n2. UK\n3. Norway\n4. Hong Kong")
        self.checkAnswer(4)
    
        print("10. What is the highest number in sudoku?\n1. 6\n2. 8\n3. 7\n4. 9")
        self.checkAnswer(4)

        return self.score

# main menu method
def main():
    # welcome
    print("Hello! This is a very simple 10 mcqs quiz.\nAll you have to do is enter the choice number or 'pass' to skip the question.\n+10 for every correct answer, -5 for every wrong answer and no point change for pass.")
    name = input("\nPlease enter your name to start the quiz: ")
    print()
    
    startTime = time.time()

    # starting the quiz class
    q = quiz(name, 0)
    score = str(q.questions())

    timeStamp = time.time()
    totalTime = timeStamp - startTime

    # contents of result file
    contents = ["\n", name, "'s Score: ", score, "/100\nStart Time: ", time.ctime(startTime), "\nEnd Time: ", 
               time.ctime(timeStamp), "\nTotal Time: ", str(int(totalTime)), " seconds", "\nTimeStamp: ", str(timeStamp), "\n"]

    # adding contents to result file
    score = open("score.txt", "a")
    score.writelines(contents)
    score.close()

    # exit statement
    print("Quiz has ended. Please open the file named 'score' to check your results!")

    # printing result if needed
    x = input("Do you want to print your result? y/n: ")

    if x.lower() == "y":
        print(''.join(contents))
    print("Program end.")

main()
    



        