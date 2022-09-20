class Rectangle:
  width = 0
  height = 0

  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __repr__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)
  
  def set_width(self,width):
   self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width*self.height)

  def get_perimeter(self):
    return (2*self.width+2*self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      str = ""
      for lines in range(self.height):
        str += "*"*self.width+"\n"
      return str

  def get_amount_inside(self, shape):
    x =  self.width // shape.width
    y =  self.height // shape.height
    return x*y
    
  
class Square(Rectangle):
  side_length = 0
  
  def __init__(self,side_length):
    self.side_length = side_length
    self.width = side_length
    self.height = side_length

  def __repr__(self):
    return "Square(side={})".format(self.side_length)

  def set_side(self, side_length):
    self.side_length = side_length
    self.width = side_length
    self.height = side_length

  def set_width(self, width):
    self.width = width
    self.height = width
    self.side_length = width

  def set_height(self, height):
    self.width = height
    self.height = height
    self.side_length = height
