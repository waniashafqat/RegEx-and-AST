# Importing the AST library for syntax tree.
import ast

# Creating a syntax tree.
syntax_tree = ast.parse("print(3+(5*2))")
print(syntax_tree)

print("The syntax tree is: ")
print(ast.dump(syntax_tree))

# Executing the abstract syntax tree.
exec(compile(syntax_tree, filename="", mode="exec"))

