from flask import Flask, request
from spacy_voices import is_passive

app = Flask(__name__)

def form_html(display_text):
    basic_template = """<style>
                        textarea {
                        width: 100%;
                        height: 100px;
                        padding: 12px 20px;
                        box-sizing: border-box;
                        border: 2px solid #000;
                        border-radius: 4px;
                        background-color: #DCDCDC;
                        font-size: 16px;
                        resize: none;
                        }
                        </style>
                        <form method="POST">
                        <textarea name="textbox"></textarea>
                        <button type="submit" name="submit">Submit</button>
                        </form>"""
    splice = basic_template.find("<button type")
    return_template = basic_template[:splice]+"<br><br><pr>"+ \
    display_text+"</br></br></pr>"+ \
    basic_template[splice:]
    return return_template

@app.route('/voice', methods=['GET', 'POST'])
def predict_voice():
    if request.method == 'POST':
        sentence = request.form.get('textbox')
        is_passive_ = is_passive(sentence)
        if is_passive_ == 'Active':
            color =  "#88f042"
        else:
            color =  "#ee2b2b"
        render_output = f"""<method class = entity style = "background: {color};
                                                            padding: 0.25em 0.3em;
                                                            margin: 0 0.25em;
                                                            line-height: 1;
                                                            border-radius: 0.35em;
                                                            -webkit-box-decoration-break: clone">{is_passive_}</method>"""
        return form_html(sentence + " = " + render_output)


    elif request.method == 'GET':
        #form_html("Some text")
        #return """<!DOCTYPE html><html><head>
        #<form method="POST">
        #<input name="text">
        #<input type="submit">
        #<br><pr>Output goes here</pr></br>
        #</form>"""
        return """<style>
        textarea {
        width: 100%;
        height: 100px;
        padding: 12px 20px;
        box-sizing: border-box;
        border: 2px solid #000;
        border-radius: 4px;
        background-color: #DCDCDC;
        font-size: 16px;
        resize: none;
        }
        </style>
        <form method="POST">
        <textarea name="textbox"></textarea>
        <br><br><pr>
        <button type="submit" name="submit">Submit</button>
        </br></br></pr>
        </form>"""

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
