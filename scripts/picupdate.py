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
andyeventOBJ = em.Event.objects.get(id=2)
mikeeventOBJ = em.Event.objects.get(id=3)
mikeevent2OBJ = em.Event.objects.get(id=4)
mikeevent3OBJ = em.Event.objects.get(id=5)
mikeevent4OBJ = em.Event.objects.get(id=8)
strangereventOBJ = em.Event.objects.get(id=10)

benOBJ.avatar = "/content/media/benavatar.jpg"
benOBJ.save()

mikeOBJ.avatar = "/content/media/mikeavatar.jpg"
mikeOBJ.save()

andyOBJ.avatar = "/content/media/andyavatar.jpg"
andyOBJ.save()

beneventOBJ.thumbnail = "/content/media/event1.jpg"
beneventOBJ.save()

andyeventOBJ.thumbnail = "/content/media/event2.jpg"
andyeventOBJ.save()

mikeeventOBJ.thumbnail = "/content/media/event3.jpg"
mikeeventOBJ.save()

mikeevent2OBJ.thumbnail = "/content/media/event4.jpg"
mikeevent2OBJ.save()

mikeevent3OBJ.thumbnail = "/content/media/event5.jpg"
mikeevent3OBJ.save()

mikeevent4OBJ.thumbnail = "/content/media/event6.jpg"
mikeevent4OBJ.save()
