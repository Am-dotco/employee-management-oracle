#EmpMainProject.py<------Main Program
from EmpMenu import menu
from EmpAdd import insertrecord
from EmpView import selectrecords
from EmpViewSingle import selectsinglerecords
from EmpUpdate import updaterecord
from EmpDelete import deleterecord
from EmpSearch import EmpSearch

while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice: "))
        match(ch):
            case 1:
                insertrecord()
            case 2:
                deleterecord()
            case 3:
                updaterecord()
            case 4:
                selectsinglerecords()
            case 5:
                selectrecords()
            case 6:
                EmpSearch()
            case 7:
                print("\tTHX FOR USING PROJECT")
                break
            case _: #Default case block
                print("\tUR SELECTION OF CHOICE IS WRONG-TRY AGAIN")
    except ValueError:
        print("\t\tDON'T ENTER ALNUMS,STRS AND SYMBOLS-TRY AGAIN")
