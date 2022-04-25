from datetime import datetime
import numpy as np
import random

random.seed(datetime.now())

class Plant:
    def __init__(self, axiom, rulesP, angle, iter, child=False):
        self.axiom = axiom
        self.sentence = axiom
        self.rules = rulesP
        self.angle = angle
        self.iters = iter
        self.distance = 4

        if child:
            # making child a slightly smaller
            self.distance /= 1+random.random()

        # Making color random of leafs (if leaf symbol is in rules)
        rgb = np.random.choice(range(256), size=3)
        self.colorRGB = rgb
        self.colorHex = '#%02x%02x%02x' % tuple(rgb)

    def iteration(self):
        startingSentence = ""
        self.rules = replaceRules(self.rules)

        for ch in self.sentence:
            if ch in self.rules.keys():
                randomisedKeys = random.choice(self.rules[ch])
                startingSentence += randomisedKeys
            else:
                startingSentence += ch
        self.sentence = startingSentence

    # Develop the plant with N iterations
    def grow(self):
        for x in range(0, self.iters):
            self.iteration()

def replaceRules(rules):
    ruleF = rules['F'][0]
    r = ruleF
    del rules['F']

    for ch in r:
        for eachKey in rules.keys():
            if ch == eachKey:
                random.shuffle(rules[eachKey])
                ruleF = ruleF.replace(ch, rules[eachKey][0])

    toReturn = {'F':[ruleF]}
    return toReturn
