def func(x,y=[4,3]):
    y.append(x)
    return y
print(func(2,[3,4]))


#[3, 4, 2]
#The default value of y is not used in this case because you provided a specific list [3, 4] 
#as the second argument when calling the function,
#which overrides the default value.