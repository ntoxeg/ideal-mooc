# Defines Existence related classes
from interaction import Experiment, Result, Interaction

class Existence(object):
    def step(self):
        pass

L_E1 = "e1"
L_E2 = "e2"
L_R1 = "r1"
L_R2 = "r2"
MOODS = ["SELF_SATISFIED", "FRUSTRATED", "BORED", "PAINED", "PLEASED"]
class ExistenceOfSatisfaction(Existence):
    def __init__(self):
        self.experiences = {}
        self.results = {}
        self.interactions = {}
        self.boredomeLevel = 4
        self.mood = ""
        self.selfSatisfactionCounter = 0

        e1 = Experiment(L_E1)
        self.experiences[L_E1] = e1
        self.experiences[L_E2] = Experiment(L_E2)
        self.prevExp = e1
        
    def step(self):
        exp = self.prevExp
        if self.mood == "BORED":
            exp = self.chooseDifferentExperience(exp)
            self.selfSatisfactionCounter = 0

        anticipatedResult = self.predict(exp)
        result = self.returnResult1(exp)
        #print("Anticipated result", anticipatedResult)
        #print("Result", result)

        self.createPrimitiveInteraction(exp, result)

        if result == anticipatedResult:
            self.mood = "SELF_SATISFIED"
            self.selfSatisfactionCounter += 1
        else:
            self.mood = "FRUSTRATED"
            self.selfSatisfactionCounter = 0

        if self.selfSatisfactionCounter >= self.boredomeLevel:
            self.mood = "BORED"

        self.prevExp = exp
        return exp.label + result.label + " " + self.mood

    def createPrimitiveInteraction(self, exp, res):
        inter = Interaction(exp, res)
        self.interactions[inter.label] = inter
        return inter

    def predict(self, exp):
        inter = None
        result = None

        #print(self.interactions)
        for i in self.interactions.values():
            if i.experiment == exp:
                inter = i

        if inter:
            result = inter.result

        return result

    def createExperience(self, label):
        if not label in self.experiences.keys():
            self.experiences[label] = Experiment(label)
        return self.experiences[label]

    def chooseDifferentExperience(self, exp):
        """ Returns first experience different than the given.
        """
        ans = None
        #print(self.experiences)
        for e in self.experiences.values():
            if e != exp:
                ans = e
                break
        return ans

    def createResult(self, label):
        if not label in self.results.keys():
            self.results[label] = Result(label)
        return self.results[label]

    def returnResult1(self, exp):
        if exp == self.createExperience(L_E1):
            return self.createResult(L_R1)
        else:
            return self.createResult(L_R2)
