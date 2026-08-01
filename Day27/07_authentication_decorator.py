# Authentication Decorator

def login_required(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome", user)

dashboard("admin")
dashboard("guest")
