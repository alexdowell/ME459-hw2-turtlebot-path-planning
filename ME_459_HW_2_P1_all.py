# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 22:59:24 2022

@author: alexa
"""
import numpy as np
import math as m

class ConfigSpace():
    
   # sets up a configuration space based on the following inputs:
   # x_bounds = [x_min,x_max]
   # y_bounds = [y_min,y_max]
   # spacing = grid spacing or step size in between values
    
    def __init__(self, x_bounds, y_bounds, spacing):
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.spacing = spacing
        
    def set_obstacles(self, obstacle_list):
        self.obstacles = obstacle_list
            
    def set_graph_coords(self):
        """graph coordinates and define the search space"""
        self.x_coords = np.arange(self.x_bounds[0], self.x_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.y_coords = np.arange(self.y_bounds[0], self.y_bounds[1]+self.spacing,
                                  self.spacing)
        
        self.generate_search_space()
    
    def generate_search_space(self):
        """generate our search space"""
        self.search_space = np.zeros((len(self.x_coords),len(self.y_coords))) 
    
     
    def place_obstacles(self, obst_list):
        """places obstacles in grid by inserting a 1""" 
        for obstacle in obst_list:
            obs_x = obstacle[0]
            obs_y = obstacle[1]
            self.search_space[obs_x, obs_y]= 1
    
    def calc_index(self,position):
        """calculate index """
        index = (position[1] - self.y_bounds[0]) / \
            self.spacing * (self.x_bounds[1] - self.x_bounds[0] + self.spacing)/ \
                self.spacing + (position[0] - self.x_bounds[0]) / self.spacing
                
        return index            
    
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

''' working on how to use the below function (which is inside the class ConfigSpace) in another function
    def check_out_bounds(self, current_position, x_bounds, y_bounds):
        """check out of bounds of configuration space"""
        
        if current_position[0] < self.x_bounds[0] or current_position[0] > self.x_bounds[1]:
            return True
        
        if current_position[1] < self.y_bounds[0] or current_position[1] > self.y_bounds[1]:
            return True
        
        return False 
    def check_if_obstacle_is_present(self,obstacle_list, node_in_question):
        """check to see if an obstacle is in the way"""
        for obstacle in obstacle_list:
            if obstacle == node_in_question:
                return True
    def check_within_obstacle(self, obstacle_list, current_position, obs_radius):
        """check if I am within collision of obstacle return True if it is
        false if I'm not"""
        for obstacle in obstacle_list:
            distance = compute_distance(current_position, obstacle)
            if abs(distance)<=obstacle_radius:
                return True
            
        return False
'''        
if __name__=='__main__':
    #set up parameters
    x_span = [0,10]
    y_span = [0,10]
    spacing = 0.5
    
#%% ##### BUILD WORLD
    configSpace = ConfigSpace(x_span, y_span, spacing)
    configSpace.set_graph_coords()
    
    obstacle_list=[(1,1), (4,4), (3,4), (5,0), (5,1), (0,7), (1,7), (2,7), (3,7)]
    obstacle_radius = float(input("Enter the turtle's radius please: "))
    configSpace.set_obstacles(obstacle_list)
#%% Build dijkstra    
    val_x, val_y = [int(x) for x in input("Enter the node in question with no commas and I'll tell you if it's valid: ").split()]
    node_in_question = [val_x, val_y]
    turtle = Turtle(0,0,spacing) # Start Location
    check_node_validity(obstacle_list, node_in_question, x_span, y_span, obstacle_radius)
    