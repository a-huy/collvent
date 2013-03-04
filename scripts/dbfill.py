import utils.djenv
import accounts.models as am
import events.models as em
import conversations.models as cm

import datetime


am.User.objects.create_superuser(password="", email="ben@gmail.com")
am.User.objects.create_superuser(password="", phone="3336598745", email="insight@yahoo.com")
am.User.objects.create_superuser(password="", phone="7878787871", email="haroldsays@msn.com")
am.User.objects.create_superuser(password="", phone="7147879715")
am.User.objects.create_superuser(password="", email="wing@yahoo.com")
am.User.objects.create_superuser(password="", phone="9092297564")
am.User.objects.create_superuser(password="", email="some_user@bing.com")
am.User.objects.create_superuser(password="", phone="2141247987")
am.User.objects.create_superuser(password="", email="daverm@hotmail.com")
am.User.objects.create_superuser(password="", phone="8085556617", email="blahgosh@aol.com")
am.User.objects.create_superuser(password="", email="cracking@yahoo.com")
am.User.objects.create_superuser(password="", email="ober@msn.com")
am.User.objects.create_superuser(password="", phone="9095556617")
am.User.objects.create_superuser(password="", phone="2155556617")
am.User.objects.create_superuser(password="", email="andy@gmail.com")
am.User.objects.create_superuser(password="", phone="7775556617")
am.User.objects.create_superuser(password="", phone="1112356977", email="inca@hotmail.com")
am.User.objects.create_superuser(password="", email="Mike@gmail.com")
am.User.objects.create_superuser(password="", email="super.man@mountain.com")
am.User.objects.create_superuser(password="", phone="1115556617")
am.User.objects.create_superuser(password="", phone="5545777798", email="something@gmail.com")

em.Place(name="Boiling Crab", 
         street_addr="71 Curtner Ave Ste. #20", 
         city="San Jose",
         zip_code=95125,
         longitude="37.302221",
         latitude="-121.863077"
).save()

em.Place(name="In n Out", 
         street_addr="604 E El Camino Real", 
         city="Sunnyvale",
         zip_code=94087,
         longitude="37.361067",
         latitude="-122.02461"
).save()

em.Place(name="Milagros Cantina", 
         street_addr="1099 Middlefield Road", 
         city="Redwood City",
         zip_code=94063,
         longitude="37.484259",
         latitude="-122.226429"
).save()



benOBJ = am.User.objects.get(email="ben@gmail.com")
andyOBJ = am.User.objects.get(email="andy@gmail.com")
mikeOBJ = am.User.objects.get(email="Mike@gmail.com")


boilingcrabOBJ = em.Place.objects.get(name="Boiling Crab")
innoutOBJ = em.Place.objects.get(name="In n Out")
milagrosOBJ = em.Place.objects.get(name="Milagros Cantina")

time1OBJ = datetime.datetime(2013, 3, 5)
time2OBJ = datetime.datetime(2013, 8, 15)
time3OBJ = datetime.datetime(2013, 3, 7)
time4OBJ = datetime.datetime(2013, 3, 18)
time5OBJ = datetime.datetime(2013, 5, 9)
time6OBJ = datetime.datetime(2013, 6, 25)
time7OBJ = datetime.datetime(2013, 3, 28)
time8OBJ = datetime.datetime(2013, 4, 1)
time9OBJ = datetime.datetime(2013, 3, 8)

em.Event(host=benOBJ, 
         description="Ben's super event", 
         location = milagrosOBJ,
         start_date = time1OBJ
        ).save()
em.Event(host=andyOBJ,
         description="WE GUNNA EAT", 
         location = boilingcrabOBJ,
         start_date =  time2OBJ
        ).save()
em.Event(host=mikeOBJ, 
         description="Classic time", 
         location = innoutOBJ,
         start_date = time3OBJ
        ).save()
em.Event(host=mikeOBJ, 
         description="Super time", 
         location = innoutOBJ,
         start_date = time4OBJ
        ).save()
em.Event(host=mikeOBJ, 
         description="Winning time", 
         location = innoutOBJ,
         start_date = time5OBJ
        ).save()
em.Event(host=benOBJ, 
         description="Spring bing", 
         location = innoutOBJ,
         start_date = time6OBJ
        ).save()
em.Event(host=andyOBJ, 
         description="Hangout version 2", 
         location = innoutOBJ,
         start_date = time7OBJ
        ).save()
em.Event(host=mikeOBJ, 
         description="Kickback", 
         location = innoutOBJ,
         start_date = time8OBJ
        ).save()
em.Event(host=benOBJ, 
         description="Hangout version x", 
         location = innoutOBJ,
         start_date = time9OBJ
        ).save()


beneventOBJ = em.Event.objects.get(id=1)
andyeventOBJ = em.Event.objects.get(id=2)
mikeeventOBJ = em.Event.objects.get(id=3)

em.Invitation(event=beneventOBJ, user=andyOBJ).save()
em.Invitation(event=beneventOBJ, user=mikeOBJ).save()
em.Invitation(event=andyeventOBJ, user=mikeOBJ).save()
em.Invitation(event=mikeeventOBJ, user=benOBJ).save()



cm.Conversation(event = beneventOBJ, title="Discuss eatery places please").save()

benconversationOBJ = cm.Conversation.objects.get(title="Discuss eatery places please")

cm.ConversationContent(title = "Ben's random link",
                       url = "www.bing.com",
                       owner = benOBJ,
                       conversation = benconversationOBJ
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = benOBJ,
                       message = "So I want you to all look at my link",
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = benOBJ,
                       message = "And please be sure to post some of your own ideas where to eat",
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = mikeOBJ,
                       message = "Do perhaps we could try something different this time",
                      ).save()

cm.ConversationContent(title = "Something different",
                       url = "www.google.com",
                       owner = mikeOBJ,
                       conversation = benconversationOBJ
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = mikeOBJ,
                       message = "So I want you to all look at my link",
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = andyOBJ,
                       message = "I wanted to try Thai food this time",
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = mikeOBJ,
                       message = "I'm open to that as well",
                      ).save()

cm.ConversationContent(title = "Thai food",
                       url = "http://en.wikipedia.org/wiki/Thai_cuisine",
                       owner = andyOBJ,
                       conversation = benconversationOBJ
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = andyOBJ,
                       message = "More like that",
                      ).save()

cm.ConversationMessage(conversation = benconversationOBJ,
                       owner = benOBJ,
                       message = "Sounds peachy",
                      ).save()


print "Done filling!\n"








