#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["Instructor Zach", "Blue", "32"]
    # display list1
    #print(list1)

    user_input= input("Please enter Instructor name?:")
    if(user_input==list1[0]):
        print("you have entered right: Instructor"+list1[0])
    else:
        print("Wrong: the instructor name is: "+list1[0])

    user_input2 = input("what is Zach fav colori?")
    if(user_input2==list1[1]):
        print("Right Zach fav color:"+list1[1])
    else:
        print("Wrong Zach fav color:"+list1[1])

    user_input3 = input("what is Zach Age?")
    if(user_input3==list1[2]):
        print("Right Zach Age: "+list1[2])
    else:
        print("Wrong Zach Age: "+list1[2])


    all_result = {user_input:list1[0], user_input2:list1[1], user_input3:list1[2]}
    
    print("Here is all the right Answer and Question>> "+ all_result.get(user_input))
    print("Here is all the right Answer and Question>> "+ all_result.get(user_input2))
    print("Here is all the right Answer and Question>> "+ all_result.get(user_input3))

main()

