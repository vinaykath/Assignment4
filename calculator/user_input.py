class UserInput:
    def __init__(self, a, b, action):
        self.a= a
        self.b= b
        self.action= action 
        #keeping the operation
    def result(self):
        return self.action(self.a, self.b) 
    #Storing the results