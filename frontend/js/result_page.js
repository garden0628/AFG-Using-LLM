let editor, editor2;
const storedData = localStorage.getItem('Data');
const outputs = JSON.parse(storedData);
const description_content = document.getElementById("description-content");
const feedback_content = document.getElementById("feedback-content");

window.onload = function() {
    editor = ace.edit("editor");
    editor2 = ace.edit("editor2");
    editor.setTheme("ace/theme/chrome");
    editor2.setTheme("ace/theme/chrome");
    editor.session.setMode("ace/mode/python");
    editor2.session.setMode("ace/mode/python");

    description_content.innerText = outputs['des'];
    feedback_content.innerText = outputs['feedback'];
    editor.getSession().setValue(outputs['patch']);
    editor2.getSession().setValue(outputs['wp']);
}

console.log(outputs);