# THE import
from cmu_graphics import *

app.shapes = []
app.shapeCount = None
app.shapeLabel = Label('', 200, 50, size=20, fill='white',bold=True)

def onMouseMove(x,y):
    cir = Circle(x,y,25,fill=rgb(50,50,50),border='blue')
    app.shapes.append(cir)
    app.shapeCount = len(app.shapes)
    app.shapeLabel.value = f'Shapes: {app.shapeCount}'
    app.shapeLabel.toFront()

# required by CMU (ignore the IDE erroring its not supposted to)
cmu_graphics.run()
