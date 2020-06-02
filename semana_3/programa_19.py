class BucleFor:

    def __init__(self):
        pass

    def bucle1(self):
        for i in range(5):
            print(i)
    
    def bucle2(self):
        for i in range(3,5):
            print(i)
        
    def bucle3(self):
        for i in range(1,10,3):
            print(i)

    def bucle4(self):
        for i in range(10,1,-4):
            print(i)

objeto = BucleFor()
objeto.bucle4()
