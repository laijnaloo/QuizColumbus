__author__ = 'Lina Andersson'
class Question():
    def __init__(self, question, answer1, answer2, answer3, answer4, rightAnswerIndex, image):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.rightAnswerIndex = rightAnswerIndex
        self.image = image

    def getRightIndex(self):
        return self.rightAnswerIndex

    def getAnswer1(self):
        return self.answer1

    def getAnswer2(self):
        return self.answer2

    def getAnswer3(self):
        return self.answer3

    def getAnswer4(self):
        return self.answer4

    def getImage(self):
        return self.image

class Status():
    def __init__(self):
        self.gamePoints = 0
        self.userAnswers = []
        self.numberOfQuestions = 10

    def setGamePoints(self, newPoint):
        numberPoints = int(newPoint)
        self.gamePoints += numberPoints

    def getGamePoints(self):
        return int(self.gamePoints)

    def addToUserAnswers(self, newElement):
        self.userAnswers.append(newElement)

    def getUserAnswers(self):
        return self.userAnswers

    def getSpecificUserAnswer(self, index):
        return self.userAnswers[index]

    def setNumberOfQuestions(self, newQuestion):
        intNumber = int(newQuestion)
        self.numberOfQuestions -= intNumber

    def getNumberOfQuestions(self):
        return self.numberOfQuestions

    def resetGamePoints(self):
        self.gamePoints = 0

    def resetUserAnswers(self):
        self.userAnswers = []

    def resetNumberOfQuestions(self):
        self.numberOfQuestions = 10


