import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

secret_key_file = "./thankyouoss-firebase-adminsdk-idy0n-6522e758e1.json"
cred = credentials.Certificate(secret_key_file)
firebase_admin.initialize_app(cred)


def fetch_thank_count(user_name: str, repo_name: str) -> str:
    try:
        db = firestore.client()
        repos = db.collection(u"repos").get()
        docs = repos[0].to_dict()
        count = docs[repo_name]["thankCount"]
        return str(count)

    except:
        return "null"
