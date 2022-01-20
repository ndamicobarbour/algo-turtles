from turtle import Screen, RawTurtle

class DataVisualizer:

	ref = dict()
	field = Screen()
	
	def __init__(self, dataset: list):
		self.dataset = dataset
		self.datacount = len(dataset)
		x_wid, y_wid = self.field.screensize()
		self.start_x = (x_wid / -2)
		self.start_y = (y_wid / -2)
		self.step_x = int(x_wid / len(dataset))
		self.step_y = int(y_wid / max(dataset))

		for datapoint in enumerate(dataset):
			index, data = datapoint
			self.ref[index] 		= dict()
			self.ref[index]['data'] = datapoint[1]
			self.ref[index]['pen'] 	= RawTurtle(canvas=self.field,
												visible=False)
			self.ref[index]['pen'].speed(0)
			self.ref[index]['pen'].penup()
			self._draw_index(index)

		self.pointer = RawTurtle(canvas=self.field,
								 visible=False)
		self.pointer.left(90)
		self.pointer.shape("classic")
		self.pointer.penup()

	def setup_counter(self):
		self.counter = dict()
		self.counter['value'] = 0
		self.counter['writer'] = RawTurtle(canvas=self.field,
										   visible=False)
		self.counter['writer'].penup()
		self.counter['writer'].goto(self.start_x + self.step_x * .25,
									self.start_y - 60)
		self.counter['writer'].write(f"Total Accesses: ",
								  move=True,
								  align="left",
								  font=("Arial", 14, "normal"))
		self.counter['counter'] = RawTurtle(canvas=self.field,
											visible=False)
		self.counter['counter'].penup()
		self.counter['counter'].goto(self.counter['writer'].pos())
		self._add_count()

	def clear_counter(self) -> None:
		self.counter['writer'].clear()
		self.counter['counter'].clear()

	def draw_border(self) -> None:
		self.border = RawTurtle(canvas=self.field)
		self.border.penup()
		self.border.goto(self.start_x, self.start_y)
		self.border.pendown()
		self.border.goto(self.start_x, self.start_y + self.step_y * max(self.dataset))
		self.border.goto(self.start_x + self.step_x * len(self.dataset), self.start_y + self.step_y * max(self.dataset))
		self.border.goto(self.start_x + self.step_x * len(self.dataset), self.start_y)
		self.border.goto(self.start_x, self.start_y)
		self.border.penup()

	def clear_border(self) -> None:
		self.border.clear()

	def clear_val(self, index: int) -> None:
		self.ref[index]['pen'].clear()

	def keep_running(self) -> None:
		self.field.mainloop()

	def read_at(self, index: int) -> int:
		self._clear_pointer()
		self._add_pointer(index)
		self._add_count(1)
		return self.ref[index]['data']

	def update_at(self, index: int, value: int) -> None:
		if self.pointer_index != index:
			self._clear_pointer()
			self._add_pointer(index)
		self._add_count(1)
		self.ref[index]['data'] = value
		self.clear_val(index)
		self._draw_index(index)

	def _add_count(self, add_val: int = 0) -> None:
		self.counter['value'] += add_val
		self.counter['counter'].clear()
		self.counter['counter'].write(f"{self.counter['value']}",
								  	  move=False,
								  	  align="left",
								  	  font=("Arial", 14, "normal"))

	def _add_pointer(self, index: int) -> None:
		self.pointer.goto(self.start_x + (index+1) * self.step_x - .5 * self.step_x,
						  self.start_y - 30)
		self.pointer.showturtle()
		self.pointer.stamp()
		self.pointer.hideturtle()
		self.pointer_index = index

	def _clear_pointer(self) -> None:
		self.pointer.clearstamps()

	def _draw_index(self, index: int) -> None:
		"""
		Draws the already defined value at index.
		"""
		pen = self.ref[index]['pen']
		val_left_bound = self.start_x + (index+1) * self.step_x - .75 * self.step_x
		val_right_bound = self.start_x + (index+1) * self.step_x - .25 * self.step_x
		val_top_bound = self.start_y + self.ref[index]['data'] * self.step_y
		pen.fillcolor("blue")
		pen.goto(val_left_bound, self.start_y)
		pen.pendown()
		pen.begin_fill()
		pen.goto(val_left_bound, val_top_bound)
		pen.goto(val_right_bound, val_top_bound)
		pen.goto(val_right_bound, self.start_y)
		pen.goto(val_left_bound, self.start_y)
		pen.end_fill()
		pen.penup()