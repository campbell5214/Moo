from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('Landing.html')


@app.route('/size', methods=['GET', 'POST'])
def size():
    if request.method == 'POST':
        # Get size data from the form
        length = float(request.form.get('length'))
        width = float(request.form.get('width'))
        weight_lbs = float(request.form.get('weight'))

        return render_template('Sound.html', length=length, width=width, weight_lbs=weight_lbs)

    return render_template('Size.html')


@app.route('/sound', methods=['GET', 'POST'])
def sound():
    if request.method == 'POST':
        sound = request.form.get('sound')
        length = request.form.get('length')
        width = request.form.get('width')
        weight_lbs = request.form.get('weight_lbs')

        return render_template('Color.html', sound=sound, length=length, width=width, weight_lbs=weight_lbs)

    return render_template('Sound.html')


@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        color = request.form.get('color')
        sound = request.form.get('sound')
        length = float(request.form.get('length'))
        width = float(request.form.get('width'))
        weight_lbs = float(request.form.get('weight_lbs'))

        # Redirect to the udders page to ask about udders
        return render_template('Udders.html', length=length, width=width, weight_lbs=weight_lbs, sound=sound, color=color)

    return render_template('Color.html')


@app.route('/udders', methods=['GET', 'POST'])
def udders():
    if request.method == 'POST':
        udders = request.form.get('udders')
        length = float(request.form.get('length'))
        width = float(request.form.get('width'))
        weight_lbs = float(request.form.get('weight_lbs'))
        sound = request.form.get('sound')
        color = request.form.get('color')

        # Cow classification logic
        if length > 6.5 and width > 5.0 and weight_lbs > 880 and sound == "moo" and color == "brown" and udders == "yes":
            return render_template('Yes.html', length=length, width=width, weight=weight_lbs, sound=sound, color=color, udders=udders)
        elif length < 3.3 or width < 2.6 or weight_lbs < 220:
            return render_template('No.html', length=length, width=width, weight=weight_lbs, sound=sound, color=color, udders=udders)
        else:
            return render_template('Maybe.html', length=length, width=width, weight=weight_lbs, sound=sound, color=color, udders=udders)

    return render_template('Udders.html')


@app.route('/yes')
def yes():
    return render_template('Yes.html')


@app.route('/no')
def no():
    return render_template('No.html')


@app.route('/maybe')
def maybe():
    return render_template('Maybe.html')


if __name__ == '__main__':
    app.run(debug=True)
