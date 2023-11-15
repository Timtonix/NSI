from InquirerPy import prompt, inquirer
import api


questions = [
    {
        "name": "method",
        "type": "list",
        "message": "Select a convert method",
        "choices": ["Rouge", "Vert", "Bleu"]

    }]
