from ArchicadDG import Point

def test():
    print dir(Point)
    pt=Point(12,22)
    print str(pt.GetX())
    pt.Offset(10,20)
    print str(pt.GetX())+"+"+str(pt.GetY())
    pt1=Point(22,42)
    print str(pt==pt1)
    pass