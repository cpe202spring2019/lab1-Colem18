# take in a list of integers. if the input is none, then raise an error. if the list is empty, return none. if the list is filled, iterate through it. while iterating
# through the list, check each integer against the maximum value variable. if the list number is smaller, continue on with the iteration. But if the list
# number is bigger, set the max value variable to that number. return the max value variable at the end.
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list == None:
      raise ValueError
   elif int_list == []:
      return None
   else:
      maxnum = int_list[0]
      for x in int_list:
         if x > maxnum:
            maxnum = x
      return maxnum

# take in a list of integers. if the input is none, raise an error. if the input is an empty list, return none. if the inputed list has at least 1 value in it, check the length
# of the list. if the length of the list is 1, return the list as it is. Otherwise take the value of the first item in the list, run a slice of the list from the
# second item to the end through this same function, essentially removing the first item. After receiving the returned list from that statement, append what was
# originally the first value in the list to the end of this new list and return the resulting list
def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError
   elif int_list == []:
      return None
   else:
      if len(int_list) == 1:
         return int_list
      else:
         temp = int_list[0]
         returnList = reverse_rec(int_list[1:len(int_list)])
         returnList.append(temp)
         return returnList

# take in a target number, a lower bound index, a higher bound index, and a list of integers. if there is no list inputed, raise an error. Otherwise begin looking
# for the target number. first, create a middle index variable by taking the double division average of the high and low bounds. Then check if the middle is equal
# to the target number. if so, return the middle index. Otherwise, check if the the target number is smaller than the middle number. if so, call this method with
# the same parameters except the high is replaced with one index lower than the middle index. return this method call. Otherwise, the target number is deemed higher than the middle, so
# call this method with all the original parameters except the lower is one index above the medium. return this method call
def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError
   else:
      if high == low:
         return None
      else:
         mid = (high + low)//2 + low
         if target == int_list[mid]:
            return mid
         elif target < int_list[mid]:
            return bin_search(target, low, mid - 1, int_list)
         else:
            return bin_search(target, mid + 1, high, int_list)