
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

def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError
   else:
      if len(int_list) == 0:
         return int_list
      else:
         temp = int_list[0]
         returnList = reverse_rec(int_list[1:len(int_list)])
         returnList.append(temp)
         return returnList

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