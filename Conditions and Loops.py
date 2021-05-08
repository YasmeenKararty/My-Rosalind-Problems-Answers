a=4606
b=9428
sumOfOdd=0
if a%2==0: #to make sure it is odd so we can directly increment loop by 2
    a=a+1
for num in range(a,b+1,2):
    sumOfOdd+=num

print(sumOfOdd)
