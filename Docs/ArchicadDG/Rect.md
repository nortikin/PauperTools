## Rect Class

### Import
```
from ArchicadDG import Rect
``` 

### Example
[demo](../../Scripts/Tests/dg_rect_test.py)

### Testing
```
import Tests.dg_rect_test as rect_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        #archicad dg rect testing
        rect_test.run_test()
        
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        print 'PyMain.FreeData' #must be print this message
        pass

```

### Class Functions

* **constructor([Point](Point.md) pt1,[Point](Point.md) pt2)**
* **constructor([Point](Point.md) loca,short width,short height)**
* **constructor(short left,short top,short right,short bottom)**
* Class constructor.
```
rct1=Rect(Point(1,1),Point(40,60))
rct2=Rect(Point(10,20),20,35)
rct3=Rect(5,8,55,88)
```

* **operator!=**
* **Boolean**
* Operator != for Point objects.

```
res=rct1!=rct2
```

* **operator==**
* **Boolean**
* Operator == for Point objects.

```
res=rct1==rct2
```

* **Set(Rect src)**
* **None**
* Sets the rectangle.
```
rct1.Set(rct2)
```

* **Set([Point](Point.md) pt1,[Point](Point.md) pt2)**
* **None**
* Sets the rectangle from the given points (left-top and right-bottom vertices).
```

```

* **Set([Point](Point.md) pt,short width,short height)**
* **None**
* Sets the rectangle from the given point (left-top), and from the sizes.
```

```

* **Set(short left,short top,short right,short bottom)**
* **None**
* Sets the rectangle from the coordinates (left-top and right-bottom).
```

```

* **SetLeft(short left)**
* **None**
* Sets the left side of the rectangle.
```

```

* **GetLeft()**
* **short**
* Retrieves the left side of the rectangle.
```

```

* **SetTop(short top)**
* **None**
* Sets the top side of the rectangle.
```

```

* **GetTop()**
* **short**
* Retrieves the top side of rectangle.
```

```

* **SetRight(short right)**
* **None**
* Sets the right side of the rectangle.
```

```

* **GetRight()**
* **short**
* Retrieves the right side of rectangle.
```

```

* **SetBottom(short right)**
* **None**
* Sets the bottom side of the rectangle.
```

```

* **GetBottom()**
* **short**
* Retrieves the bottom side of rectangle.
```

```

* **SetLeftTop([Point](Point.md) pt)**
* **None**
* Sets the left and top sides of the rectangle.
```

```

* **GetLeftTop()**
* **[Point](Point.md)**
* Retrieves the left and top sides of the rectangle.
```

```

* **SetLeftBottom([Point](Point.md) pt)**
* **None**
* Sets the left and bottom sides of the rectangle.
```

```

* **GetLeftBottom()**
* **[Point](Point.md)**
* Retrieves the left and bottom sides of the rectangle.
```

```

* **SetRightTop([Point](Point.md) pt)**
* **None**
* Sets the right and top sides of the rectangle.
```

```

* **GetRightTop()**
* **[Point](Point.md)**
* Retrieves the right and top sides of the rectangle.
```

```

* **SetRightBottom([Point](Point.md) pt)**
* **None**
* Sets the right and bottom sides of the rectangle.
```

```

* **GetRightBottom()**
* **[Point](Point.md)**
* Retrieves the right and bottom sides of the rectangle.
```

```

* **SetCenter([Point](Point.md) pt)**
* **None**
* Sets the center of the rectangle.
```

```

* **GetCenter()**
* **[Point](Point.md)**
* Retrieves the center of the rectangle.
```

```

* **SetWidth(short width)**
* **None**
* Sets the width of the rectangle.
```

```

* **GetWidth()**
* **short**
* Retrieves the width of the rectangle.
```

```

* **SetHeight(short height)**
* **None**
* Sets the height of the rectangle.
```

```

* **GetHeight()**
* **short**
* Retrieves the height of the rectangle.
```

```

* **SetSize(short width,short height)**
* **None**
* Sets the size of the rectangle.
```

```

* **Move(short dx,short dy)**
* **None**
* Moves the rectangle.
```

```

* **Resize(short dx,short dy)**
* **None**
* Resizes the rectangle.
```

```

* **Inflate(short dx,short dy)**
* **None**
* Inflates the rectangle.
```

```

* **IsEmpty()**
* **Boolean**
* Checks if the rectangle is empty.
```

```

* **Contains([Point](Point.md) pt)**
* **Boolean**
* Checks if the rectangle contains the specified point.
```

```

* **Contains(short x,short y)**
* **Boolean**
* Checks if the rectangle contains the specified point, given with x and y coordinates.
```

```

* **IsIntersecting(Rect other)**
* **Boolean**
* Check whether the current rectangle intersects with another rectangle.
```

```

* **Intersect(Rect other)**
* **Boolean**
* Get the intersection of the current rectangle and the other rectangle
```

```

