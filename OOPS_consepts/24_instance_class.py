class flowers:
    Fragrance="fresh"#class attribute

    def __init__(self,name,colour,Fragrance):
        self.name=name              #instance attributes
        self.colour=colour
        self.Fragrance=Fragrance    #overrides class attributes

    def get_fragrance(self):
        print(f"the tree is full of fragrant",{self.name},"and the fragrance was",{self.Fragrance})


f=flowers("chafa","yellow","floral")
print(f.Fragrance)    #will always prints instance
print(flowers.Fragrance) #will always print class attributes

