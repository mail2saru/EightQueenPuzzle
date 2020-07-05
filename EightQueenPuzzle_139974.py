import random

class QueensEight:

    def __init__(self,size):
        self.pos = []
        self.score = 0
        self.queencount = range(size)
        for i in self.queencount:
            self.pos.append(random.randint(0,7))

    def calcscore(self):
        pos_rdiag = []
        pos_ldiag = []

        for i in self.queencount:
            x = i
            y = self.pos[i]
            rdiag = x + y
            ldiag = x - y
            pos_rdiag.append(rdiag)
            pos_ldiag.append(ldiag)
        pos_set = set(self.pos)
        rdiag_set = set(pos_rdiag)
        ldiag_set = set(pos_ldiag)

        self.score = len(pos_set) + len(rdiag_set) + len(ldiag_set)


class QueenEPopulation:

    def initpopln(self,popln,qsize):
        self.queenpopuln = []
        self.toppopln = 0
        self.top2ndpopln = 0
        self.max_score = 0
        self.poplncount = range(popln)
        for i in self.poplncount:
            self.queenpopuln.append(QueensEight(qsize))

    def scorepopln(self):
        for i in self.poplncount:
            self.queenpopuln[i].calcscore()

    def gettoppopln(self):
        for i in self.poplncount:
            if self.max_score < self.queenpopuln[i].score:
                self.max_score = self.queenpopuln[i].score
                self.top2ndpopln = self.toppopln
                self.toppopln = i

    def crossoverpopln(self):
        crosspoint = random.randint(0,7)
        temp = self.queenpopuln[self.toppopln].pos[crosspoint]
        self.queenpopuln[self.toppopln].pos[crosspoint] = self.queenpopuln[self.top2ndpopln].pos[crosspoint]
        self.queenpopuln[self.top2ndpopln].pos[crosspoint] = temp

    def mutatepopln(self):
        for i in self.poplncount:
            mutatpoint = random.randint(0,10)
            if mutatpoint < 8:
                self.queenpopuln[i].pos[mutatpoint] = random.randint(0,7)


popln_size = 10
queen_count = 8

queenpopulnobj = QueenEPopulation()

""" Generate initial population"""
queenpopulnobj.initpopln(popln_size,queen_count)

"""Score Population"""
queenpopulnobj.scorepopln()

""" Get the top two population"""
queenpopulnobj.gettoppopln()

while queenpopulnobj.max_score < 24:

    """Perfrom Cross on top two population"""
    queenpopulnobj.crossoverpopln()

    """Perfom mutation on  population at random position"""
    queenpopulnobj.mutatepopln()

    """Score Population"""
    queenpopulnobj.scorepopln()

    """ Get the top two population"""
    queenpopulnobj.gettoppopln()

    print(queenpopulnobj.max_score)

""" to print by column number
for i in range(queen_count):
    print(queenpopulnobj.queenpopuln[queenpopulnobj.toppopln].pos[i])
"""

""" to print by row number """

for i in range(queen_count):
    print(queenpopulnobj.queenpopuln[queenpopulnobj.toppopln].pos.index(i))













