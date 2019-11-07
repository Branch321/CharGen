'''
CharGen is a character creator for a custom ruleset
'''

import random

def choose_skills():
    list_o_skills = ["Academics(Brain)" , "Athletics(Brawn)", "Electronics(Brain)", "Driving(Brain)", "Fighting(Brawn)", "Healing(Brain)",
    "Intimidation(Brawn)", "Investigation(Brain)", "Notice(Brain)", "Performance(Brawn)", "Persuasion(Brawn)", "Power * (Brain / Brawn)", "Repair (Brain)", "Riding(Brawn)", "Science(Brain) ",
                     "Shooting(Brawn)", "Street Smart(Brain)", "Survival(Brawn)" , "Throwing(Brawn)"]
character_sheet = []
character_sheet.append('Name: \n')
character_sheet.append('\n')
# Generate your number
number = str(random.randint(5,15))
character_sheet.append('Number: ' + number + '\n')
character_sheet.append('\n')
character_sheet.append('Armor: \n')
character_sheet.append('\n')
character_sheet.append('Health Points: \n')
character_sheet.append('\n')
character_sheet.append('Skills: \n')
character_sheet.append('\n')
character_sheet.append('Notes: \n')
character_sheet.append('\n')

print(*character_sheet)

