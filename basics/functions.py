import datetime
import getpass

def hello(user):
    print("Hello py develoṕer: ", user)

def now(date):
    print(date)

def app():
    hello(getpass.getuser())
    now(datetime.datetime.now())

app()
