from flask import Flask, request, render_template
import re

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/matches', methods=['POST'])
def matches():
    reg_expression = request.form.get('regular_expression')
    test_string = request.form.get('test_string')
    matches = re.findall(reg_expression, test_string)
    return render_template('matches.html', matches=matches)


if __name__=="__main__":
    app.run(debug=True)