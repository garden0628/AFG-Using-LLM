from flask import Flask, request, render_template, jsonify
from AFG_system.main_system import Dataset, run_AFG_system

app = Flask(__name__)

@app.route("/generate-feedback", methods=['POST'])
def generate_feedback():
    des = request.form['Description']
    wp = request.form['Wrong_Program']
    tcs = request.form['TestCases']
    print(des, wp, tcs)
        
    Dataset.run(des, wp, tcs)
    patch_program, feedback = run_AFG_system()
    print(patch_program, feedback)
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)