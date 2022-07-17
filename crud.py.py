import csv

def save():
        rno=int(input("Enter rno"))
        name=input("Enter Name")
        marks=float(input("Enter marks"))
        record=[rno,name,marks]
        f=open("database.csv","a",newline="\n")
        writer=csv.writer(f)
        writer.writerow(record)
        f.close()
        print("Data Saved")
def disp():
        f=open("database.csv")
        reader=csv.reader(f)
        for row in reader:
                print(row[0],row[1],row[2])
        f.close()
def modify():
        r=int(input("Enter rno to be modified"))
        f=open("database.csv")
        reader=csv.reader(f)
        l=[]
        for row in reader:
                if int(row[0])==r:
                        print("Current details are")
                        print(row[0],row[1],row[2])
                        row[1]=input("Enter new name")
                        row[2]=float(input("Enter new marks"))
                        l.append(row)
                        
                else:
                        l.append(row)
                        
        f.close()
        f=open("database.csv","w",newline="\n")
        writer=csv.writer(f)
        for row in l:
                writer.writerow(row)
        f.close()
def delete():
        None

ch=1
while ch!=5:
        print("Press 1 to save")
        print("Press 2 to disp")
        print("Press 3 to modify")
        print("Press 4 to delete")
        ch=int(input("Enter choice"))
        if ch==1:
                save()
        elif ch==2:
                disp()
        elif ch==3:
                modify()
        elif ch==4:
                delete()
