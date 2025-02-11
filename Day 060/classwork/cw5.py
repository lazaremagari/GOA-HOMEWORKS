#  მომხმარებელს შემოატანინეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელიც მიიღებს პარამტეტრად მომხმარებლის შემოტანილ 
# რიცხვს ფუნქციამ უნდა დააბრუნოს ეს რიცხვი არის თუ არა ხუთის ჯერადი
num = int(input("enter number here -> "))
def numberi(numm):
    if numm % 5 == 0:
        print("this number can be devided by 5!")
    else:
        print("this number can't be devided by 5")
numberi(num)