############### Author -- Subham (subham.1@iitj.ac.in) ###########################
##################################################################################
#!/usr/bin/python3

import numpy as np 
from random import random, randint
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from rrt_subham import take_inputs, plot_obstacle, check_collision, display

# # Used for gif making
# import imageio
# import os


### Biased RRT
def rand_node_generate(goal_node, map_x, map_y):
    int_num = randint(0,100)
    if int_num <= 20:
        rand_node = goal_node
    else:
        rand_node = [round(map_x*random(),2), round(map_x*random(),2)]

    return rand_node

def biased_rrt(start_node, goal_node, all_obstacles):
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
    plt.title("Biased RRT with Obstacles")
    plt.xlabel("X-Position")
    plt.ylabel("Y-Position")
    plt.xlim(0, map_x)
    plt.ylim(0, map_y)
    plot_obstacle(all_obstacles, color="b")

    # # Making Gif of plots
    # frames =[]
    # frame_ind = 0

    current_node = start_node
    while ~goal_found:
        new_rand_node = rand_node_generate(goal_node, map_x, map_y)
        s = len(TreeConn)
        distanceCheck = []
        for k in range(s):
            
            dist = np.sqrt((TreeConn[k][0] - new_rand_node[0])**2 + ((TreeConn[k][1] - new_rand_node[1])**2))
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


        # ### gif creation
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

    
    # # build gif
    # with imageio.get_writer('biased_rrt.gif', mode='I') as writer:
    #     for frame in frames:
    #         image = imageio.imread(frame)
    #         writer.append_data(image)
    # # Remove files
    # for frame in set(frames):
    #     os.remove(frame)



    path = [[px,py] for px, py in zip(path_x, path_y)]
    return path, final_path_nodes






if __name__ == "__main__":

    ### Sample Inputs
    start_node = [1,1]
    goal_node = [8,8]
    all_obstacles = [(5,5,1),(6,2,1),(2,5,1)]

    ### Takes Inputs from User
    # start_node, goal_node, all_obstacles = take_inputs()

    path, final_path_nodes = biased_rrt(start_node, goal_node, all_obstacles)
    display(final_path_nodes)
    plt.show()