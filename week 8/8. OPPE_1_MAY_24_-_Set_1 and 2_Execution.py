# def abs_diff_between_sum_add_sum_of_sqr(a : int, b:int) :
#     a = a
#     b = b 

#     sum_of_ywo_int = a + b
#     sum_of_squares = a*a + b*b 
#     abs_diff =  abs(sum_of_ywo_int-sum_of_squares)
#     return (f"1. your 1st number is {a} and 2md umber is {b} \n and absolute difference is {abs_diff} ")


# a = int(input("Enter your 1st number : "))
# b = int(input("Enter your 2st number : "))
# abs_diff = abs_diff_between_sum_add_sum_of_sqr(a,b)
# print(abs_diff)


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [(1,1),(2,2),(3,3)]
# final_output = []  

# for i in range(len(list1))  :
#     # final_output.append(list1[i])
#     # final_output.append(list2[i])
#     # final_output.append(list3[i])
#     final_output.extend([list1[i],list2[i],list3[i]])

# print(final_output)

# a = 23456

# print(len(set(str(a))) == len(list(str(a))))
import re 
passage = '''A paragraph 
is a
 group of sentences that develops a single idea. Paragraphs are a fundamental part of any piece of writing that is longer than a few sentences. They help the reader understand the structure of the writing and grasp its main points.'''

dict_letter = {}

passage = (passage.lower().strip())
for i in list(re.split(r"[ \n]+",passage)) :
    if i[0] not in dict_letter :
        dict_letter[i[0]] = 1 
    else :
        dict_letter[i[0]] += 1

print(dict_letter)
print(max(dict_letter, key = dict_letter.get))

tridip = "t1r2i3d4"

