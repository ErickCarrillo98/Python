from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/<num>')
def rowsDown(num):
    return render_template('index2.html', down = num)


if __name__=="__main__":
    app.run(debug = True)
