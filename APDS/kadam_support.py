import random
positive_reinforces_list=["Excellent", "Very Good", "Well Done", "Awesome"," Good Job", "Correct"]
supportive_reinforces_list=["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]

def positive_reinforces():
    print(random.choice(positive_reinforces_list))

def supportive_reinforces():
    print(random.choice(supportive_reinforces_list))

