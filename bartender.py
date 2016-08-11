questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def askQuestions():
    askStrong=input(questions["strong"] + " " + "Answer Yes or No.")
    askSalty=input(questions["salty"] + " " + "Answer Yes or No.")
    askBitter=input(questions["bitter"] + " " + "Answer Yes or No.")
    askSweet=input(questions["sweet"] + " " + "Answer Yes or No.")
    askFruity=input(questions["fruity"] + " " + "Answer Yes or No.")
    if askStrong == "yes":
        strong = True
    elif askStrong =="y":
        strong = True
    else:
        strong = False

    if askSalty == "yes":
        salty = True
    elif askSalty =="y":
        salty = True
    else:
        salty = False
        
    if askStrong == "yes":
        strong = True
    elif askStrong =="y":
        strong = True
    else:
        strong = False
        
    if askStrong == "yes":
        strong = True
    elif askStrong =="y":
        strong = True
    else:
        strong = False
        
    if askStrong == "yes":
        strong = True
    elif askStrong =="y":
        strong = True
    else:
        strong = False

if __name__ == '__main__':
   askQuestions()

