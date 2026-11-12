#Program for Reading Single Record from Employee Table-fetchone
import oracledb as orc
def selectsinglerecords():
    try:
        con=orc.connect("system/root@localhost/orclpdb")
        cur=con.cursor()
        kl=int(input("enter employee id for single record:"))
        sq="select * from employee where eno=:%d"%kl
        cur.execute(sq,(kl,))
        print("-----------------------------------------")
        record=cur.fetchone()
        if record:
            for value in record:
                print("\t{}".format(value),end="\t")
            print()
        else:
            print("Record not found")
        print("-----------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
