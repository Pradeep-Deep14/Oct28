string="PYTHON"
List=list((x,len(x))for x in string)
print(List)

#This code converts each character of the string "PYTHON" into a tuple containing the character and its length. 
#Here's the output of the code:[('P', 1), ('Y', 1), ('T', 1), ('H', 1), ('O', 1), ('N', 1)]
#It creates a list of tuples, where each tuple consists of a character from the string and its corresponding length, which is always 1 
#for individual characters in this case.