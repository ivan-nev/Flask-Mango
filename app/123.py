from app import Memory
from datetime import datetime

Memory(memory=25, ts=datetime.now(), device='my_comp2').save()

d=datetime.now()
print (datetime.now())

mems = Memory.objects(device='my_comp2')
print([str(me.id) for me in mems])