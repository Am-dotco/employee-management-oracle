#Program for Reading Complete Records from Employee Table along with Column Names
#OracleSelectRecordsWithMetaDtaEx2.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/root@localhost/orclpdb")
        cur=con.cursor()
        sq="select * from employee"
        cur.execute(sq)
        #Code for Getting Meta Data (Column Names)
        print("-----------------------------------------")
        for colname in [colinfo[0] for colinfo in cur.description]:
            print("\t{}".format(colname),end="\t")
        print()
        #Code for Getting Records
        print("-----------------------------------------")
        records=cur.fetchall()
        if(len(records)==0):
            print("\t\tNo records found")
        else:
            for record in records:
                for value in record:
                    print("\t{}".format(value),end="\t")
                print()
        print("-----------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)

#Main Program
