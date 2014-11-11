# Defines Existence related classes
from interaction import Experiment, Result, Interaction, InteractionV


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
        self.boredom_level = 4
        self.mood = ""
        self.selfSatisfactionCounter = 0

        e1 = Experiment(L_E1)
        self.experiences[L_E1] = e1
        self.experiences[L_E2] = Experiment(L_E2)
        self.prevExp = e1
        
    def step(self):
        exp = self.prevExp
        if self.mood == "BORED":
            exp = self.choose_different_experience(exp)
            self.selfSatisfactionCounter = 0

        anticipated_result = self.predict(exp)
        result = self.return_result010(exp)
        #print("Anticipated result", anticipatedResult)
        #print("Result", result)

        self.create_primitive_interaction(exp, result)

        if result == anticipated_result:
            self.mood = "SELF_SATISFIED"
            self.selfSatisfactionCounter += 1
        else:
            self.mood = "FRUSTRATED"
            self.selfSatisfactionCounter = 0

        if self.selfSatisfactionCounter >= self.boredom_level:
            self.mood = "BORED"

        self.prevExp = exp
        return exp.label + result.label + " " + self.mood

    def create_primitive_interaction(self, exp, res):
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

    def create_experience(self, label):
        """

        :param label: The label of an experiment
        :rtype: Experiment
        """
        if not label in self.experiences.keys():
            self.experiences[label] = Experiment(label)
        return self.experiences[label]

    def choose_different_experience(self, exp):
        """ Returns first experience different than the given.
        """
        ans = None
        #print(self.experiences)
        for e in self.experiences.values():
            if e != exp:
                ans = e
                break
        return ans

    def create_result(self, label):
        """

        :param label: The label of a result
        :rtype: Result
        """
        if not label in self.results.keys():
            self.results[label] = Result(label)
        return self.results[label]

    def return_result010(self, exp):
        if exp == self.create_experience(L_E1):
            return self.create_result(L_R1)
        else:
            return self.create_result(L_R2)


class ExistenceVS(ExistenceOfSatisfaction):

    """Implements valence as well as self-satisfaction
    """

    def __init__(self):
        super().__init__()
        self.experiences = {}
        self.results = {}
        self.interactions = {}
        self.boredomLevel = 4
        self.mood1 = ""
        self.mood2 = ""
        self.selfSatisfactionCounter = 0

        e1 = self.create_experience(L_E1)
        e2 = self.create_experience(L_E2)
        r1 = self.create_result(L_R1)
        r2 = self.create_result(L_R2)
        self.prevExp = e1

        self.primitive_interaction_with_valence(e1, r1, -1)
        self.primitive_interaction_with_valence(e1, r2, 1)
        self.primitive_interaction_with_valence(e2, r1, -1)
        self.primitive_interaction_with_valence(e2, r2, 1)
        
    def step(self):
        exp = self.prevExp
        if self.mood2 == "PAINED" or self.mood1 == "BORED":
            exp = self.choose_different_experience(exp)
            self.selfSatisfactionCounter = 0

        anticipated_result = self.predict(exp)
        result = self.return_result010(exp)
        #print("Anticipated result", anticipatedResult)
        #print("Result", result)

        enacted_interaction = self.get_primitive_interaction(exp, result)

        if enacted_interaction.valence >= 0:
            self.mood2 = "PLEASED"
        else:
            self.mood2 = "PAINED"
        
        if result == anticipated_result:
            self.mood1 = "SELF_SATISFIED"
            self.selfSatisfactionCounter += 1
        else:
            self.mood1 = "FRUSTRATED"
            self.selfSatisfactionCounter = 0

        if self.selfSatisfactionCounter >= self.boredomLevel:
            self.mood1 = "BORED"

        self.prevExp = exp
        return exp.label + result.label + " " + self.mood1 + ", " + self.mood2

    def primitive_interaction_with_valence(self, exp, res, val):
        """

        :rtype : InteractionV
        """
        inter = InteractionV(exp, res, val)
        self.interactions[inter.label] = inter
        return inter

    def get_primitive_interaction(self, exp, res):
        return self.interactions[exp.label + res.label]
