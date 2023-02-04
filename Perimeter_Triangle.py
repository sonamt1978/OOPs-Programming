class Triangle:
    def __init__(self,s1,s2,s3):
        self.a=s1
        self.b=s2
        self.c=s3
    def peri(self):
        perimeter=self.a+self.b+self.c
        
        print(f"Perimeter is:", perimeter)
side1 = int(input("Enter side 1:"))
side2 = int(input("Enter side 2:"))
side3 = int(input("Enter side 3:"))
sides = Triangle(side1,side2,side3)
sides.peri()
