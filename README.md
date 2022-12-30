# RegEx-and-AST
Implementation of Regular Expression (RegEx) and Abstract Syntax Tree (AST) in Python.

## Regular Expression (RegEx)
•	Step 1: Tokenization of Expression

The first step in implementing a lexical analyzer is to tokenize the expression. This involves breaking down the string into individual elements such as numbers, symbols, and words. 
For example, the expression “ a + (b * c) ” can be broken down into the following tokens:
[ 'a', '+', '(', 'b', '*', 'c', ')' ]

•	Step 2: Building Regex for the Expression

The next step is to build a regular expression (regex) for the expression. This allows the lexer to identify and match patterns within the string. 
For example, the regex for the expression “ a + (b * c) ” might look like this:
[ a-z A-Z ] + |\d + | [ ^ \w \s ]
This regex will match any alphabetic character (a-z or A-Z) or any special character ( + ,  - ,  * ,  / ,  (  or ) ).

•	Step 3: Tokens of the Expression

The final step is to display the output for tokens of the expression. This is done by looping through the expression and matching each element against the regex. If a match is found, the corresponding tag is displayed. 
For example, in the expression “a + (b * c)”, the following tags would be displayed:
['VARIABLE', 'OPERATOR', 'PAREN_OPEN', 'VARIABLE', 'OPERATOR', 'VARIABLE', 'PAREN_CLOSE']

![image](https://user-images.githubusercontent.com/73712563/210098490-3c8f77be-1aa5-43ba-a02d-59f5d0f25a9f.png)

![image](https://user-images.githubusercontent.com/73712563/210098505-8ecbadd7-c40f-45d2-82c8-c87f5941f03b.png)



## Abstract Syntax Tree (AST)
The AST library of python provides the means to construct an abstract syntax tree of a Python code. This is a useful tool for analyzing, understanding and representing the structure of the code.

An AST is a tree structure that represents the syntactic structure of a program. It consists of nodes, which can be either terminals or non-terminals. Terminals are symbols that cannot be further expanded, such as identifiers, literals, operators, and keywords. Whereas non-terminals are symbols that can be further expanded, such as functions, classes, and variables. Moreover, it provides a set of APIs to construct an abstract syntax tree. The APIs can be used to construct a node and then connect it to other nodes in the tree by also providing methods to traverse the tree and perform various operations on it.
The AST library of python is used in many applications such as code analysis, code refactoring, code generation, and static analysis. It is also used to generate code from a given AST.

![image](https://user-images.githubusercontent.com/73712563/210098522-7cd67476-899e-4611-867a-e802f6b5999a.png)

![image](https://user-images.githubusercontent.com/73712563/210098530-75722052-bd64-404e-b550-4ae0732426cb.png)


