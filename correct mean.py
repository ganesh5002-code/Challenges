# correcting the mean of 40 numbers
mean1 = 38
total_numbers = 40
wrong_number = 56
correct_number = 36

print("The incorrect mean is", mean1)

incorrect_sum = mean1*total_numbers
print("The incorrect sum is", incorrect_sum)

correct_sum = incorrect_sum - ((wrong_number)-(correct_number))
print("The correct sum is", correct_sum)

mean2 = correct_sum/total_numbers
print("The correct mean is", mean2)
