
#HARD-CODING : A value is considered hard-coded if data is fixed and cannot be changed without editing the program itself.
#and it is a dangerous practice. If we hard-coded the player weight at 73kg, then the next time the player changed weight 
#we would need to edit the code—find everywhere the player was mentioned and change 73kg to the new value.

player_weight = 73
print(player_weight)
73
player_weight = 73 + 5
print(player_weight)
78
#Given that the assignment operator works right-to-left, 
#it will first evaluate the player_weight on the right-hand side,
#at which point the variable’s value is 73. The interpreter will take that 73,
#add 5 to it, and return it to be assigned to the item on the left-hand side
#of the operator,which is “player_weight.” In the third line of code we see
#that the player_weight variable now has the value 78.



RESERVED WORDS IN PYTHON 

#In a programming language, some words already have specific meanings and cannot be reused by programmers. These are known as reserved words.
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async',
#'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#'finally', 'for', 'from', 'global', 'if', 'import','in', 'is', 'lambda', 
#'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


