# learn basic
# print("Hello world!")
# variables, Strings, Numbers
# Get A User's Input (Test)
# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# print("My name is " + name + " and my age is ", age)

# word replacement exercise
# list in python (mảng giống với js), tạo list có 2 dạng
# countries = ["King", "Kaka", "Australia"]
# thay thế string trong mảng
# countries[0] = "dungvv"
# print(countries[1:])
# print(countries)
# sort như js
# name = ["dung", "hong", "nhung", "tam", "ngoc", "huynh"]
# name.sort()
# print(name)

# list methods
# them mang 2 voa mang 1
# list1 = [1,2,3,4,5,6]
# list2 = ["an", "hinh", "tam", "nhung", "hung", "nga"]
# list1.extend(list2)
# print(list1)

# function
# def greetings_func(name):
#     print("hahaha", name)
# greetings_func('dungvv')
# if ... else...
while True:
    operation = input("Nhập phép tính (+, -, *, /) hoặc 'exit' để thoát: ")

    if operation == 'exit':
        print("Cảm ơn bạn đã sử dụng chương trình.")
        break

    if operation not in ['+', '-', '*', '/']:
        print("Phép tính không hợp lệ! Vui lòng nhập lại.")
        continue
    try:
        num1 = float(input("Nhập số thứ nhất: "))
        num2 = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ.")
        continue

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Lỗi: Không thể chia cho 0!")
            continue
        else:
            result = num1 / num2

    print("Kết quả:", result)
