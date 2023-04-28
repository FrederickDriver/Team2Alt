########################IMPORTS STATEMENTS#######################


######UTILITY FUNCTIONS: FILEWRITING:DIRECTORY STRUCTURE#########

#shuffle_dir([paths],[permutation])
  #takes in a list of strings and a list of integers of size n
  #returns a list of size n where every element at index i is equal to paths[permutation[i]]
  # e.g. if paths is ["<path>/dir_train","<path>/dir_test"] and permutation is [0,1,0,1,1]
  #the resulting list would be ["<path>/dir_train","<path>/dir_test","<path>/dir_train","<path>/dir_test","<path>/dir_test"]
def shuffle_dir(paths, permutation):
    pass

#make_permutations(n,[probability_distribution]):
  #takes in an integer n and a list of floats that sum up to 1
  #returns a list of size n where each element is an index of probability_distribution, corresponding to a random selection weighted by the said distribution
  #example, if n is 100, probability_distribution is [0.8,0.2] about 80 percent of the elements in the output should be 0 and 20 percent should be 1
def make_permutations(n, dist):
    pass

#make_directories(path, train_name, test_name):
  #take in a path, and creates the yolo directory structure
  #returns a list of paths [ images/train , images/test , labels/train , labels/test ]
def make_directories(path, train_name,test_name):
    pass
##########UTILITY FUNCTIONS: FILEWRITING: IMAGES#############

#save_frames([image_list], [paths], prefix): 
  #takes in a list of numpy arrays, and a list of directories to put the frames, which must both be of the same length
  # and a prefix which should usually be <Datarow_ID>.png
  #saves the frames, returns the total number of frames if successful, returns -1 if failed.
def save_frames(im_list, paths, prx): 
    pass

##########UTILITY FUNCTIONS: FILEWRITING: TEXT#############
#write_yolo_annotations([paths], [< Datarow_ID , yolo_label_string >])
  #takes in a strings "paths" and a list of tuples: Datarow_ID , yolo_label_string
  #iterates through the list with iterator "i" 
  #creates a text file in the directory of each "path" with the filename <Datarow_ID>_<i>.txt
  #and writes yolo_label_string into the contents
def write_yolo_annotations(paths, id_label):
    pass

