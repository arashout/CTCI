from typing import List, Dict
import sys

# ENUMS -> Helps with type completetion and accidental misspelling
SUSPICIOUS_BATCH = 'SUSPICIOUS_BATCH'
SHORTENED_JOB = 'SHORTENED_JOB'

class Job:
    def __init__(self, contractor_name: str, start_line: int):
        self.contractor_name = contractor_name
        self.start_line = start_line

        # To be set later
        self.violation_type = 'None'
        self.completion_line = 0                
    
    def __repr__(self) -> str:
        if self.violation_type == SHORTENED_JOB:
            return '{0}:{1}:{2}'.format(self.start_line, self.contractor_name, self.violation_type)
        elif self.violation_type == SUSPICIOUS_BATCH:
            return '{0}:{1}:{2}'.format(self.completion_line, self.contractor_name, self.violation_type)
        else:
            return '{0}:{1}'.format(self.start_line, self.contractor_name)

    def __str__(self) -> str:
        if self.violation_type == SHORTENED_JOB:
            return '{0}:{1}:{2}'.format(self.start_line, self.contractor_name, self.violation_type)
        elif self.violation_type == SUSPICIOUS_BATCH:
            return '{0}:{1}:{2}'.format(self.completion_line, self.contractor_name, self.violation_type)
        else:
            return '{0}:{1}'.format(self.start_line, self.contractor_name)

events: List[str] = sys.stdin.readlines()

invoice_count = 0
contractors: Dict[str, List[Job]] = {}

for i, event in enumerate(events):
    event = event.strip('\n')

    if 'START' in event:
        name = event.split(';')[0]

        if name not in contractors:
            contractors[name] = [Job(name, i)]
        else:
            contractors[name].append(Job(name, i))
    
    else:
        split_event = event.split(';')
        name = split_event[0]
        # Can assume that name WILL be in dictionary
        # Since no malformed input...
        jobs: List[Job] = contractors[name]

        # Convert ids to numbers instead of strings
        invoice_ids = [int(id) for id in split_event[1:]]
        
        # Vector of True/False if they are shortened jobs
        shortened_vector = [id < invoice_count for id in invoice_ids]
        violation = ''

        if any(shortened_vector):
            # Mark all jobs as SUSPICIOUS_BATCH
            violation = SUSPICIOUS_BATCH
            
            if all(shortened_vector):
                violation = SHORTENED_JOB
        
        for job in jobs:
            job.completion_line = i
            job.violation_type = violation

        # Assume previous invoice ids were correct so update counter
        invoice_count = max(invoice_ids)

# Output
for jobs in contractors.values():
    if jobs[0].violation_type == SUSPICIOUS_BATCH:
        print(jobs[0])
    elif jobs[0].violation_type == SHORTENED_JOB:
        for job in jobs:
            print(job)
        

