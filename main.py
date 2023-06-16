"""
Here we call methods and functions,
 and also make instanse from the question class.
"""

from question import *
from input import *

question_bank = []

input_value = 0

while (input_value != 4):

    input_value = int(input("select the code: \n1.Descriptive Question \n2.Optional Question \n3.Show the Question Bank \n4.Exit\n "))

    if (input_value == 1):
        question_content = descriptive_question_input()
        question_bank.append(question_content)
        print(f"------------------** \n Your Q text is: {question_content.text}\n and has been saved! \n**---------------------")

        update_status = input("Do you want to update? [type y as YES and n as NO]\n")

        if (update_status == 'y'):
            new_text = input("Enter a new text for your question:\n")  
            question_content.update(new_text)
            print(f"-----------------**\nYour new question text is:\n{question_content.text}\nand has been updated\n**--------------")



    elif (input_value == 2):
        question_content = optional_question_input()
        question_bank.append(question_content)
        print(f"---------**\n Your new question text is: \n{question_content.text}, \nand the option is: \n{question_content.option} \n all have been saved!\n--------------")

        update_status = input("Do you want to update? [type y as YES and n as NO]\n")

        if (update_status == 'y'):
            new_text = input("Enter a new text for your question:\n")
            new_option = input("Please Enter a new option:\n")
            question_content.update(new_text, new_option)



    elif (input_value == 3):
        if (question_bank):
            print('------------** Your Question Bank is: **---------------\n')
            j = 0
            for i in question_bank:
                print (f"{j}. {i.text}, \n")
                j += 1

        else:
            print('------**Nothing inserted yet!!**------------')



    elif(input_value == 4):
        print("---------** Exit **----------")



    else:
        print("----------** not valid **-----------")

    
        



    
        



    





