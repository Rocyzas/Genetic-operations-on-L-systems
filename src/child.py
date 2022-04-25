import random
from plant import Plant

def mergeColors(colorRGBA1, colorRGBA2):
    red   = (colorRGBA1[0] + colorRGBA2[0]) / 2
    green = (colorRGBA1[1] + colorRGBA2[1]) / 2
    blue  = (colorRGBA1[2] + colorRGBA2[2]) / 2
    return '#%02x%02x%02x' % tuple([int(red), int(green), int(blue)])

def makeChild(father, mother):
    rules = {}
    for k in father.rules.keys():
       rules[k] = father.rules[k]

    for k in mother.rules.keys():
        if (not rules.get(k)):
            rules[k] = mother.rules[k]
        else:
            rules[k] = rules[k] + mother.rules[k]

    # taking all rules from mother and father
    for k in rules.keys():
        # shuffling them
        random.shuffle(rules[k])
        # for each key getting one random number of rules
        numberRules = random.randint(0, len(rules[k]))
        if numberRules!=0:
            rules[k] = rules[k][:numberRules]

    axiomChild = random.choice([father.axiom, mother.axiom])
    childAngle = random.randint(min(father.angle, mother.angle), max(father.angle, mother.angle))
    childIter = min(father.iters, mother.iters)

    child = Plant(axiomChild,rules, childAngle, childIter, child=True)
    child.colorHex = mergeColors(father.colorRGB, mother.colorRGB)
    return child
