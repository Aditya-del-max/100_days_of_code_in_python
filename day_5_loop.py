'''fruits=["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for fruit in fruits:
    print(fruit)
    print("I love " + fruit + "!")
    if fruit == "Date" and fruit == "Elderberry":
        break
print("All fruits have been printed.", fruit)'''
'''
student_heights = input("Enter the heights of students separated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height: {total_height}")
'''
#x= input("enter numbers with space:- ").split()
#print(max(x))
numbers= input("enter numbers with space:- ").split()
for number in range(0, len(numbers)):
    numbers[number]= int(numbers[number])
heighest_score=0
for number in numbers:
    if number > heighest_score:
        heighest_score = number
print(f"The highest score is: {heighest_score}")
