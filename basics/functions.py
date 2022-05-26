import datetime
import getpass

def hello(user):
    text = user
    print("Hello py develoṕer: ", text)

def now():
    print(datetime.datetime.now())

def app():
    hello(getpass.getuser())
    now()

app()
