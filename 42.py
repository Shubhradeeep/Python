# Write a program to input player's name (string) and runs (integer) scored for n number of players where n should be input from the keyboard. Store the player’s details in a dictionary called 'cricket'. After preparing the dictionary, input the player's name and print the runs scored by the player otherwise returns'-1' if the player's name is not found.

names = [ "Virat Kholi","M.S Dhoni","Srikar Bharat","Shreyas Iyer","Ishant Sharma"]
print("Enter the runs scored by each player respectively(seprated by comma)\n",names)
score = input()
score = score.split(",")
dict={}
i = 0
for name in names:
    item = int(score[i])
    dict[name] = item
    i = i +1
search = input("\nWhich player score are you searching for? ")
if search not in dict:
    print("-1")
else:
    print(dict[search])



