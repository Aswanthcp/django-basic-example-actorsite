import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.


my_dict = [
    {
    'image':"https://assets.gqindia.com/photos/6254110f5f4f4f56d4a3d7d2/2:3/w_720,h_1080,c_limit/Yash%20to%20Ram%20Charan%20These%20are%20the%2011%20highest-paid%20South%20Indian%20actors.jpg",
    "name":"Yesh ",
    "details":"Born on 8th January 1986, Yash started his acting career in theatre. He made his television debut with the Kannada show Nanda Gokula which was extremely successful and worked in various other TV shows after that. He made his big screen debut with Moginna Manasu and headlined many superhits like Googly, Raja Huli, Gajakesari, and Mr and Mrs Ramachari."
},
    {
    'image':"https://igimages.gumlet.io/tamil/gallery/actor/dhanush/dhanush090218_9.jpg?w=600&dpr=1.3",
    "name":"Danush",
    "details":"Venkatesh Prabhu Kasthuri Raja (born 28 July 1983),[3] known professionally as Dhanush, is an Indian actor, producer, director, lyricist and playback singer who predominantly works in Tamil cinema.[4] Starring in 46 films over his career, among his accolades are four National Film Awards."
},
        {
    'image':"https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Sushant_sr_Manish_M_B%27day_bash.jpg/330px-Sushant_sr_Manish_M_B%27day_bash.jpg",
    "name":"Sushant Kumar",
    "details":"Sushant Singh Rajput was born on January 21, 1986 in Purnia, Bihar to K. K. Singh and Usha Singh. He has 4 sisters (i.e. Neetu, Meetu, Priyanka & Shweta). He was an Indian television & film actor, dancer and entrepreneur. He became a household name after playing the role of Manav in the TV series,. "
},
        {
    'image':"https://www.themoviedb.org/t/p/w235_and_h235_face/wvoBULQimwguAGPOHZ8TDoy7jBJ.jpg",
    "name":"Mohanlal",
    "details":"Mohanlal was born to Viswanathan Nair (father) and Santhakumari (mother) in the Pathanamthitta district of Kerala, which is located in the southern part of India on the 21st May 1960. Starting his career with a classic villain role, he has now become an outstanding actor in Malayalam Cinema"
},
]




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        print(2)
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            request.session['username'] = username
            # login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Bad Credentials!!")
    return render(request, "signin.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request, "index.html",{"my_dict":my_dict})
    return redirect(login_user)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(login_user)