import random
from config import Config


def papoupapa(sujet1):
    if sujet1 == "papas":
        sujet2 = "papous"
        return sujet2
    elif sujet1 == "papous":
        sujet2 ="papas"
        return sujet2
    
def laoupasla(brique):
    if random.random() < 0.5:
        return random.choice(brique)
    else: 
        return ""
def complement_present(complement):
    if complement == "":
        return ""
    else:
        return random.choice(Config.determinant_facultatif2)

def gener_bloc():
    
    complement = ["poux"]
    present = laoupasla(complement)
    sujet = random.choice(Config.sujet1)
    briques = [
        random.choice(Config.debut), 
        random.choice(Config.determinant), 
        sujet, 
        laoupasla(Config.determinant_facultatif1), 
        papoupapa(sujet), 
        complement_present(present), 
        present, 
        random.choice(Config.entre_deux)
        ]
    return " ".join([x for x in briques if x != ""])
