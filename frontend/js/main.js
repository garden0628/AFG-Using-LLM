let editor;
const description = document.getElementById("description-content");
const testcaseContainer = document.getElementById("testcase-container");
const testcaseWidth = testcaseContainer.clientWidth * 0.45;
const textareas = [];

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
}

function getTextAreaValues() {
    const values = textareas.map(textarea => textarea.value);
    return values;
}

function appendToForm(form, value, key) {
    var hiddenField = document.createElement('input');
    hiddenField.setAttribute('type', 'hidden');
    hiddenField.setAttribute('name', key);
    hiddenField.setAttribute('value', value);
    form.appendChild(hiddenField);
}

function sendInputs(description_content, code, testcases) {
    var form = document.createElement("form");
    form.setAttribute('method', 'post');
    form.setAttribute('action', 'http://127.0.0.1:5000/generate-feedback');
    document.charset="utf-8";
    
    appendToForm(form, description_content, "Description");
    appendToForm(form, code, "Wrong_Program");
    appendToForm(form, testcases, "TestCases");

    document.body.appendChild(form);
    form.submit();
}

function generateFeedback() {
    var description_content = description.value;
    var code = editor.getSession().getValue();
    var testcases = getTextAreaValues();

    sendInputs(description_content, code, testcases);
    // console.log(description.value);
    // console.log(code);
    // console.log(testcases);
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

    testcaseContainer.appendChild(input);
    testcaseContainer.appendChild(output)

    textareas.push(input);
    textareas.push(output);
    console.log(textareas);
}