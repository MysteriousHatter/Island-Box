from django.shortcuts import render
from musicbeats.models import Song, Watchlater, History, Channel,Albums
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.db.models import Case, When
from django.views.generic import  ListView, DetailView
from django.template import loader

def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/musicbeats/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'musicbeats/history.html', {"history": song})

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "Your Song is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your Song is Succesfully Added"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"musicbeats/songpost.html", {'song': song, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "musicbeats/watchlater.html", {'song': song})

def follow_unfollow_profile(request):
    context = {}
    if request.method == "POST":
        check = Channel.objects.filter(user=request.user)
        print(check, len(check))
        if len(check) > 0:

            my_channel = Channel.objects.get(user=request.user)
            pk = request.POST.get('profile_pk')
            context['my_channel'] = my_channel
            obj = Channel.objects.get(pk=pk)

            if obj.user in my_channel.following.all():
                my_channel.following.remove(obj.user)
            else:
                my_channel.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('musicbeats: channel-list-view')

def songs(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.html', {'song': song})

def albumDes(request, id):
    albums = Albums.objects.filter(songs_id=id).first()
    return render(request, 'musicbeats/albumDescription.html', {'albums': albums})

def albums(request):
    album = Albums.objects.all()
    return render(request, 'musicbeats/albums.html', {'albums': album})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)   
        redirect("/")

    return render(request, 'musicbeats/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        Bio = request.POST['bio']
        Img = request.POST['uimages']

        myuser = User.objects.create_user(username, email, pass1, Bio, Img)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)

        channel = Channel(name=username)
        channel.save()

        return redirect('/')

    return render(request, 'musicbeats/signup.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def channelView(request,channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preserved)


    return render(request, "musicbeats/channel.html", {"channel": chan, "song": song})

class ChannelListView(ListView):
    model = Channel
    template_name = 'musicbeats/channel2.html'
    context_object_name = 'profiles' # object_list as default

    def get_queryset(self):
        return Channel.objects.all().exclude(user=self.request.user)

class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'musicbeats/channelDetail.html'


    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Channel.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = {}
        view_profile = self.get_object()
        check = Channel.objects.filter(user=self.request.user)
        print(check, len(check))
        if len(check) > 0:
            context = super().get_context_data(**kwargs)
            my_profile = Channel.objects.get(user=self.request.user)

            if view_profile.user in my_profile.following.all():
                follow = True
            else:
                follow = False

            return context



def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.FILES['images']
       # albumlink = request.POST['album']
        credit = request.POST['credit']
        song = request.FILES['file']

        song_model = Song(name=name, singer=singer, tags=tag, image=image, credit=credit, song=song)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()

    return render(request, "musicbeats/upload.html")


def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs = song.filter(name__icontains=query)

    return render(request, 'musicbeats/search.html', {"songs": qs, "query": query} )


