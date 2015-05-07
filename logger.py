
class Logger():
    def __init__(self,isEnabled=True):
        self.isEnabled=isEnabled
    def d(self,message):
        if self.isEnabled:
            self.show('DEBUG:\n '+message+" \n")

    def i(self,message):
        if self.isEnabled:
            self.show('INFO:\n '+message+" \n")


    def show(self,message):
        print message
        
