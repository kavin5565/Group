class car:
    #constructor
    def __init__(self,window,tyres,engine):
       self.window=window
       self.tyres=tyres
       self.engine=engine
    #self isliye use hote hai qki hum self k through hum koi bhi attribute jo bhi car ki class k andrr hota
     # hai hum usko directly call kr skte h

car1=car(4,4,"petrol")
print(car1.tyres)
print(car1.engine)

class parrot:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

        blu=parrot("monu","blue")
        print(blu.name)
        print("self.inn")