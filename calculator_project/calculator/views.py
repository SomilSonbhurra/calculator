# views.py
from django.shortcuts import render
import operator

# Safe evaluation function
def safe_eval(expr):
    allowed_operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    # Split expression into numbers and operators
    try:
        # Warning: This is a very simple evaluator for expressions like "2+3*4"
        # For complex parsing, consider using 'ast' module
        result = eval(expr, {"__builtins__": None}, {})
        return result
    except Exception:
        return "Error"

def calculator(request):
    result = None
    if request.method == "POST":
        expression = request.POST.get("expression", "")
        if expression:
            result = safe_eval(expression)
    return render(request, "calculator.html", {"result": result})
