class Employee():
    pass
employee=Employee()
employee.salary=122000
employee.firstname='alice'
employee.lastname='wonderland'
print(employee.firstname+" "+employee.lastname+" "+"$"+str(employee.salary))

class Dog:
    species=['canis lupus']
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.state="sleeping"
    def command(self,x):
        if x==self.name:
            self.bark(2)
        elif x=="sit":
            self.state="sit"
        else:
            self.state="wag tail"
    def bark(self,freq):
        for i in range(freq):
            print("["+self.name+"]: Woof!")
bello=Dog("bello","black")
aliz=Dog("aliz","grey")
print(bello.color)
print(aliz.color)
bello.bark(1)
aliz.command("sit")
print("[aliz]: "+aliz.state)
bello.command("no")
print("[bello]: "+bello.state)
aliz.command("alice")
bello.species+=["wulf"]
print(len(bello.species)==len(aliz.species))
