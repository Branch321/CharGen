'''
CharGen is a character creator for a custom ruleset
'''

import random

def choose_skills():
    spent_skill_points = 0
    total_skills_points = 9
    character_skill_list = {}

    list_o_skills = ["Academics(Brain)" , "Athletics(Brawn)", "Electronics(Brain)", "Driving(Brain)", "Fighting(Brawn)", "Healing(Brain)",
    "Intimidation(Brawn)", "Investigation(Brain)", "Notice(Brain)", "Performance(Brawn)", "Persuasion(Brawn)", "Power * (Brain / Brawn)", "Repair (Brain)", "Riding(Brawn)", "Science(Brain) ",
                     "Shooting(Brawn)", "Street Smart(Brain)", "Survival(Brawn)" , "Throwing(Brawn)"]
    while spent_skill_points != total_skills_points:
        # FIXME: This shit sucks
        character_skill_list[list_o_skills[random.randint(0,len(list_o_skills))]] = random.randint(0,total_skills_points)
        total_skills_points -= character_skill_list[list_o_skills[random.randint(0,len(list_o_skills))]]
    print(character_skill_list)



character_sheet = []
character_sheet.append('Name: \n')
character_sheet.append('\n')
# Generate your number
number = random.randint(5,15)
character_sheet.append('Number: ' + str(number) + ' ' + ("(Brain)\n" if number <= 10  else "(Brawn)\n"))
character_sheet.append('\n')
character_sheet.append("Armor: " + str(20-number) + "\n")
character_sheet.append('\n')
character_sheet.append('Health Points: 3 \n')
character_sheet.append('\n')
character_sheet.append('Skills: \n')
choose_skills()
character_sheet.append('\n')
character_sheet.append('Notes: \n')
character_sheet.append('\n')

print(*character_sheet)

