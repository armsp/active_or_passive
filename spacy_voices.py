import spacy
from spacy.matcher import Matcher

Active = "Harry ate six shrimp at dinner.\
Beautiful giraffes roam the savannah.\
Sue changed the flat tire.\
We are going to watch a movie tonight.\
I ran the obstacle course in record time.\
The crew paved the entire stretch of highway.\
Mom read the novel in one day.\
The critic wrote a scathing review.\
I will clean the house every Saturday.\
The staff is required to watch a safety video every year.\
She faxed her application for a new job.\
Tom painted the entire house.\
The teacher always answers the students’ questions.\
The choir really enjoys that piece.\
Who taught you to ski?\
The forest fire destroyed the whole suburb.\
The two kings are signing the treaty.\
The cleaning crew vacuums and dusts the office every night.\
Larry generously donated money to the homeless shelter.\
No one responded to my sales ad.\
The wedding planner is making all the reservations.\
Susan will bake two dozen cupcakes for the bake sale.\
The science class viewed the comet.\
Who ate the last cookie?\
Alex posted the video on Facebook.\
The director will give you instructions.\
Thousands of tourists view the Grand Canyon every year.\
The homeowners remodeled the house to help it sell.\
The team will celebrate their victory tomorrow.\
The saltwater eventually corroded the metal beams.\
The kangaroo carried her baby in her pouch.\
Some people raise sugar cane in Hawaii.\
He buys a camera.\
She drinks water.\
I know him.\
Water fills a tub.\
Women are not treated as equals.\
John has to study all afternoon.\
John is a good student.\
The dragon has scorched the metropolis with his fiery breath.\
After suitors invaded her house, Penelope had to think of ways to delay her remarriage.\
The Lao People’s Revolutionary Party set up a new system of drug control laws.\
Research points to heart disease as the leading cause of death in the United States.\
The surgeon positions the balloon in an area of blockage and inflates it.\
James writes the letters.\
James wrote the letters.\
James is writing the letters.\
James has written the letters.\
James is going to write the letters.\
James will write the letters.\
James was writing the letters.\
The scientists had found the cure, but it was too late.\
The scientists will have found a cure by then.\
 I keep the butter in the fridge.\
John is keeping my house tidy.\
Mary kept her schedule meticulously.\
The theater was keeping a seat for you.\
I have kept all your old letters.\
He had kept up his training regimen for a month.\
Mark will keep the ficus.\
If you told me, I would keep your secret.\
I would have kept your bicycle here if you had left it with me.\
She wants to keep the book.\
Judy was happy to have kept the puppy.\
I have a feeling that you may be keeping a secret.\
Having kept the bird in a cage for so long, Jade wasn't sure it could survive in the wild.\
Guests might not play chess.\
He might meet Dewi.\
Dewi must not open the gate every morning.\
He must finish his duty in a week.\
I may not buy the computer.\
He may sell the house.\
May I buy the computer?\
Risky can not buy this car every time.\
She can sell the car every time.\
Can she play a violin?"

Passive = "A camera is bought by him.\
Water is drunk by her.\
He is known to me.\
A tub is filled with water.\
Sugar is sold in kilograms.\
There is a considerable range of expertise demonstrated by the spam senders.\
It was determined by the committee that the report was inconclusive.\
We were invited by our neighbors to attend their party.\
Groups help participants realize that most of their problems and secrets are shared by others in the group.\
The proposed initiative will be bitterly opposed by abortion rights groups.\
Minor keys, modal movement, and arpeggios are shared by both musical traditions.\
In this way, the old religion was able to survive the onslaught of new ideas until the old gods were finally displaced by Christianity.\
First the apples are picked, then they are cleaned, and finally they’re packed and shipped to the market.\
New York is considered the most diverse city in the U.S.\
It is believed that Amelia Earhart’s plane crashed in Pacific Ocean.\
Hungarian is seen as one of the world’s most difficult languages to learn.\
Skin cancers are thought to be caused by excessive exposure to the sun.\
George Washington was elected president in 1788.\
Two people were killed in a drive-by shooting on Friday night.\
Ten children were injured when part of the school roof collapsed.\
I was hit by the dodgeball.\
The metropolis has been scorched by the dragon’s fiery breath.\
When her house was invaded, Penelope had to think of ways to delay her remarriage.\
A new system of drug control laws was set up.\
Heart disease is considered the leading cause of death in the United States.\
The balloon is positioned in an area of blockage and is inflated.\
The Exxon Company accepts that a few gallons might have been spilled.\
100 votes are required to pass the bill.\
Over 120 different contaminants have been dumped into the river.\
Baby Sophia was delivered at 3:30 a.m. yesterday.\
The letters are written by James.\
The letters were written by James.\
The letters are being written by James.\
The letters have been written by James.\
The letters are going to be written by James.\
The letters will be written by James.\
The letters were being written by James.\
The cure had been found, but it was too late.\
A cure will have been found by then.\
Mistakes were made.\
The butter is kept in the fridge.\
My house is being kept tidy.\
Mary's schedule was kept meticulously.\
A seat was being kept for you.\
All your old letters have been kept.\
His training regimen had been kept up for a month.\
The ficus will be kept.\
If you told me, your secret would be kept.\
Your bicycle would have been kept here if you had left it with me.\
The book wants to be kept.\
The puppy was happy to have been kept.\
I have a feeling that a secret may be being kept.\
The bird, having been kept in a cage for so long, might not survive in the wild.\
The car can be sold by her every time.\
Can a violin be played by her?\
The house may be sold by him.\
May the computer be bought by me?\
The computer may not be bought by me.\
His duty must be finished by him in a week.\
The gate must not be opened by Dewi every morning.\
Dewi might be met by him.\
Chess might not be played guests.\
At dinner, six shrimp were eaten by Harry.\
The savannah is roamed by beautiful giraffes.\
The flat tire was changed by Sue.\
A movie is going to be watched by us tonight.\
The obstacle course was run by me in record time.\
The entire stretch of highway was paved by the crew.\
The novel was read by Mom in one day.\
A scathing review was written by the critic.\
The house will be cleaned by me every Saturday.\
A safety video will be watched by the staff every year.\
The application for a new job was faxed by her.\
The entire house was painted by Tom.\
The students’ questions are always answered by the teacher.\
That piece is really enjoyed by the choir.\
By whom were you taught to ski?\
The whole suburb was destroyed by the forest fire.\
The treaty is being signed by the two kings.\
Every night the office is vacuumed and dusted by the cleaning crew.\
Money was generously donated to the homeless shelter by Larry.\
My sales ad was not responded to by anyone.\
All the reservations will be made by the wedding planner.\
For the bake sale, two dozen cookies will be baked by Susan.\
The comet was viewed by the science class.\
The video was posted on Facebook by Alex.\
Instructions will be given to you by the director.\
The Grand Canyon is viewed by thousands of tourists every year.\
The house was remodeled by the homeowners to help it sell.\
The victory will be celebrated by the team tomorrow.\
The metal beams were eventually corroded by the saltwater.\
The baby was carried by the kangaroo in her pouch.\
The last cookie was eaten by whom?"
try:
    nlp = spacy.load('en_core_web_sm')
except:
    nlp = spacy.load('en')
matcher = Matcher(nlp.vocab)
def is_passive(sentence):
    doc = nlp(sentence)
    passive_rule = [{'DEP': 'nsubjpass'}, {'DEP': 'aux', 'OP': '*'}, {'DEP': 'auxpass'}, {'TAG': 'VBN'}]
    matcher.add('Passive', None, passive_rule)
    matches = matcher(doc)
    if matches:
        return "Passive"
    else:
        return "Active"

if __name__=='__main__':
    #nlp = spacy.load('en_core_web_sm')
    #matcher = Matcher(nlp.vocab)
    text = Passive
    doc = nlp(text)
    sents = list(doc.sents)
    print("Number of Sentences = ",len(sents))
    for sent in doc.sents:
        for token in sent:
            print(token.dep_,token.tag_, end = " ")
        print()
    passive_rule = [{'DEP':'nsubjpass'},{'DEP':'aux','OP':'*'},{'DEP':'auxpass'},{'TAG':'VBN'}]
    matcher.add('Passive',None,passive_rule)
    matches = matcher(doc)
    print(len(matches))
