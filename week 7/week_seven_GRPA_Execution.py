# teams = {
#     "KKR": 0,
#     "PK": 0,
#     "DC": 0,
#     "MI": 0,
#     "CSK": 0,
#     "RR": 0,
#     "RCB": 0,
#     "SH": 0
# }
# multiple_inputs = [ 
# "CSK,DC,KKR,MI,PK,RR,RCB,SH",
# "DC,KKR,MI,PK,RR,RCB,SH",
# "KKR,MI,PK,RR,RCB,SH",
# "MI,PK,RR,RCB,SH",
# "PK,RR,RCB,SH",
# "RR,RCB,SH",
# "RCB,SH",
# "SH" ]

# # for i in multiple_inputs :
# #     for j in i.split(",") :
# #         if j in teams.keys() :
# #              teams[j] -= len(teams.keys())

# # print(teams)

# for i in range(8) :
#     teas_in_line = multiple_inputs[i].split(",")
#     winning_team = teas_in_line[0]
#     teams[winning_team] += len(teas_in_line) - 1

# # def tuple_call(x :tuple) :
# #     return(-x[1],x[0])
# # tuple_dict = teams.items()
# # sorted_teams = sorted(teams.items(),key=tuple_call() )

# # sorted_dict = sorted(teams.values(),key=) 
# print(teams)     

# # tuple_items = list(teams.items())
# # sorted_tuple = sorted(tuple_items, key=lambda x : -x[1])
# # print(dict(sorted_tuple))


# sorted(teams.items(), key=lambda x : (-(x[1])))


# D1 = {1: 2, 2: 3, 3: 4}
# D2 = {1: 10, 4: 15, 5:10}
# priority = "first"

# D1 = {'a': 1, 'b': 2}
# D2 = {'a': 10, 'c': 3}
# priority = "second"

# if  priority == "first" :
#     for key,val  in  D2.items() :
#         if key not in D1 :
#             D1[key] = val
# else :
#     for key,val  in  D1.items() :
#         if key not in D2 :
#             D2[key] = val


# # expected_output  = {'a': 10, 'b': 2, 'c': 3}
# # print(D2 == expected_output)


# # merged = D1.update(D2) 
# # print(merged)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# new_matrix  = []
# row = 0
# col = 1

# for i in  range(len(matrix)) :
#     if i != row :
#             temp_matrix = []
#             temp_file = ""

#             for j in range(len(matrix[0])) :
#                 if j != col :
#                     temp_matrix.append(matrix[i][j])        
#             new_matrix.append(temp_matrix)
            
# for i in new_matrix  :
#     print(*i,sep=",")


expected_output = {
  "Chennai Express": {
    "S1": 5,
    "S2": 10,
    "S3": 15
  },
  "Mumbai Express": {
    "S1": 10,
    "S2": 20
  }
}


time_of_input =  int(input("Enter the number of train details that you want to put : "))

final_train_list = {} 

while  time_of_input !=0 :
    time_of_input -= 1 
    train_name = input("Enter the train name : ")
    number_of_bath = int(input("Enter total Number of bath : "))
    tem_train_list = {}
    for i in range(number_of_bath) :
        name_of_bath = input("enter the name of bath : ")
        num_of_seat = int(input("enter the number of seat : "))
        tem_train_list[name_of_bath] = num_of_seat
    final_train_list[train_name] =  tem_train_list
print(final_train_list)
  