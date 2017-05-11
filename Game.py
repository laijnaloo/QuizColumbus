__author__ = 'Lina Andersson'
#Lina Andersson
#Inlamningsuppgift
#Multimediaprogrammering i Python
#Python 3
#Windows

from tkinter import*
from GameStatus import Question, Status
from GameGui import GUI, GameButton
from GameSound import Sound
from random import *

class Game():
    def __init__(self):
        self.gui = GUI()

        self.gui.setTitel("Quiz Columbus")
        self.counter = 0
        self.listOfQuestionsIndex = [0,1,2,3,4,5,6,7,8,9]
        self.questionNumberIndex = 1
        self.answer1 = None
        self.question = None
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None
        self.questionCounter = None
        self.readInQuestions()
        self.status = Status()

        self.createStartPage()
        mainloop()

    def createStartPage(self):
        #Create and place start logo
        self.startLogo = GameButton("logo", self.gui)
        self.startLogo.createLabel(self.gui.root, 400, 283, 0, 126)

        #Create and place start button
        self.startButton = GameButton("startButton", self.gui)
        self.startButton.createLabel(self.gui.root, 400, 100, 0, 350, lambda x: self.cleanStartPage())

        #Create and place question button
        self.questionButton = GameButton("questionButton", self.gui)
        self.questionButton.createLabel(self.gui.root, 400, 78, 0, 0, lambda x: self.createQuestionPage())

    def createQuestionPage(self):
        #Remove objects from start page to make place for new items on question page
        self.startLogo.destroy()
        self.startButton.destroy()
        self.questionButton.destroy()

        #Create and place background
        self.questionPage = GameButton("questionPageBackground", self.gui)
        self.questionPage.createLabel(self.gui.root, 400, 600 , 0, 0)

        #Create and place back button
        self.backButton = GameButton("backToStartButton", self.gui)
        self.backButton.createLabel(self.gui.root, 250, 70, 80, 510, lambda x: self.cleanFromQuestionPage())

        self.headerText = self.gui.text(self.gui.root, "How do I play Quiz Columbus?", 30, 125, 12, "white", "#4fc8fc", 350, 30)
        self.discriptionText = self.gui.text(self.gui.root, "Quiz Columbus is a quiz were you in an easy and fast way "
                                                            "will learn more about Christofer Columbus and his voyages "
                                                            "to the new world. \n\nTo play the game you only need to push "
                                                            "the Start button and then the quiz begins. A question will "
                                                            "be shown on the top of the page and underneath it you can "
                                                            "choose between four possible answers. Only one of them is "
                                                            "right, so pick carefully."
                                                            "\n\nBut dont be to slow! You only have ten seconds to answer "
                                                            "the question and if you dont answer one point will be "
                                                            "taken from you. \n\nGet so many points as possible and compete "
                                                            "with yourself or your friends!", 30, 165, 10, "white", "#bbbbbb", 350, 260)

    def cleanFromQuestionPage(self):
        #Remove objects from previous page to be able to create a new one
        self.questionPage.destroy()
        self.backButton.destroy()
        self.createStartPage()
        self.headerText.destroy()
        self.discriptionText.destroy()


    def cleanStartPage(self):
        #Remove objects from previous page to be able to create a new one

        #Sound indicating that the game begins
        self.timeSound = Sound("startGame.WAV")
        self.timeSound.playSound()

        #Remove objects from start page to make place for new items on quiz page
        self.startLogo.destroy()
        self.startButton.destroy()
        self.questionButton.destroy()
        self.countDown()
        self.createQuizPage()

    def createQuizPage(self):
        #Create white box were all the possile answers are shown
        self.answerBox = GameButton("whiteBox", self.gui)
        self.answerBox.createLabel(self.gui.root, 400, 285, 0, 320)

        self.questionAndAnswer()

    def countDown(self):
        #Image showing the number of seconds the user have to answer a question
        self.numbersList = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

        if self.counter == 10:
            self.counter = 0
            self.gui.root.after(1000, self.countDown)
            self.checkUserAnswer(-1)
        elif self.counter == -1:
            #Stop counting secounds
            self.questionCounter.destroy()
        else:
            if self.questionCounter != None:
                self.questionCounter.destroy()
            self.questionCounter = GameButton(self.numbersList[int(self.counter)], self.gui)
            self.questionCounter.createLabel(self.gui.root, 400, 78, 0, 0)
            self.gui.root.after(1000, self.countDown)
            self.counter += 1

    def randomiseQuestion(self):
        #get a random question from the file
        return randint(0,len(self.questAndAnswer) - 1)

    def readInQuestions(self):
        #Read in question and answers from file to an 2d-list. In the list the question comes first,
        # then the answers followed by how many points the answers gives.
        self.questAndAnswer = []
        file = open("questionsAndAnswers.txt", "r")
        lines = file.readlines()

        self.infoArray = []
        for line in lines:
            self.questAndAnswer.append(line.split("\t"))

    def questionAndAnswer(self):
        #randomise question
        self.questNumber = self.randomiseQuestion()

        #read in answers, questions ect.
        questionArray = self.questAndAnswer[self.questNumber]
        self.questAndAnswer.remove(questionArray)
        self.quest = questionArray[0]
        self.answer1 = questionArray[1]
        self.answer2 = questionArray[2]
        self.answer3 = questionArray[3]
        self.answer4 = questionArray[4]
        self.rightAnswerIndex = questionArray[5]
        self.questionImage = questionArray[6]

        #make an instance of all the question related information
        self.questionInstance = Question(self.quest, self.answer1, self.answer2, self.answer3, self.answer4, self.rightAnswerIndex, self.questionImage)

        self.imageQuestion = GameButton(self.questionImage, self.gui)
        self.imageQuestion.createLabel(self.gui.root, 400, 204, 0, 80)

        self.question = self.gui.text(self.gui.root, str(self.quest), 30,
                                      275, 14, "#4fc8fc", "white", 350, 50)

        self.answer1 = self.gui.text(self.gui.root, str(self.answer1), 11,
                                     337, 14, "white", "#818181", 189, 115, lambda x: self.checkUserAnswer(1))

        self.answer2 = self.gui.text(self.gui.root, str(self.answer2), 200,
                                     337, 14, "white", "#818181", 189, 115, lambda x: self.checkUserAnswer(2))

        self.answer3 = self.gui.text(self.gui.root, str(self.answer3), 11,
                                      452, 14, "white", "#818181", 189, 115, lambda x: self.checkUserAnswer(3))

        self.answer4 = self.gui.text(self.gui.root, str(self.answer4), 200,
                                      452, 14, "white", "#818181", 189, 115, lambda x: self.checkUserAnswer(4))

        self.questionNumber = self.gui.text(self.gui.root, str(self.questionNumberIndex) + " of 10", 11,
                                      567, 12, "white", "#bebebe", 378, 23)
        self.questionNumberIndex += 1

    def checkUserAnswer(self, userAnswerIndex):
        self.status.setNumberOfQuestions(-1)

        #if the asnwer is right
        if int(userAnswerIndex) == int(self.questionInstance.getRightIndex()):
            self.yesSound = Sound("yes.WAV")
            self.yesSound.playSound()
            self.status.addToUserAnswers("right")
            self.status.setGamePoints(1)

            #changes background color depending on which button the user pressed
            if int(self.questionInstance.getRightIndex()) == 1:
                self.answer1.destroy()
                self.answer1 = self.gui.text(self.gui.root, self.questionInstance.getAnswer1(), 11,
                                     337, 12, "#d6fbd6", "#818181", 189, 115)
            elif int(self.questionInstance.getRightIndex()) == 2:
                self.answer2.destroy()
                self.answer2 = self.gui.text(self.gui.root, self.questionInstance.getAnswer2(), 200,
                                     337, 12, "#d6fbd6", "#818181", 189, 115)
            elif int(self.questionInstance.getRightIndex()) == 3:
                self.answer3.destroy()
                self.answer3 = self.gui.text(self.gui.root, self.questionInstance.getAnswer3(), 11,
                                      452, 12, "#d6fbd6", "#818181", 189, 115)
            else:
                self.answer4.destroy()
                self.answer4 = self.gui.text(self.gui.root, self.questionInstance.getAnswer4(), 200,
                                      452, 12, "#d6fbd6", "#818181", 189, 115)
        #if the user run out of time
        elif userAnswerIndex == -1:
            self.timeSound = Sound("time.WAV")
            self.timeSound.playSound()
            self.status.addToUserAnswers("time")
            self.status.setGamePoints(-1)

        #if the user answers is wrong
        else:
            self.yesSound = Sound("no.WAV")
            self.yesSound.playSound()
            self.status.addToUserAnswers("wrong")
            self.status.setGamePoints(-1)

            #changes background color depending on what the user choose
            if int(userAnswerIndex) == 1:
                self.answer1.destroy()
                self.answer1 = self.gui.text(self.gui.root, self.questionInstance.getAnswer1(), 11,
                                     337, 12, "#f9c8c8", "#818181", 189, 115)
            elif int(userAnswerIndex) == 2:
                self.answer2.destroy()
                self.answer2 = self.gui.text(self.gui.root, self.questionInstance.getAnswer2(), 200,
                                     337, 12, "#f9c8c8", "#818181", 189, 115)
            elif int(userAnswerIndex) == 3:
                self.answer3.destroy()
                self.answer3 = self.gui.text(self.gui.root, self.questionInstance.getAnswer3(), 11,
                                      452, 12, "#f9c8c8", "#818181", 189, 115)
            else:
                self.answer4.destroy()
                self.answer4 = self.gui.text(self.gui.root, self.questionInstance.getAnswer4(), 200,
                                      452, 12, "#f9c8c8", "#818181", 189, 115)
        self.gui.root.after(100, self.checkIfMoreQuestions)

    #keeps track of number of questions and if there is any more that the user should answer
    def checkIfMoreQuestions(self):
        if len(self.questAndAnswer) == 0:
            self.createResultPage()
        else:
            if self.answer1 != None:
                self.question.destroy()
                self.answer1.destroy()
                self.answer2.destroy()
                self.answer3.destroy()
                self.answer4.destroy()
                self.imageQuestion.destroy()

            self.counter = 0
            self.answerBox.destroy()
            self.questionNumber.destroy()
            self.createQuizPage()

    #cleans the window from previoud page and creates the result page
    def createResultPage(self):
        self.counter = -1
        self.questionCounter.destroy()
        self.answer1.destroy()
        self.answer2.destroy()
        self.answer3.destroy()
        self.answer4.destroy()
        self.question.destroy()
        self.imageQuestion.destroy()

        self.questionNumber.destroy()
        self.imageQuestion.destroy()
        self.answerBox.destroy()

        #Create elements for score page
        self.scoreBackground = GameButton("scoreBackground", self.gui)
        self.scoreBackground.createLabel(self.gui.root, 400, 600, 0, 0)

        self.scoreText = self.gui.text(self.gui.root, "Score", 160,
                                      20, 12, "white", "#bababa", 100, 50)

        self.userScores = self.gui.text(self.gui.root, str(self.status.getGamePoints()) + " points", 110,
                                      70, 24, "white", "#4fc8fc", 200, 40)

        self.HighScore = self.gui.text(self.gui.root, "Highscore: " + str(self.readInHighScore()) + " points",105,
                                      140, 12, "white", "#bababa", 200, 30)

        self.scoreDescription = GameButton("scoreDescription", self.gui)
        self.scoreDescription.createLabel(self.gui.root, 277, 25, 30, 200)

        self.oneToFour = GameButton("1to4", self.gui)
        self.oneToFour.createLabel(self.gui.root, 278, 11, 30, 240)

        self.fiveToEight = GameButton("5to8", self.gui)
        self.fiveToEight.createLabel(self.gui.root, 278, 11, 30, 320)

        self.nineToTen = GameButton("9to10", self.gui)
        self.nineToTen.createLabel(self.gui.root, 278, 11, 30, 400)

        #Circles showing the users answers
        #First row
        self.circle1 = GameButton(self.status.getSpecificUserAnswer(0), self.gui)
        self.circle1.createLabel(self.gui.root, 69, 72, 37, 230)

        self.circle2 = GameButton(self.status.getSpecificUserAnswer(1), self.gui)
        self.circle2.createLabel(self.gui.root, 69, 72, 130, 230)

        self.circle3 = GameButton(self.status.getSpecificUserAnswer(2), self.gui)
        self.circle3.createLabel(self.gui.root, 69, 72, 223, 230)

        self.circle4 = GameButton(self.status.getSpecificUserAnswer(3), self.gui)
        self.circle4.createLabel(self.gui.root, 69, 72, 316, 230)

        #second row
        self.circle5 = GameButton(self.status.getSpecificUserAnswer(4), self.gui)
        self.circle5.createLabel(self.gui.root, 69, 72, 37, 310)

        self.circle6 = GameButton(self.status.getSpecificUserAnswer(5), self.gui)
        self.circle6.createLabel(self.gui.root, 69, 72, 130, 310)

        self.circle7 = GameButton(self.status.getSpecificUserAnswer(6), self.gui)
        self.circle7.createLabel(self.gui.root, 69, 72, 223, 310)

        self.circle8 = GameButton(self.status.getSpecificUserAnswer(7), self.gui)
        self.circle8.createLabel(self.gui.root, 69, 72, 316, 310)

        #third row
        self.circle9 = GameButton(self.status.getSpecificUserAnswer(8), self.gui)
        self.circle9.createLabel(self.gui.root, 69, 72, 37, 390)

        self.circle10 = GameButton(self.status.getSpecificUserAnswer(9), self.gui)
        self.circle10.createLabel(self.gui.root, 69, 72, 130, 390)

        #Takes the user to start page again
        self.playAgain = GameButton("playAgain", self.gui)
        self.playAgain.createLabel(self.gui.root, 246, 40, 90, 500, lambda x: self.resetGame())

    def resetGame(self):

        #destroy score page
        self.playAgain.destroy()
        self.circle1.destroy()
        self.circle2.destroy()
        self.circle3.destroy()
        self.circle4.destroy()
        self.circle5.destroy()
        self.circle6.destroy()
        self.circle7.destroy()
        self.circle8.destroy()
        self.circle9.destroy()
        self.circle10.destroy()
        self.scoreBackground.destroy()
        self.scoreText.destroy()
        self.userScores.destroy()
        self.HighScore.destroy()
        self.scoreDescription.destroy()
        self.oneToFour.destroy()
        self.fiveToEight.destroy()
        self.nineToTen.destroy()

        #reset game status information
        self.counter = 0
        self.listOfQuestionsIndex = [0,1,2,3,4,5,6,7,8,9]
        self.questionNumberIndex = 1
        self.answer1 = None
        self.question = None
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.answer4 = None
        self.questionCounter = None

        self.status.resetGamePoints()
        self.status.resetNumberOfQuestions()
        self.status.resetUserAnswers()

        self.readInQuestions()
        self.status = Status()

        self.createStartPage()

    def readInHighScore(self):

        #Read in old highscore
        highScoreFile = open("highScore.txt", "r")
        highScoreInt = int(highScoreFile.read())

        if int(self.status.getGamePoints()) > highScoreInt:
            #Write in new highscore
            highScore = open('highScore.txt', 'w')
            highScore.write(str(self.status.getGamePoints()))
            highScore.close()

            #Get new highscore and return it
            highScoreFile = open("highScore.txt", "r")
            highScoreInt = int(highScoreFile.read())
            return highScoreInt
        else:
            #return old highscore
            return highScoreInt



def main():
    Game()

if __name__ == "__main__":
        main()