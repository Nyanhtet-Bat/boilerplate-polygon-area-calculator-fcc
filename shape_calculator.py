class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_height(self,height):
    self.height = height

  def set_width(self, width):
    self.width = width

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 *  self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width < 51 and self.height <51:
      shape = "*" * self.width 
      return (shape + "\n" )* self.height
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    return(self.get_area()//shape.get_area())

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_width(self, side):
    Rectangle.width = side

  def set_height(self, side):
    Rectangle.height = side
  
  def __str__(self):
   return f"Square(side={Rectangle.width})"
