'''
CharGen is a character creator for a custom ruleset
'''

import random

def choose_skills_unit_test(test_number):
    '''
    Checking to make sure Power option works in choose_skills function
    :param test_number: Parameter that determines how many tests to run
    :return: Dictionary full of chosen skills and the amount of points placed in them
    '''
    for i in range(0,test_number):
        sum = 0
        dictionary = choose_skills()
        if "Power * (Brain / Brawn)" in dictionary.keys():
            # print(dictionary)
            for element in dictionary.keys():
                if element == "Power * (Brain / Brawn)":
                    sum+=dictionary[element]*2
                else:
                    sum += dictionary[element]
            if sum != 9:
                print("Failed")

def choose_skills():
    # TODO: Doesn't take into account player may have two powers and they are linked to Brain or Brawn not both
    # TODO: need to add +/- modifiers in this function
    total_skills_points = 9
    character_skill_list = {}
    list_o_skills = ["Academics(Brain)", "Animal Handling(Brawn)", "Athletics(Brawn)", "Electronics(Brain)",
                     "Driving(Brawn)", "Fighting(Brawn)", "Healing(Brain)",
                     "Insight(Brain)", "Intimidation(Brawn)", "Investigation(Brain)", "Notice(Brain)",
                     "Performance(Brawn)", "Persuasion(Brawn)", "Power * (Brain / Brawn)", "Repair (Brain)",
                     "Science(Brain) ",
                     "Shooting(Brain)", "Stealth(Brawn)", "Street Smart(Brain)", "Survival(Brawn)", "Throwing(Brawn)"]

    while total_skills_points !=0:
        which_skill = random.randint(0,len(list_o_skills)-1)
        how_much_skill = 0
        if which_skill == 11 and total_skills_points>1:
            how_much_skill = random.randint(1, total_skills_points//2)
            if list_o_skills[which_skill] not in character_skill_list:
                character_skill_list[list_o_skills[which_skill]] = 0
            total_skills_points -= how_much_skill*2
            character_skill_list[list_o_skills[which_skill]] += how_much_skill
        elif which_skill != 11 and total_skills_points >= 1:
            how_much_skill = random.randint(1,total_skills_points)
            if list_o_skills[which_skill] not in character_skill_list:
                character_skill_list[list_o_skills[which_skill]] = 0
            total_skills_points -= how_much_skill
            character_skill_list[list_o_skills[which_skill]] += how_much_skill
    return character_skill_list


number_of_characters = 4
text_file_name = 'char_sheet.txt'
with open(text_file_name, 'w+') as file:
    for x in range(0, number_of_characters):
        character_sheet = []
        character_sheet.append('Name: \n')
        character_sheet.append('Bio: \n')
        character_sheet.append('Public Goal: \n')
        character_sheet.append('Private Goal: \n')
        # Generate your number
        number = random.randint(5, 15)
        character_sheet.append('BB Number: ' + str(number) + ' ' + ("(Brain)\n" if number <= 10 else "(Brawn)\n"))
        character_sheet.append("Armor: " + str(20 - number) + "\n")
        character_sheet.append('Health Points: 5 \n')
        character_sheet.append('Weapon: \n')
        character_sheet.append('Items: \n')
        character_sheet.append('Skills: \n')
        skill_dict = choose_skills()
        for element in skill_dict.keys():
            character_sheet.append(
                '    ' + str(element) + ': ' + ('-' if "Brawn" in str(element) else '+') + str(
                    skill_dict[element]) + '\n')
        character_sheet.append('\n')
        character_sheet.append('Notes: \n')
        for x in range(0, 4):
            character_sheet.append('\n')
        print(*character_sheet)
        file.writelines(character_sheet)
