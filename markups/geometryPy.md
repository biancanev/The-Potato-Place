# geometryPy Documentation
Version: 1. 0. 0

Status: Stable

### Intoduction
geometryPy is an easy way to draw simple graphics on the terminal window. This software is meant for beginners to learn how to code.

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
| `setCanvas(width, height)` | Creates a canvas with dimensions `width` x `height`. All parameters are integers |
| `testCanvas(width, height)` | Prints a fully colored canvas with dimensions `widht` x `height`. All parameters are integers |
| `invertColors()` | Inverts the terminal colors |

### Basics
The two most basic classes of this program are the `draw` and `analyze` classes. The `draw` class' basic function is the `render()` function, which takes five arguments: `shape`, `length`, `width`, `xpos`, `ypos`. Therefore, in this example:
```python
draw.Render("rectangle", 10, 40, 0, 0)
```
the terminal will draw out a 10 x 40 rectangle at (0, 0), or the top left corner.
Here is a full list of `draw` class functions
| Function | Use |
| --- | --- |
| `Shape(shape, width, height, xpos, ypos)` | Defines the given `shape` with the dimensions of `width` x `height` at (`xpos`, `ypos`), but *does not draw it*. `shape` should be a string. `length`, `width`, `xpos`, and `ypos` should be integers. Current supported `shape` are: `"circle"`, `"triangle"`, and `"rectangle"` |
| `Render(shape, width, height, xpos, ypos)` | Draws the given `shape` with the dimensions of `width` x `height` at (`xpos`, `ypos`). `shape` should be a string. `length`, `width`, `xpos`, and `ypos` should be integers. Current supported `shape` are: `"circle"`, `"triangle"`, and `"rectangle"` |
| `Translate(obj, origin, xmov, ymov)` | Moves the object specified by `obj` by `xmov` on the x-axis and `ymov` on the y-axis. The translation is based at the `origin`. `obj` should be an object. `origin` should be a tuple. `xmov` and `ymov` should be integers |
| `Rotate(obj, origin, deg)` | Rotates the object defined by `obj` by `deg` degrees at the `origin`. `obj` should be an object. `origin` should be a tuple. `deg` should be a float |
| `Dilate(obj, origin, scale)` | Scales the object defined by `obj` by a scale of `scale` based at the `origin`. `obj` should be an object. `origin` should be a tuple. `scale` should be a float |
| `Combine(obj1, obj2)` | Combines objects, `obj1` and `obj2` to form a complex shape. `obj1` and `obj2` should be objects. |


The `analyze` class does not actually draw shapes, but rather gives a detailed analysis on a hypothetical shape.
Here is a full list of `analyze` class functions:
| Function | Use |
| --- | --- |
| `Rect(width, height, xpos, ypos)` | Gives area, vertices, and position of hypothetical rectangle with given dimensions `width` x `height` at location (`xpos`, `ypos`). All parameters are integers |
| `RightTriangle(base, height, xpos, ypos)` | Gives area, vertices, and position of hypothetical right triangle with given dimensions `base` x ` height` at location (`xpos`, `ypos`). All parameters are integers |
| `RegularPolygon(sides, length, xpos, ypos)` | Gives area, vertices, and position of hypothetical regular polygon with `sides` number of sides and with a common side length of `length` located at position (`xpos`, `ypos`). All parameters are integers |

### Basic Example 
```python
#Basic Drawing
import geometryPy.py
#Initialize Canvas
canvas.setCanvas(100,100)

#Begin Drawing
ellipse1 = draw.Render('ellipse', 10 5, 50, 50)#ellipse
rect1 = draw.Render('rectangle', 10, 20, 45, 50)#rectangle
shape1 = draw.Combine(ellipse1, rect1)#creates complex shape

```
