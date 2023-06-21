
"""QUES 1 1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.

answer--

 *        ---- expression multipication operator
'Hello'    ---- value string
 -87.8     --value float
 -         --- expression subtraction operator
 /        ---  expression division operator
 +        ---  expression addition  operator
 6        --- value interger
 """

"""" QUES 2  What is the difference between string and variable? 

It is enclosed within single quotes (' ') or double quotes (" "). Strings can contain letters,
 numbers, symbols, and whitespace.They are typically used to store and manipulate textual data.
  For example, "Hello, World!" 

Variable: A variable is a symbolic name that represents a memory location used to store a value.
 It acts as a container for storing data of different types, including strings.
 Variables are used to store and manipulate data throughout a program
 
 for example--- a = b + c , in this case a is a varible. we can use a = b+c where we wanted. 
 
 """

"""" QUES 3. Describe three different data types.

three most common data type in python are integers , boolean , float 

integer ---  (int): The integer data type represents whole numbers, both positive and negative, 
 without any decimal points.
 For example, 0, 5, -10 are all integers. 
 
float --- data type is used to represent floating-point numbers, which are numbers that can have a decimal point.
Floats are used to store and manipulate decimal values, such as 3.14, -2.5, or 0.
 
Boolean (bool): The boolean data type has only two possible values:
True or False. Booleans are used to represent logical states, such as the result of a comparison or a condition.
They are typically used in decision-making and control flow structures. 
For example, a comparison like 5 > 3 would result in the boolean value True. Booleans are essential for conditions,
 loops, and boolean algebra.

"""

"""" 4. What is an expression made up of? What do all expressions do?

An expression is made up of one or more elements combined together in a meaningful way to produce a value. 
These elements can include literals, variables, operators, and function calls.


4.2--Expressions can be used for various purposes, such as performing calculations, making decisions based on 
conditions,or assigning values to variables. They are an integral part of writing code and manipulating 
data in programming.
"""

""" 5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?

Expressions can be as simple as a single variable or a literal value, or they can be more complex with multiple 
components.
For example, 2 + 3 is an expression that evaluates to 5, and x * y is an expression that calculates the product
of the variables x and y.

A statement is a complete instruction or command that performs an action. It carries out a specific task,
such as assigning values to variables, controlling the flow of execution, or defining functions.
assignment statement like spam = 10 assigns the value 10 to the variable spam.
Other types of statements include if statements, for loops, function declarations, and more.
 
expressions produce a value, whereas statements perform an action or carry out a specific task.
Expressions are often used within statements to compute or determine values. 
Statements are the building blocks of programs, defining the logic and behavior of the code.
"""
"""" 6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
if run it will it give ruselt 22 because no varible assingned in second line.Therefore, the original value of bacon 
remains unchanged. bacon + 1, if we assing varible to second then it works"
"""
bacon = 22
bacon = bacon + 1 # now ruselt will be 23
print (bacon)

"""7. What should the values of the following two terms be?"""
a ='spam' + "spamspam"
print (a)

b = "spam" * 3
print (b)

""""8. Why is eggs a valid variable name while 100 is invalid?

the variable name eggs is valid because it adheres to the rules and conventions 
for variable naming in Python. On the other hand, 100 is invalid because
 it violates the rule of not starting with a digit.
"""
"""9. What three functions can be used to get the integer, floating-point number, or string
version of a value?

three functions to obtain the integer, floating-point number, or string version of a value:
three function are int(),str(),float()

for example int(5.6)  # Returns 5
            float(10)  # Returns 10.0
            str(25)  # Returns "25"
"""
"""10. Why does this expression cause an error? How can you fix it?
"i have eaten" + 99 + "burotios"  """

"""if we run this this will error because  the + operator is used 
for both addition and string concatenation. However, when trying to concatenate a string 
with a non-string value, such as an integer, an error occurs."""
"in order to run this we int to string this process call typecasting "

ab = "i have eaten" + " 99" + " burotios"
print(ab)


























