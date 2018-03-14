from typing import List, Dict
import sys

class Job:
    def __init__(self, start: int, completed: bool, short: bool):
        self.start = start
        self.completed = completed
        self.short = short
    
    def __repr__(self) -> str:
        return '{0}:{1}:{2}'.format(self.start, self.completed, self.short)

def parse_event(e: str):
    pass

events: List[str] = sys.stdin.readlines()

contractors: Dict[str, List[Job]] = {}

for i, event in enumerate(events):
    event = event.strip('\n')

    if 'START' in event:
        name = event.split(';')[0]

        if name not in contractors:
            contractors[name] = [Job(i, False, False)]
        else:
            contractors[name].append(Job(i, False, False))
        
for k,v in contractors.items():
    print(k, v)

