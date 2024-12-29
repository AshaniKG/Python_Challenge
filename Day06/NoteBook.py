import os 
import glob

#___________________________________CREATE_NOTE_FUNCTION___________________________________

def Create_Note(title):
    note = open(f"{title}.txt", "w")
    note.write (input("Add content: "))
    note.close()


#___________________________________EDIT_NOTE_FUNCTION___________________________________

def Edit_Note(title):
    note = open (f"{title}", "a")
    note.write (input("\nWhat do you want to add: "))
    note.close()


#___________________________________DELETE_NOTE_FUNCTION___________________________________

def Delete_Note(title):
    if os.path.exists (title):
        os.remove (title)


#___________________________________READ_NOTE_FUNCTION______________________________________


def Read_Note(title):
    note = open(f"{title}", "r")
    print(f"Content: {note.read()}")
    note.close()


#___________________________________VIEW_ALL_FUNCTION____________________________________

def View_All():
    allFiles = glob.glob("*.txt")
    i = 1

    print ("\nFILE LIST:")

    for x in allFiles:
        print (f" {i}) {x}")
        i += 1


    
#/////////////___________________________________________________________/////////////       

    
print ("\n 1.CREATE NOTE\n 2.EDIT NOTE\n 3.DELETE NOTE\n 4.SEARCH NOTE\n 5.VIEW ALL\n 6.EXIT\n")
option = int (input("Choose an option (Enter option number): "))

while option != 6:
#___________________________________CREATE_NOTE_OPTION___________________________________

    if option == 1:
        Create_Note(input("\nEnter note title: "))
    

#___________________________________EDIT_NOTE_OPTION_____________________________________

    elif option == 2:
        #////-----------To view the file list-------------
        View_All() 

        #////--------------Create a list--------------
        allFiles = glob.glob("*.txt")

        number = int (input("\nEnter title number of the note you want to edit: ")) 
        index = number - 1 
        chosen = allFiles[index]
        print (f"\n{number}) {chosen}")

        #////-------------To show the note content--------------
        Read_Note(chosen)

        #////-------------To enable edit note--------------
        Edit_Note(chosen)


#___________________________________DELETE_NOTE_OPTION_____________________________________

    elif option == 3:
        #////--------------To view the file list---------------
        View_All()
        
        #////--------------To find the deleting file---------------
        allFiles = glob.glob("*.txt")

        number = int (input("\nEnter title number of the note you want to delete: "))
        index = number - 1
        chosen = allFiles[index]

        #////--------------To delete the file---------------
        Delete_Note(chosen) 


#___________________________________SEARCH_NOTE_OPTION_____________________________________

    elif option == 4:
        search = input ("\nEnter the title of the note you want to search: ")
        check = (f"{search}.txt")

        allFiles = glob.glob("*.txt")
        i = 1

        #////---------------To search from the list-----------------
        for x in allFiles:
            if x == check:
                
                #////---------------To print note title-----------------
                print(f"\n{i}) {x}") 

                #////---------------To read note content-----------------
                Read_Note(x)
                break

            i += 1   


#___________________________________VIEW_ALL_OPTION_____________________________________

    elif option == 5:

        allFiles = glob.glob("*.txt")
        i = 1

        for x in allFiles:

            #////---------------To print note title-----------------
            print (f"\n{i}) {x}")

            #////---------------To read note content-----------------
            Read_Note(x)

            i += 1


    print ("\n 1.CREATE NOTE\n 2.EDIT NOTE\n 3.DELETE NOTE\n 4.SEARCH NOTE\n 5.VIEW ALL\n 6.EXIT\n")
    option = int (input("Choose an option (Enter option number): "))


