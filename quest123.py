# def num_to_words(num):
#     if num < 0:
#         return "minus " + num_to_words(-num)
#     if num == 0:
#         return "zero"


#     units = [
#         "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
#     ]
#     teens = [
#         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
#         "sixteen", "seventeen", "eighteen", "nineteen"
#     ]
#     tens = [
#         "", "", "twenty", "thirty", "forty", "fifty", "sixty",
#         "seventy", "eighty", "ninety"
#     ]
#     thousands = "thousand"

#     words = ""

#     if num >= 1000:
#         words += units[num // 1000] + " " + thousands + " "
#         num %= 1000

#     if num >= 100:
#         words += units[num // 100] + " hundred "
#         num %= 100

#     if num >= 20:
#         words += tens[num // 10] + " "
#         num %= 10

#     if num >= 10:
#         words += teens[num - 10] + " "
#     else:
#         words += units[num] + " "

#     return words.strip()

# if __name__ == "__main__":
#     try:
#         number = int(input("Enter a number (0-9999): "))
#         if 0 <= number <= 9999:
#             print(f"{number} in words is: '{num_to_words(number)}'")
#         else:
#             print("Please enter a number between 0 and 9999.")
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2  
#         left_half = arr[:mid]  
#         right_half = arr[mid:]

#         merge_sort(left_half) 
#         merge_sort(right_half)  

#         i = j = k = 0  

        
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

        
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     return arr
# def printarray(arr):
#     for i in range(len(arr)):
#         print(arr[i],ends=' ')
#     print()
# arr = [7,2,5,6,3,1,8,4]
# print ("original array is: ",arr)

# merge_sort(arr)

# print ("sorted array is: ")
# printarray(arr)
# if __name__ == "__main__":
   
#     input_array = input("Enter numbers separated by spaces: ")

#     sample_array = list(map(int, input_array.split()))
    
#     sorted_array = merge_sort(sample_array)
#     print("Sorted array:", sorted_array)
def binarysearching(arr,x,low,high):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[11,22,35,56,89,93]
x=int(input('enter the element to search :'))
result=binarysearching(arr,x,0,len(arr)-1)
if result!= -1:
    print('the sorted index is :' , result)
else:
    print('not found')