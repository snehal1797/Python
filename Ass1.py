class Main():


    def a1(self):
        a=int(input("Enter any no:"))
        if a>0:
          print(a, "is positive")
        elif a<0:
           print(a, "is negative")
        else:
           print("Entered number is zero")
           return  a


    def a2(self):
         b = int((input("Enter any number")))
         if b*3<60:
            print("Father's age is less")
         elif b*3>60:
            print("Father's age is greater")
         else:
            print("Father's age is equal to son's age")

    def a3(self):
         c = int(input("Enter any year"))
         if c%400==0:
            print(c, "is leap year")
         elif c%100==0:
            print(c, "is not leap year")
         elif c%4==0:
            print(c, "is  leap year")
         else:
            print(c, "is not leap year")


    def a4(self):
        people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
              2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
              3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
              4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'},

              5: {"name": {"Aishwarya": "cool"},
                  "loc": ["Mumbai", "Pune"]},

              6: {"name": {"Snehal": "good"},
                  "loc": ("kolhapur", "Pune")}

              }
        print(people[5]["name"]["Aishwarya"])
        print(people[5]["loc"])
        print(people[6]["name"]["Snehal"])
        print(people[6]["loc"])

obj=Main()
obj.a1()
obj.a2()

obj1=Main()
obj1.a3()
obj1.a4()



