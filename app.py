Config = {
    "apiKey": "AIzaSyCPoxbn9xRpDQg82gmU4dEFvPjQtjmyCkw",
    "authDomain": "tutorial-e31ea.firebaseapp.com",
    "databaseURL": "https://tutorial-e31ea.firebaseio.com",
    "projectId": "tutorial-e31ea",
    "storageBucket": "tutorial-e31ea.appspot.com",
    "messagingSenderId": "334563498521",
    "appId": "1:334563498521:web:19a8efdd1cd18f9cefa888",
    "measurementId": "G-2278S0VQ60"
  }

firebase = pyrebase.initialize_app(config)
 
db = firebase.database()

@app.route('/api/data/co2',methods=["GET","POST"])
def a():
    if request.method=='GET':
        value=request.args.get('')
        return value

if __name__ == "__main__":
    app.run()

    

