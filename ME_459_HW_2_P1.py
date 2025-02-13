# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:21:29 2022

@author: alex
"""


import numpy as np
import math as m

def check_within_obstacle(obstacle_list, current_position, obstacle_radius):
    """check if I am within collision of obstacle return True if it is
    false if I'm not"""
    for obstacle in obstacle_list:
        distance = compute_distance(current_position, obstacle)
        if abs(distance)<=obstacle_radius:
            return True
        else:    
            return False

def check_if_obstacle_is_present(obstacle_list, node_in_question):
    """check to see if an obstacle is in the way"""
    for obstacle in obstacle_list:
        if obstacle == node_in_question:
            return True

def check_obstacle_exists(obstacle_list):
    """sanity check to see if obstacle exists"""
    for obst in obstacle_list:
        if configSpace.search_space[obst[0],obst[1]] == 1:
            print("yes", configSpace.search_space[obst[0],obst[1]])

   
def compute_distance(current_pos, another_pos):
    """compute distance"""
    dist = m.sqrt((another_pos[0] - current_pos[0])**2+(another_pos[1]- current_pos[1])**2)
    
    return dist
    #return dist(current_pos, another_pos)

def check_out_bounds( current_position, x_bounds, y_bounds):
        """check out of bounds of configuration space"""
        
        if current_position[0] < x_bounds[0] or current_position[0] > x_bounds[1]:
            return True
        
        if current_position[1] < y_bounds[0] or current_position[1] > y_bounds[1]:
            return True
        
        return False
    
def check_node_validity(obstacle_list, node_in_question, x_bounds, y_bounds, turtle_radius):
    """ check if current node is valid """
    
    if check_out_bounds(node_in_question, x_bounds, y_bounds) == True:
        print("the node in question is out of bounds")
        return False
    
    elif check_if_obstacle_is_present(obstacle_list, node_in_question) == True:
        print("the node in question is an obstacle")
        return False
    
    elif check_within_obstacle(obstacle_list, node_in_question, turtle_radius) == True:
        print("the node in question is too close to an obstacle")
        return False
    
    else:
        print("the node in question is valid")
        return True
if __name__=='__main__':
    #set up parameters
    x_span = [0,10]
    y_span = [0,10]
    spacing = 0.5
    obstacle_list=[(1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), (3,7)]
    turtle_radius = float(input("Enter the turtle's radius please: "))
    val_x, val_y = [int(x) for x in input("Enter the node in question with no commas and I'll tell you if it's valid: ").split()]
    node_in_question = [val_x, val_y]
    check_node_validity(obstacle_list, node_in_question, x_span, y_span, turtle_radius)
    