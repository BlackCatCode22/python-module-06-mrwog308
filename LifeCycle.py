class Party:

    def __init__(self):
        self.x = 0
        print('built party')

    def party(self):
        self.x = self.x + 1
        print("party", self.x)

    def __del__(self):
        print('killer party', self.x)

class Concert:

    def __init__(self):
        self.x = 0
        print('built concert')

    def concert(self):
        self.x = self.x + 1
        print("concert", self.x)

    def __del__(self):
        print('killer concert', self.x)

pa = Party()
co = Concert()
pa.party()
pa.party()
pa.party()
pa = 'parties'
co.concert()
co.concert()
co.concert()
# pa = 'parties' 
co = 'concerts'
print('thats a lot of',pa)
print('thats a lot of',co)
