# GeometryPy Documentation
Version: 1. 0. 1

Status: Under Construction

### Intoduction
GeometryPy is an easy way to draw simple graphics on the terminal window. This software is meant for beginners to learn how to code. Get code [here](https://biancanev.github.io/The-Potato-Place/store/apps/geometryPy).

### Getting Started
In order to start using geometryPy, you need to create a `canvas`. To do this, there is a `canvas` class. To create a basic canvas, use the function `setCanvas()`, which takes two parameters: `width`, `height`. You can see how big the canvas you created is by using the `testCanvas()` function. Here is an example of a fully set up program:
```python
#Basic Setup
import geometryPy.py
canvas.setCanvas(100, 100)
canvas.testCanvas(100, 100)
print("The setup is done!")
```
Here is a full list of canvas functions:
| Function | Use |
| --- | --- |
| `setCanvas(canvas, width, height)` | Creates a canvas with dimensions `width` x `height`. `canvas` is an object `width` and `height` are integers. |
| `testCanvas(canvas)` | Prints a full colored canvas with the dimensions of canvas `canvas`. `canvas` is an object. |
| `invertColors()`* | Inverts the terminal colors. |

\* Note that `invertColors()` has been depreciated as of v0.5.0 
### Basics
The two most basic classes of this program are the `draw` and `analyze` classes. The `draw` class' basic function is the `render()` function, which takes five arguments: `shape`, `length`, `width`, `xpos`, `ypos`. Therefore, in this example:
```python
draw.Render("rectangle", 10, 40, 0, 0)
```
the terminal will draw out a 10 x 40 rectangle at (0, 0), or the top left corner. The coordinate system used in this library places the origin(0,0) at the top left and the maximum(width, height) at the bottom right.
Here is a full list of `draw` class functions
| Function | Use |
| --- | --- |
| `Shape(shape, width, height, xpos, ypos)` | Defines the given `shape` with the dimensions of `width` x `height` at (`xpos`, `ypos`), but *does not draw it*. This is usually used in conjunction with the `paint()` or one of the `animate()` transformations. `shape` should be a string. `length`, `width`, `xpos`, and `ypos` should be integers. Current supported `shape` are: `"circle"`, `"triangle"`, and `"rectangle"`. |
| `Render(shape, width, height, xpos, ypos)` | Draws the given `shape` with the dimensions of `width` x `height` at (`xpos`, `ypos`). `shape` should be a string. `length`, `width`, `xpos`, and `ypos` should be integers. Current supported `shape` are: `"circle"`, `"triangle"`, and `"rectangle"`. |
| `Paint(obj)` | Prints the object `obj` onto the canvas. |
| `Translate(obj, origin, xmov, ymov)` | Moves the object specified by `obj` by `xmov` on the x-axis and `ymov` on the y-axis. The translation is based at the `origin`. `obj` should be an object. `origin` should be a tuple. `xmov` and `ymov` should be integers. |
| `Rotate(obj, origin, deg)` | Rotates the object defined by `obj` by `deg` degrees at the `origin`. `obj` should be an object. `origin` should be a tuple. `deg` should be a float. |
| `Dilate(obj, origin, scale)` | Scales the object defined by `obj` by a scale of `scale` based at the `origin`. `obj` should be an object. `origin` should be a tuple. `scale` should be a float. |
| `Combine(obj1, obj2)` | Combines objects, `obj1` and `obj2` to form a complex shape. `obj1` and `obj2` should be objects. |

Note that all `origin` are located at the top left of the shape

The `analyze` class does not actually draw shapes, but rather gives a detailed analysis on a hypothetical shape.
Here is a full list of `analyze` class functions:
| Function | Use |
| --- | --- |
| `Rect(width, height, xpos, ypos)` | Gives area, vertices, and position of hypothetical rectangle with given dimensions `width` x `height` at location (`xpos`, `ypos`). All parameters are integers. |
| `RightTriangle(base, height, xpos, ypos)` | Gives area, vertices, and position of hypothetical right triangle with given dimensions `base` x ` height` at location (`xpos`, `ypos`). All parameters are integers. |
| `RegularPolygon(sides, length, xpos, ypos)` | Gives area, vertices, and position of hypothetical regular polygon with `sides` number of sides and with a common side length of `length` located at position (`xpos`, `ypos`). All parameters are integers. |

### Basic Example 
```python
#Basic Drawing
import geometryPy.py
#Initialize Canvas
canvas.setCanvas(100,100)

#Begin Drawing
ellipse1 = draw.Shape('ellipse', 10, 5, 50, 50)#ellipse
rect1 = draw.Shape('rectangle', 10, 20, 45, 50)#rectangle
shape1 = draw.Combine(ellipse1, rect1)#creates complex shape
draw.Rotate(shape1, (10, 5), 45)

#Other Python scripts can be included too!
print("Hello World")
print(10+2)
```

### Advanced
You can begin implementing more advanced functions to draw more complex objects.

### Shading
> Please note that shading is currently still under work and may not work as you would like.
>
> For more information contact us.

The `shade` class is a good way to add dimensions to your drawing. Here is a list of functions in the class:
| Function | Use |
| --- | --- |
| `shadeShape(obj, style)` | Shades the shape `obj`. You can customize the shading style using `style`. Current styles are `normal` and `textured.`|

### Animation
The `animate` class is a great tool to make simple animations. First define an animation sequences as a variable using the `animate()` function.
```python
import geometryPy.py
canvas1 = canvas()
canvas1.setCanvas(100,100)
scene1 = animate()
```
This will create a timeline. Default values for this timeline are a duration of 30 seconds and a framerate of 30 frames per second. You can change these values by using:
```python
scene1.length = #your duration
scene1.framerate = #FPS
```
Next, draw a shape just as you would in a drawing.
```python
body = draw.Shape("rectangle", 10, 5, 50, 50)
```
Similar to the `draw` class, the `animate` class also has `translate()`, `rotate()`, and `scale()` functions. The difference is that there are new parameters: `obj` `pos1`, `pos2` `duration`. Therefore, a fully coded animation would be:
```python
import geometryPy.py
#setup animation area
canvas1 = canvas()
canvas1.setCanvas(100,100)
#create a scene
scene1 = animate()
scene1.length = 5
scene1.framerate = 60
#create the object
body = draw.Shape("rectangle", 10, 5, 50, 50)
#animate the object
animate.translate(body, (50, 50), (60, 60), 5)#move from positon(50, 50) to positon (60, 60) in 5 seconds
```
A full list of functions is here:
| Function | Use |
| --- | --- |
| `animate()` | Create a new animation scene. Editable values are `animate().length` and `animate().framerate` which edit the duration of the animation and the framerate of the animation, respectively. |
| `translate(obj, pos1, pos2, duration)` | Move an object `obj` from `pos1` to `pos2` in `duration` seconds. `obj` should be an object. `pos1` and `pos2` should be tuples. `duration` should be an integer or float. |
| `rotate(obj, pos1, pos2, duration)` | Rotate an object `obj` from `pos1` to `pos2` in `duration` seoconds. `obj` should be an object. `pos1` and `pos2` should be tuples. `duration` should be an integer or float. |
| `scale(obj, size, duration)` | Scale an object `obj` from its current size by a scale of `size` in `duration` seconds. `obj` should be an object. `scale` and `duration` should be integers or floats. |
| `destroy(obj)` | Destroys all instances of object `obj` |
| `createTimeline(name)`\* | Creates an accessible timeline called `name` in order to view all animation sequences |

\*`createTimeline()` has been depreciated since v.0.5.0

### Versions
| Tag | Release Date | Status | Notes |
| :---: | :---: | :---: | --- |
|v.0.1.0 | 5/2/20 | Unstable | N/a |
|v.0.1.1 | 5/7/20 | Stable | Fixed bugs \[*Depreciated*\] |
|v.0.2.0 | 5/28/20 | Stable | First stable release \[*Depreciated*\] |
|v.0.3.0 | 6/5/20 | Unstable | Added advanced functions \[*Depreciated*\] |
|v.0.4.0 | 6/15/20 | Unstable | Fixed bugs \[*Depreciated*\] |
|v.0.5.0 | 6/23/20 | Stable | Fixed bugs \[*Depreciated*\] |
|v.1.0.0 | 7/5/20 | Stable | Released for commercial use |
|v.1.0.1(Curr) | 7/10/20 | Unstable | Added animation class |
