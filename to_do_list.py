
#To-Do List

import pickle

with open("to_do_data.csv",'rb') as f:
    try:
        to_do_list = pickle.load(f)
    except:
        to_do_list = {}

mainloop = True
while mainloop:
    input1 = input("What do you want to do?\n1.View list \n2. Add item to list \n3. Remove item from lsit \n4. Check item form list \n5. Uncheck item from list \n6.Nothing\n")
    if input1 == '1':
        if len(to_do_list) == 0:
            print("List is empety")
        else:
            for item,checked in to_do_list.items():
                if checked:
                    print(item,": checked")
                else:
                    print(item,": unchecked")

    elif input1 == '2':
        input2 = input("add item to list ")
        to_do_list[input2] = False
        print("itme added to list")

    elif input1 == '3':
        input2 = int(input("enter the index of the item "))
        try:
            to_do_list.pop(list(to_do_list.keys())[input2-1])
            print("item remover from list")
        except:
            print("invalid input")

    elif input1 == '4':
        input2 = int(input("enter the index of the item "))
        try:
            to_do_list[list(to_do_list.keys())[input2-1]] = True
            print("item checked")
        except:
            print("invalid input")

    elif input1 == '5':
        input2 = int(input("enter the index of the item "))
        try:
            to_do_list[list(to_do_list.keys())[input2-1]] = False
            print("item unchecked")
        except:
            print("invalid input")

    elif input1 == '6':
        mainloop = False

    else:
        print("!invalid input!")

f.close()

with open("to_do_data.csv",'wb') as f:
    pickle.dump(to_do_list,f)
f.close()
