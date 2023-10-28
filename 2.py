def func():
    try:
        return 10
    finally:
        return 20
print(func())


#20
#Though there is try block if finally block is present 
#the return value in finally block is executed