#-------------------------------------Parent class--------------------------------------------

class myPet:
    def __init__(self, name):
        self.name = name
        
#-------------------------------------Bath the pet function--------------------------------------------

    def is_bath(self):
        print(f"{self.name}: Good Morning dear owner..! It's shower time..\n \nACTIVITIES:\n 1.Bath the pet\n 2.Feed the pet\n 3.Play with pet\n 4.put the pet to sleep \n")

        doBath = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))

        while doBath < 5:
            if doBath == 1:
                print (f"\n{self.name}: Nice bath. I feel so clean..!!\n")
                myPet.is_hungry(self)
                break

            else:
                print (f"\n{self.name}: Wait.. I'm dirty! Let's take a bath first..")
                doBath = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))


#-------------------------------------Feed the pet function--------------------------------------------

    def is_hungry(self):
        print(f"{self.name}: Ooh.. Now I'm hungry..\n \nACTIVITIES:\n 1.Bath the pet\n 2.Feed the pet\n 3.Play with pet\n 4.put the pet to sleep \n")
        
        doFeed = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))

        while doFeed < 5:
            if doFeed == 2:
                print (f"\n{self.name}: I'm full. Thank you..!!\n")
                myPet.is_boring(self)
                break

            else:
                print (f"\n{self.name}: No.. I'm hungry! Can we eat something..?")
                doFeed = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))


#-------------------------------------Play with function--------------------------------------------

    def is_boring(self):
        print(f"{self.name}: I have nothing to do. I feel lonely..\n \nACTIVITIES:\n 1.Bath the pet\n 2.Feed the pet\n 3.Play with pet\n 4.put the pet to sleep \n")
        
        doPlay = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))

        while doPlay < 5:
            if doPlay == 3:
                print (f"\n{self.name}: It was fun. I'm so happy..!!\n") 
                myPet.is_tired(self)
                break

            else:
                print (f"\n{self.name}: I'm bored! I want to play..")
                doPlay = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): ")) 


#-------------------------------------Put to sleep function--------------------------------------------

    def is_tired(self):
        print("hi")
        print(f"{self.name}: Time for bed. I'm so tired..\n \nACTIVITIES:\n 1.Bath the pet\n 2.Feed the pet\n 3.Play with pet\n 4.put the pet to sleep \n")

        doSleep = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))

        while True:
            if doSleep == 4:
                print (f"\n{self.name}: {self.name} is sleeping. Good Night dear owner..!!")
                break

            else:
                print (f"\n{self.name}: But.. I'm tired! Let's rest now..")
                doSleep = int (input("CHOOSE WHAT TO DO (ENTER ACTIVITY NUMBER): "))


#-------------------------------------Child classes--------------------------------------------

#-----------Class for a dog------------

class petDog (myPet):
    def __init__(self, name):
        self.name = name

    def my_Dog(self):
        print(f"{self.name}: Hi.. I'm {self.name}! Happy to be your pet dog")

#-----------Class for a cat------------
        
class petCat (myPet):
    def __init__(self, name):
        self.name = name

    def my_Cat(self):
        print(f"{self.name}: Hi.. I'm {self.name}! Happy to be your pet cat")

#-----------Class for a rabbit------------

class petRabbit (myPet):
    def __init__(self, name):
        self.name = name

    def my_Rabbit(self):
        print(f"{self.name}: Hi.. I'm {self.name}! Happy to be your pet Rabbit")



#-------------------------------------Object Creation--------------------------------------------


print ("WELCOME..!! DO YOU NEED A PET..?? \n\nCHOOSE ONE FOR YOU:\n 1.Dog\n 2.Cat\n 3.Rabbit\n")
getPet = int (input("Enter the number of the pet you want: "))

#-----------If the pet is dog------------

if getPet == 1:
    dog = petDog(input("\nChoose a name for your dog: "))
    dog.my_Dog()

    print("\nNOW YOU HAVE A PET.. TAKE GOOD CARE OF YOUR PET\n")

    dog.is_bath()
    
#-----------If the pet is cat------------

elif getPet == 2:
    cat = petCat(input("\nChoose a name for your cat: "))
    cat.my_Cat()

    print("\nNOW YOU HAVE A PET.. TAKE GOOD CARE OF YOUR PET\n")

    cat.is_bath()

#-----------If the pet is rabbit------------

elif getPet ==3:
    rabbit = petRabbit(input("\nChoose a name for your Rabbit: "))
    rabbit.my_Rabbit()

    print("\nNOW YOU HAVE A PET.. TAKE GOOD CARE OF YOUR PET\n")

    rabbit.is_bath()

 
