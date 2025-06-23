import scratchattach as sa
cloud = sa.get_scratch_cloud("1191601784")
events = cloud.events()

@events.event
def on_set(activity): 
    print(f"Variable {activity.var} was set to the value {activity.value} at {activity.timestamp} by {activity.username}")
@events.event
def on_ready():
   print("Event listener ready!")

events.start()