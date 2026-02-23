from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

"""
Parse et évalue une expression mathématique simple.

Cette fonction prend une expression contenant deux opérandes et un seul
opérateur, la parse et retourne le résultat du calcul.

Args:
    expr (str): L'expression à évaluer (format: "nombre operateur nombre").
                Les espaces sont ignorés.

Returns:
    float: Le résultat de l'opération mathématique.

Raises:
    ValueError: Si l'expression est vide, invalide, contient plusieurs
                opérateurs, ou si les opérandes ne sont pas des nombres.
"""
def calculate(expr: str):
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

"""
Route principale de l'application.

Gère les requêtes GET et POST.

Returns:
    str: La page HTML rendue avec le résultat du calcul (le cas échéant).
            En cas d'erreur lors du calcul, un message d'erreur est affiché.
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)