from ast import Try
import unittest
import altFile as af
import numpy as np
from scipy import stats
import os, shutil, random
#TO USE UNIT TESTS SIMPLY CALL
#python -m unittest alt_file_unittest.py 
#TO UNIT TEST ONLY 1 CLASS
#python -m unittest alt_file_unittest.<NAME OF CLASS>
#TO UNIT TEST ONLY 1 CLASS TEST CASE
#python -m unittest alt_file_unittest.<NAME OF CLASS>.<TEST CASE FUNCTION>
class TestWriteMethods(unittest.TestCase):

    def test_shuffle_dir(self):
        s1, s2 = "string1" , "string2"
        all1 = list(af.make_permutations(10,[0,1],[0,1]))
        all0 = list(af.make_permutations(10,[0,1],[1,0]))
        
        alls1 = af.shuffle_dir([s1,s2], all0)
        alls2 = af.shuffle_dir([s1,s2], all1)
        testmsg = [ "\n\nTestMessage:\n -inputs: ([s1,s2], all0)\n-Expected output was a list of string1:\n-Output= {all1}",
                    "\n\nTestMessage:\n -inputs: ([s1,s2], all1)\n-Expected output was a list of string2:\n-Output= {all0}"]
        self.assertEqual(alls1, [s1]*10,testmsg[0] )
        self.assertEqual(alls2, [s2]*10,testmsg[1] ) 


    def test_make_permutations(self):
        all1 = list(af.make_permutations(10,[0,1],[0,1]))
        all0 = list(af.make_permutations(10,[0,1],[1,0]))
        
        #create a list of 100 permutations of a list of 100 numbers
        #each with a different distribution of size "steps"
        #the first permutation should have a single 1 in it
        #the second should have 2, the third should have a sum around 3 and so on
        steps=100
        perm_binary_tests  = [sum(af.make_permutations(steps,[0,1],[i/steps,(steps-i)/steps])) for i in range(steps)]
        perm_binary_truths = range(steps)
        tt, p_value = stats.ttest_ind(perm_binary_tests, perm_binary_truths)
        testmsg = [ "\n\nTestMessage:\n -inputs: (10,[0,1],[0,1])\n-Expected output was a list of 1's:\n-Output= {all1}",
                    "\n\nTestMessage:\n -inputs: (10,[0,1],[1,0])\n-Expected output was a list of 0's:\n-Output= {all0}",
                    "\n\nTestMessage:\n -inputs: %d different binary example\n We reject the null hyothesis that the output of make_permutations has the same distribution as p_dist " %(steps)]

        self.assertEqual(all1, [1]*10,testmsg[0] )
        self.assertEqual(all0, [0]*10,testmsg[1] )
        self.assertTrue(p_value > 0.05,testmsg[2])

    def test_make_directories(self):
        inputs = path, train_name, test_name = "./yolo_highway/", "train_data", "test_data"
        expected_out_paths = [path+"images/"+train_name,path+"images/"+test_name,path+"labels/"+train_name,path+"labels/"+test_name]

        out_paths = af.make_directories(path, train_name,test_name)
        
        msg_vars = ( ''.join(inputs), ''.join(expected_out_paths), ''.join(out_paths) ) 
        testmsg =  "\n\nTestMessage:\n -inputs: %s \n-Expected output was that the filestructure would be (%s):\n-Output= %s" % (msg_vars)               
        self.assertEquals(out_paths, expected_out_paths,testmsg)

        for p in expected_out_paths:
            self.assertTrue(os.path.isdir(p),"\n\nTestMessage:\n -inputs: %s\n-Expected output was for this directory to be created, but currently it does not exist"%(p))
        shutil.rmtree(path)

    def test_save_frames(self):
        n=100
        id = prx = '295844578'
        def f ():
            arr = np.zeros((360,360))
            arr[180:200,:]=1
            return arr
        im_list = [ f() ]*n

        inputs = path, train_name, test_name = "./yolo_highway/", "train_data", "test_data"
        out_paths = af.make_directories(*inputs)
        image_dirs = out_paths[:2]
        file_paths = af.make_permutations(n,image_dirs,[.5,.5])

        self.assertIsNot(-1,af.save_frames(im_list, file_paths,prx),"save frames returned a negative 1 which means imwrite failed to save a frame")
        for i in range(len(file_paths)):
            filename = file_paths[i]+os.sep+prx+"_"+str(i)+".png"
            self.assertTrue(os.path.isfile(filename),"\n\nTestMessage:\n -inputs: %s\n-Expected output was for this file to be created, but currently it does not exist"%(filename))

    def test_write_yolo_annotation(self):
        inputs = path, train_name, test_name = "./yolo_highway/", "train_data", "test_data"
        out_paths = af.make_directories(path, train_name,test_name)
        label_paths = out_paths[2:]   
        num_label_entries= n = 10     
        file_paths = af.make_permutations(n,label_paths,[.5,.5])
        
        label = ['10 60 14 90 24']*n
        id = ['295844578']*n

        af.write_yolo_annotations(file_paths, list(zip(id,label)))
        for i in range(len(file_paths)):
            filename = file_paths[i]+os.sep+id[i]+"_"+str(i)+".txt"
            self.assertTrue(os.path.isfile(filename),"\n\nTestMessage:\n -inputs: %s\n-Expected output was for this file to be created, but currently it does not exist"%(filename))

if __name__ == '__main__':
    unittest.main()