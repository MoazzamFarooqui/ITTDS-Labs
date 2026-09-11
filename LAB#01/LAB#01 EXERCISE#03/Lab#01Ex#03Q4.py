def calculate(numbers):
    maximum=max(numbers)
    minimum=min(numbers)
    average=sum(numbers)/len(numbers)
    return maximum,minimum,average

numbers=[1,2,3,4,5]

maximum,minimum,average=calculate(numbers)

print("Maximum:",maximum)
print("Minimum:",minimum)
print("Average:",average)

