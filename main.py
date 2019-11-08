'''
CharGen is a character creator for a custom ruleset
'''

import random

def choose_skills_unit_test(test_number):
    '''
    Checking to make sure Power option works in choose_skills function
    :param test_number:
    :return:
    '''
    for i in range(0,test_number):
        sum = 0
        dictionary = choose_skills()
        if "Power * (Brain / Brawn)" in dictionary.keys():
            for element in dictionary.keys():
                if element == "Power * (Brain / Brawn)":
                    sum+=dictionary[element]*2
                else:
                    sum += dictionary[element]
            if sum != 9:
                print("Failed: ",end='')
                print(dictionary)

def choose_skills():
    total_skills_points = 9
    character_skill_list = {}
    list_o_skills = ["Academics(Brain)" , "Athletics(Brawn)", "Electronics(Brain)", "Driving(Brain)", "Fighting(Brawn)", "Healing(Brain)",
    "Intimidation(Brawn)", "Investigation(Brain)", "Notice(Brain)", "Performance(Brawn)", "Persuasion(Brawn)", "Power * (Brain / Brawn)", "Repair (Brain)", "Riding(Brawn)", "Science(Brain) ",
    "Shooting(Brawn)", "Street Smart(Brain)", "Survival(Brawn)" , "Throwing(Brawn)"]

    while total_skills_points !=0:
        # FIXME: still need to fix power stuff
        which_skill = random.randint(0,len(list_o_skills)-1)
        how_much_skill = 0
        if which_skill == 11 and total_skills_points>1:
            how_much_skill = random.randint(1, total_skills_points//2)
            total_skills_points -= how_much_skill*2
            if list_o_skills[which_skill] not in character_skill_list.keys():
                character_skill_list[list_o_skills[which_skill]] = 0
            character_skill_list[list_o_skills[which_skill]] += how_much_skill
        elif which_skill!=11 and total_skills_points>=1:
            how_much_skill = random.randint(1,total_skills_points)
            total_skills_points -= how_much_skill
            if list_o_skills[which_skill] not in character_skill_list.keys():
                character_skill_list[list_o_skills[which_skill]] = 0
            character_skill_list[list_o_skills[which_skill]] += how_much_skill
    return character_skill_list

choose_skills_unit_test(10000000)
'''
character_sheet = []
character_sheet.append('Name: \n')
# Generate your number
number = random.randint(5,15)
character_sheet.append('Number: ' + str(number) + ' ' + ("(Brain)\n" if number <= 10  else "(Brawn)\n"))
character_sheet.append("Armor: " + str(20-number) + "\n")
character_sheet.append('Health Points: 3 \n')
character_sheet.append('Skills: \n')
character_sheet.append(choose_skills())
character_sheet.append('\n')
character_sheet.append('Notes: \n')

print(*character_sheet)
'''
