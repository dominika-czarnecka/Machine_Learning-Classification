from scipy.spatial.distance import cosine
import math
fs = open("C:\\Users\\Wojciech\\Desktop\glove.6B.100d.txt", 'r', encoding='utf8')


def TOEFLParser(filename):
    tf = open(filename, 'r', encoding='utf8')
    state = 0
    question_words = []
    possibilities_bag = []
    answers = []
    for line in tf:
        if len(line.split()) == 0:
            question_words.append(question_word)
            possibilities_bag.append(possibilities)
            state = 0
        elif len(line.split()) == 2:
            if state == 1:
                possibilities.append(line.split()[1])
            if state == 0:
                question_word = line.split()[1]
                possibilities = []
                state = 1
        else:
            if line.split()[3] == 'a':
                answers.append(1)
            if line.split()[3] == 'b':
                answers.append(2)
            if line.split()[3] == 'c':
                answers.append(3)
            if line.split()[3] == 'd':
                answers.append(4)

def cosine2(v1, v2):
    v1v2 = 0
    for i in range(100):
        v1v2 += v1[i] * v2[i]
    v1norm = 0
    for i in range(100):
            v1norm += v1[i] * v1[i]
    v1norm = math.sqrt(v1norm)
    v2norm = 0
    for i in range(100):
        v2norm += v2[i] * v2[i]
    v2norm = math.sqrt(v2norm)
    return v1v2/(v1norm*v2norm)

#model = {}
#i = 0
#for i,line in enumerate(fs):
  #  if i % 1000:
   #     print(i)
   # tokens = line.split()
   # vec = [0 for i in range(100)]
   # for i in range(100):
   #     vec[i] = float(tokens[i+1])
  #  model[tokens[0]] = vec

#king_vec = model["king"]
#queen_vec = model["queen"]
#man_vec = model["man"]
#woman_vec = model["woman"]

#print(cosine(king_vec, queen_vec))
#print(cosine(king_vec, man_vec))
#print(cosine(queen_vec, woman_vec))
#print(cosine(man_vec, woman_vec))

(question_words,possibilites_bag,answers) = TOEFLParser("C:\\Users\\Wojciech\\Desktop\\toefl.txt")
print(question_words)
print(possibilites_bag)
print(answers)