def absval(a, b):
    diff = a - b
    if diff < 0:
        diff = -diff
    return diff

class Job:

    fields = ['agriculture/food/nautral resources',
              'business/management/administration',
              'communications/information systems',
              'engineering/manufacturing/technology',
              'health science technology',
              'human services',
              'arts/literature']

    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return self.name + '\n' + self.fields[self.field]

class Fig:

    genders = ["cis woman", " cis man", "non-binary", "agender", "trans man", "trans woman"]
    race = ["asian", "native american", "black", "white", "mixed"]
    sexualities = ["ace", "demisexual", "gay", "lesbian", "bi", "pan", "straight", "queer"]
    romas = ["gay", "lesbian", "bi", "pan", "straight", "queer", "aro"]
    countries = ["United States", "the UK", "Mexico", "South Africa", "Greece", "Rome", "China", "Frace", "Germany"]

    figures = []

    def __init__(self, f=None, l=None, r=None, s=None, g=None, b=[0,0,0], d = [0,0,0], c = "United States", ff = None, i = None, roma = None, j = Job('person',0)):
        # g, s, r are stored as indices
        self.fname = f
        self.lname = l
        self.race = r
        self.sexuality = s
        self.gender = g
        self.job = j
        self.birthdate = b # [year, month, day]
        self.deathdate = d # [year, month, day]
        self.country = c
        self.ff = ff
        self.image = i
        self.bio = ""

        # if self.sexuality == 0 or self.sexuality == 1:
        #     self.roma = self.romas[roma]
        # else:
        #     self.roma = self.sexuality


        self.figures.append(self)

    def __str__(self):
        letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
        onlyLetters = ''
        both =  self.fname + self.lname
        for char in both:
            if letters.find(char) != -1:
                onlyLetters += char
        return onlyLetters

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def getFigure(s):
        for f in Fig.figures:
            if f.__str__() == s:
                return f

    def set_race(self, race):
        self.race = race

    def set_sexuality(self, sexuality):
        self.sexuality = sexuality

    def set_gender(self, gender):
        self.gender = gender

    def set_birthdate(self, yr, mnth, day):
        self.birthdate[0] = yr
        self.birthdate[1] = mnth
        self.birthdate[2] = day

    def set_deathdate(self, yr, mnth, day):
        self.birthdate[0] = yr
        self.birthdate[1] = mnth
        self.birthdate[2] = day

    def setBio(self, bio):
        self.bio = bio

    def compare_to(self, other):
        sum = 0
        if self.race == other.race:
            smallest = 0
            if len(self.race) > len(other.race):
                smallest = len(other.race)
            else:
                smallest = len(self.race)

            for r in self.race:
                if self.race in other.race:
                    sum += 1/smallest
        if self.sexuality == other.sexuality:
            sum += 1
        if self.gender == other.gender:
            sum += 1
        if self.job.field == other.job.field:
            sum += 1
        if absval(self.birthdate[0], other.birthdate[0]) < 20:
            sum += 1
        if self.country == other.country:
            sum += 1
        return sum

    def similar_to(self, amt=5):
        figs = [];
        for i in range(amt):
            figs.append([-1])
        for f in self.figures:
            similarity = self.compare_to(f)
            added = False
            for i in range(amt):
                if self != f and similarity > figs[i][0]:
                    figs.insert(i, [similarity,f])
                    added = True
                    break;
        return figs[0:amt]

    def filter(races=None, rAO=0, sexualities=None, sAO=0, genders=None, gAO=0, bDate=None, minMax=None, countries=None, cAO=0, sort=None):
        for f in Fig.figures:
            if races != None:
                r = fits_filter(f.race, races, rAO)
            if sexualities != None:
                s = fits_filter([f.sexuality], sexualities, sAO)
            if genders != None:
                g = fits_filter([f.gender], genders, gAO)
            if bDate != None:
                yr = f.birthdate[0]
                b = (yr >= minMax[0] and yr <= minMAx[1])
            if countries != None:
                c = fits_filter([f.country], countries, cAO)
            return r and s and g and b and c

    # def search(in):
    #     results = []
    #     for f in Fig.figures:
    #         sum = 0
    #         for char in in:
    #             if char in f:
    #                 sum += 1;
    #         if sum > char * 0.75:
    #             results.append(f);
    #     return results

    def fits_filter(figList, l, AO):
        if AO == 0:
            for i in l:
                if not i in figList:
                    return False
            return True
        else:
            for i in l:
                if i in figList:
                    return True
            return False
