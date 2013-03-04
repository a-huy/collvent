import utils.djenv
import accounts.models as am
import events.models as em
import conversations.models as cm
import time
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
strangerOBJ = am.User.objects.get(email="some_user@bing.com")


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
         title="Ben's super event", 
         location = milagrosOBJ,
         start_date = time1OBJ,
         description = "Well this is a event for ben super"
        ).save()
em.Event(host=andyOBJ,
         title="WE GUNNA EAT", 
         location = boilingcrabOBJ,
         start_date =  time2OBJ,
         description = "Let me tell you something about WE GUNNA EAT"
        ).save()
em.Event(host=mikeOBJ, 
         title="Classic time", 
         location = innoutOBJ,
         start_date = time3OBJ,
         description = "Dancing with a classic time come and have some fun"
        ).save()
em.Event(host=mikeOBJ, 
         title="Super time", 
         location = innoutOBJ,
         start_date = time4OBJ,
         description = "A super time is a fun time and the best time come on in"
        ).save()
em.Event(host=mikeOBJ, 
         title="Winning time", 
         location = innoutOBJ,
         start_date = time5OBJ,
         description = "I like to win and so should you and this is it"
        ).save()
em.Event(host=benOBJ, 
         title="Spring bing", 
         location = innoutOBJ,
         start_date = time6OBJ,
         description = "It's spring time so let's have some fun!"
        ).save()
em.Event(host=andyOBJ, 
         title="Hangout version 2", 
         location = innoutOBJ,
         start_date = time7OBJ,
         description = "this should be better than version 1, hopefully"
        ).save()
em.Event(host=mikeOBJ, 
         title="Kickback", 
         location = innoutOBJ,
         start_date = time8OBJ,
         description = "At my place and there should be no neighbors around so blast it"
        ).save()
em.Event(host=benOBJ, 
         title="Hangout version x", 
         location = innoutOBJ,
         start_date = time9OBJ
        ).save()
em.Event(host=strangerOBJ, 
         title="UKNOWN never seen", 
         location = milagrosOBJ,
         start_date = time9OBJ,
         description = "THIS IS A SECRET DESCRIPTION YOU CAN'T SEE IT!"
        ).save()


beneventOBJ = em.Event.objects.get(id=1)
andyeventOBJ = em.Event.objects.get(id=2)
mikeeventOBJ = em.Event.objects.get(id=3)
strangereventOBJ = em.Event.objects.get(id=4)

em.Invitation(event=beneventOBJ, user=andyOBJ).save()
em.Invitation(event=beneventOBJ, user=mikeOBJ).save()
em.Invitation(event=andyeventOBJ, user=mikeOBJ).save()
em.Invitation(event=mikeeventOBJ, user=benOBJ).save()

time1chat = datetime.datetime(2013, 3, 5)
time2chat = datetime.datetime(2013, 3, 6)
time3chat = datetime.datetime(2013, 3, 7)
time4chat = datetime.datetime(2013, 3, 8)
time5chat = datetime.datetime(2013, 3, 9)
time6chat = datetime.datetime(2013, 3, 10)
time7chat = datetime.datetime(2013, 3, 11)
time8chat = datetime.datetime(2013, 3, 12)
time9chat = datetime.datetime(2013, 3, 13)

cm.Conversation(event = beneventOBJ, title="Discuss eatery places please").save()
cm.Conversation(event = beneventOBJ, title="When to eat?").save()
cm.Conversation(event = beneventOBJ, title="General").save()
cm.Conversation(event = strangereventOBJ, title="THREAD SECRET never seen").save()

benconversationWHEREOBJ = cm.Conversation.objects.get(title="Discuss eatery places please")
benconversationWHENOBJ = cm.Conversation.objects.get(title="When to eat?")
benconversationGENOBJ = cm.Conversation.objects.get(title="General")


someoneconversationOBJ = cm.Conversation.objects.get(title="THREAD SECRET never seen")

cm.ConversationContent(title = "Ben's random link",
                       url = "www.bing.com",
                       owner = benOBJ,
                       conversation = benconversationWHEREOBJ
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = benOBJ,
                       message = "So I want you to all look at my link",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = benOBJ,
                       message = "And please be sure to post some of your own ideas where to eat",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = mikeOBJ,
                       message = "Do perhaps we could try something different this time",
                      ).save()

time.sleep(3)

cm.ConversationContent(title = "Something different",
                       url = "www.google.com",
                       owner = mikeOBJ,
                       conversation = benconversationWHEREOBJ
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = mikeOBJ,
                       message = "Check mine out too",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHENOBJ,
                       owner = mikeOBJ,
                       message = "We should discuss the time",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHENOBJ,
                       owner = benOBJ,
                       message = "Yea, how about tomorrow?",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = andyOBJ,
                       message = "I wanted to try Thai food this time",
                      ).save()

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = mikeOBJ,
                       message = "I'm open to that as well",
                      ).save()

time.sleep(3)

cm.ConversationContent(title = "Thai food",
                       url = "http://en.wikipedia.org/wiki/Thai_cuisine",
                       owner = andyOBJ,
                       conversation = benconversationWHEREOBJ
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = andyOBJ,
                       message = "More like that",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = benconversationWHENOBJ,
                       owner = andyOBJ,
                       message = "I can agree with that",
                      ).save()

time.sleep(3)


cm.ConversationMessage(conversation = benconversationWHEREOBJ,
                       owner = benOBJ,
                       message = "Sounds peachy",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = someoneconversationOBJ,
                       owner = strangerOBJ,
                       message = "YOUSHALLNEVER SEE THIS COMMENT",
                      ).save()

time.sleep(3)

cm.ConversationMessage(conversation = someoneconversationOBJ,
                       owner = strangerOBJ,
                       message = "NOR WILL YOU SEE THIS ONE",
                      ).save()

benOBJ.avatar = "/content/media/benavatar.jpg"
benOBJ.save()

mikeOBJ.avatar = "/content/media/mikeavatar.jpg"
mikeOBJ.save()

andyOBJ.avatar = "/content/media/andyavatar.jpg"
andyOBJ.save()

beneventOBJ = "/content/media/event1.jpg"
beneventOBJ.save()

print "Done filling!\n"








