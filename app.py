from flask import Flask,request,render template
from deep translator  import Google translator

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    telugu_text=''
    tamil_text=''
    error=''
    if request.method=='POST':
        telugu_text=request.form.get('telugu_text','').strip()
        if telugu_text:
            try:
                translator =GoogleTranslator(
                    source="te",
                    target="ta",
                )
                tamil_text=translator.translate(telugu_text)
            except Exception as e:
                error="Translation Failed .Please try again."
        else:
            error="please enter telugu text."
        return
            

if __name__ == '__main__':
    app.run(debug=True)