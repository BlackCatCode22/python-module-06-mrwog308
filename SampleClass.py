class Party:

   def __init__(self):
     self.x = 0

   def party(self) :
     self.x = self.x + 1
     print("party",self.x)

class Concert:

   def __init__(self):
     self.x = 0

   def concert(self) :
     self.x = self.x + 2
     print("concert",self.x)

an = Party()
co = Concert()
an.party()
an.party()
an.party()
co.concert()
co.concert()
co.concert()