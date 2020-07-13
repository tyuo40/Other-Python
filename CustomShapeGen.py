#Custom Shape Generator
#Using turtle graphics library
#By John C. Parsons 2020


import turtle


class Polygon:
	def __init__(self, sides, name, size, color, line_thickness=3):
		self.sides = sides
		self.name = name
		self.size = size
		self.color = color
		self.line_thickness = line_thickness
		self.interior_angles = (self.sides-2)*180
		self.angle = self.interior_angles/self.sides
		return

	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.line_thickness)
		for i in range(self.sides):
			turtle.forward(self.size)
			turtle.left(180-self.angle)
		return


def main():
	print("Welcome to CUstom SHape Generator (CSG) by John C. Parsons")
	shapesides = int(input("How many sides does your shape have?: "))
	shapename = input("Give your shape a name: ")
	shapesize = input("(Optional)(Default = 50, press enter to skip) Input length of each side (in pixels): ")
	if shapesize == "":
		shapesize = 50
	else:
		shapesize = int(shapesize)

	shapecolor = input("(Optional)(Default = Black, press enter to skip) Input the color you want the shape to be: ")
	if shapecolor == "":
		shapecolor = "black"

	shapeline = input("(Optional)(Default = 3, press enter to skip) Input the line thickness (in pixels) for each side: ")
	if shapeline == "":
		shapeline = 3
	else:
		shapeline = int(shapeline)

	shape = Polygon(shapesides,shapename,shapesize,shapecolor,shapeline)
	shape.draw()
	turtle.done()
	return

main()
