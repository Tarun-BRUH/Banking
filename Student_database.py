import pickle
import time
class Teacher :
    no_of_teachers = 0

    def __init__(self):

        Teacher.no_of_teachers +=1

        self.TeacherData = None 
        self.Name  = None
        self.Password = None
        self.Address = None
        self.DOB = None
        self.Email = None
        self.Phno = None
        self.info = None

    def InputData(self,lst) :
        
        self.Name  = lst[0]
        self.Password = lst[1]
        self.Address = lst[2]
        self.DOB = lst[3]
        self.Email = lst[4]
        self.Phno = lst[5]
        self.age = lst[6]
      


def LoginPage():
    global process

    print("Welcome to the student database")
    print(" ")
    txt ="""Select 1 - Existing Account,
Select 2 - Create New Account,
Select 3 - Exit :"""
    try:
        x = int(input(txt))
    except ValueError:
        print("Invalid Option")
        LoginPage()
        return

    if x ==1:
        SignIn()
    elif x==2:
        SignUp()
    elif x == 3:
        process = False
    else:
        print("Invalid Option")


def SignUp() :
    print("")
    print(r"\\\ Create New Account ///")
    Data = []
    obj = Teacher()
    
    Username  = input("Enter your Username(cannot be changed) : ")
    if userNAMEerror(Username) == True:
        SignUp()
        return
    

    if UserEF(Username) == True :
        SignUp()
        return
    elif len(Username) == 0:
        
        print("Username can't be blank")
        SignUp()

        return
        
    elif len(Username) < 6:
        print("Minimum username length is 6")
        SignUp()
        return
    
        
    Password = input("Enter your Password : ")
    if len(Password) == 0:
        print ("Password can't be blank")
        SignUp()
        return
    
    elif len(Password) < 6:
        print ("Minimum password length is 6")
        SignUp()
        return
    
    elif Password == Username :
        print ("Username and password cannot be same ")
        SignUp()
        return
    
    RePassword = input("Re-Enter your Password : ")
        
    if Password != RePassword :
        print (" ")
        print ("Passwords do not match ")
        print (" ")
        SignUp()
        return
        
                
    Address = input("Enter your current address : ")
    if len(Address) == 0:
        print ("Address can't be blank")
        SignUp()
        return

    DOB = input("Enter Date of Birth (DD/MM/YYYY) : ")
    if dateError(DOB) == True :
        SignUp()
        return
    
    Email = input("Enter a valid Email ID : ")
    if emailError(Email) == True :
        SignUp()
        return

    Phno = input("Enter your Phone number : ")
    if phoneError(Phno) == True :
        SignUp()
        return
    
        
    Age = input("Enter your age : ")
    if ageError(Age,DOB) == True :
        SignUp()
        return
    
   
    Data.append(Username)
    Data.append(Password)
    Data.append(Address)
    Data.append(DOB)
    Data.append(Email)
    Data.append(Phno)
    Data.append(Age)

    obj.InputData(Data)
    transferData(obj)
    print ("")
    print ("SignUp complete ") 

class StudentDetails():
    no_of_students = 0

    def __init__(self):

        StudentDetails.no_of_students+=1

        self.StudentData = 0
        self.Name = None
        self.SRN =None
        self.year = None
        self.DOB =None
        self.Phno =None
        self.ISA1 = None
        self.ISA2 = None
        self.ESA1 = None
        self.ISA3 = None
        self.ISA4 = None
        self.ESA2 = None
        self.Assigment_sem1 = None
        self.Assignment_sem2 = None
        self.SGPA1 = None
        self.SGPA2 = None
        self.GPA = None
        

    def InputDataStu(self,lst):
        self.Name = lst[0]
        self.SRN =lst[1]
        self.year = lst[2]
        self.DOB =lst[3]
        self.Phno =lst[4]
        
        

def CreateAccStu():
    print("")
    print(r"\\\ Add New Student to Database///")
    Data1 = []
    obj = StudentDetails()

    Name = input("Enter name of the student :")
    if snameError(Name) == True:
        print("Enter valid name(Eg. No underscores)")
        CreateAccStu()
        return
    
    SRN = input("Enter SRN of the student :")
    if SRNerror(SRN) == True:
        print("SRN error")
        CreateAccStu()
        return
    
    if UserEF(str(SRN),"Data\\student") == True:
        
        CreateAccStu()
        return
    Year = input("Enter the year of the student(Format:First,Second,Third,Fourth) :")
    if Year not in ["First","Second","Third","Fourth"]:
        print("Enter in correct format")
        CreateAccStu()
        return
    DOB = input("Enter DOB of student(format : DD/MM/YYYY :")
    if dateError(DOB) == True:
        CreateAccStu()
        return
    Phno = input("Enter Phone number of student :")
    if phoneError(Phno)== True:
        CreateAccStu()
        return

    Data1.append(Name)
    Data1.append(SRN)
    Data1.append(Year)
    Data1.append(DOB)
    Data1.append(Phno)
    

    obj.InputDataStu(Data1)
    transferDataStu(obj)
    print("")
    print("Student Account successfully added to database")

def transferDataStu(obj):
    path = 'Data\\' + ("student"+obj.SRN)
    f = open(path,"wb+")
    pickle.dump(obj,f)
    f.close()
    
    
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Student:
    txt = "Student Database Operations \n1.Create an account for a student \n2.Add results to a students account \n3.View details of a particular student \n4.Calculate results \n5.Exit "
    
    @staticmethod
    def menu(instance):
        global process
        
        while True: 
            print(" ")
            print (Student.txt)
            prompt = (input("Enter an option :"))
            if prompt =="1":
                CreateAccStu()

            elif prompt =="2":
                EnterMarks()

            elif prompt =="3":
                ViewDetailStu()
                
            elif prompt =="4":
                Calcgrade()
            
            elif prompt == "5":
                global process
                process == False
                break
            
            else:
                print("Invalid Choice")

def ViewDetailStu():
    print("Login to the students profile")
    stu = input("Enter SRN of the student :")
    try:
        fname = open("Data\\"+"student"+str(stu),"rb+")
        f = pickle.load(fname)
    except:
        print("Requested student profile not available")
        ViewDetailStu()
        return

    print("Entered",f.Name,"'s profile")
    print("SRN :",f.SRN)
    print("Year :",f.year)
    print("DOB :",f.DOB)
    print("Phone Number :",f.Phno)
    t = ['EP','EE','EM','MS','CS']
    s = ['CH','EC','EM','CV','CS']
    if f.ISA1:
        print("ISA1 marks ",list(zip(t,f.ISA1)))
    if f.ISA2:
        print("ISA2 marks ",list(zip(t,f.ISA2)))
    if f.ESA1:
        print("ESA1 marks ",list(zip(t,f.ESA1)))
    if f.Assigment_sem1:
        print("Assignment1 marks ",list(zip(t,f.Assigment_sem1)))
    if f.SGPA1:
        print("Semester 1 GPA",f.SGPA1)
    else:
        print("Adequate information not available to get semester1 GPA")
    if f.ISA3:
        print("ISA3 marks ",list(zip(s,f.ISA3)))
    if f.ISA4:
        print("ISA4 marks ",list(zip(s,f.ISA4)))
    if f.ESA2:
        print("ESA2 marks ",list(zip(s,f.ESA2)))
    if f.Assignment_sem2:
        print("Assignment2 marks ",list(zip(s,f.Assignment_sem2)))
    if f.SGPA2:
        print("Semester 2 GPA",f.SGPA2)
    elif ((f.SGPA1) and not(f.SGPA2)):
        print("Adequate information not available for semester2 GPA")
    if f.GPA:
        print("Whole year GPA",f.GPA)
        
    
            

def EnterMarks():
    print("Login to the students profile")
    stu = input("Enter SRN of the student :")
    while True:
        try:
            fname = open("Data\\"+"student"+str(stu),"rb+")
            f = pickle.load(fname)
        except:
            print("Requested student profile not available")
            return

        print("Entered",f.Name,"'s profile")
        txt=("""Enter option 1.ISA1
      option 2.ISA2
      option 3.ESA1
      option 4.ISA3
      option 5.ISA4
      option 6.ESA2
      option 7.Assignment(Sem1)
      option 8.Assingment(Sem2)
      option 9.Exit""")
        print("To enter the marks")
        print(txt)
        opt = int(input("Enter option :"))
        if opt == 1:
            ISA1()
            f.ISA1 =isa1
            
            transferDataStu(f)
        elif opt == 2:
            if f.ISA1:
                ISA2()
                f.ISA2 = isa2
                transferDataStu(f)
            else:
                print("ISA1 results not yet entered, so ISA2 results cannot be entered")

        elif opt ==3:
            if f.ISA2:
                ESA1()
                f.ESA1 = esa1
                transferDataStu(f)
            else:
                print("ISA2 results not yet entered, so ESA1 results cannot be entered")

        elif opt ==4:
            if f.ESA1:
                ISA3()
                f.ISA3 =isa3
                transferDataStu(f)
            else:
                print("Semester 1 results not entered, so semester 2 attributes cannot be entered")

        elif opt ==5:
            if f.ISA3:
                ISA4()
                f.ISA4 = isa4
                transferDataStu(f)
            else:
                print("ISA3 results not yet entered, so ISA4 results cannot be entered")
        elif opt ==6:
            if f.ISA4:
                ESA2()
                f.ESA2 = esa2
                transferDataStu(f)
            else:
                print("ISA4 results not yet entered, so ESA2 results cannot be entered")

        elif opt ==7:
            ASem1()
            f.Assigment_sem1 = asem1
            
            transferDataStu(f)

        elif opt ==8:
            ASem2()
            f.Assignment_sem2 = asem2
            transferDataStu(f)
            
        elif opt ==9:
            break
        else:
            print("Invalid option")
            EnterMarks()
            return
            


asem1 =None
def ASem1():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 15)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Engineering Physics :"))
        EE=int(input("Enter marks obtained in Electrical Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Mechanical Engineering Sciences :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ASem1()
        return
    if EP>15 or EE>15 or EM>15 or MS>15 or CS>15:
        print("Marks entered is greater than max marks")
        ASem1()
        return
    else:
        global asem1
        asem1 = [EP,EE,EM,MS,CS]
    

asem2 =None
def ASem2():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 15)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Engineering Physics :"))
        EE=int(input("Enter marks obtained in Electrical Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Mechanical Engineering Sciences :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ASem2()
        return
    if EP>15 or EE>15 or EM>15 or MS>15 or CS>15:
        print("Marks entered is greater than max marks")
        ASem2()
        return
    else:
        global asem2
        asem2 = [EP,EE,EM,MS,CS]
    
isa1 =None
def ISA1():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 40)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Engineering Physics :"))
        EE=int(input("Enter marks obtained in Electrical Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Mechanical Engineering Sciences :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ISA1()
        return
    if EP>40 or EE>40 or EM>40 or MS>40 or CS>40:
        print("Marks entered is greater than max marks")
        ISA1()
        return
    else:
        global isa1
        isa1 = [EP,EE,EM,MS,CS]
    
isa2 =None
def ISA2():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 40)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Engineering Physics :"))
        EE=int(input("Enter marks obtained in Electrical Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Mechanical Engineering Sciences :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ISA2()
        return
    if EP>40 or EE>40 or EM>40 or MS>40 or CS>40:
        print("Marks entered is greater than max marks")
        ISA2()
        return
    else:
        global isa2
        isa2 = [EP,EE,EM,MS,CS]


esa1 =None
def ESA1():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 100)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Engineering Physics :"))
        EE=int(input("Enter marks obtained in Electrical Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Mechanical Engineering Sciences :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ESA1()
        return
    if EP>100 or EE>100 or EM>100 or MS>100 or CS>100:
        print("Marks entered is greater than max marks")
        ESA1()
        return
    else:
        global esa1
        esa1 = [EP,EE,EM,MS,CS]

isa3 =None
def ISA3():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 40)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Chemistry :"))
        EE=int(input("Enter marks obtained in Electronic Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Civil Engineering :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ISA3()
        return
    if EP>40 or EE>40 or EM>40 or MS>40 or CS>40:
        print("Marks entered is greater than max marks")
        ISA3()
        return
    else:
        global isa3
        isa3 = [EP,EE,EM,MS,CS]
isa4 =None
def ISA4():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 40)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Chemistry :"))
        EE=int(input("Enter marks obtained in Electronic Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Civil Engineering :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ISA4()
        return
    if EP>40 or EE>40 or EM>40 or MS>40 or CS>40:
        print("Marks entered is greater than max marks")
        ISA4()
        return
    else:
        global isa4
        isa4 = [EP,EE,EM,MS,CS]


esa2 =None
def ESA2():
    print("Enter Marks obtained by student in First Semester Assignments(Max Marks 100)")
    #[EP,EE,EM,MS,CS]
    try:
        EP=int(input("Enter marks obtained in Chemistry :"))
        EE=int(input("Enter marks obtained in Electronic Engineering :"))
        EM=int(input("Enter marks obtained in Engineering Math :"))
        MS=int(input("Enter marks obtained in Civil Engineering :"))
        CS=int(input("Enter marks obtained in Computer Science :"))
    except:
        print("Invalid Input please enter integer values only")
        ESA2()
        return
    if EP>100 or EE>100 or EM>100 or MS>100 or CS>100:
        print("Marks entered is greater than max marks")
        ESA2()
        return
    else:
        global esa2
        esa2 = [EP,EE,EM,MS,CS]
        
def calcSGPA(l1,l2,l3,l4):
    #[EP,EE,EM,MS,CS]
    #l1 = ISA1, l2 = ISA2, l3 = ESA
    temp = []
    for i in range(5):
        a = (15*(l1[i]/40))+(15*(l2[i]/40))+(60*(l3[i]/100))+(10*(l4[i]/15))
        temp.append(a)

    s = 0
    for i in temp:
        s = s+(i*4)

    End = s/20
    SGPA =End/9.175
    if SGPA>10:
        return 10
    else:
        return SGPA
    
def Calcgrade():
    stu = input("Enter SRN of the student :")
    
    try:
        fname = open("Data\\"+"student"+str(stu),"rb+")
        f = pickle.load(fname)
    except:
        print("Requested student profile not available")
        return


    sgpa1 = sgpa2 = gpa = None
    if f.ISA1 and f.ISA2 and f.ESA1 and f.Assigment_sem1:
        sgpa1 = calcSGPA(f.ISA1,f.ISA2,f.ESA1,f.Assigment_sem1)
        print("Semester 1",sgpa1)
    if f.ISA3 and f.ISA4 and f.ESA2 and f.Assigment_sem1:
        sgpa2 = calcSGPA(f.ISA3,f.ISA4,f.ESA2,f.Assignment_sem2)
        print("Semester 2",sgpa2)
    print("Whole Year GPA",(sgpa1+sgpa2)/2)
    f.SGPA1,f.SGPA2= sgpa1,sgpa2
    f.GPA = (f.SGPA1 + f.SGPA2)/2
    transferDataStu(f)
    
    
    
    
                    
def SignIn():
    print ("Sign in to your account (press 0 to exit)")
    print ("")
    Username = input("Enter your username  : ")
    
    if Username == '0' :
        print ("Exiting...")
        print (" ")
        LoginPage()

        return
    
    Password = input("Enter your Password : ")

    if Password == '0' :
        print ("Exiting...")
        print (" ")
        LoginPage()

        return
    
    print (" Logging in .  ")
    print ("",end = "")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".",end = "")


    try : 
     
        path = "Data\\teacher" + Username
        f = open(path,'rb')
        custObj = pickle.load(f)


        if Username == custObj.Name and Password == custObj.Password:
            print ("Logged in ")

        
        else :
            print (" Invalid Username/Password ")
            SignIn()
            return
    
    except :
        print (" Invalid Username/Password ")
        SignIn()
        return
        

    
    time.sleep(1)

    opt(custObj)

def opt(custObj):
    global process
    """try:"""
#------------------------------------------------------------------------------
    option = int(input("Enter 1 to enter menu or 0 to exit : "))
    if option == 1 :
        Student.menu(custObj)
        return
    elif option == 0 :
        process  =False
            
    else :
        print ("Invalid option try again ")
        opt(custObj)
#------------------------------------------------------------------------------
    """except:
        print ("Invalid choice")
        opt(custObj)"""

def UserEF(cust1,path = 'Data\\teacher'):
    #checks whether objects are being overriden
    try:
        
        foo = open(path + cust1,'rb')
    except IOError and EOFError and FileNotFoundError and OSError :
        return False

    try:
        tempuser = pickle.load(foo)
    except EOFError:
        return False
    
    if cust1 == tempuser.Name  :
        print (" Account already exists")
        foo.close()
        return True
    
    if path == "Data\\student":
        if cust1 == tempuser.SRN:
            print("Student account already exists")
            return True
        else:
            return False

    else :
        foo.close()
        return False
def userNAMEerror(Username):
    temp = Username
    if set(temp) - {' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '}:
        print("Please enter only alphabets and spaces, No special characters allowed")
        return True
        
def snameError(name):
    a = set(name) - {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '}
    if a:
        return True
    else:
        return False
def SRNerror(SRN):
    #SRN = PES1201800073
    if SRN[0:3] != "PES":
        return True
    elif len(SRN) != 13:
        return True
    try:
        int(SRN[3:])

    except:
        return True

    else:
        return False
    
        

def dateError(date) :
    #DD/MM/YYYY

    try : 
        if date[2] != "/" or date[5] != "/":
            print ("Date not in correct format")
            return True
        
        elif int(date[0:2]) not in range(1,32):
            print ("Wrong Date Type ")
            return True

        elif int(date[3:5]) not in range(1,13):
            print ("Wrong Date Type")
            return True

        elif int(date[6:10]) not in range(1940,2002):
            print ("Not in age limit")
            return True

        elif len(str(date)) == 0:
            print ("Date can't be blank")
            return True

        elif len(str(date)) < 10:
            print ("Invalid date - length")
            return True
        
        else:
            return False

    except TypeError :
        print ("Wrong Date Value")
        return True
    except IndexError :
        print ("Wrong Date Value ")
        return True

def emailError(email) :
    q1 = (email[-4:-1] + email[len(email)-1])
    q2 =(email[-3:-1] + email[len(email)-1])
    q3 =(email[-5:-1] + email[len(email)-1])

    if '@' not in email :
        print ("Invalid email ID  ")
        return True
        
    elif q1 != ".com" and q2 != ".in" and q3 != ".mail" :
        
        
        print ("Invalid email ID ")
        return True

   
    elif len(email) == 0   :
        print ("Invalid email ID ")
        return True

        
    else :
        return False
        
    
def phoneError(phone) :
    for i in phone :
        if int(i) not in range(0,10):
            print ("Invalid phone number1")
            
            break
            return  True
        
    if len(phone) != 10:
        print ("Invalid Phone Number len")
        return True

    else:
        return False
    
def ageError(Age,DOB):
    v = 2018 - int(DOB[6:10]) 
    
    if len(str(Age)) == 0:
        print ("Please enter a valid age")
        return True
    elif int(Age) not in range(17,70):
        print ("Age limit - not satisfied")
        return True
    elif int(Age) not in range(v-1,v+2):
        print ("Date of birth and age dont match")
        return True
    
    else:
        return False
    
    
    

def transferData(obj):
    path = 'Data\\' + ("teacher"+obj.Name)
    f = open(path, 'wb')
    

    pickle.dump(obj,f)
    f.close()



process = True
while process:
    LoginPage()
