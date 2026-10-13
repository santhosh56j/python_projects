import os, json, base64, getpass
from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
FILE = "vault.json"
def key_from_password(password, salt):
    raw = pbkdf2_hmac("sha256", password.encode(), salt, 200_000, 32)
    return base64.urlsafe_b64encode(raw)
def load():
    if not os.path.exists(FILE): return None
    with open(FILE) as f: return json.load(f)
master = getpass.getpass("Master password: ")
data = load()
if data:
    salt = base64.b64decode(data["salt"])
    key = key_from_password(master, salt)
    f = Fernet(key)
    try:
        records = json.loads(f.decrypt(data["blob"].encode()).decode())
    except Exception:
        raise SystemExit("Wrong password or damaged vault.")
else:
    salt = os.urandom(16); key = key_from_password(master, salt)
    f = Fernet(key); records = {}
while True:
    print("\n1.Add  2.List  3.Get  4.Delete  5.Exit")
    choice = input("Choice: ")
    if choice == "1":
        site = input("Site: "); user = input("Username: ")
        pwd = getpass.getpass("Password: ")
        records[site] = {"username": user, "password": pwd}
    elif choice == "2":
        print(*records.keys(), sep="\n")
    elif choice == "3":
        site = input("Site: "); print(records.get(site, "Not found"))
    elif choice == "4":
        records.pop(input("Site: "), None)
    elif choice == "5":
        blob = f.encrypt(json.dumps(records).encode()).decode()
        with open(FILE, "w") as fp:
            json.dump({"salt": base64.b64encode(salt).decode(), "blob": blob}, fp)
        break