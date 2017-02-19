import jimbob
import unittestdef 
three_times_x_plus_two(x):   
   y = jimbob.three_times(x)    
   if y is None:        
       return None    
   else:        
       return y + 2
       
       
class MyTest(unittest.TestCase):    
    def test(self):        
        self.assertEqual(three_times_x_plus_two(3), 11)        
        self.assertEqual(three_times_x_plus_two(3.1), 11.3)        
        self.assertEqual(three_times_x_plus_two("a"), None)
