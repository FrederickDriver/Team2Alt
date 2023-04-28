import unittest
import altFile as af
from scipy import stats

class TestStringMethods(unittest.TestCase):

    def test_shuffle_dir(self):
        pass
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
                    "\n\nTestMessage:\n -inputs: {steps} different binary example\n We reject the null hyothesis that the output of make_permutations has the same distribution as p_dist "]

        self.assertEqual(all1, [1]*10,testmsg[0] )
        self.assertEqual(all0, [0]*10,testmsg[1] )
        self.assertTrue(p_value > 0.05,testmsg[2])


  
if __name__ == '__main__':
    unittest.main()