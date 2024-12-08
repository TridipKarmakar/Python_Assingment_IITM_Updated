import time # this library is for time measurement   


def obvious_search(l : list, element : int) :
    '''Check if a given element k is present in a list L or not. 
    This function was authored by S. R. S. Iyengar '''
    for x in l :
        if element == x :
            return 1
    return 0 

# list_of_element =  [i for i in range(1000000000)]
# element = 999999766
# a = time.time()
# status_of_element =  binary_search(list_of_element , element )
# b = time.time()
# print(status_of_element, b-a)


def binary_search(l : list, element : int) :
    ''''This function is alternative for the obvious search. It does exactly what is expected from the ovious_search, but in the efficient way. 
    This method is popularly called the binary search'''

    # we want to shrink my list 
    # we will do that using a while loop 
    begin = 0 # first element in L
    end = len(l) -1  # the last element in L is in len(L)
    print(f"outer {begin} and {end}")
    # use a while loop to look at the list and keep halving it 
    while (end - begin > 0 ) : 
        # we will handle the case when the number of elements is less that or equal to 1
        
        #Compute the mid which os the mid point of the begin to end.
        mid  =  (begin+end)//2
        
        print("the begin is : ",begin)
        print("the mid is   : ",mid)
        print("the end is   : ",end)
        print("the list is  : ",l)
        

        if (l[mid] == element) :
            return 1

        #if the middle element is grater that k, then cut the right side and retain the left side. 
        if (l[mid] > element ) :
            end = mid -1 
        
        # if the middle element is less that k, then cut the left side and retain the right side. 
        if(l[mid]<element) :
            begin = mid + 1
        print("this is the end of while loop")

    if begin == element or end == element :
        return 1 
    else :
        return 0


list_of_element =  [i for i in range(10)]
element = 11
a_1 = time.time()
status_of_element_binary =  binary_search(list_of_element , element )
b_1 = time.time()
diff_time_1 = b_1 - a_1  

print(f" this is the result of binary search - status is : {status_of_element_binary} and time is : {diff_time_1}")


a_2 = time.time()
status_of_element_obvious =  obvious_search(list_of_element , element )
b_2 = time.time()
diff_time_2 = b_2-a_2

print(f" this is the result of obvious search - status is : {status_of_element_obvious} and time is : {diff_time_2}")
print(f"the less time taken by binary search {diff_time_2 - diff_time_1}")

print((9+8)//2)