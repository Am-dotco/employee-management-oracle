#Program for Deleting the Record from Employee
#By accepting employee Number
#OracleDeleteRecordEx3.py
import oracledb as orc
def deleterecord():
    while(True):
        try:
            conobj=orc.connect("system/root@127.0.0.1/orclpdb")
            curobj=conobj.cursor()
            #Accept employee number
            print("-------------------------------------------------------")
            empno=int(input("Enter Employee Number to Delete Record:"))
            dq="delete from employee where eno=%d"%(empno)
            curobj.execute(dq)
            conobj.commit()
            if(curobj.rowcount>0):
                print("{} Employee Record Deleted--verify".format(curobj.rowcount))
            else:
                print("Employee Record Does not Exist")
            print("-------------------------------------------------------")
            ch = input("Do you want to Delete Another Record?(yes/no):")
            if (ch.lower() == "no"):
                print("Thax for Using Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle:",db)
        except ValueError:
            print("Don't Enter Alnums,strs and symbols for empno")

