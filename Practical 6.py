# Binary Search
import bisect

def binary_search(list_name,value):
	i = bisect.bisect_left(list_name,value)
	if i != len(list_name) and list_name[i] == value:
		return i + 1
	else:
		return "No"	

def main():
	list_ = [1,45,32,9,12,3,45]
	
	print("list is",list_)
	choice = input("Press'Y' to continue with default list and 'N' to Enter new List ")
	if choice == "N" or choice =="n":
		string_list = input("Enter your numbers seperated with a Space ")
		list_ = [int(x) for x in string_list.split()]
	list_ = sorted(list_)	
	while True:
		value = input("Enter the value to search ")
		if value.isdigit():
			value = int(value)
			break
	print("The value",value,"is at",binary_search(list_,value),"position in list")	

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
	

