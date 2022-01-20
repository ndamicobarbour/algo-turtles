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

		self.pointer = RawTurtle(canvas=field,
								 visible=False)
		self.pointer.left(90)
		self.pointer.shape("classic")
		self.pointer.penup()

	def setup_pointer()

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
		self.border.goto(self.start_x, self.start_y + self.step_y * max(dataset))
		self.border.goto(self.start_x + self.step_x * len(dataset), self.start_y + self.step_y * max(dataset))
		self.border.goto(self.start_x + self.step_x * len(dataset), self.start_y)
		self.border.goto(self.start_x, self.start_y)
		self.border.penup()

	def clear_border(self) -> None:
		self.border.clear()

	def clear_val(self, index: int) -> None:
		self.ref[index]['pen'].clear()


	def keep_running(self) -> None:
		self.field.mainloop()


	def switch_if_greater(self, index_one: int, index_two:int) -> None:
		# print("in switch_if_greater")
		self._add_pointer(index_one)
		self._add_pointer(index_two)
		val_one = self.ref[index_one]['data']
		val_two = self.ref[index_two]['data']
		self._add_count(2)
		if val_one > val_two:
			self.ref[index_two]['data'] = val_one
			self.ref[index_one]['data'] = val_two
			self.clear_val(index_one)
			self.clear_val(index_two)
			self._add_count(2)
			self._draw_index(index_one)
			self._draw_index(index_two)
		self._clear_pointer()


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
		# print(f"val_left_bound = {val_left_bound}")
		# print(f"val_right_bound = {val_right_bound}")
		# print(f"val_top_bound = {val_top_bound}")
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

# sortables = [1,2,3,4,5,6,7,8,9,10]
# example = DataVisualizer(sortables)
# # example.clear_val(0)
# # example.clear_val(3)
# example.field.mainloop()