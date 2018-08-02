## Point Class

### Import
```
from ArchicadDG import Point
``` 

### Example
[demo](../Scripts/Tests/dg_point_test.py)


### Functions

* **constructor(short x,short y)**
* Class constructor.
```
pt1=Point(1,1)
pt2=Point(10,20)
```

* **SetX(short x,short y)**
* **None**
* Sets the x, y coordinates of the point.
```
pt1.Set(4,4)
pt2.Set(40,60)
```


* **SetX(short x)**
* **None**
* Sets the x coordinate of the point.

```
pt1.SetX(5)
pt2.SetX(12)
```

* **GetX()**
* **short**
* Retrieves the x coordinate of the point.

```
x1=pt1.GetX()
x2=pt2.GetX()
```

* **SetY(short y)**
* **None**
* Sets the y coordinate of the point.

```
pt1.SetY(6)
pt2.SetY(18)
```

* **GetY()**
* **short**
* Retrieves the y coordinate of the point.

```
x1=pt1.GetY()
x2=pt2.GetY()
```

* **Offset(short x,short y)**
* **None**
* Moves the point with the specified offset.

```
pt1.Offset(9,33)
pt2.Offset(13,44)
```

* **operator!=**
* **Boolean**
* Operator != for Point objects.

```
res=pt1!=pt2
```

* **operator==**
* **Boolean**
* Operator == for Point objects.

```
res=pt1==pt2
```
