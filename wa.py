from flask import Flask, render_template

wa = Flask(__name__)

@wa.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bütün interfeyslərdən giriş üçün host='0.0.0.0'
    wa.run(debug=True, host='0.0.0.0', port=5000)
