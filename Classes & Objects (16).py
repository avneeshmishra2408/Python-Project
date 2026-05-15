class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name,"Tennis Player")
        elif self.occupation == 'actor':
            print(self.name,"Actor")

    def speaks(self):
        print(self.name , "How are you ?")

tom = Human("Tom Cruise" , "actor")
tom.do_work()
tom.speaks()