class Dzong:
    name="Punakha Dzong" #Initialization of class attributes
    location="Punakha"   #Initialization of class attributes
    year_built=1631      #Initialization of class attributes
	
    def display_history(self,name,year): #Method
        print(f"Name: {name}")
        print(f"Location: {self.location}")
        print(f"Year:{year}")
        
dzong=Dzong() #Creation of objects
dzong.display_history("Paro",1980) #calling method
dzong1=Dzong()
dzong1.display_history("Thimphu",1898)
