import random

def main():
	grid_size: int = 10

	robots_name: str = (input("Please provide the robots name: "))
	robots_id: int = int(input("please provide the robots ID: "))

	row_coord: int = random.randint(0, grid_size)
	col_coord: int = random.randint(0, grid_size)

	direction: str = random.choice(["west", "east", "north", "south"])

	row_coord, col_coord = normalise_coords(row_coord, col_coord, grid_size)
	coord_quadrant = get_robots_coord_quadrant(row_coord, col_coord, grid_size)

	print_init_message(robots_name, robots_id, row_coord,
			  col_coord, coord_quadrant, direction)
	
	update_robot_position(row_coord, col_coord, grid_size, direction)
	
	

def update_robot_position(row_coord: int, col_coord: int, grid_size: int, direction: str):
	
	while not is_border(row_coord, col_coord, grid_size):

		print_update_message(False)
		row_coord, col_coord = move_robot(row_coord, col_coord, direction) 
		print_position_message(row_coord, col_coord, direction)

	
	print_update_message(True)
		


def normalise_coords(row_coord: int, col_coord: int, grid_size: int):
		

	row_coord = 0 if row_coord < 0 else row_coord
	col_coord = 0 if col_coord < 0 else col_coord

	row_coord = grid_size -1 if row_coord > grid_size -1 else row_coord
	col_coord = grid_size -1 if col_coord > grid_size -1 else col_coord


	return row_coord, col_coord



def get_robots_coord_quadrant(row_coord: int, col_coord: int, grid_size: int):

	quadrant_border = grid_size // 2
		
	if row_coord > col_coord:
		hor_quadrant = "left"

	else:
		hor_quadrant = "right"

	if row_coord > quadrant_border:
		vert_quadrant = "Bottom"

	else:

		vert_quadrant = "Top"


	coord_quadrant = " ".join([vert_quadrant, hor_quadrant])

	return coord_quadrant


def move_robot(row_coord: int, col_coord: int, direction: str) -> tuple:
	
	move_direction = {"east": (0,-1), "west": (0,1), "north": (-1,0), "south": (1,0)}

	
	current_position =  (row_coord, col_coord)

	updated_position = tuple(map(sum, zip(
		current_position, move_direction[direction])))
	
	breakpoint()
	return updated_position[0], updated_position[1]


def is_border(row_coord: int, col_coord: int, grid_size) -> bool:
	
	is_down_border = (row_coord == (grid_size -1) or (col_coord == (grid_size -1)))

	is_upper_border = ((row_coord == 0) or (col_coord == 0)) 

	is_border = is_upper_border or is_down_border
	return is_border
		
	
def print_position_message(row_coord: int, col_coord: int, direction: str):

	print(f"I am curently at {(row_coord,col_coord)}, facing {direction}")


def print_update_message(is_border: bool):
	
	if not is_border:
		print("Moving one step forward.")
	else:
		print("I have a wall in front of me !")


def print_init_message(name: str, robots_id: int,  row_coord: int, col_coord: int, coord_quadrant, direction: str):

	message = f"\n Robot's name is {name}. Robot's Id is: {robots_id}\n\n"
	message += f"Robot's coordinate quadrant is: {coord_quadrant} \n\n"

	print(message)
	print_position_message(row_coord, col_coord, direction)


if __name__ == "__main__":

	main()
