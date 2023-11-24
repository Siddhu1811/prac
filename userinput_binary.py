import array as arr
def accept_roll():
    a = arr.array('I', [])    #from array import *  
                            #arrayName = array(typecode, [initializers])   
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(int(input("Enter the Roll Number : ")))
    return a


# Print the Roll Numbers of the Students

def print_roll(a):
    for i in range(0, len(a)):
        print("\t", a[i], end=" ")
    print()
    

# It returns location of x in given array arr
# if present, else returns -1
def binary_search_NR(a, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if a[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif a[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver program
if __name__ == "__main__":

   #unsort_A = arr.array('I', [])  # array of unsigned integer
   #ins_sort_A = arr.array('I', [])
    flag = 1

    while flag == 1:
        menu = "1. Accept Student Roll Numbers of students who attended training program\n" \
               "2. Display the Roll Numbers of students who attended training program\n" \
               "3. Binary Search (Non-Recursive) \n" \
               "4. Exit \n "
        print(menu)

        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_roll()

        elif choice == 2:
            print_roll(unsort_A)


        elif choice == 3:
            roll = int(input("Enter the Roll Number to be search : "))

            index = binary_search_NR(unsort_A, 0, len(unsort_A) - 1, roll)
            if index == -1:
           
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        else:
            print("Wrong choice")
            flag = 0
