let editor;
const description = document.getElementById("description-content");
const testcaseContainer = document.getElementById("testcase-container");
const testcaseWidth = testcaseContainer.clientWidth * 0.45;
var textareas = new Array();

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/chrome");
    editor.session.setMode("ace/mode/python");
}

function sendInputs(data) {
    console.log(data);
    
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/generate-feedback");
    xhr.setRequestHeader("content-type", "application/json");
    
    xhr.onload = () => {
        if (xhr.status == 200) {
            var feedback_results = xhr.response;
            console.log(feedback_results);
            console.log("success");
            localStorage.setItem('Data', feedback_results);
            window.location.replace("http://127.0.0.1:5500/frontend/result_page.html");
        } else {
            alert("Error");
        }
    };
    xhr.send(data);
}

function getTextAreaValues() {
    const values = textareas.map(textarea => textarea.value);
    return values;
}

function changeTCForm(arrayTC) {
    var tc = new Array();
    for (var i=0; i<arrayTC.length; i+=2){
        var setCase = new Object();
        setCase.input = arrayTC[i];
        setCase.output = arrayTC[i+1];
        tc.push(setCase);
    }
    return JSON.stringify(tc);
}

function generateFeedback() {
    var description_content = description.value;
    var code = editor.getSession().getValue();
    var testcases = getTextAreaValues();
    testcases = changeTCForm(testcases);

    var inputs = new Object();
    inputs.description = description_content;
    inputs.wrong_program = code;
    inputs.testcase = testcases;

    var input_data = JSON.stringify(inputs)
    sendInputs(input_data);
}

function addTestCase() {
    var input = document.createElement("textarea");
    var output = document.createElement("textarea");

    input.placeholder = "Input";
    console.log(testcaseContainer.style.width);
    input.style.width = `${(testcaseWidth)}px`;
    input.style.margin = `5px 15px 3px 0`;
    output.placeholder = "Output";
    output.style.width = `${(testcaseWidth)}px`;
    output.style.margin = `5px 15px 3px 0`;

    testcaseContainer.append(input);
    testcaseContainer.append(output);

    textareas.push(input);
    textareas.push(output);
}