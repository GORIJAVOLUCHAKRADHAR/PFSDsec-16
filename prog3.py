#regular expression  library function   1.findall    2.search   3.split    4.sub
import re
x="IN KLU AT KLU"
y= re.findall("KL",x)
print(x)
print(y)

#using search
import re
txt = "The rain in Spain"
x = re.search("i", txt)
print("The first white-space character is located in position:", x.start())

#using split
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#using sub
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)