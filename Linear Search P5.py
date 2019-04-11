# Linear Search


def linear_search(list_name,value):
	return_value = 0
	for item in list_name:
		return_value += 1
		if item	== value:
			return return_value
	return "No"		

#another definition forlinear_search(list_names,value)
 
"""
def linear_search(list_name,value):
	for i in range(len(list_name)):
		if list_name[i] == value:
			return i + 1
	return "No"		
"""


def main():

	list_ = [1,45,32,9,12,3,45]
	choice = input("Press'Y' to continue with default list and 'N' to Enter new List ")
	if choice == "N" or choice =="n":
		string_list = input("Enter your numbers seperated with a Space ")
		list_ = [int(x) for x in string_list.split()]
	list_ = sorted(list_)
	print("list is",list_)	
	while True:
		value = input("Enter the value to search ")
		if value.isdigit():
			value = int(value)
			break
	print("The value",value,"is at",linear_search(list_,value),"position in list")	

if __name__ == '__main__':
			choices = ["Y","y","N","n"]
			while True:
				main()
				while True:
					repeat = input("Press'Y' to Search again and 'N' to Exit ")	
					if repeat in choices:
						break
					print("Please follow instructions correctly")	
				if repeat == "N" or repeat =="n":
					break	

