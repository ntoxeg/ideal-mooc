class Experiment(object):
    def __init__(self, _label):
        self.label = _label

    def __equals__(self, other):
        return self.label == other.label

class Result(object):
    def __init__(self, _label):
        self.label = _label

class Interaction(object):
    def __init__(self, _exp, _res):
        self.label = _exp.label + _res.label
        self.experiment = _exp
        self.result = _res

    def __repr__(self):
        return self.label
