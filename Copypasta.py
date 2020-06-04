
#This is a function to iteratively find Spread changes within the text file
#
# def spread():
#     index = 0
#     dex = 0
#     out = []
#     write_flag = False
#     param = '                 6,461' #indexed at
#     pl = len(param)
#     dl = len(readfile)
#     #acquires Total Secondary Marketing P/L
#     for index in range(dl):
#         transf_obj = readfile[index]
#         if transf_obj[0:pl] == param:
#             transf_obj_list = list(transf_obj)
#             for dex in range(len(transf_obj_list)):
#                 if transf_obj_list[dex] == '0' or transf_obj_list[dex] == '1' or transf_obj_list[dex] == '2' or \
#                         transf_obj_list[dex] == '3' or transf_obj_list[dex] == '4' or transf_obj_list[dex] == '5' or \
#                         transf_obj_list[dex] == '6' or transf_obj_list[dex] == '7' or transf_obj_list[dex] == '8' or \
#                         transf_obj_list[dex] == '9' or transf_obj_list[dex] == '(' or transf_obj_list[dex] == ')' or \
#                         transf_obj_list[dex] == ',' or transf_obj_list[dex] == '-':
#                     write_flag = True
#                 else:
#                     if write_flag:
#                         return out
#                     else:
#                         write_flag = False
#                 if write_flag:
#                     out.append(transf_obj_list[dex])
#                 dex += 1
#             return out
#         index += 1
#         if index > 40:
#             print(index)



#
# def spread():
#     index = 146
#     dex = 0
#     out = []
#     write_flag = False
#     param = '6,461' #indexed at
#     pl = len(param)
#     dl = len(readfile)
#     transf_obj = readfile[index]
#     transf_obj_list = list(transf_obj)
#     for dex in range(len(transf_obj_list)):
#         if transf_obj_list[dex] == '0' or transf_obj_list[dex] == '1' or transf_obj_list[dex] == '2' or \
#                 transf_obj_list[dex] == '3' or transf_obj_list[dex] == '4' or transf_obj_list[dex] == '5' or \
#                 transf_obj_list[dex] == '6' or transf_obj_list[dex] == '7' or transf_obj_list[dex] == '8' or \
#                 transf_obj_list[dex] == '9' or transf_obj_list[dex] == '(' or transf_obj_list[dex] == ')' or \
#                 transf_obj_list[dex] == ',' or transf_obj_list[dex] == '-':
#             write_flag = True
#         else:
#             if write_flag:
#                 return out
#             else:
#                 write_flag = False
#         if write_flag:
#             out.append(transf_obj_list[dex])
#         dex += 1
#     return out