from app import app
 
 
@app.route('/')
def home():
    return "Emily says 'Hello world!'"



