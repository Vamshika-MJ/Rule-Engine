# backend/rule_engine.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left
        self.right = right
        self.value = value

# Sample to create AST for rule
def create_rule(rule_string):
    # Parse the rule string and return the AST (Node structure)
    # Placeholder for actual parsing logic
    pass

def combine_rules(rules):
    # Logic to combine multiple ASTs
    pass

def evaluate_rule(ast, data):
    # Evaluate the AST against input data
    pass


import re

def create_rule(rule_string):
    # Simplified parsing logic for example
    tokens = re.findall(r'\w+|[><=]|[()]+|AND|OR', rule_string)
    stack = []
    
    for token in tokens:
        # Build AST (simple parser for now)
        # Add logic to handle parentheses and operators
        pass
    
    return Node("operator", left=None, right=None)  # Example node

def combine_rules(rules):
    # Logic to merge ASTs
    # This is an example where we just combine two rules for simplicity
    combined_ast = Node("operator", left=rules[0], right=rules[1], value="AND")
    return combined_ast

def evaluate_rule(ast, data):
    # Recursively evaluate the AST against the input data
    if ast is None:
        return False
    if ast.type == "operand":
        # Evaluate operands
        return data.get(ast.value)
    # Evaluate operators recursively
    left_eval = evaluate_rule(ast.left, data)
    right_eval = evaluate_rule(ast.right, data)
    
    if ast.value == "AND":
        return left_eval and right_eval
    elif ast.value == "OR":
        return left_eval or right_eval
    return False
