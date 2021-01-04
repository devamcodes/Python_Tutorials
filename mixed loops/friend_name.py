list_of_friends = []
def add_friends():
    add_friends = 1
    while add_friends != 0:
        friend_name =  input("Please enter your friend's name: ")
        list_of_friends.append(friend_name)
        add_friends = int(input("continue adding?\n=>"))

def find_friend():
    find_friend = input("Please enter the name of the friend you want to search for:\n=> ")
    for element in list_of_friends:
        if element == find_friend:
            print(f"Found Him/Her! at location {list_of_friends.index(element)}")
    else:
        print("Duh! I cannot find your friend sorry!")
    input("Program executed!")

while 1:
    add_friends()
    find_friend()