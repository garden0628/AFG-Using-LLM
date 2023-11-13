let editor;
const description = document.getElementById("description-content");
const testcaseContainer = document.getElementById("testcase-container");
const testcaseWidth = testcaseContainer.clientWidth * 0.45;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
}

function generateFeedback() {
    var code = editor.getSession().getValue();
    var testcases = [];

    console.log(description.value);
    console.log(code);
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
}