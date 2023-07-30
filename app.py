from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load classroom data from the JSON file
with open('data/classroom_data.json') as f:
    classroom_data = json.load(f)

volunteers = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        location = request.form['location']
        spoken_languages = request.form['spoken_languages']
        availability = request.form['availability']

        # Store the volunteer data in the list
        volunteers.append({
            'name': name,
            'location': location,
            'spoken_languages': spoken_languages,
            'availability': availability
        })

        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/volunteers')
def volunteer_list():
    return render_template('volunteers.html', volunteers=volunteers)

if __name__ == '__main__':
    app.run(debug=True)
