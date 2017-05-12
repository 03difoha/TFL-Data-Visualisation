import pyrebase


config = {
  "apiKey": "XXXXXXXXX",
  "authDomain": "XXXXXXXX",
  "databaseURL": "XXXXXXXXX",
  "storageBucket": "XXXXXXXXX",
  "serviceAccount": "XXXXXXXXX"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("YOUR-EMAIL", "FIREBASE PASSWORD")
db = firebase.database()