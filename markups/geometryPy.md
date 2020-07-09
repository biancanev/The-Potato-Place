# geometryPy Documentation
Version: 1.0.0

Status: Stable

### Intoduction
geometryPy is an easy way to draw simple graphics on the terminal window. This software is meant for beginners to learn how to code.

### Basics
The two most basic classes of this program are the `draw` and `analyze` classes. The `draw` class' basic function is the `render()` function, which takes five arguments: `shape`, `length`, `width`, `xpos`, `ypos`. Therefore, in this example:
```python
draw.Render("rectangle", 10, 40, 0, 0)
```
the terminal will draw out a 10 x 40 rectangle at (0, 0), or the top left corner.
Here is a full list of `draw` class functions
| Function | Use |
| --- | --- |
| `Render(shape, length, width, xpos, ypos)` | Draws the given `shape` with the dimensions of `length` x `width` at (`xpos`, `ypos`). `shape` should be a string. `length`, `width`, `xpos`, and `ypos` should be integers. |
| `Translate(obj, origin, xmov, ymov)` | Moves the object specified by `obj` by `xmov` on the x-axis and `ymov` on the y-axis. The translation is based at the `origin`. `obj` should be an object. `origin` should be a tuple. `xmov` and `ymov` should be integers |
| `Rotate(obj, origin, deg)` | Rotates the object defined by `obj` by `deg` degrees at the `origin`. `obj` should be an object. `origin` should be a tuple. `deg` should be an integer |

The `analyze` class does not actually draw shapes, but rather gives a detailed analysis on a hypothetical shape.
