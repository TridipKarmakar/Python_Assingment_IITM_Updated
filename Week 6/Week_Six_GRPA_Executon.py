# import Week_Six_GRPA_Assingments as week_six


# name, age, rollno = (week_six.get_student_details())
# print(f"The student name is {name}, age is {age} and the roll no is {rollno}.")

# number = ("1,2,3,4,5")

# list_comma_separated_value = week_six.get_comma_separated_integers()
# print(list_comma_separated_value)

# n = 2
# batsman_runs_dict = {}
# batsman_runs = ["Math-90","Science-85"]
# for i in batsman_runs :
#     key, value = i.split("-")
#     batsman_runs_dict[key] = value
# print(batsman_runs_dict)

# n = 2
# batsman_run = []

# for i in range(n):
#     batsman_run.append(input().split("-"))

# # for subject , score  in batsman_run :
# #     Score_dict[subject] = int(score)
# # print(Score_dict)

# Score_dict = {subject : int(score) for subject, score in batsman_run}
# print(Score_dict)

# nums= [1,3,4,5]

# print("{nums[1]:.3f}")
# import random

# # print(num)
# random.seed(42)
# i = 0
# status = False
# while status != True :
    # num = random.randint(0,100)
    # if num == 0 :
    #     print(num)
    #     break 
    # if i % 10 == 0 :
    #     print(num,end = "\n")
    # else :
    #     print(num,end = ",")
    # i += 1
    # for i in range(1,11) :
    #     num = random.randint(0,100)
    #     if i == 10 :
    #         print(num, end="\n")
    #     elif num == 0 :
    #         print(num)
    #         status = True
    #         break     
    #     else :
    #         print(num, end = ",")
    
# name ="player1"
# number=9
# runs=[2,3,4,4,6]

# print(name,number,*runs,sep = ",")

# course_scores = {"course1":78, "course3":89,"course2":90}

# for course, number in sorted(course_scores.items()) :
#     print(f"{course}:{number}")
# batsman_runs = [
#         ("batsman1",[1,2,1,4,6,2,2,1]),
#         ("batsman2",[2,2,6,4,1]),
#         ("batsman3",[6,1,2,4,4,2])]

# for batsman , run in batsman_runs :
#     print(batsman, end = "-")
#     print(*run, sep = ",")

# student_marks = [
#         {'rollno': 1, 'city': 'chennai', 'age': 23, 'course1': 86, 'course2': 69, 'course3': 86}, 
#         {'rollno': 2, 'city': 'mumbai', 'age': 19, 'course1': 78, 'course2': 65, 'course3': 89}
#     ]

# ''''
#     Output: 
#     1,chennai,23,86,69,86
#     2,mumbai,19,78,65,89
#     '''

# for i in student_marks :
#     print(*(list(i.values())),sep = "\n")

# num = 14681

# print(num == int("".join(sorted(list(i for i in str(num))))))
list_of_number  = [1, 2, 3, 121, 23, 32, 450]

count = 0 
for i in list_of_number :
    if len(str(i)) == 1  :
        count += 1
    elif (i == int("".join(sorted(list(k for k in str(i)))))) :
        count += 1
print(count)
