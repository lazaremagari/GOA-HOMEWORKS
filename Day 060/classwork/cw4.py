#    4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელიც მიიღებს პარამტეტრად მომხმარებლის შემოტანილ რიცხვს ფუნქციამ უნდა დააბრუნოს ეს რიცხვი ლუწია თუ კენტი
num = int(input("enter number here -> "))
def luwi_kenti(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
luwi_kenti(num)