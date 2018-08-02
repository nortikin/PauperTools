from ArchicadDG import Rect

def rect_print(rect,title):
    top=rect.GetTop()
    left=rect.GetLeft()
    right=rect.GetRight()
    bottom=rect.GetBottom()

    print "_____"+title+"_____"
    print "top("+str(top)+")"
    print "left("+str(left)+")"
    print "right("+str(right)+")"
    print "bottom("+str(bottom)+")"
    pass



def run_test():
    rct1=Rect(1,1,40,60)
    rect_print(rct1,"one")
    rct2=Rect(20,20,60,60)
    rect_print(rct2,"two")
    print "IsIntersecting:"+str(rct1.IsIntersecting(rct2))
    int_rct=rct1.Intersect(rct2)
    rect_print(int_rct,"three")
    pass

