#Program for Updating Record in employee Table
import oracledb as orc
def updaterecord():
    while(True):
        try:
            conobj=orc.connect("system/root@localhost/orclpdb")
            curobj=conobj.cursor()
            print("-----------------------------------------")
            empno=int(input("Enter Employee Number for Updating:"))

            # First check whether the employee number exists
            curobj.execute("select * from employee where eno=%d"%(empno,))
            if curobj.fetchone() is None:
                print("No record exists for Employee Number",empno)
                print("-----------------------------------------")
                break      # stop here, do not go further

            # Record found, now take the new data
            empname=input("Enter Employee New Name:")
            empsal=float(input("Enter Employee New Salary:"))
            empcomp=input("Enter Employee New Company Name:")
            print("-----------------------------------------")

            uq="update employee set name='%s', sal=3%d, compname='%s' where eno=%d"%(empname,empsal,empcomp,empno)
            curobj.execute(uq)
            conobj.commit()
            print(curobj.rowcount,"Employee Record Updated")
            print("-----------------------------------------")
            break
        except orc.DatabaseError as db:
            print("Problem in Oracle:",db)
            break
        except ValueError:
            print("Please enter a valid number")