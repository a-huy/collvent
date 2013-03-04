from collections import defaultdict
from django.utils import timezone
from datetime import timedelta

class WeekGroup:
	def __init( title ):
		this.title = title
		this.dayGroups = []
	
class DayGroup:
	def __init( date ):
		this.date = date
		this.hourGroups = []
	
class HourGroup:
	def __init( time ):
		this.time = time
		this.events = []

def groupIntoWeeks( events ):
	groups = []
	thisWeek = []
	nextWeek = []
	rest = []
	endThisWeek = timezone.now() - timedelta(hours=8)
	endNextWeek = timezone.now()
	while True:
		if endThisWeek.strftime("%A") == 'Wednesday':
			endNextWeek = endThisWeek + timedelta(days=7)
			break
		endThisWeek += timedelta(days=1)
	for event in events:
		if event.start_date < endThisWeek:
			thisWeek.append(event)			
		elif event.start_date < endNextWeek:
			nextWeek.append(event)
		else:
			rest.append(event)
	if thisWeek:
		# print 'this week: ', thisWeek
		dayGroups = groupIntoDays(thisWeek);
		groups.append( {'title':'This Week', 'dayGroups':dayGroups} )
	if nextWeek:
		dayGroups = groupIntoDays(nextWeek);
		groups.append( {'title':'Next Week', 'dayGroups':dayGroups} )
	if rest:
		dayGroups = groupIntoDays(rest);
		groups.append( {'title':'Rest', 'dayGroups':dayGroups} )
	return groups

def groupIntoDays( events ):
	groups = []
	weekdays = ['sun', 'mon', 'tues', 'wed', 'thur', 'fri', 'sat']
	dayEventLists = defaultdict(list)
	for event in events:
		dayEventLists[event.start_date.weekday()].append(event)
	for index, eventList in dayEventLists.items():
		# print 'dayEventList: ', eventList
		if eventList:
			hourGroups = groupIntoHours( eventList )
			# print 'hourGroups: ', hourGroups
			groups.append( {'day':weekdays[index], 'hourGroups':hourGroups} )
	return groups
 
def groupIntoHours( events ):
	groups = []
	hourEventLists = defaultdict(list)
	for event in events:
		hourEventLists[event.start_date.time().hour].append(event)
	for index, eventList in hourEventLists.items():
		# print 'hourEventList: ', eventList
		if index < 12:
			ampm = 'a'
		else:
			ampm = 'p'
		hour = "%s%s" % ((index % 12), ampm)
		groups.append({'hour':hour, 'events':eventList})
	return groups