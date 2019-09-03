#Program to convert string to integer array


#inputs required:
string="1,200,34,4,5,6"

seperator=','




#function [requires input in above format]


def string_to_array(string, seperator):
    




    b=list(list(string.split(seperator)))
    o=[]


    for i in range(0,len(b)):
        o.append(int(b[i]))


    return o





#function call

print(string_to_array(string,seperator))


