from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from AFG_system.main_system import Dataset, run_AFG_system
import json

app = Flask(__name__)
CORS(app)
CORS(app, resources={r'*':{'origins':'http://127.0.0.1:5500'}})

@app.route("/generate-feedback", methods=['POST'])
def generate_feedback():
    inputs = request.get_json()
    des = inputs['description']
    wp = inputs['wrong_program']
    tcs = json.loads(inputs['testcase'])
    # print(des, wp, tcs)
    # print(type(des), type(wp), type(tcs), type(tcs[0]))
    # print(tcs[0]['input'])
    # print(tcs[0]['output'])
        
    Dataset.run(des, wp, tcs)
    patch_program, feedback = run_AFG_system()
    
    data = {'des': des, 'wp': wp, 'patch': patch_program, 'feedback': feedback}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)