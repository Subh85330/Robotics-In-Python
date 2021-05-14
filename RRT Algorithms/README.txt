#################### Submitted By - Subham ####################
############# mail id = subham.1@iitj.ac.in (subhamk356@gmail.com) ################

Method 1 -- Graphical User Interface
	Run file mowito_gui.py
	A GUI will be opened where you can choose start position, goal position and 
	obstacle position and size.
	For this method (GUI) You can only add obstacles upto 3. To remove all 
	obstacles input 0 in all field of all obstacles.
	Then choose the version of RRT.
	Press Start Button.
	To Run again please wait untill last figure disappear.



Method 2 -- Direct Run the file
	for basic RRT run the file - rrt_subham.py
	for biased RRT run the file - rrt_biased_subham.py
	for RRT star run the file - rrt_star_subham.py

	Input Method 1 - sample input 
	start node = [x, y]
	goal node = [xd, yd]
	all_obstacles = [(xo1, yo1, size1),(xo2, yo2, size2),....(xon, yon, sizen)]

	Input Method 2 - From User Through terminal
	comment sample input then run the file



Note:
Give values of between 0 and 10 for x and y.
for method 1 you can add upto 3 obstacles whereas for method 2 you can add more obstalces.
Please keep all files in same folder