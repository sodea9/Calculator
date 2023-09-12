class Operator():
    def __init__(self):
        self.op = ""
    
    def get(self):
        return self.op
    
    def set(self, newOp):
        self.op = newOp