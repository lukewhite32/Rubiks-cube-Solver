class Corner:                        # Unfortunately, inheritance isn't a thing in python
  def __init__(self, color1, color2, color3, posX, posY):
    self.color1 = color1
    self.color2 = color2
    self.color3 = color3
    self.correctCenter1 = color1
    self.correctCenter2 = color2
    self.correctCenter3 = color3
    self.cubeTwist = 0             # 0 = correct, 1 = twisted clockwise, 2 = twisted counter-clockwise
    self.posX = posX               # Explained in "cube" class; all in relation to facing white w/blue on top
    
 def changePos(self, orient):
    if orient == "c":
        if self.posX = 
