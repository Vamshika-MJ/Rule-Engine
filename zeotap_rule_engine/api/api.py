# api/api.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.rule_engine import create_rule, combine_rules, evaluate_rule

from flask import Flask, request, jsonify
from backend.rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Rule Engine API!"

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule')
    ast = create_rule(rule_string)
    return jsonify({"ast": str(ast)})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    asts = [create_rule(rule) for rule in rules]
    combined_ast = combine_rules(asts)
    return jsonify({"combined_ast": str(combined_ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    ast_json = request.json.get('ast')
    data = request.json.get('data')
    result = evaluate_rule(ast_json, data)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
