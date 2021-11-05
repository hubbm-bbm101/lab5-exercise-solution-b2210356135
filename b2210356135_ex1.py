n = int(input("Give me a number: "))
sum_odd = 0
sum_even = 0
even_counter = 0

for i in range(1, n+1):
    if(i%2):
        sum_odd += i
    else:
        sum_even += i
        even_counter += 1
print("Sum of odd numbers: ", sum_odd)
print("Average of even numbers: ", sum_even/even_counter)