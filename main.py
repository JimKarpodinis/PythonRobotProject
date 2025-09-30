def main():

	grid_size: int = 10

	robots_name: str = (input("Please provide the robots name: "))
	robots_id: int = int(input("please provide the robots ID: "))
	robots_row_coord: int = int(input("Please provide the robots row coordinate: "))
	robots_col_coord: int = int(input("Please provide the robots col coordinate: "))

	robots_row_coord, robots_col_coord = normalise_coords(robots_row_coord, robots_col_coord, grid_size)
	robots_coord_quadrant = get_robots_coord_quadrant(robots_row_coord, robots_col_coord, grid_size)

	message = get_message(robots_name, robots_id, robots_row_coord, robots_col_coord, robots_coord_quadrant)

	print(message)


def normalise_coords(robots_row_coord: int, robots_col_coord: int, grid_size: int):
		

	robots_row_coord = 0 if robots_row_coord < 0 else robots_row_coord
	robots_col_coord = 0 if robots_col_coord < 0 else robots_col_coord

	robots_row_coord = grid_size -1 if robots_row_coord > grid_size -1 else robots_row_coord
	robots_col_coord = grid_size -1 if robots_col_coord > grid_size -1 else robots_col_coord


	return robots_row_coord, robots_col_coord



def get_robots_coord_quadrant(robots_row_coord: int, robots_col_coord: int, grid_size: int):

	quadrant_border = grid_size // 2
		
	if robots_row_coord > robots_col_coord:
		hor_quadrant = "left"

	else:
		hor_quadrant = "right"

	if robots_row_coord > quadrant_border:
		vert_quadrant = "Bottom"

	else:

		vert_quadrant = "Top"


	robots_coord_quadrant = " ".join([vert_quadrant, hor_quadrant])


	return robots_coord_quadrant


def get_message(name: str, robots_id: int,  robots_row_coord: int, robots_col_coord: int, robots_coord_quadrant):

	message = f"\n Robot's name is {name}. Robot's Id is: {robots_id}\n\n"
	message += f"Robot's coordinates are: \n robots row coordinate: {robots_row_coord} robots col coordinate: {robots_col_coord} \n\n"
	message += f"Robot's coordinate quadrant is: {robots_coord_quadrant}"

	return message


if __name__ == "__main__":

	main()
