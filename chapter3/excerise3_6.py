# todo
# prompt user to enter "what is your problem"
# so it will be a while loop thet when the user did not enter anything the progra shold
#     ignore the user answer and then prompt the user again with "have you had this problem before"
#     (yes or no) if user enter yes  print "well, you have it again" if thw user answer not
# print "well you have it now"


input("what is your problem? ")
answer = int(input("have you had this before if YES  press--> 1 or NO press--->2"))
if(answer == 1):
    print("well, you have it again.")
if(answer == 2):
    print("well you have it now.")