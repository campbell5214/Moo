from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/landing')
def landing():
    return render_template('Landing.html')



@app.route('/size', methods=['GET', 'POST'])
def size():
    if request.method == 'POST':
        # Get size data from the form
        length = float(request.form.get('length'))
        width = float(request.form.get('width'))
        weight = float(request.form.get('weight'))

        # Store the size data to be passed along
        return render_template('Sound.html', length=length, width=width, weight=weight)

    return render_template('Size.html')


@app.route('/sound', methods=['GET', 'POST'])
def sound():
    if request.method == 'POST':
        # Get sound data from the form
        sound = request.form.get('sound')
        length = request.form.get('length')
        width = request.form.get('width')
        weight = request.form.get('weight')

        # Pass the collected data to the next page (Color)
        return render_template('Color.html', sound=sound, length=length, width=width, weight=weight)

    return render_template('Sound.html')


@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        # Get color data from the form
        color = request.form.get('color')
        sound = request.form.get('sound')
        length = request.form.get('length')
        width = request.form.get('width')
        weight = request.form.get('weight')

        # Decision-making logic based on all inputs
        if float(length) > 2.0 and float(width) > 1.5 and float(weight) > 400 and sound == "moo" and color == "brown":
            # It's a cow
            return render_template('Yes.html', length=length, width=width, weight=weight, sound=sound, color=color)
        elif float(length) < 1.0 or float(width) < 0.8 or float(weight) < 100:
            # Definitely not a cow
            return render_template('No.html', length=length, width=width, weight=weight, sound=sound, color=color)
        else:
            # Maybe it's a cow (uncertain)
            return render_template('Maybe.html', length=length, width=width, weight=weight, sound=sound, color=color)

    return render_template('Color.html')


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
