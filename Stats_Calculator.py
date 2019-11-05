import math

def stats_calc(inputs='help', *args):
	"""This is a basic stats calculator. Call the function with "stats_calc([list of numbers], 'commands')". All commands \
must be inside quotes, otherwise it won't work. 

List of commands:
	sort - sorts the list
	mean - finds the average of all values within the list
	median - finds the middle value of the list
	mode - finds the number(s) that occur most in the data
	range - finds the range of the set
	5 num summary - returns the five number summary (min, lower quartile median, median, upper quartile median, max)
	variance - finds the variance of the list
	mean deviation - finds the average deviation from the mean
	std deviation - finds the standard deviation of the list
"""	
	def print_sort(input_list, level):
		print("Original list: " + str(input_list))
		new_list = input_list
		new_list = sorted(new_list)
		print("Sorted list: " + str(new_list))
		return new_list

	def mean(input_list, level):
		total = 0
		for item in input_list:
			total = total + item

		total = total / len(input_list)
		if level == 1:
			print("mean = " + str(total))
		return total

	def median(input_list, level):
		input_list.sort()
		total = input_list
		med_index = len(input_list) / 2
		# if number of terms is odd
		if str(med_index).endswith(".5"):
			med_index = med_index - 0.5				# to round down
			total = total[int(med_index)]
			if level == 1:
				print("median = " + str(total))							# indices start at 0, not 1
			return total, [med_index] 						# gives the median and index of the median
		# if number of terms is even
		else:
			total = (total[int(med_index) - 1] + total[int(med_index)]) / 2
			if level == 1:
				print("median = " + str(total))
			return total, [med_index - 1, med_index]		# gives the median and indices of the median
		
	def mode(input_list, level):
		input_list.sort()
		
		mode_num = []		# index -1 == # of times, all others == nums 
		num_times = 0
		start_index = 0
		curr_num = input_list[0]
		
		for index, num in enumerate(input_list):
			if num != curr_num:
				if index - start_index > num_times:
				    mode_num = [input_list[index - 1]]
				    num_times = index - start_index
				    print(str(index) + " " + str(start_index))
				elif index - start_index == num_times:
				    mode_num.append(input_list[index - 1])
				curr_num = num 
				start_index = index
		if len(input_list) - start_index > num_times:
		    mode_num = [curr_num]
		    num_times = len(input_list) - start_index
		elif len(input_list) - start_index == num_times:
		    mode_num.append(curr_num)

		# so we don't say everything is the mode
		if num_times == len(input_list):
			mode_formatted = "N/A"
			mode_num = ["N/A"]
		else:
			mode_formatted = "{}".format(mode_num[0])
			for item in mode_num[1:]:
				mode_formatted = mode_formatted + ", {}".format(item)
		
		if level == 1:
			print("Mode is {0} with {1} times found.".format(mode_formatted, num_times))
		return mode_num
	
	def my_range(input_list, level):
			input_list.sort()
			if level == 1:
				print("Range {0}. \nLowest val = {1} \nHighest val = {2}".format(input_list[-1] - input_list[0], 
																				 input_list[0], input_list[-1]))
			return (input_list[0], input_list[-1], input_list[-1] - input_list[0])		# gives (low, high, range)
	
	def variance(input_list, level):
		total = 0
		# for the one time they ask for showing work
		# raw_num_variance = [] 
		for item in input_list:
			total = total + (item - mean(input_list, level=2))**2
			# raw_num_variance.append(item - mean(input_list, level=2))
		total = total / len(input_list)
		if level == 1:
			print("variance = " + str(total))
			# print(raw_num_variance)
		return total
	
	def std_deviation(input_list, level):
		total = variance(input_list, level=2)
		total = math.sqrt(total)
		if level == 1:
			print("std deviation = " + str(total))
		return total
	
	def mean_dev(input_list, level):
		total = 0
		for item in input_list:
			total = total + abs(mean(input_list, level=2) - item)
		total = total / len(input_list)
		if level == 1:
			print("mean deviation = " + total)
		return total
	
	def five_num(input_list, level):
		# returns (low, lq median, median, hq median, high)
		min_num, max_num, input_range = my_range(input_list, level=2)
		median_num, median_indices = median(input_list, level=2)
		
		if len(median_indices) == 2:			# even number of items in list
			median_indices = int(median_indices[1])
			low_quart = input_list[:median_indices]
			high_quart = input_list[median_indices:]
		else:
			median_indices = int(median_indices[0])
			low_quart = input_list[:median_indices]
			high_quart = input_list[median_indices + 1:]		# since we don't count the median as part of either quartile
		low_quart_med = median(low_quart, level=2)[0]
		high_quart_med = median(high_quart, level=2)[0]
		if level == 1:
			print("5 number summary: {0}, {2}, {4}, {3}, {1}".format(min_num, max_num, low_quart_med, high_quart_med, median_num))
		return [min_num, low_quart_med, median_num, high_quart_med, max_num]
	
	if inputs == 'help':
		print(stats_calc.__doc__)
		return 0
	elif type(inputs) is not list:
		print("ERROR: Inputs are not a list.")
		return 1
	elif inputs == []:
		print("ERROR: Empty list.")
		return 1
	elif not(all(type(item) is int for item in inputs)):
		print("ERROR: Invalid input list.")
		return 1
	elif len(args) == 0:
		print("No arguments passed.")
		return 1
	
	functions = {'sort':print_sort, 'mean':mean, 'median':median, 'mode':mode, 'range':my_range, 
				 'std deviation':std_deviation, 'variance':variance, 'mean deviation':mean_dev, '5 num summary':five_num}
	for arg in args:
		if arg in list(functions.keys()):
			functions[arg](inputs, level=1)
		else:
			print("ERROR: {} is an unknown function.".format(arg))
			print("Type in 'stats_calc()' or 'stats_calc('help')' for a list of valid commands.")
			return 1
	return 0

# outlier < quartile 1 - 1.5*iqr 
# outlier > quartile 3 + 1.5*iqr
# iqr == interquartile range 
