def generate_matchups(n_array):  
  
  if len(n_array) > 1:
  
    median_id = len(n_array) //2
    left_array = n_array[:median_id]
    right_array = n_array[median_id:]
    right_array.reverse()
    
    buffer_array = [i for i in zip(left_array, right_array)]    
    processed_array = generate_matchups(buffer_array)
    
    return processed_array
    
   else:
     return n_array 
