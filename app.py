from flask import Flask, render_template,request,jsonify
from flask_cors import CORS
from chat import get_response
import pyttsx3
from bs4 import BeautifulSoup

app=Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    # TODO: check if text is valid
    response=get_response(text)
    
    message={"answer": response}

# to convert text in to speech

    with open('base.html', 'r') as file:
        html_data = file.read()

    soup = BeautifulSoup(html_data, 'html.parser')
    
    checkbox = soup.find('input', {'type': 'checkbox'})
    # second=soup.find_all('labels', {'type': 'checkbox'})

    # if checkbox.get('checked') == 'checked': (not working)
    if checkbox.has_attr('checked'):


        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()
        print("The checkbox is checked.")
        return jsonify(message)
    else:
        # engine = pyttsx3.init()
        # engine.say(response)
        # engine.runAndWait()
        print("The checkbox is not checked.")
        return jsonify(message)
        

if __name__ =="__main__":
    app.run(debug=True)    