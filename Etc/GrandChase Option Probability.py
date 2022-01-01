import random

options = ["ATK", "DEF", "VIT", "HP", "MP", "LVL", "SATK", "SDEF", "EXP", "CRIT RATE", "CRIT DAMAGE"]

rare = 2
epic = 3
unique = 4
trial = 1000000

ATK, DEF, VIT, HP, MP, LVL, SATK, SDEF, EXP, CRIT_RATE, CRIT_DAMAGE = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
공치치 = 0
필치치 = 0
공필치치 = 0
치치 = 0

for x in range(trial):
    newlist = options.copy()

    for y in range(unique):
        s = newlist.pop(random.randrange(0, len(newlist)))
        if (s == options[0]):
            ATK += 1
        elif (s == options[1]):
            DEF += 1
        elif (s == options[2]):
            VIT += 1
        elif (s == options[3]):
            HP += 1
        elif (s == options[4]):
            MP += 1
        elif (s == options[5]):
            LVL += 1
        elif (s == options[6]):
            SATK += 1
        elif (s == options[7]):
            SDEF += 1
        elif (s == options[8]):
            EXP += 1
        elif (s == options[9]):
            CRIT_RATE += 1
        elif (s == options[10]):
            CRIT_DAMAGE += 1

    if CRIT_RATE == 1 and CRIT_DAMAGE == 1:
        if ATK == 1 and SATK == 1:
            공필치치 += 1
        elif SATK == 1:
            필치치 += 1
        elif ATK == 1:
            공치치 += 1
        else:
            치치 += 1

    ATK, DEF, VIT, HP, MP, LVL, SATK, SDEF, EXP, CRIT_RATE, CRIT_DAMAGE = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


print("---- Total of {0} tries ----".format(trial))
print("치치: {0}번 성공\t\t{1}%".format(치치, 치치/trial*100))
print("공치치: {0}번 성공\t\t{1}%".format(공치치, 공치치/trial*100))
print("필치치: {0}번 성공\t\t{1}%".format(필치치, 필치치/trial*100))
print("공필치치: {0}번 성공\t\t{1}%".format(공필치치, 공필치치/trial*100))
# print("ATK: \t\t {0}\nDEF: \t\t {1}\nVIT: \t\t {2}\nHP: \t\t {3}\nMP: \t\t {4}\nLVL: \t\t {5}\nSATK: \t\t {6}\nSDEF: \t\t {7}\nEXP: \t\t {8}\nCRIT_RATE: \t {9}\nCRIT_DAMAGE: \t {10}".format(ATK, DEF, VIT, HP, MP, LVL, SATK, SDEF, EXP, CRIT_RATE, CRIT_DAMAGE))
