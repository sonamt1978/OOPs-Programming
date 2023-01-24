class Dzong:
    def __init__(self):
        self.name1="Sonam"
        self.location1="Thimphu"
        self.built1=1897
        
    def display_history(self):
        print(f"Name: {self.name1}")
        print(f"Location: {self.location1}")
        print(f"Year: {self.built1}")
    
dzong=Dzong()
dzong.display_history()

dzong_1=Dzong()
dzong_1.display_history()

dzong_2=Dzong()
dzong_2.display_history()
