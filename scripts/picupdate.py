import utils.djenv
import accounts.models as am
import events.models as em
import conversations.models as cm
import time
import datetime

benOBJ = am.User.objects.get(email="ben@gmail.com")
andyOBJ = am.User.objects.get(email="andy@gmail.com")
mikeOBJ = am.User.objects.get(email="Mike@gmail.com")
strangerOBJ = am.User.objects.get(email="some_user@bing.com")

beneventOBJ = em.Event.objects.get(id=1)


benOBJ.avatar = "/content/media/benavatar.jpg"
benOBJ.save()

mikeOBJ.avatar = "/content/media/mikeavatar.jpg"
mikeOBJ.save()

andyOBJ.avatar = "/content/media/andyavatar.jpg"
andyOBJ.save()

beneventOBJ.thumbnail = "/content/media/event1.jpg"
beneventOBJ.save()