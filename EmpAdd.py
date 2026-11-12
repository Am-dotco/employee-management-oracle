#Program for accepting Employee Deatils from KBD
# and Insert into employee table
#OracleInsertRecordEx2.py
import oracledb as orc
def insertrecord():
    while(True):
        try:
            conobj=orc.connect("system/root@localhost/orclpdb")
            curobj=conobj.cursor()
            #Read Employee Values
            print("----------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            empcompname=input("Enter Employee Company Name:")
            print("----------------------------------------------")
            iq="insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,empcompname)
            curobj.execute(iq )
            conobj.commit()
            print("{} Employee Record Inserted into employee Table--verify".format(curobj.rowcount))
            print("----------------------------------------------")
            ch=input("Do you want to Insert Another Record?(yes/no):")
            if(ch.lower()=="no"):
                print("Thax for Using Program")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle:",db)
        except ValueError:
            print("Don't Enter Alnums,strs and symbols for empno,salary")
#Main Program
