import os
import random
class File_manager:
    def __init__(self,base_folder="File_manager"):
        self.base_folder=base_folder
        self.student_folder=os.path.join(self.base_folder,"all_students")
        self.author_folder=os.path.join(self.base_folder,"all_authors")
        os.makedirs(self.student_folder,exist_ok=True)
        os.makedirs(self.author_folder,exist_ok=True)

    # method 1 : Create student files.
    def create_student(self,stu_name,stu_age,stu_course,stu_mob):
        filename=f"{stu_name}.txt"
        file_path=os.path.join(self.student_folder,filename)
        if os.path.exists(file_path):
            print(f"Student {stu_name}.txt already exists.")
            return 
            
        with open(file_path,"w") as file:
            stu_id=random.random()*10000
            file.write(F"ID:{str(int(stu_id))}\n")
            file.write(F"Name:{stu_name}\n")
            file.write(F"Age:{stu_age}\n")
            file.write(F"Course:{stu_course}\n")
            file.write(F"Mobile:{stu_mob}\n")
        print(f"File {stu_name}.txt successfully created")

    def delete_students(self):
        files=os.listdir(self.student_folder)
        if ".txt" not in files:
            print("No files to remove")
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path=os.path.join(self.student_folder,file_name)
                os.remove(file_path)
                print(f"{file_path} is Removed..")

    def delete_specific_student():
        pass

    def update_student():
        pass

    def show_all_students():
        pass

    def read_students():
        pass

    def create_author():
        pass

    def create_book():
        pass

    def read_book():
        pass
    
fm=File_manager()
fm.create_student("Aman",33,"DS",8999999)

