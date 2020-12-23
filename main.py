#Might be better ways but this is the best way of choice if someone don't like a character in there simply delete it
list = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "q",
    "w",
    "e",
    "r",
    "t",
    "z",
    "u",
    "i",
    "o",
    "p",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "y",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Z",
    "-",
    "+",
    "#",
    ".",
    ":",
    ";",
    "_",
    "?",
    "&",
    "%",
    "$",
    "!",
    "<",
    ">",
    "(",
    ")"
}
#list
import random
count = 0
list3 = []
for list2 in list:
    list3 = [list2] + list3
eingabe = input("How long should your password be? :")
count2 = 0
list4 = ""
wahl = True
while wahl:
    count2 = count2 + 1
    list4 = list3[random.randint(0, 56)] + list4
    if count2 == int(eingabe):
        text = "Your Password is {}"
        print(text.format((list4)))
        text2 = "Your last password was \n {}"
        save = open("last_password.txt", "w")
        save.write(text2.format((list4)))
        save.close()
        input("Type ENTER to exit")
        wahl = False


