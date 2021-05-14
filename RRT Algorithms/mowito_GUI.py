############### Submitted by -- Subham (subham.1@iitj.ac.in) ###########################
############### Submitted TO -- Mowito #################################################

from tkinter import *
from rrt_subham import *
from rrt_biased_subham import *
from rrt_star_subham import *


def get_input():
    start_x = start_var_x.get()
    start_y = start_var_y.get()
    goal_x = goal_var_x.get()
    goal_y = goal_var_y.get()

    obstacle_x_1 = obstacle1_var_x.get()
    obstacle_y_1 = obstacle1_var_y.get()
    obstacle_size_1 = obstacle1_var_size.get()
    obstalce1 = (obstacle_x_1, obstacle_y_1, obstacle_size_1)

    obstacle_x_2 = obstacle2_var_x.get()
    obstacle_y_2 = obstacle2_var_y.get()
    obstacle_size_2 = obstacle2_var_size.get()
    obstalce2 = (obstacle_x_2, obstacle_y_2, obstacle_size_2)

    obstacle_x_3 = obstacle3_var_x.get()
    obstacle_y_3 = obstacle3_var_y.get()
    obstacle_size_3 = obstacle3_var_size.get()
    obstalce3 = (obstacle_x_3, obstacle_y_3, obstacle_size_3)

    rrt_choice_value = rrt_choice.get()
    start_node = [start_x, start_y]
    goal_node = [goal_x, goal_y]
    all_obstacles = [obstalce1, obstalce2, obstalce3]
    return rrt_choice_value, start_node, goal_node, all_obstacles



def run():
    rrt_choice_value, start_node, goal_node, all_obstacles = get_input()
    if rrt_choice_value == 1:
        print("You Selected Basic RRT")
        path, final_path_nodes = rrt(start_node, goal_node, all_obstacles)
    elif rrt_choice_value == 2:
        print("You Selected Biased RRT")
        path, final_path_nodes = biased_rrt(start_node, goal_node, all_obstacles)
    else:
        print("You Selected RRT Star")
        path, final_path_nodes = rrt_star(start_node, goal_node, all_obstacles)
    display(final_path_nodes)

root = Tk()
root.geometry("540x540")
root.maxsize(540, 540)
root.minsize(540, 540)
root.title("Rapdialy Exploring Random Tree - Submitted By Subham")

##################### frames ######################
input_frame = Frame(root, bg="white", borderwidth=3 ,relief=SUNKEN)
# output_frame = Frame(root, bg="brown", borderwidth=3)
logo_frame = Frame(root, bg="white", borderwidth=3)



logo_frame.pack(fill=X)
input_frame.pack(padx=10, pady=10, fill=X)

######################################################
###############    Input Frame ######################


# Labels for Entry widgets
Label(input_frame, text="X Value").grid(row=1, column=1)
Label(input_frame, text="Y Value").grid(row=1, column=2)
Label(input_frame, text="Start Node").grid(row=2, column=0)
Label(input_frame, text="Goal Node").grid(row=3, column=0)
Label(input_frame, text="X-Position").grid(row=4, column=1)
Label(input_frame, text="Y-Position").grid(row=4, column=2)
Label(input_frame, text="Size").grid(row=4, column=3)
Label(input_frame, text="Obstacle 1").grid()
Label(input_frame, text="Obstacle 2").grid()
Label(input_frame, text="Obstacle 3").grid()

# Entry widgets variables
start_var_x = DoubleVar(value=1)
start_var_y = DoubleVar(value=1)
goal_var_x = DoubleVar(value=9)
goal_var_y = DoubleVar(value=9)

obstacle1_var_x = DoubleVar(value=4)
obstacle1_var_y = DoubleVar(value=4)
obstacle1_var_size = DoubleVar(value=1)
obstacle2_var_x = DoubleVar(value=2)
obstacle2_var_y = DoubleVar(value=7.2)
obstacle2_var_size = DoubleVar(value=1)
obstacle3_var_x = DoubleVar(value=7.1)
obstacle3_var_y = DoubleVar(value=5)
obstacle3_var_size = DoubleVar(value=1)
# entry visits
Entry(input_frame, textvariable=start_var_x).grid(row=2, column=1, pady=15, padx=5)
Entry(input_frame, textvariable=start_var_y).grid(row=2, column=2, pady=15, padx=5)
Entry(input_frame, textvariable=goal_var_x).grid(row=3, column=1, pady=15, padx=5)
Entry(input_frame, textvariable=goal_var_y).grid(row=3, column=2, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle1_var_x).grid(row=5, column=1, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle1_var_y).grid(row=5, column=2, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle1_var_size).grid(row=5, column=3, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle2_var_x).grid(row=6, column=1, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle2_var_y).grid(row=6, column=2, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle2_var_size).grid(row=6, column=3, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle3_var_x).grid(row=7, column=1, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle3_var_y).grid(row=7, column=2, pady=15, padx=5)
Entry(input_frame, textvariable=obstacle3_var_size).grid(row=7, column=3, pady=15, padx=5)

# Radio Button
Label(input_frame, text="Select RRT").grid(row = 8, column=0)

rrt_choice = IntVar()
rrt_choice.set(1)
Radiobutton(input_frame, text="Basic RRT", variable=rrt_choice, value=1).grid(row = 8, column=1)
Radiobutton(input_frame, text="Biased RRT", variable=rrt_choice, value=2).grid(row = 8, column=2)
Radiobutton(input_frame, text="RRT Star", variable=rrt_choice, value=3).grid(row = 8, column=3)

Button(input_frame, text="Start", command=run, padx=10, font=("Helvetica",12,"bold"), bg="green").grid(column=2, pady=10)

# pack entry visits using grid
moweto_photo = PhotoImage(file = "mowito.png")
Label(logo_frame, image = moweto_photo).pack()
Label(logo_frame, text="Presents").pack(anchor='e', padx=15)
Label(logo_frame, text="RRT InterFace", border=2, font="bold").pack(padx=15)
root.mainloop()