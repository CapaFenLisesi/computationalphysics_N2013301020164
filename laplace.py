class Position(object):
    """Represent a position in 2-d Euclidean space

    attributes:x,y
    """
    def print_pos(self):
        print '%.4f,%4f' %(self.x,self.y)
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def __str__(self):
        return '(%.4f,%.4f)' %(self.x,self.y)
    def __add__(self,other):
        final=Position()
        final.x=self.x+other.x
        final.y=self.y+other.y
        return final
       
p_1=Position(1.0,2.0)
p_2=Position(3.0,4.0)
p_3=p_1+p_2
p_3.print_pos()

