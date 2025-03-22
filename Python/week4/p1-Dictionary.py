Student = {
    "momeni" : ["yousof", "momeni" , "103"] , 
    "vejahat" : ["kourosh", "vejahat" , "103"] ,
    "fazeli" : ["amir", "fazeli" , "203"]
}

def search():
    search = input("Search student:")
    if search in Student :
        print("white...")
        print(Student[search])
    else:
        print("Student not finde.")

search()