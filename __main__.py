import math

a = [12, 29, 24, 36, 52, 38, 47, 69, 47, 33, 52, 58, 68, 48]
a.sort()
print(a)
print("len of list: " + str(len(a)))

# mean
total = 0
for item in a:
    total = total + item

total = total / len(a)
print("mean = " + str(total))
mean = total


# std deviation
total = 0
nums_squared = [] 
for item in a:
    total = total + abs(item - mean)**2
    nums_squared.append(abs(item - mean)**2)

total = total / len(a)
total = math.sqrt(total)
print("std deviation = " + str(total))

# 'inputs' should be a list of values
def stats_cheat(inputs, *args):
    def print_sort(input_list, from_func):
        new_list = input_list
        new_list = sorted(new_list)
        if not from_func:
            print(new_list)
        return new_list
        
    def mean(input_list):
        total = 0
        for item in input_list:
            total = total + item
        
        total = total / len(input_list)
        print("mean = " + str(total))
        return total
        
    def median(input_list):
        total = print_sort(input_list, True)
        med_index = len(input_list) / 2
        # if number of terms is odd
        if str(med_index).endswith(".5"):
            med_index = med_index + 0.5          # to round up
            total = total[int(med_index) - 1]
			print(total)      # indices start at 0, not 1
            return total 
        # if number of terms is even
        else:
			total = (total[int(med_index) - 1] + total[int(med_index)]) / 2
            print(total)
			return total
            
    def std_deviation(input_list):
		total = 0
		nums_squared = [] 
		for item in input_list:
    		total = total + abs(item - mean)**2
    		nums_squared.append(abs(item - mean)**2)

		total = total / len(input_list)
		total = math.sqrt(total)
		print("std deviation = " + str(total))
		return total

    funcs = {'sort':print_sort, 'mean':mean, 'median':median, 'std deviation':std_deviation 
            }
    for arg in args:
        if arg in list(funcs.keys()):
            if arg == 'sort':
                funcs[arg](inputs, False)
            else:
                funcs[arg](inputs)
        else:
            print("ERROR: Unknown function.")
            return 1
    
if __name__ == "__main__":
  # mainly testing stuff here
  stats_cheat([42, 34, 6, 45], 'sort', 'mean','median')
