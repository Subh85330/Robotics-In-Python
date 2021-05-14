############### Author -- Subham (subham.1@iitj.ac.in) ###########################
##################################################################################
#!/usr/bin/python3


import numpy as np 
from random import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# # Used for gif making
# import imageio
# import os


def take_inputs():
    start_x = float(input("Enter the x value of start node: "))
    start_y = float(input("Enter the y value of start node: "))
    start_node = [start_x, start_y]
    goal_x = float(input("Enter the x value of goal node: "))
    goal_y = float(input("Enter the y value of goal node: "))
    goal_node = [goal_x, goal_y]
    no_of_obstacles = int(input("Enter the number of obstcles: "))
    all_obstacles = []
    for i in range(no_of_obstacles):
        x_obstacal = float(input(f"Enter the x location of obstacle {i+1}: "))
        y_obstacal = float(input(f"Enter the y location of obstacle {i+1}: "))
        size = float(input(f"Enter the size of obstacle {i+1}: "))
        all_obstacles.append((x_obstacal, y_obstacal, size))
    return start_node, goal_node, all_obstacles

def plot_obstacle(all_obstacles, color="c"):
    for obstacle in all_obstacles:
        x, y, size = obstacle[0],obstacle[1],obstacle[2]
        xl = [x, x+size, x, x-size, x]
        yl = [y-size, y, y+size, y, y-size]
        plt.fill(xl, yl, color)

def check_collision(x, y, all_obstacles):
    # will return True if there is no collision and False if there is a collision
    margin = 0.02
    for (x_obs, y_obs, size) in all_obstacles:
        dx = x_obs - x
        dy = y_obs - y
        distance_newNode_obstacle = dx * dx + dy * dy
        if distance_newNode_obstacle <= size**2 + margin:
            return False 

    return True

def display(final_path_nodes):
    print("Final Path node indices: ")
    for i in range(len(final_path_nodes)):
        print(f"-->{final_path_nodes[i]}", end =" ")
    print()
def rrt(start_node, goal_node, all_obstacles):
    parent = []
    map_x =10
    map_y = 10
    max_distance = 0.5
    no_of_nodes = 0
    parent.append(no_of_nodes)
    goal_found = False
    
    TreeConn = []
    TreeConn.append(start_node)

    fig = plt.plot(start_node[0],start_node[1],'*g',goal_node[0], goal_node[1],'*g', markersize=12)
    plt.title("Basic RRT with Obstacles")
    plt.xlabel("X-Position")
    plt.ylabel("Y-Position")
    plt.xlim(0, map_x)
    plt.ylim(0, map_y)

    plot_obstacle(all_obstacles, color="b")


    # Making Gif of plots
    # frames =[]
    # frame_ind = 0

    current_node = start_node
    while ~goal_found:
        new_rand_node = [round(map_x*random(),2), round(map_x*random(),2)]
        s = len(TreeConn)
        distanceCheck = []
        for k in range(s):    
            dist = round(np.sqrt((TreeConn[k][0] - new_rand_node[0])**2 + ((TreeConn[k][1] - new_rand_node[1])**2))) # second norm (euclidian distance)
            distanceCheck.append(dist)
        

        min_index = distanceCheck.index(min(distanceCheck))
        nearst_node = TreeConn[min_index]

        if (distanceCheck[min_index] <= max_distance):        
            current_node = new_rand_node

        else:
            norm = np.sqrt((new_rand_node[0] - TreeConn[min_index][0])**2 + (new_rand_node[1] - TreeConn[min_index][1])**2)
            unit_vector = [new_rand_node[0] - TreeConn[min_index][0], new_rand_node[1] - TreeConn[min_index][1]]/norm
            new_node = [TreeConn[min_index][0] + unit_vector[0]*max_distance, TreeConn[min_index][1] + unit_vector[1]*max_distance]
            current_node = new_node
            

        if check_collision(current_node[0], current_node[1], all_obstacles):
            plt.plot([nearst_node[0], current_node[0]], [nearst_node[1], current_node[1]], color='b')
            plt.plot(current_node[0], current_node[1], 'ro')
            plt.pause(0.01)
            no_of_nodes = no_of_nodes + 1
            TreeConn.append(current_node)
            parent.append(min_index)

        cond = np.linalg.norm((TreeConn[no_of_nodes-1][0] - goal_node[0],TreeConn[no_of_nodes-1][1] - goal_node[1])) <= max_distance
        if np.linalg.norm((TreeConn[no_of_nodes][0] - goal_node[0],TreeConn[no_of_nodes][1] - goal_node[1])) <= max_distance:
            current_node = goal_node
            no_of_nodes = no_of_nodes +1
            TreeConn.append(current_node)
            parent.append(no_of_nodes-1)
            goal_found  =True




                ### gif creation
        # frame = f'{frame_ind}.png'
        # frames.append(frame)
        # frame_ind+=1
        # # save frame
        # plt.savefig(frame)

        if goal_found:

            rev_path = []
            rev_path.append(no_of_nodes)
            i=1
            
            while parent[rev_path[i-1]] != 0:
                rev_path.append(parent[rev_path[i-1]])
                
                i=i+1
            rev_path.append(0)
            
            final_path_nodes = rev_path[::-1]
            path_x = []
            path_y = []

            for j in final_path_nodes:
                path_x.append(TreeConn[j][0])
                path_y.append(TreeConn[j][1])


            plt.plot(path_x,path_y, linewidth=3.5, color='k')
            plt.pause(6)




            # #  for gif making
            # frames.append(frame)
            # frame_ind+=1
            # # save frame
            # plt.savefig(frame)

            break



    #     # build gif
    # with imageio.get_writer('rrt_simple.gif', mode='I') as writer:
    #     for frame in frames:
    #         image = imageio.imread(frame)
    #         writer.append_data(image)
    # # Remove files
    # for frame in set(frames):
    #     os.remove(frame)

    
    path = [[px,py] for px, py in zip(path_x, path_y)]
    return path, final_path_nodes


if __name__ == "__main__":

    #### Sample Inputs
    start_node = [1,1]
    goal_node = [8,8]
    all_obstacles = [(5,5,1),(6,2,1),(2,5,1)]

    ### Takes Inputs from User
    # start_node, goal_node, all_obstacles = take_inputs()

    path, final_path_nodes = rrt(start_node, goal_node, all_obstacles)
    display(final_path_nodes)
    plt.show()