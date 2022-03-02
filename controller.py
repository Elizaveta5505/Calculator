import dif as dif     
import user_int
 
def console(): 
    value_a = user_int.get_value() 
    value_b = user_int.get_value() 
    dif.init(value_a, value_b) 
    result = dif.do_it() 
    user_int.user_data(result, 'result')  