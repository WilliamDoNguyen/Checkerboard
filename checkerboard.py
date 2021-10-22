from flask import Flask, render_template
checkerboard = Flask(__name__)

@checkerboard.route('/')
def cond_one():
    reps = 8
    return render_template("checkerboard.html", reps = reps)

@checkerboard.route('/4')
def cond_two():
    reps = 4
    return render_template("checkerboard2.html", reps = reps)


@checkerboard.route('/<x>/<y>')
def cond_three(x,y):
    reps = int(x)
    inner = int(y)
    return render_template("checkerboard3.html", reps = reps, inner = inner)

if __name__=="__main__":
    checkerboard.run(debug=True)
