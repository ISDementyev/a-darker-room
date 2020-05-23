import time
import keyboard
import threading as thr
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()
sched.start()

def fireCooling():
    global fireNow
    if 0 < fireNow <= 2:
        fireNow -= 1
        fireExamine()

def roomCooling():
    global roomNow
    if 0 < roomNow <= 3:
        roomNow -= 1
        roomExamine()

def fireExamine():
    global fireNow
    print('the fire is', fireStates[fireNow])

def roomExamine():
    global roomNow
    print('the room is', roomTemps[roomNow])

def woodExamine():
    global woodCount
    print('you have',woodCount,"wood")

sched.add_job(fireCooling, 'interval', seconds = 5)
sched.add_job(roomCooling, 'interval', seconds = 15)

fireStates = ['dead','lit','roaring']
fireNow = 0
roomTemps = ['freezing','cold', 'warm', 'hot']
roomNow = 0
stokeCount = 0
woodCount = 10
builder = False
fireExamine()
roomExamine()
woodExamine()

# Room environment
while True:
    keyboard.wait('a')
    if woodCount > 0:
        woodCount -= 1
        stokeCount += 1
        if fireNow < 2:
            fireNow += 1
        if roomNow < 3:
            roomNow += 1
    fireExamine()
    roomExamine()
    woodExamine()
    if stokeCount == 9:
        print("a stranger walks in the room")
        builder = True

# Builder's state

builderStates = ['shivering, cold', 'shivering', 'warm', 'sweating']

def builderHealth(healthnum):
    global builderStates
    time.sleep(25)
    print('The builder is', builderStates(healthnum))

while builder = True:
    builderHealth(roomNow)
