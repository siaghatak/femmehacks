from people import Fig

from flask import Flask
from flask import url_for
from flask import render_template

import random

apollo = '''
<h2>Apollo</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Apollo-WaltersArt.jpg"
alt = "Image of Apollo, the Greek and Roman god" width = "400" height =" 550">
<p>While Apollo is but a myth, his presence as a queer figure of great influence is
notable. He was involved romantically and sexually with a large number of men, and
thus is considered a patron of homosexual unions, often being worshipped
for the sake of blessing such relationships. One notable gay relationship
Apollo was involved in was with Admetus of Pherae, a noble left in charge
of his punishment after he killed Delphyne. There are variations to this myth,
with some claiming that Apollo abandoned his godly pride for the sake of this
lover of his, choosing to live as his servant in the mortal plane. However,
regardless of the version being referenced, Apollo and Admetus fostered
a wholesome and loving relationship, starkly contrasting an abundance of
romantic involvements within Greek Mythology. Admetus later grew to set his
sights on a woman named Alcestis, so Apollo, out of love, helped him
pursue her. Afterwards, when Admetus accidentally snubbed Artemis, she sent
snakes after him, and Apollo returned to save his ex-lover from demise.</p>'''

#first, last, race,sex,gen,bday,deathday,country
ahf1 = Fig("", "Apollo", [3], 7, 1, [3000], [3000], 4)
ahf1.setBio(apollo)

Achilles = '''
<h2>Achilles</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/b/ba/Achilles_fighting_against_Memnon_Leiden_Rijksmuseum_voor_Oudheden.jpg"
alt "Image of the Trojan hero Achilles" width = "400" height = "500" class= 'hfi'>
<p>There is  a large amount of debate over the nature of Achilles' relationship
with Patroclus, a fellow man: some consider it to be platonic, while others deem it
romantic: that said, not only is the gay interpretation of it absolutely valid,
it is based in cultural depictions. Ancient Greek literature portrays them as
lovers, even in works by famous authors such as Plato. In the Iliad, the
tale from which both men originated, Homer (the author) leaves the nature of their
relationship ambiguous--nonetheless, they have become a key component of LGBTQ+
history. Achilles treats Patroclus gently in the Iliad, starkly contrasting
his demeanor towards nearly everyone else in the poem. Many modern works,
including <i>The Song of Achilles,</i> are based on the gay undertones
of such a dynamic.</p>
'''
ahf2 = Fig("", "Achilles",[3], 7, 1, [3000], [3000] , 4)
ahf2.setBio(Achilles)

ahf3 = Fig("", "Sappho", [3], 7, 0, [3000], [3000] , 4)
Sappho = '''
<h2>Sappho</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/6/6e/Fresco_showing_a_woman_so-called_Sappho_holding_writing_implements%2C_from_Pompeii%2C_Naples_National_Archaeological_Museum_%2814842101892%29_restored.jpg"
alt = "Image of Sappho, the Greek Poet" width = "400" height = "400" class= 'hfi'>
'''
ahf3.setBio(Sappho)

ahf4 = Fig("", "Emperor Ai",[0], 7, 1, [-27], [-1] , 6)
Ai = '''<h2>Emperor Ai</h2>
<img src = "https://cdn2.picryl.com/photo/1650/12/31/chinese-the-twenty-four-ministers-of-the-tang-tang-dynasty-emperor-taizong-0106d4-1024.jpg"
alt = "Image of the Chinese Emperor Ai" width = '600' height = '300' class= 'hfi'>
'''
ahf4.setBio(Ai)

ahf5 = Fig("", "Emperor Hadrian",[3], 2, 1, [117], [138] , 5)
Hadrian = '''<h2>Hadrian</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/9/9c/Hadrian_Greek_BM_Sc1381.jpg"
alt = "Image of Roman Emperor Hadrian" width = '400' height = '600' class= 'hfi'>
'''
ahf5.setBio(Hadrian)
ahf6 = Fig("", "Emperess Elagabalus",[0], 7, 1, [-27], [-1] , 6)
El = '''<h2>Elagabalus</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Bust_of_a_youth_from_the_time_of_Elagabalus%2C_3rd_cent._A.D._%28NAM_2350_1-4-2020%29.jpg"
alt = "Image of Roman Empress/Emperor Elagabalus" width = '350' height = '500' class= 'hfi'>
<p>An Empress/Emperor with a complicated history, they are reported to have
  been romantically involved with women and men alike, though the degree to which
  is frequently debatable--much of what we know about them is derived from the
  writings of Cassius Dio, a historian with a likely bias against them.
  One of the men Dio reports Elagabalus to have dated, a former slave known as
  Hierocles, is generally regarded as one of the primary reasons for
  opposition to the throne. Elagabalus liked it when he (Hierocles) called
  them his queen, mistress, and wife, and once they corrected someone for referring
  to them as a lord instead of a lady. In fact, they are (supposedly) one of the
  first people to ever ask for sex reassignment via surgery--some sources even
  suggest that they offered half of the entire empire to any who could provide
  them with a vagina. Of course, all of this is possibly exaggerated by Dio, since
  he is the primary source of information about Elagabalus' personal life--but that
  is only a possibility, and applies to a significant amount of ancient history.</p>
'''
ahf6.setBio(El)

#first, last, race,sexu,gen,bday,deathday,country
ohf1 = Fig("Emily", "Bronte", [3], 0, 0, [1818], [1848], 1,7)
eb = '''<h2>Emily Bronte</h2>
 <img src = "https://api.ndla.no/image-api/raw/emily_1.jpg" alt = "Image of the author Emily Bronte"
 width = '500' height = '250' class= 'hfi'>'''
ohf1.setBio(eb)

ohf2 = Fig("Karl", "Heinrich Ulrichs", [3], 7, 1, [1825], [1895], 8)
khu = '''<h2>Karl Heinrich Ulrichs</h2>
 <img src= "https://upload.wikimedia.org/wikipedia/commons/a/a9/Ulrichs-Gedenktafel_%28Burgdorf%29.jpg"
 alt = "Image of a plaque dedicated to Karl Heinrich Ulrichs" width = '600' height = '500' class= 'hfi'>
'''
ohf2.setBio(khu)

ohf3 = Fig("Oscar", "Wilde", [3], 7, 1, [1854], [1900], 1)
ow = '''<h2>Oscar Wilde</h2>
 <img src = "https://cdn.pixabay.com/photo/2016/01/27/23/06/oscar-wilde-1165561_1280.jpg"
 alt = "Image of the author Oscar Wilde" width = '350' height = ' 500' class= 'hfi'>
'''
ohf3.setBio(ow)

ohf4 = Fig("Emily", "Dickenson", [3], 7, 0, [1830], [1886], 0)
ed = '''<h2>Emily Dickinson</h2>
 <img src = "https://live.staticflickr.com/8123/8654989359_a605db393e_b.jpg"
 alt = "Image of the poet Emily Dickinson" width = '350' height = '450' class= 'hfi'>
'''
ohf4.setBio(ed)

ohf5 = Fig("Frida", "Kahlo", [5], 4, 0, [1907], [1954], 2)
fk = '''<h2>Frida Kahlo</h2>
<img src = "https://live.staticflickr.com/5177/5493700957_7c9d09f9c0.jpg"
alt = "Image of the painter Frida Kahlo" width = '350' height = '450' class= 'hfi'>
'''
ohf5.setBio(fk)

ohf6 = Fig("Eleanor", "Roosevelt", [3], 7, 0, [1884], [1962], 0)
er = '''<h2>Eleanor Roosevelt</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/0/04/Eleanor_Roosevelt_was_a_member_of_the_Women%27s_Trade_Union_League_and_in_1946_was_elected_head_of_United_Nations_Human_Rights_Commission._%285278986359%29.jpg"
alt = "Image of the activist and former first lady of the USA: Eleanor Roosevelt" width = '400' height = '500' class= 'hfi'>

'''
ohf6.setBio(er)

ohf7 = Fig("Virginia", "Woolf", [3], 4, 0, [1907], [1954], 2)
vw = '''<h2>Virginia Woolf</h2>
 <img src = "https://api.ndla.no/image-api/raw/syb79ac5.jpg"
 alt = "Image of the author Virginia Woolf" width = '375' height = '500' class= 'hfi'>
 <p>Married to Leonardo Woolf, this acclaimed author and feminist
   had affair with Vita Sackville-West,
   and her novel Orlando is believed to be her love letter to said lover.</p>
'''
ohf7.setBio(vw)

ohf8 = Fig("Nikola", "Tesla", [3], 0, 1, [1856], [1943], 2, 6)
nt = '''<h2>Nikola Tesla</h2>
 <img src = "https://cdn.pixabay.com/photo/2020/07/24/02/49/person-5432766_1280.png"
 alt = "Image of the inventor and engineer Nikola Tesla" width = '300' height = '400' class= 'hfi'>
'''
ohf8.setBio(nt)

# #first, last, race,sexu,gen,bday,deathday,country
mthf1 = Fig("Marsha", "Johnson", [2], 2, 4, [1945], [1992], 0)
mj = '''
<h2>Marsha P Johnson</h2>
<img src = "https://live.staticflickr.com/65535/50538004627_b6f0317c92_c.jpg"
alt = "Image of the activist and drag queen Marsha P Johnson" width = '500' height = '400' class= 'hfi'>
'''
mthf1.setBio(mj)

mthf2 = Fig("Sylvia", "Rivera", [5], 7, 2, [1951], [2002], 0)
sr = '''
<h2>Sylvia Rivera</h2>
<p>Sylvia Rivera was heavily involved with the Gay Liberation Front, heavily
  activating in favor of gay rights in the US, especially after the Stonewall riots.
  She was a drag queen, and is widely regarded as one of the most influential modern LGBTQ+ figures,
  along with Marsha P Johnson, one of her close friends that she worked with. They established STAR,
  the Street Transvestite Action Revolutionaries, together. The organization aimed to aid homeless youth,
  particularly those that were drag queens or identified as gay or trans.
  The motivation for this, aside from mere pure intent, likely derived from her own experiences with homelessness:
  due to her feminine expression, she was kicked out of the house at the age of eleven,
  and had to work as a prostitute at so young an age. Her name, Sylvia, was given
  to her by drag queens who took her in during this time.</p>'''
mthf2.setBio(sr)

mthf3 = Fig("Josephine", "Baker", [2], [2,4], 4, [1906], [1975], )
jb = '''<h2>Josephine Baker</h2>
<img src = "https://live.staticflickr.com/1682/26111522535_4ebcaebebe_b.jpg"
alt = "Image of the entertainer and actress Josephine Baker" width = '350' height = '500' class= 'hfi'>'''
mthf3.setBio(jb)

mthf5 = Fig("Alan", "Hart", [3], 6, 4, [1890], [1987], 0)
ah = '''
<h2>Alan L. Hart</h2>
<p>An intelligent physician, researcher, and writer, Hart was one of the first
  FTM transgender persons to undergo a hysterectomy: he lived the rest of his
  life in the US as a man. His parents were supportive throughout Alan’s youth
  and allowed him to dress and live as a man, enabling him to freely express and
  explore his gender. He attended Albany College and Stanford, receiving his
  Ph.D. from The University of Oregon. He is notable for his four novels, as well
  as his work at using radiology to detect tuberculosis. While there is some debate
  as to his identifying as transgender or transsexual, with some people instead
  referring to him as lesbian, many trans youth today might see themselves in him:
  he was frequently ostracized for his transition, thus forced to keep his previous
  life as a 'woman' secret to almost everyone he met. He had experiences with
  conversion therapy (due to his being labelled as a 'lesbian' in spite of his
  gender identity), and began hormone therapy when it became available immediately
  after World War II.</p>'''
mthf5.setBio(ah)

mthf6 = Fig("James", "Baldwin", [2], 2, 1, [1924],[1987], 0)
jb = '''
<h2>James Baldwin</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/f/f3/James_Baldwin_37_Allan_Warren_%28cropped%29.jpg"
alt = "Image of the author and activist James Baldwin" width = '300' height = '400' class= 'hfi'>
'''
mthf6.setBio(jb)

mthf7 = Fig("Alan", "Turing", [3], 2, 1, [1912],[1954], 1)
at = '''
<h2>Alan Turing</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/3/3a/Alan_Turing_Age_16_Colorized.jpg"
alt = "Image of the scientist and mathematician Alan Turning" width = '380' height = '500' class= 'hfi'>
'''
mthf7.setBio(at)

mthf8 = Fig("Sally", "Ride", [3], 3, 0, [1951], [2012], 0)
sr = '''<h2>Sally Ride</h2>
<img src = "https://cdn2.picryl.com/photo/1984/12/31/sally-ride-first-us-woman-in-space-1024.jpg"
alt = "Image of the physicist and astronaut Sally Ride" width = '380' height = '500' class= 'hfi'>
'''
mthf8.setBio(sr)

mthf9 = Fig("Hayley", "Kiyoko", [3, 0, 4], 3, 0, [1991], None, 0)
hk = '''
<h2>Hayley Kiyoko</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/e/ed/Hayley_Kiyoko_2018.png"
alt = "Image of the singer Hayley Kiyoko" width = '500' height = '400' class= 'hfi'>
'''
mthf9.setBio(hk)

mthf10 = Fig("Jamie", "Raines", [3], 4, 4, [1994], None, 1)
jr = '''
<h2>Jamie Raines</h2>
<p>Jamie Raines, also known online as Jammidodger, is a British Youtuber.
  He has over 907,000 subscribers on his youtube channel, where he posts a
  mixture of serious video essays, informational videos focused on education
  surrounding LGBTQ+ based issues, and funny meme-based videos.</p>
'''
mthf10.setBio(jr)

mthf11 = Fig("Micheal", "Dillon", [3], 6,  4, [1915], [1962], 1)
md = '''<h2>Michael Dillon</h2>
<p>Dillon was the first trans man to undergo phalloplasty or the surgical
  construction of a penis as well as receive testosterone therapy.
  He later studied to become a doctor and worked as a Naval doctor.
  After the media discovered that he was trans however, Dillon
  forced to flee to India where he lived out the rest of his days as a
  Buddhist monk.</p>'''
mthf11.setBio(md)

mthf11 = Fig("Bayard", "Rustin", [2], 2, 1, [1912], [198], 0)
br = '''<h2>Bayard Rustin</h2>
<img src = "https://freesvg.org/img/Bayard-Rustin.png"
alt = "Image of the activist Bayard Rustin" width = '400' height = '400' class= 'hfi'>
<p>MLK’s right hand man in the Civil Rights Movement, he helped to organize the
  1963 March on Washington, but due to his sexuality, was widely ignored
  for his contributions.</p>'''
mthf11.setBio(br)

mthf12 = Fig("Simon", "Nkoli", [2], 2, 1, [1957], [1998], 3)
sn = '''
<h2>Simon Nkoli</h2>
<img src = "https://upload.wikimedia.org/wikipedia/commons/8/8a/Simon_nkoli.png"
alt = "Image of the activist Simon Nkoli" width = '400' height = '500' class= 'hfi'>
<p> Simon Nkoli was a gay rights activist who was heavily involved in speaking out about
  AIDS in South Africa. He established the Saturday Group, which was the first official
  group for black gay men in Africa. At one point in his activism he was given the death
  penalty on accusations of treason, and during his time in prison he came out, setting a
  unique precedent and drastically changing public perception of gay rights. Later, after
  charges were dropped and he was set free, he founded GLOW (Gay and Lesbian Organisation of
  the Witwatersrand) and helped organize the very first pride parade in South Africa. At the
  height of the HIV epidemic, he openly admitted to being infected, and established a safe space
  for fellow HIV-positive men in Johannesburg. Sadly, the infection was what took his life.</p>
'''
mthf12.setBio(sn)

app = Flask(__name__)
Fig.similar_to(ohf6)

@app.route("/lgbtqhistory.html")
def home():
    final = ''
    final += "<a href=" + url_for("home") + ">Home<br></a>"
    final += "<a href=" + url_for("about") + ">About<br></a>"
    final += "<a href=" + url_for("resources") + ">Resources<br></a>"
    final += "<a href=" + url_for("terminology") + ">Terminology<br></a>"
    for f in Fig.figures:
        final += f.bio
        url = url_for('figurePage', figure = f.__str__())
        text = 'Go to ' + f.fname + ' ' + f.lname + "'s page"
        final += "<a href=" + url + ">" + text + "</br></a><br>"
    return final

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route('/resources.html')
def resources():
    return render_template('resources.html')

@app.route('/terminology.html')
def terminology():
    return render_template('terminology.html')

@app.route("/<figure>")
def figurePage(figure):
    final = ''
    final += "<a href=" + url_for("home") + ">Home<br></a>"
    final += "<a href=" + url_for("about") + ">About<br></a>"
    final += "<a href=" + url_for("resources") + ">Resources<br></a>"
    final += "<a href=" + url_for("terminology") + ">Terminology<br></a>"

    f = Fig.getFigure(figure)

    name = f.fname + " " + f.lname
    # heading = "<h1>" + name + "<h1>"
    bio = f.bio
    final += bio

    if f.gender != None:
        final += 'Gender: ' + Fig.genders[f.gender]
    if f.sexuality != None:
        final += '<br>Sexuality: ' + Fig.sexualities[f.sexuality]
    if f.race != None:
        final += '<br>Race(s): '
        for r in f.race:
            final += Fig.race[r]
    if f.country != None:
        final += '<br>Country: ' + Fig.countries[f.country]
    if f.birthdate != None:
        if (f.birthdate[0] > 2022):
            final += '<br>Ancient Times'
        elif (f.birthdate[0] < 0):
            final += '<br>Birthyear: ' + str(-f.birthdate[0]) + ' BCE'
        else:
            final += '<br>Birthyear: ' + str(f.birthdate[0])
    if f.deathdate != None:
        final += '<br>Death: unknown, still alive, or not filled yet'
    else:
        final += '<br>Death: ' + str(f.deathdate[0])

    recs = "<h2>Here are some similar people to " + name + ": <h2>"
    final += recs

    sim = f.similar_to()
    ppl = "<h3>"
    for i in sim:
        nextPerson = i[1]
        url = url_for("figurePage", figure=nextPerson.__str__())
        nextName = nextPerson.fname + " " + nextPerson.lname
        ppl += "<a href=" + url + ">" + nextName + "</br></a>"

    return final + ppl + "<h3>"

if __name__=='__main__':
    app.run()
