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