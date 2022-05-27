from flask import  Flask,render_template
app=Flask(__name__)
@app.route('/')
def web():
    return render_template('web1.html')
app.run()