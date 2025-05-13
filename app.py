from flask import Flask, request

from processing import do_translation

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        inputText = None
        inputText = request.form["inputText"]
        if inputText is not None:
            result = do_translation(inputText)
            return '''
                <html>
                    <body>
                        <p>original: {inputText} The result is: {result}</p>
                        <p><a href="/">Click here to translate again</a> </p>
                    </body>
                </html>
            '''.format(inputText=inputText, result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your text here:</p>
                <form method="post" action=".">
                    <p><input name="inputText" /></p>
                    <p><input type="submit" value="Do translation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)



#from flask import Flask, request
#from processing import do_translate
#
## following example at
## https://blog.pythonanywhere.com/169/
#
#app = Flask(__name__)
#app.config["DEBUG"] = True
#
#@app.route("/", methods=["GET", "POST"])
#def adder_page():
#    errors = ""
#    if request.method == "POST":
#        inputPhrase = None
#        inputPhrase = request.form["Type your entry in traditional spelling here:"]
#        if inputPhrase is not None:
#            result = do_translate(inputPhrase)
#            return '''
#                <html>
#                    <body>
#                        <p>The translation in soundspel is:</p>
#                        <p>{result}</p>
#                        <p><a href="/">Click here to translte another phrase</a>
#                    </body>
#                </html>
#            '''.format(result=result)
#
#    return '''
#        <html>
#            <body>
#                {errors}
#                <p>Enter your phrase:</p>
#                <form method="post" action=".">
#                    <p><input name="inputPhrase" /></p>
#                    <p><input type="submit" value="Translate to Soundspel" /></p>
#                </form>
#            </body>
#        </html>
#    '''.format(errors=errors)
