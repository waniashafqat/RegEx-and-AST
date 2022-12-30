# Importing the re module for regular expressions.
import re


# Function for Tokenization of the expression.
def tokenize(expression):
    # Building the RegEx pattern.
    regex = "[a-zA-Z]+|\d+|[^\w\s]"
    tokens = re.findall(regex, expression)
    return tokens


expression = "a + (b * c)"
tokens = tokenize(expression)
print("\nTokens of the expression are: ", tokens)




