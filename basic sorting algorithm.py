# This projects uses random module to input 5 random numbers and sort them using the function named arrange_list()
# The code from line 3 to 20 was my first attempt in making the algorithm 
import random
rand_list = []
rand_list.append(random.randrange(0,101))
rand_list.append(random.randrange(0,101))
rand_list.append(random.randrange(0,101))
rand_list.append(random.randrange(0,101))
rand_list.append(random.randrange(0,101))
print(rand_list)
def arrange_list(list_):
    for i in range(0,len(list_)):
        if i  != 0:
            if list_[i-1] > list_[i]:
                list_[i],list_[i-1] = list_[i-1],list_[i]
                arrange_list(list_)
    print(list_)
print("firts attempt")
arrange_list(rand_list)

# But this code is not the most right way to sort the list as it gives the same output multiple times
# Here when we get the output after the print statment from line 17 the code is not finished and prints output multiple times 
# This is because the algoritm works with a recursive function and it repeats it self like a loop
# So basically after the first output we need to break the loop to eliminate the excess outpus

# correction
var = True
def _arrange_list_(list_):
  for i in range(0,len(list_)):
        if i  != 0:
            if list_[i-1] > list_[i]:
                list_[i],list_[i-1] = list_[i-1],list_[i]
                arrange_list(list_)
                break
  if var:  
      print(list_)
    var = False

# Note: this will give us the only one output but this is not the fastest as it runs even after giving the required data
