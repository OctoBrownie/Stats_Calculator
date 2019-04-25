import math

def stats_calc(inputs='help', *args):
	"""This is a basic stats calculator. Call the function with "stats_calc([list of numbers], 'commands')". All commands \
must be inside quotes, otherwise it won't work. 

List of commands:
	sort - sorts the list
	mean - finds the average of all values within the list
	median - finds the middle value of the list
	std deviation - finds the standard deviation of the list
Created by Crystal Lee, in hopes of making the stats unit in her math class easier to go through.
"""	
	def print_sort(input_list):
		print("Original list:" + str(input_list))
		new_list = input_list
		new_list = sorted(new_list)
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
		input_list.sort()
		total = input_list
		med_index = len(input_list) / 2
		# if number of terms is odd
		if str(med_index).endswith(".5"):
			med_index = med_index + 0.5				# to round up
			total = total[int(med_index) - 1]
			print(total)							# indices start at 0, not 1
			return total 
		# if number of terms is even
		else:
			total = (total[int(med_index) - 1] + total[int(med_index)]) / 2
			print(total)
			return total
	def mode(input_list):
		input_list.sort()
		mode_num = [input_list[0], 1]		# index -1 == # of times, all others == nums 
		last_num = [input_list[0], 1]		# the last num used
		
		for item in input_list[1:]:
			if item == last_num[0]:				# keep incrementing until it isn't the last num anymore
				last_num[1] = last_num[1] + 1
			else:								# whereupon it will check whether it is the new mode or not
				if last_num[1] == mode_num[-1]:
					mode_num = mode_num[:-1] + [last_num[0]] + [mode_num[-1]]
				elif last_num[1] > mode_num[-1]:
					mode_num = last_num
				last_num = [item, 1]
				
		if last_num[1] == mode_num[-1]:				# to include the last numbers in the mode count
			mode_num = mode_num[:-1] + [last_num[0]] + [mode_num[-1]]
		elif last_num[1] > mode_num[-1]:
			mode_num = last_num

		# so we don't say everything is the mode
		if (len(mode_num[:-1])*mode_num[-1]) == len(input_list):			# mode(s) * # of times shows up == amt of #s counted
			mode_formatted = "N/A"
		else:
			mode_formatted = "{}".format(mode_num[0])
			for item in mode_num[1:-1]:
				mode_formatted = mode_formatted + ", {}".format(item)

		print("Mode is {0} with {1} times found.".format(mode_formatted, mode_num[-1]))
		return mode_num		# returns modes (index 0 to index -2) and the amount of times found (index -1)
		
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
	
	if inputs == 'help':
		print(stats_calc.__doc__)
		return 0
	elif inputs == []:
		print("Empty list.")
		return 1
	elif not(all(type(item) is int for item in inputs)):
		print("Invalid input list.")
		return 1
	
	functions = {'sort':print_sort, 'mean':mean, 'median':median, 'std deviation':std_deviation, 'mode':mode 
			}
	for arg in args:
		if arg in list(functions.keys()):
			if arg == 'sort':
				functions[arg](inputs, False)
			else:
				functions[arg](inputs)
		else:
			print("ERROR: Unknown function.")
			return 1

if __name__ == "__main__":
	# mainly testing stuff here
	stats_calc([42, 34, 6, 45], 'sort', 'mean','median')
