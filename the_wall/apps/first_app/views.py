from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message, Comment

  # the index function is called when root is visited
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    f = request.POST
    valid = True
    if len(f['first_name']) < 4:
        messages.error(request, 'First name must have at least 4 characters.')
        valid = False
    if len(f['last_name']) < 4:
        messages.error(request, 'Last name must have at least 4 characters.')
        valid = False
    if len(f['email']) < 8:
        messages.error(request, 'Email must have at least 8 characters', extra_tags='email')
        valid = False
    if len(f['password']) < 8:
        messages.error(request, 'Password name must have at least 8 characters.')
        valid = False

    if not f['password'] == f['password_confirmation']:
        messages.error(request, 'Password and passowrd confirmation do not match')
        valid = False

    if not valid:
        return redirect('/')
    else:
        if User.objects.filter(email=f['email']).exists():
            messages.error(request, 'You have already registered, please login.')
            return redirect('/')

        hashed_pw = bcrypt.hashpw(f['password'].encode(), bcrypt.gensalt())

        # print("Password is {}".format(hashed_pw))
        User.objects.create(first_name=f['first_name'], last_name=f['last_name'], email=f['email'], password= hashed_pw)
        messages.success(request, 'You are now registered. Please login.')
    return redirect('/')

def login(request):
    f = request.POST
    print(f)
    try:
        user = User.objects.get(email = f['email'])
        password_valid = bcrypt.checkpw(f['password'].encode(), user.password.encode())
        if password_valid:
            request.session['logged_in'] = True
            request.session['user_id'] = user.id
            # send to next page/url or give message
            messages.success(request, 'You are now logged in.')
        else:
            messages.error(request, "Password/email did not match.")
    except User.DoesNotExist:
        messages.error(request, 'Could not find user with this login info.')
    except Exception as err:
        print(err)
        messages.error(request, 'Something else went wrong.')
    # send to next page/url
    return redirect('/dashboard')

def dashboard(request):
    if not 'user_id' in request.session:
        messages.error(request, 'You need to log in to view this page.')
        return redirect('/')
    all_messages = Message.objects.all().order_by('-created_at')

    context = {
        'all_messages': all_messages,
        'logged_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'first_app/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_message(request):
    print(request.POST)
    if len(request.POST['message']) < 5:
        messages.error(request, 'Your post must have at least 5 characters.')
        return redirect('/dashboard')
    # this next line gets the user object based on the user that is logged in
    user = User.objects.get(id=request.session['user_id'])
    # creates the message -- message comes from the form (request.POST)
    # the user comes from session
    Message.objects.create(message=request.POST['message'], user = user)
    return redirect('/dashboard')


def add_comment(request, message_id):
    print(request.POST)
    if len(request.POST['comment']) < 5:
        messages.error(request, 'Your comment must have at least 5 characters.')
        return redirect('/dashboard')

    user = User.objects.get(id=request.session['user_id'])

    message = Message.objects.get(id=message_id)

    Comment.objects.create(comment=request.POST['comment'], message = message, user = user)

    return redirect('/dashboard')