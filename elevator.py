count=0
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    def __str__(self):
        return "Current floor: {}".format(self.current)
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current +=1
        else:
            print("No such floor")
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > 0:
            self.current -=1
        else:
            print("No such floor")
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        global count
        count=0
        while True:
            if self.current == floor:
                print("Floor reached")
                break
            elif floor < self.current:
                self.down()
                count=count-1
            elif floor > self.current:
                self.up()
                count=count+1
elevator = Elevator(-1, 10, 0)
while True:
    tf=int(input("Enter the required floor: "))
    print(elevator.current)
    elevator.go_to(tf)
    print("Elevator movement: ",count)
    
