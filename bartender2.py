import random

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
        
    if askBitter == "yes":
        bitter = True
    elif askBitter =="y":
        bitter = True
    else:
        bitter = False
        
    if askSweet == "yes":
        sweet = True
    elif askSweet =="y":
        sweet = True
    else:
        sweet = False
        
    if askFruity == "yes":
        fruity = True
    elif askFruity =="y":
        fruity = True
    else:
        fruity = False
        
    askQuestions.answers = {
        "strong": strong,
        "salty": salty,
        "bitter": bitter,
        "sweet": sweet,
        "fruity": fruity
    }
    
    
    
def chooseIngred():
    list = []
    if askQuestions.answers['strong'] == True:
        list.append(random.choice(ingredients['strong']))
    if askQuestions.answers['salty'] == True:
        list.append(random.choice(ingredients['salty']))  
    if askQuestions.answers['bitter'] == True:
        list.append(random.choice(ingredients['bitter']))
    if askQuestions.answers['sweet'] == True:
        list.append(random.choice(ingredients['sweet'])) 
    if askQuestions.answers['fruity'] == True:
        list.append(random.choice(ingredients['fruity'])) 
    
    adj = ['Happy','Crazy','Amazing']
    noun = ['Girl','Island','Tea']
    print("Here is your" + " " + random.choice(adj) + " " + random.choice(noun) + ",which is made of " + str(list))  

if __name__ == '__main__':
    askName = input("What's your name?")
    print("Nice to meet you "+askName+"! Tell me your preference!")

    def anotherDrink():
        askQuestions()
        chooseIngred()
        another = input("Do you want another drink?")
        if another == "yes":
           askQuestions()
           chooseIngred()
           anotherDrink()
        elif another == "y":
           askQuestions()
           chooseIngred()
           anotherDrink()
        else:
           print('Ok. Pay now!')
       
    anotherDrink()
   

