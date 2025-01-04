from TrackerParent import Stream
from TrackerChild import Biology_Stream 
from TrackerChild import Maths_Stream 


#////--------------------Choose the Option----------------------

print ("MAIN MENU\n 1) INSERT MARKS\n 2) CHECK MARKS\n 3) EXIT\n")

option = int (input ("Choose what you want to do (Enter number): "))


while option != 3:

    #_____________________________TO INSERT MARKS______________________________

    if option == 1: 
        
        #////--------------------Choose the Stream----------------------

        print("\n 1) BIOLOGY STREAM\n 2) MATHEMATICS STREAM\n")

        choice = int (input ("Enter the number of the stream: ")) 


    #_____________________________FOR A BIO STUDENT______________________________ 

        if choice == 1:
            B_index = int (input("\nEnter student index: "))
            B_name = input ("Enter student name: ")

            B_subject1 = int (input("\nMarks for Biology: "))
            B_subject2 = int (input("Marks for Physics: "))
            B_subject3 = int (input("Marks for Chemistry: "))
            B_english = int (input("Marks for English: ")) 


            #////--------------------Creating the object for Bio Stream mark inserting----------------------
            
            B_Student = Biology_Stream (B_subject1, B_subject2, B_subject3, B_english)


            #////--------------Applying the total function to calculate and print the total for Bio Student----------------

            B_total = B_Student.cal_total (B_subject1, B_subject2, B_subject3, B_english) 
            print (f"\nTotal is: {B_total}")


            #////-------------Applying the average function to calculate and print the average for Bio Student---------------

            B_average = B_Student.cal_average (B_subject1, B_subject2, B_subject3, B_english, B_total) 
            print (f"Average is: {B_average}")
            

            #////--------------------Save all details to file (Bio Stream)----------------------

            B_save = B_Student.save_details (B_index, "B", B_name, "Biology Stream", B_subject1, B_subject2, B_subject3, "Biology", "Physics", "Chemistry", B_english, B_total, B_average)


            #////--------------------Show all details from file (Bio Stream)----------------------

            B_show = B_Student.show_details(B_index, "B") 



        #_____________________________FOR A MATHS STUDENT______________________________

        if choice == 2:
            M_index = int (input("\nEnter student index: "))
            M_name = input ("Enter student name: ")

            M_subject1 = int (input("\nMarks for Mathematics: "))
            M_subject2 = int (input("Marks for Physics: "))
            M_subject3 = int (input("Marks for Chemistry: "))
            M_english = int (input("Marks for English: "))


            #////--------------------Creating the object for Maths Stream mark inserting----------------------
            
            M_Student = Maths_Stream (M_subject1, M_subject2, M_subject3, M_english)


            #////--------------Applying the total function to calculate and print the total for Maths Student----------------

            M_total = M_Student.cal_total (M_subject1, M_subject2, M_subject3, M_english)  
            print (f"\nTotal is: {M_total}")


            #////-------------Applying the average function to calculate and print the average for Maths Student---------------

            M_average = M_Student.cal_average (M_subject1, M_subject2, M_subject3, M_english, M_total) 
            print (f"Average is: {M_average}")


            #////--------------------Save all details to file (Maths Stream)----------------------

            M_save = M_Student.save_details (M_index, "M", M_name, "Mathematics Stream", M_subject1, M_subject2, M_subject3, "Mathematics", "Physics", "Chemistry", M_english, M_total, M_average)


            #////--------------------Show all details from file (Maths Stream)----------------------

            M_show = M_Student.show_details(M_index, "M") 




    #_____________________________TO CHECK MARKS______________________________

    if option == 2:

        #////--------------------Choose the check method----------------------

        print (" \n1) CHECK MARKS BY STREAM \n2) CHECK MARKS BY INDEX\n")

        method = int (input ("Choose a method: "))


        #_____________________________CHECK MARKS BY STREAM______________________________

        if method == 1:

            #////--------------------Choose the Stream----------------------

            print ("\n 1) BIOLOGY STREAM\n 2) MATHEMATICS STREAM\n")

            view = int (input ("Enter number of the stream: ")) 


            #_____________________________CHECK MARKS FROM BIO STREAM______________________________

            if view == 1:

                B_list = "B"

                #////--------------------Creating the second object for Bio Stream mark checking----------------------
                
                B_Files = Biology_Stream ("Biology", "Physics", "Chemistry", "English")


                #////--------------------Print Bio file list---------------------- 

                print ("\nFILE LIST FROM BIOLOGY STREAM: \n")

                B_fileList = B_Files.view_files (B_list)  


                #////--------------------Choosing a Bio file and viewing the details of the chosen file----------------------

                check = int (input ("\nEnter file number you want to check: ")) 

                number = check - 1 

                B_streamSelect = B_Files.number_selected (number) 


                
            #_____________________________CHECK MARKS FROM MATHS STREAM______________________________

            if view == 2: 
                M_list = "M"

                #////--------------------Creating the second object for Maths Stream mark checking----------------------
                
                M_Files = Maths_Stream ("Mathematics", "Physics", "Chemistry", "English")


                #////--------------------Print Maths file list---------------------- 

                print ("\nFILE LIST FROM MATHEMATICS STREAM: \n")

                M_fileList = M_Files.view_files (M_list)  


                #////--------------------Choosing a Maths file and viewing the details of the chosen file----------------------

                check = int (input ("\nEnter file number you want to check: ")) 

                number = check - 1 

                M_streamSelect = M_Files.number_selected (number) 



        #_____________________________CHECK MARKS BY INDEX______________________________

        if method == 2:

            search = int (input ("Enter index number: "))

            #////--------------------Creating an object to find the file by index----------------------

            Student_Index = Stream (" ", " ", " ", " ") 


            #////-------------------To find and view the file by index----------------------

            studentFile = Student_Index.find_index (search)  



    print ("MAIN MENU\n 1) INSERT MARKS\n 2) CHECK MARKS\n 3) EXIT\n")

    option = int (input ("Choose what you want to do (Enter number): "))