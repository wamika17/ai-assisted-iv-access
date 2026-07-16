from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """

    <h1>Smart AI-Assisted IV Access System</h1>

    <hr>

    <h2>Patient Information</h2>

    <p><b>Name:</b> John Doe</p>

    <p><b>Heart Rate:</b> 72 BPM</p>

    <p><b>SpO₂:</b> 98%</p>

    <p><b>Vein Visibility:</b> Good</p>

    <p><b>DIVA Score:</b> 2</p>

    <p><b>Recommended Vein:</b> Left Median Cubital Vein</p>

    """

if __name__ == "__main__":
    app.run(debug=True)
