# fruits = ["Apple","Orange","Grapes","Banana","Cherry"]
# fruit_prices = {"Orange": 4, "Grapes": 3,"Banana": 2, "Cherry": 5,}


   


# # def dictionary_operation(fruit_prices : dict , fruits :list ):
# #     # add the fruit fruits[0] to fruit_prices with cost 3
# #     fruit_prices[fruits[0]] = 3
# #     print(f'1. list of fruits price after adding 3 in 0th index {fruit_prices}')
    
# #     # modify the cost of fruits[1] as 2 in fruit_prices
# #     fruit_prices[fruits[1]] = 2
# #     print(f'2. list of fruits price after update 2 in 1th index {fruit_prices}')
    
# #     # increase the cost of fruits[2] by 2 in fruit_prices
# #     fruit_prices[fruits[2]] += 2
# #     print(f'3. list of fruits price after increase by 2 in 2nd index {fruit_prices}')
    
# #     # delete both key and value for fruits[3] from fruit_prices
# #     del  fruit_prices[fruits[3]]
# #     print(f'4. list of fruits price after after delete the 3rd index fruits {fruit_prices}')
    
# #     # print the price of fruits[4]
    
# #     print(f"5. Price of the fruits in 4th index {fruit_prices[fruits[4]]}")

# #     # print the names of fruits in fruit prices as a list sorted in ascending order
# #     print(f"6. List of fruits {sorted(fruit_prices.keys())}")

# #     # print the prices of the fruits as a list sorted in ascending order.
# #     print(f"7. price of the fruits {sorted(fruit_prices.values())}")

# # ##use of the above functions
# # print("# list of fruits")
# # for i in enumerate(fruits) :
# #    print(i, end = ', ')
# # print('')
# # dictionary_operation(fruit_prices,fruits)
# # def increase_price(fruit_prices) :
# #     '''
# #     Increase the prices of every fruit by 20 percent and round to two decimal places

# #     Arguments:
# #     fruit_prices: dict - fruit name as key and price as value

# #     Return:
# #     None - Do not return any thing - modify inplace

# #     '''

# #     for fruits in fruit_prices:
# #         fruit_prices[fruits] *= 1.2
# #         fruit_prices[fruits]  = round(fruit_prices[fruits],2)

# # increase_value = increase_price(fruit_prices)

# # print(f'8. Fruits value after increase the price of all fruits at 20% {fruit_prices}')

# # str_input = '''Apple,2
# # Banana,3
# # Orange,4
# # Grapes,3
# # Papaya,5'''


# # def dict_from_string(string:str , key_type, value_type) :
# #     D = {}
# #     for line in string.split('\n') :
# #         key, value = line.split(",")
# #         D[key_type(key)] = value_type(value)
# #     return(D) 

# # dict_value = dict_from_string(str_input,str,int)
# # print(f"9. The new dictionary after converting from string {dict_value}")

# def dict_to_string(D : dict) -> str :
#     x = ("\n".join(str(key)+","+str(values) for key,values in D.items()))
#     return str(x)

# print(f"10. The dictionary again converted into a strings \n{(dict_to_string(dict_value))} \n-- The End of GRPA - 1 --")
# print()

# fruit_prices2 =  {'Apple':2.0,'Banana':2.0,'Orange':4.0,'Grapes':3.0,'Papaya':5.0}
# list_purchase = [("Apple",3),("Orange",5),("Grapes",4)]

# def total_price(fruit_prices2: dict, list_purchase ) -> float :

#     total = 0
#     for fruits , qty_purchase in list_purchase :
#         total += (fruit_prices2[fruits] * qty_purchase)

#     return(total) 

# total_price_of_purchase_items = total_price(fruit_prices2,list_purchase)
# print(f"11. The total price of purchased items {total_price_of_purchase_items}")

# def total_price_no_loops(fruit_prices2: dict, list_purchase ) -> float :
#     list_comp = sum((fruit_prices2[fruits] * qty_purchase) for fruits , qty_purchase in list_purchase) 
#     return(f"12. The total price of purchased using sum features {list_comp}")

# total_price_of_purchase_items = total_price(fruit_prices2,list_purchase)
# print(f"12. The total price of purchased using sum features {total_price_of_purchase_items}")


# def find_cheapest_fruit(fruit_prices2 : dict ) -> str :

#     fruit_prices2_tuples =  list(fruit_prices2.items())
#     min_fruits, min_price = fruit_prices2_tuples[0] 

#     for fruit,price in fruit_prices2_tuples[1:] :
#         if price < min_price :
#             min_fruits = fruit 
#             min_price = price
#         elif price == min_price : 
#             min_fruits += ", " + fruit


#     if "," in min_fruits :

#         return(f"13. The cheapest price fruits are {min_fruits} and the price is Rs.{min_price}")

#     else :
#         return(f"13. The cheapest price fruit is {min_fruits} and the price is Rs.{min_price}")

# cheapest_fruit = find_cheapest_fruit(fruit_prices2)
# print(cheapest_fruit)

# def find_cheapest_fruit_without_loop(fruit_prices2 : dict ) -> str :
#     return(min(fruit_prices2, key = fruit_prices2.get), min(fruit_prices2.values()))

# cheapest_fruit_name,cheapest_fruit_price = (find_cheapest_fruit_without_loop(fruit_prices2))
# print("The cheapest fruits is",cheapest_fruit_name,"and the price is rs.",cheapest_fruit_price)



# # list_of_fruits = ["Avocado","Apple","Banana","Blackberry","Cherry","Cranberry","Grape","Mango"]

# # keys_set = set()
# # D = {}
# # for fruit in list_of_fruits :    
# #     keys_set.update(fruit[0]) 

# # for key in keys_set :
# #     D[key] = []
# # print(D)
# # for fruit in list_of_fruits :
# #     print(fruit)
# #     for key in D :
# #         if fruit[0] == key : 
# #             D[key].append(fruit)

# # print(D)


# # group

# list_of_fruits = ["Avocado","Apple","Banana","Blackberry","Cherry","Cranberry","Grape","Mango"]
# def group_fruits (list_of_fruits : list) :

#     fruits_with_first_letter = {}
#     for fruit in list_of_fruits :
#         if fruit[0] not in fruits_with_first_letter :
#             fruits_with_first_letter[fruit[0]] = []
#         fruits_with_first_letter[fruit[0]].append(fruit)
#     return{ letter : sorted( fruits) for letter , fruits in fruits_with_first_letter.items()}

# fruits_list_with_first_letter = group_fruits(list_of_fruits)
# print(f"14. The dictionary of fruits with the first letter as key {fruits_list_with_first_letter}")


# fruits_bin_price = {'Apple':7,'Banana':3,'Orange':4,'Grapes':6,'Papaya':5,'Mango':2,'Amla':1,'Jackfruit':10}

# def bin_fruits(fruits_bin_price : dict ):
#     binned_fruits = { category : set() for category  in ["cheap","affordable", "costly"]}
#     for fruit in fruits_bin_price :
#         if fruits_bin_price[fruit] < 3 :
#             binned_fruits["cheap"].add(fruit)
#         elif  6 >= fruits_bin_price[fruit] >= 3 :
#             binned_fruits["affordable"].add(fruit)
#         else  :
#             binned_fruits["costly"].add(fruit)
        
#     return(binned_fruits)

# bin_fruits_dict = bin_fruits(fruits_bin_price) 
# print(f"15. The list of the bin fruits as per the category is : {bin_fruits_dict}")

# # index of the first occurrence

# row = [0, 0, 1, 1, 0]
# print(f"16. The index number of the first occurrence element in the given list is : {row.index(1)}")

# # index of the last occurrence
# print(f"17. The index number of the last occurrence element in the given list is : {len(row) - 1 - row[::-1].index(1)}")


# matrix = [
# [0, 0, 1, 1],
# [0, 0, 0, 1],
# [1, 1, 1, 1],
# [1, 0, 0, 0],
# [1, 1, 0, 0]
# ] 


# def is_valid_coordinate(x :int , y : int , matrix) :
#     r , c = len(matrix) , len(matrix[0])
#     if 0 <= x < r and 0 <= y <c :
#         return "a valid coordinate in the given matrix."    
#     else :
#         return  "not a valid coordinate in the given matrix." 
# row = 3
# col = 2
# is_valid  = is_valid_coordinate (row, col, matrix)

# print(f"18. The given {row} X {col} is {is_valid}" )
# import re 
# passage='''
# aaaa bbbb cccc AAAA bbbb
# CCCCCC DDDDD CCCCC CdcDC
# abab cDcD
# '''

# set_list ={}
# passage = passage.strip()

# for first_letter in list(re.split(r'[ \n]+', passage)) :
#     if first_letter[0].lower() in set_list   :
#         set_list[first_letter[0].lower()] = set_list[first_letter[0].lower()] +1  

#     elif first_letter[0] not in set_list:
#         set_list[first_letter[0].lower()] = 1

# print(f"19. Maximum number of first letter in a strings is : {max(set_list, key = set_list.get)}")


# matrix = [
# [0, 0, 1, 1],
# [0, 0, 0, 1],
# [1, 1, 1, 1],
# [1, 0, 0, 0],
# [1, 1, 0, 0]
# ] 


# def valid_adjacent_coordinates(x:int,y:int, M):
#     '''
#     Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
#     '''
#     return {
#       (x1,y1)
#       for x1,y1 in {(x-1,y), (x+1,y), (x,y-1),(x,y+1)} # all the possible adjacent coordinates
#       if is_valid_coordinate(x1,y1, M)
#     }

# valid_adj_cod = valid_adjacent_coordinates(1,3,matrix)
# print("20. The adjacent coordinates are : " , valid_adj_cod)
















# '---------------------------------------------------------------------------- OPPE_assingments may sets'
# print()
# print("OPPE_assingments may sets")
# print()
# def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
#     '''
#     Given two integers, find the absolute difference between 
#     their sum and the sum of their squares.
#     Eg. 
#     a, b = 2,3 
#     sum is 5
#     sum of squares is 13 
#     absolute difference is 8

#     Args:
#         a - int : The first integer.
#         b - int : The second integer.

#     Returns:
#         int: absolute difference between the sum and the sum of squares
#     '''     
#     abs_difference =  abs((a*a)-(b*b))

#     return(abs_difference)

# a = 2
# b = 3

# abs_diff = abs_diff_between_sum_and_sum_of_squares(2,3) 

# print(f'1. absolute difference between the sum and the sum of squares is : {abs_diff}')

# strings_swaps  = "abcdefghi"
# strings_swaps  = "abcde"

# def swap_except_middle_three(s : str) :

#     middle_string =  strings_swaps[int(((len(strings_swaps)-1)/2)-1):int(((len(strings_swaps)-1)/2)+2)]
#     right_string = strings_swaps[int(((len(strings_swaps)-1)/2)+2):]
#     left_string = strings_swaps[:int(((len(strings_swaps)-1)/2)-1)]


#     return(right_string+middle_string+left_string)


# strings_swaps_value = swap_except_middle_three(strings_swaps) 

# print(f"2. The modified string with the parts swapped is : {strings_swaps_value}")


# # list1 = [1, 2, 3,4]
# # list2 = ['a', 'b', 'c', 'd']
# # list3 = [(1,1),(2,2),(3,3), (4,4 )]

# # #output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]
# # output = []
# # start = 0 
# # end = 0

# # for items1 in list1 :
# #     end += 1
# #     output.append(items1)
# #     for items2 in list2[start:end]:
# #         print(items2)
# #         output.append(items2)
# #         for items3 in list3[start:end] :
# #             output.append(items3)   
# #             start +=1   
# # print(output)


# def interleave_lists(list1, list2, list3) :
#     list_output = []
#     for item in range(len(list3)) :
#         list_output.extend((list1[item],list2[item],list3[item]))

#     return(list_output)


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [(1,1),(2,2),(3,3)]
    
# output_list = interleave_lists(list1,list2,list3)

# print(f'4. A list containing interleaved elements from all three lists : {output_list}')



# num_input  = "123456"

# def has_more_than_5_unique_digits(num_input) :
#     num_input = set(num_input)
#     if (len(num_input)) > 5 :
#         return True
#     else :
#         return False
# more_than_5_digits = has_more_than_5_unique_digits(num_input)
# print(f'5. True if the integer has more than 5 unique digits, otherwise False. : {more_than_5_digits}')

# #def final_position(pos : tuple, value : tuple , time : int ) -> tuple :
# # if my coordinates 
# pos = (6,3) 
# value = (4,5)
# time = 5

# def final_position(pos : tuple, value :tuple, time : int) -> tuple :

#     # from the above value the final position will be 

#     final_x = (pos[0] + value[0]) * time
#     final_y = (pos[1] + value[1]) * time

#     return((final_x,final_y ))

# get_final_position = final_position(pos,value,time)

# print("6. The final positions is :", get_final_position)

# d = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# l = [9,8,7,1,2]

# def remove_keys_not_in_list (d:dict , l: list ) -> None : 
    
#     key_list = list(d.keys())
#     for i in key_list :
#         if i not in l :
#             del d[i]

# final_dict = remove_keys_not_in_list(d,l)
# print("7. The final dictionary after deleting all keys in mot present in list l :", d )


# passage = '''
# This is a test sentence where I wanted
# to let you know that the sentences are
# multi-line and words are separated by spaces.
# The first letters may be of different case but you
# should consider it as lowercase and return the lowercase
# letter as the result. Also check the other test cases
# where you can easily count the most occuring first letter.
# '''

# import re

# def most_occurring_first_letter(passage: str) -> str :
#     list_of_letter = {}
#     passage = passage.strip()
#     for words in list(re.split(r'[ \n]+', passage)) :
#         if words[0] not in list_of_letter : 
#             list_of_letter[words[0].lower()] = 1
#         else : 
#             list_of_letter[words[0].lower()] += 1

#     return(max(list_of_letter , key=list_of_letter.get)) 


# # problem 4 

# # loop_input = int(input())

# # final_output = [] 

# # while (loop_input > 0) :

# #     numbers = input() 
# #     unique_numbers_set  = set(str(numbers))
# #     list_repetition =  []

# #     for number in unique_numbers_set :

# #         list_repetition.append(str(numbers).count((number))) # number of repetition in the numbers strings
# #         list_repetition.append(int(number))
        
# #     for i in list_repetition :
# #         final_output.append(i)
# #     loop_input -= 1

# # print(final_output)

# def run_length_encode(n : int , numbers : list ):
#     results = []

#     for number in numbers :
#         encoded = []
#         current_digit = number [0]
#         count = 1

#         for i in range(1, len(number)) :
#             if number[i] == current_digit :
#                 count += 1
#             else :
#                 encoded.append(f"{count} {current_digit}")    
#                 current_digit = number[i]
#                 count = 1



# number =  4  # int(input())
# import_data = '' 
# for i in range(number) :
#     import_data_1 = input()
#     import_data += import_data_1
#     import_data += '\n'

# lines  = import_data.strip().split('\n')
# n = int(lines[0].strip())
# numbers = [line.strip() for line in lines[0:]]
# print(numbers)

# def is_odd_indices_alpha_and_even_indices_digits(string : str) -> bool :
    
#     for index ,  char in  enumerate(string) : 
#         if index % 2 == 0 :
#             if not char.isdigit() :
#                 return False
#         else :
#             if not char.isalpha() :
#                 return False
#     return True
# string = 'a1b2c3'
# print("8. Is in odd index the value is alpha and in even index the value is odd ? :", is_odd_indices_alpha_and_even_indices_digits(string ) )


# l = [1, 2, 3, 4, 5, 6]
# #rint("The original list is :", l)
# for i in range(1 , len(l), 2) :
#     l[i-1] , l[i] = l[i] , l[i-1] 

# for i in range(0,len(l),2) :
#     l[i+1] , l[i] = l[i] , l[i+1]


# print("9. swiping the odd index value in even index :", l)

# string_1 = "water"
# string_2 = "watch"
# # expected_output = {'e','r'}
# expected_output = set({})

# # for i in string_1 :
# #         if i not in string_2 :
# #             expected_output.update(i)
# # print(expected_output)
# # alternative logic is set difference : 
# expected_output =  set(string_1) - set(string_2)
# print("10. Unique character presents which are not present in the second strings are :",expected_output )


# is_equal = (2, 3) 
# a , b = is_equal 

# print("11. Final out-put of tuples with ",(a,) * b + (b,) * a)   

# int_n = 5 

# def num_squares(n : int) -> dict[int,int] :
#     final_dict = { i : i**2 for i in range( 1,int_n + 1)}
#     return(final_dict)

# final_output = num_squares(int_n)
# print("11. Dictionary with key and their squares as values :",final_output)


# batsmen = [
# {'name': 'Batsman1', 'runs': 50, 'team': 'TeamA'},
# {'name': 'Batsman2', 'runs': 30, 'team': 'TeamB'},
# {'name': 'Batsman3', 'runs': 70, 'team': 'TeamA'},
# {'name': 'Batsman4', 'runs': 40, 'team': 'TeamC'},
# {'name': 'Batsman5', 'runs': 60, 'team': 'TeamB'}
# ]

# team = 2
# # find out the top 2 teams based on the total run each have scored -
 
# list_of_k = {}

# for dict_from_batsman in   range(len(batsmen)) :
#     if batsmen[dict_from_batsman]["team"] not in list_of_k : 
#         list_of_k[batsmen[dict_from_batsman]["team"]] = batsmen[dict_from_batsman]["runs"]
#     else :
#         list_of_k[batsmen[dict_from_batsman]["team"]] = list_of_k[batsmen[dict_from_batsman]["team"]]+batsmen[dict_from_batsman]["runs"]
# list_of_keys = list(list_of_k.keys())[:team]
# print("12. Top two teams are :" , list_of_keys)


# matrix = [[1, 0, 0, 0],[0, 1, 1, 0],[0, 0, 0, 1],[1, 1, 1, 1]]

# max_zeros1 = -1
# row_index = -1

# for index, row in enumerate(matrix) :
#     zero_count  = row.count(0)
#     if zero_count > max_zeros1 :
#         max_zeros1 = zero_count
#         row_index = index

# print(f"13. The maximum zeros in the index number is {row_index} and maximum zero is {row_index}" )

# matrix = [[1, 0, 0, 0],
#           [0, 1, 1, 0],
#           [0, 0, 0, 1],
#           [1, 1, 1, 1]]

# # # def next_coordinate_with_value (x: int, y: int, matrix ) :
# # # Find the next coordinates 
# # x = 2
# # y = 2
# # coordinates = {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
# # print(coordinates) 
# # for i, j in coordinates :
# #     print(i, j) 


# #next coordinates with value :
# x = 3
# y = 3
# value = 0 

# def next_coordinate_with_value(x, y , value ,matrix ) : 
#     next_coordinates = {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
    
#     for i, j in next_coordinates :
#         if i < len(matrix) and j < len(matrix[0]) : 
#             if matrix[i][j] == value :
#                 return(i, j) 

# next_coordinates = next_coordinate_with_value(x,y,value,matrix)
# print(f"14. The next coordinates is  {next_coordinates}")

# def valid_adjacent_coordinates (x : int , y : int , matrix) :


# matrix = [[1, 0, 0, 0],
#           [0, 1, 1, 0],
#           [0, 0, 0, 1],
#           [1, 1, 1, 1]]

# final_list = []
# for row in range(len(matrix)-1,0, -1) :
#     for col in  range(len(matrix[0])-1,0,-1) :
#         if matrix[row][col] == 1 :
#             final_list.append((row,col))
# print(final_list)
          
# numbers = [0, 8, 5, 3, 10]

# def groupby(data:list, key:callable):
#     '''
#     Given a list of items, and a key, create a dictionary with the key as key function called 
#     on item and the list of items with the same key as the corresponding value. 
#     The order of items in the group should be the same order in the original list
#     '''

#     groups = {}
#     for item in data:
#         group = key(item)
#         if group not in groups:
#             groups[group] = []
#         groups[group].append(item)
#     return groups
# numbers = [0, 8, 5, 3, 10]
# list_of_fruits = ["Apple", "Orange", "Banana"]
# print(list(map(lambda x : x > 5 , numbers)))
# print(list(filter(lambda x : x > 5 , numbers)))
# print(sum(filter(lambda x : len(str(x)) == 2 , numbers)))
# print(all(map(lambda x : "a" in  x.lower()  , list_of_fruits)))

# for index, value in enumerate(list_of_fruits)  :
#     print(f"{index}. {value}" )

# # print(all(map(lambda x : "a" in  x.lower()  , list_of_fruits)))
# countries = ["United States", "Brazil", "Nigeria", "India", "Australia"]
# capitals = ["Washington, D.C.","Brasilia", "Abuja", "New Delhi", "Canberra"]

# for country , capital in zip(countries, capitals) :
#     print(f"{country} - {capital }")

# keys = "abcd"
# value = [1,2,3,4]
# # dict_out = {}
# # for key , value in zip(keys,value) :
# #     dict_out[key] = value

# print(dict(zip(keys,value)))

# def filter_true(x: int ) :
#     if x == 2 :
#         return False 
#     else :
#         return True
    

# # print(list(map(print_list,value)))
# # print(list(filter(filter_true,value)))
# words = ["Apple","Banana","Orange","Kiwi","Cherry"]

# def more_than_five(word : str) :
#     if len(word) > 5 :
#         return True


# word_more_that_five  = list(words.index(i) for i in list(filter(more_than_five ,words )) if i in words )
# print(word_more_that_five)

# print(list(map(lambda x : x[0],filter(lambda y : len(y[1]) > 5 , enumerate(words)))))

# chars = "abcd"
# repeats = [2,4,3,1]


# print("".join((map(lambda x : x[0]* x[1] ,zip(chars,repeats)))))

# matrix = [
# [0, 0, 1, 1],
# [0, 0, 0, 1],
# [1, 1, 1, 1],
# [1, 0, 0, 0],
# [1, 1, 0, 0]
# ]
# output_matrix = [
# [0, 0, 10, 9],
# [0, 0, 0, 8],
# [4, 5, 6, 7],
# [3, 0, 0, 0],
# [2, 1, 0, 0]
# ]

# Count_dig = 1

# for i in range(len(matrix)-1,-1,-1) :
#     print(i)

# for row in  range(len(matrix)-1,-1,-1) :
#     for col in range(0,len(matrix[0])) :
#         if matrix[row][col] == 1 :
#             matrix[row][col] = Count_dig 
#             Count_dig +=1
# print(matrix)


# numbers = [3,4,5,6,7]
# print(list(map(lambda x : x > 5, numbers))) 

# words_str = "Given a list of words check if all words has the letter a(case insensitive) in it."

# words = words_str.split(' ')

# # print(words)
# # print(list(map(lambda x : 'a' in x.lower(), words)))
# list_apple =  ["apple","orange","banana"]

# for i, value in enumerate(list_apple,start=1) :
#     print(i,value)



# words = ["Apple","Banana","Orange","Kiwi","Cherry"]

# list_of_fruits =(list(i[0] for i in list(filter(lambda x : len(x[1]) > 5 ,enumerate(words)))))
# print(list_of_fruits)


# data = ["Apple","Banana","Orange","Orango","Kuttaj","Cherry","Mango"]

# dzier_output = {
#     5: ["Apple", "Mango"],
#     6: ["Banana","Orange","Cherry"]}


# def group_by(data : list , key : callable) :
#     group_by_dict = {}
#     for items in data:
#         group_key = key(items)
#         if group_key not in group_by_dict :
#             group_by_dict[group_key] = []
#         group_by_dict[group_key].append(items)
#     return group_by_dict


# Group_by_dict = group_by(data,len)
# print(Group_by_dict)


# numbers  = ("1,2,3,4,5")
# list_of_ages = list(map(int,numbers.split(",")))
# print(list_of_ages)

name, age, *roll = "Tridip Karmakar", 12, 13, 14 ,15 ,16 ,17, 18, 21 

print(roll)
