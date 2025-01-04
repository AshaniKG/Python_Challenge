from pathlib import Path


#____________________________PARENT_CLASS________________________________

class Stream:
    def __init__ (self, subject1, subject2, subject3, english):
        
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.english = english 


#------------------Total of all subjects-------------------

    def cal_total (self, subject1, subject2, subject3, english):

        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.english = english 

        total = subject1 + subject2 + subject3 + english

        return total
    

#------------------Average of all subjects-------------------

    def cal_average (self, subject1, subject2, subject3, english, total):

        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.english = english
        self.total = total

        average = total / 4

        return average 


#------------------Save all details to file-------------------

    def save_details (self, index, letter, name, S_stream, subject1, subject2, subject3, sub1, sub2, sub3, english, total, average):
        
        self.index = index 
        self.letter = letter
        self.name = name
        self.S_stream = S_stream
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.english = english 
        self.total = total
        self.average = average
        

        save = open (f"{self.letter}_{self.index}.txt", "a") 
        save.write (f"Student Index = {self.index} \nSudent Name = {self.name} \n\nStream = {self.S_stream} \n\n{self.sub1} = {self.subject1} \n{self.sub2} = {self.subject2} \n{self.sub3} = {self.subject3} \nEnglish = {self.english} \n\nTotal Marks = {self.total} \nAverage = {self.average} \n\n")
        save.close()


#------------------Show all details from file-------------------

    def show_details (self, index, letter):
        self.index = index 
        self.letter = letter

        print (f"\nSAVED TO FILE: {self.letter}_{self.index}.txt\n")

        show = open (f"{self.letter}_{self.index}.txt", "r") 
        print (show.read())
        show.close()


#------------------View all files-------------------

    def view_files (self, list):
        self.list = list

        directory = Path (r"C:\Users\ashan\Desktop\Python\Python_Challenge")

        i = 1 

        for file in directory.glob ("*.txt"):
            if (f"{self.list}") in file.name:
                print (f"{i}) {file.name}") 
                i += 1


#------------------View details by selecting file number-------------------

    def number_selected (self, number):
        self.number = number 
        
        directory = Path (r"C:\Users\ashan\Desktop\Python\Python_Challenge")

        streamList = []

        for file in directory.glob ("*.txt"):
            if (f"{self.list}") in file.name:
                streamList.append (f"{file.name}") 

        chosen = streamList[self.number]

        print (f"\nSTUDENT FILE < {chosen} >: \n")

        select = open (f"{chosen}", "r") 
        print (select.read())
        select.close()
 
    
    def find_index (self, find): 
        self.find = find 

        directory = Path (r"C:\Users\ashan\Desktop\Python\Python_Challenge") 

        for file in directory.glob ("*.txt"):
            if (f"{self.find}") in file.name:

                print (f"\nSTUDENT FILE < {file.name} >: \n") 

                found = open (f"{file.name}", "r") 
                print (found.read()) 
                found.close() 
