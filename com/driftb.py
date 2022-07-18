class Driftbottle:
 
    def __init__(self, number, is_empty = True):
        self.number = number
        self.is_empty = is_empty
        self.message = None
   
    def insert_message(self):
        if self.is_empty == True:
            self.message = input(str("insert message:"))
            self.is_empty = False
            return self.message
        else:
            print("it already has a message")
            return self.message
 
    def retrieve_message(self):
        if self.is_empty == True:
            print("Nothing")
        elif self.is_empty == False:
            print("retrieve message from the bottle", self.message)
            self.is_empty = True

bottle1 = Driftbottle(1)
bottle1.insert_message()
bottle1.insert_message()
bottle1.retrieve_message()



