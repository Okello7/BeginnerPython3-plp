#In-built functions
#User defined functions
#Classes and Objects
   # Classes are created by keyword class.
   # Attributes are the variables that belong to a class.
    #Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

class Computer:
    #Attribute/ Variables
    #Behaviour/ Methods
    def config(self):
        print("i5, 16gb RAM,1TB")

com1 = Computer()
com2 = Computer()
print(type(com1))
Computer.config(com1)
com1.config()
com2.config()

#File handling
with open("test.txt", 'w') as a:
    a.write("Do you know the math?")

with open("fintech.txt") as f:
    print(f.read())

# f.read(5) This line returns an error ValueError: I/O operation on closed file.
b = open("Borana Dicctionary.txt", "r")
b.read()
#b.close()

#Dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("Printing Employee data...")
print(Employee)

#Modules (Attributes, functions, varibles) the same grouped code

#Self Test
#Create a dictionary named personalDetails
personalDetails = {"FirstName":"James", "LastName":"Ouko","Age":22}
personalDetails["PhoneNumber"] = "0712345678"
personalDetails["Email"] = "student@gmail.com"
print("##***")
print(personalDetails.keys())
print(personalDetails)
#Using the relevant properties and methods do the following;
#    Update Age to 55                                       
#    Print the LastName                                      
#    Print length of the dictionary

personalDetails["Age"] = 55
print(personalDetails, end = "\n")
print(personalDetails["LastName"])
print(len(personalDetails))

