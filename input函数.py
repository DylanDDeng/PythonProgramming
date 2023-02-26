# 记录输入的两个数之和 
number_input_a = int(input('Please enter the number you want:'))  

number_input_b = int(input('Please enter the number you want:'))  
print('the summation of the two numbers we enter is: ', number_input_a + number_input_b ) 


# 记录输入100以内的输入的两个数之和，若输入的数超过100，报错  
number_input_a = int(input('Please enter the number you want:')) 
assert number_input_a <100, 'please enter the number less than 100'
number_input_b = int(input('Please enter the number you want:'))  
assert number_input_b <100, 'please enter the number less than 100'
print('the summation of the two numbers we enter is: ', number_input_a + number_input_b ) 

