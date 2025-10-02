import random

def main():

    final_cell = (9, 9)
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

    move_to_final_cell(row_coord, col_coord,
                       direction, grid_size, final_cell)
	
	
def move_to_final_cell(row_coord: int, col_coord: int,
                      direction: str, grid_size: int, final_cell: tuple):

    coords = (row_coord, col_coord)

    while coords != final_cell:

        row_coord, col_coord = update_robot_position(
                row_coord, col_coord, grid_size, direction)

        direction = update_robot_direction(row_coord, col_coord, direction)

        coords = (row_coord, col_coord)

    print_final_cell_message()


def print_final_cell_message():

    print("I am drinking Rebena. I am happy !")


def update_robot_direction(row_coord: int, col_coord: int, direction: str):

    print_rotation_message()
    direction = rotate_robot(direction)
    print_position_message(row_coord, col_coord, direction)

    return direction


def print_rotation_message():

    print("Turning 90 degrees clockwise \n")


def update_robot_position(row_coord: int, col_coord: int, grid_size: int, direction: str):
	
    while can_move(row_coord, col_coord, grid_size, direction):

        print_update_message(True)
        row_coord, col_coord = move_robot(row_coord, col_coord, direction) 
        print_position_message(row_coord, col_coord, direction)

    print_update_message(False)

    return row_coord, col_coord


def can_move(row_coord: int, col_coord: int, grid_size: int, direction: str) -> bool:

        row_coord, col_coord = move_robot(row_coord, col_coord, direction)

        can_move = not is_over_border(row_coord, col_coord, grid_size)

        return can_move

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
	
	return updated_position[0], updated_position[1]


def rotate_robot(direction: str) -> str:

    new_direction = {"north": "east",
                     "south": "west",
                     "west": "north",
                     "east": "south"}

    return new_direction[direction]



def is_over_border(row_coord: int, col_coord: int, grid_size) -> bool:
	
	is_over_down_border = (row_coord > (grid_size -1) or (col_coord > (grid_size -1)))

	is_over_upper_border = ((row_coord < 0) or (col_coord < 0)) 

	is_over_border = is_over_upper_border or is_over_down_border

	return is_over_border
		
	
def print_position_message(row_coord: int, col_coord: int, direction: str):

	print(f"I am curently at {(row_coord,col_coord)}, facing {direction}")


def print_update_message(can_move: bool):
	
	if can_move:
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
