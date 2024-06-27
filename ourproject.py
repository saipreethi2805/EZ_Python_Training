ov = {89: 70, 87: 40, 104: 50,47:69}
nv = {89: 35, 87: 50, 104: 40,106:45}
class File:
    def __init__(self, ov, nv):
        self.ov = ov
        self.nv = nv
        self.ms = {} 
        self.msc = 0 
        

    def create(self):
        self.ov={}
        self.nv={}
        
        n1=int(input('enter the numbers in old version: '))
        n2=int(input('enter the numbers in new version: '))

        for i in range (n1):
            r=int(input('enter the roll number: '))
            m=int(input('enter the marks: '))
            self.ov[r]=m
        for i in range (n2):
            r=int(input('enter the roll number: '))
            m=int(input('enter the marks: '))
            self.nv[r]=m
    

    def add(self):
        choice = input("Enter 'Yes' if you want to add a roll number from the old version: ")
        if choice == "yes":
            rn = int(input("Enter the roll number to add from the old version: "))
            if rn in self.ov:
                print("Roll number is already existing")
            m=int(input('enter the marks: '))
            self.ov[rn]=m
            print(ov)
        choice = input("Enter 'Yes' if you want to add a roll number from the new version: ")
        if choice == "yes":
            rn = int(input("Enter the roll number to add from the new version: "))
            if rn in self.nv:
                print("Roll number is already existing")
            m=int(input('enter the marks: '))
            self.nv[rn]=m
            print(nv)
    
    def remove(self):
        choice = input("Enter 'Yes' if you want to remove a roll number from the old version: ")
        if choice == "yes":
            rn = int(input("Enter the roll number to remove from the old version: "))
            if rn in self.ov:
                self.ov.pop(rn)
                print(ov)
            else:
                print("Roll number not found in the old version.")
        
        choice = input("Enter 'Yes' if you want to remove a roll number from the new version: ")
        if choice == "yes":
            rn = int(input("Enter the roll number to remove from the new version: "))
            if rn in self.nv:
                self.nv.pop(rn)
                print(nv)
            else:
                print("Roll number not found in the new version.")

    def update(self):
        choice=input("Enter Yes if you want to change the old version: ")
        if choice=="yes":
            while True:
                rn=int(input("enter the roll number you want to change:"))
                if rn==-1:
                    break
                marks=int(input("enter the marks:"))
                self.ov[rn]=marks
        choice=input("Enter Yes if you want to change the New version: ")
        if choice=="yes":
            while True:
                rn=int(input("enter the roll number you want to change:"))
                if rn==-1:
                    break
                marks=int(input("Enter the marks"))
                self.nv[rn]=marks

    def generate_migration_script(self):
        self.msc += 1 
        added = []
        modify= []
        removed= []

        for rn,m in self.nv.items():
            if rn not in self.ov:
                added.append([rn, m]) 
            elif self.ov[rn]!=m:
                modify.append([rn, self.ov[rn], m]) 

        for rn,m in self.ov.items():
            if rn not in self.nv:
                removed.append([rn, m])
        # self.ms[self.msc]=[]  
        ms = {}
        ms['A'] = sorted(added)
        ms['R']=sorted(removed)
        ms['M']=sorted(modify)
        
        self.ms[self.msc] = ms 

        return added ,removed,modify
    
    
    
    def displayMS(self, msID): 
        ms = '' 
        mst = self.ms[msID]
        for rn,m in (mst['A']):
            ms+=f'A {rn:3d} {m:3d}\n'
        for rn,m in (mst['R']):
            ms+=f'R {rn:3d} {m:3d}\n'    
        for rn,ov,nv in (mst['M']):
            ms+=f'M {rn:3d} {ov:3d} {nv:3d}\n'
        print(ms)

    
    
    def rollback_migration(self, msID): 
        t = self.nv 
        a = self.ms[msID]['A'] 
        r=self.ms[msID]['R']
        mo=self.ms[msID]['M']
        nv = self.nv 
        print(self.ov)
        print(nv) 
        for rn,m in r: 
            nv[rn]=m 
        for r,o,n in mo: 
            nv.pop(r) 
            nv[r]= o  
        for rn,m in a: 
            nv.pop(rn) 
        self.nv = dict(sorted(self.nv.items()))  
        print(nv)
        self.ov = t 


r1 = File(ov, nv)
def Guidelines():
    print("Enter 1 to create")
    print("Enter 2 to update")
    print("Enter 3 to add") 
    print("Enter 4 remove")
    print("Enter 5 to Generate migration script")
    print("Enter 6 to display")
    print("Enter 7 to rollback")

while True : 
    Guidelines() 
    choice = int(input('Enter your choice : '))
    if choice==-1:
        break
    match choice :
        case 1 : 
            r1.create()
        case 2 :
            r1.update 
        case 3 :
            r1.add() 
        case 4 :
            r1.remove()
        case 5 :
            r1.generate_migration_script()
            print(r1.ov)
            print(r1.nv)
            print(r1.ms)
        case 6:
            msID = int(input("Enter migration script ID: "))
            r1.displayMS(msID) 
        case 7:
            msID = int(input("Enter migration script ID: ")) 
            r1.rollback_migration(msID) 
        case _ :
            print("Invalid choice")

            
