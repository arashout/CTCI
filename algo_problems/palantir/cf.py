from typing import List, Dict
import sys
import bisect

# Constants to avoid mis-spellings
SUSPICIOUS_BATCH = 'SUSPICIOUS_BATCH'
SHORTENED_JOB = 'SHORTENED_JOB'

class Job:
    def __init__(self, name, start_line, highest_invoice):
        self.name = name
        self.start_line = start_line
        # The invoice count at the time of the job start
        self.highest_invoice = highest_invoice
        
        # Set these on job completion
        self.type = ''
        self.completion_line = 0
    
    def __repr__(self):
        if self.type == SHORTENED_JOB:
            return '{0},{1},{2}'.format(self.start_line, self.name, self.type)
        elif self.type == SUSPICIOUS_BATCH:
            return '{0},{1},{2}'.format(self.completion_line, self.name, self.type)
        else:
            return '{0},{1},{2}'.format(self.start_line, self.name, self.completion_line)

    def __str__(self):
        if self.type == SHORTENED_JOB:
            return '{0};{1};{2}'.format(self.start_line, self.name, self.type)
        elif self.type == SUSPICIOUS_BATCH:
            return '{0};{1};{2}'.format(self.completion_line, self.name, self.type)
        else:
            return '{0},{1}'.format(self.start_line, self.name)
    
    def __lt__(self, other):
        return self.completion_line < other.completion_line

def findViolations(datafeed):
    events = datafeed
    
    invoice_count = 0 # Keep track of highest invoice
    contractors = {}
    sorted_jobs = []

    for i, event in enumerate(events):
        i = i + 1 # 1-Indexed

        event = event.strip('\n')
        event_splits = event.split(';')
        name = event_splits[0]

        if 'START' == event_splits[1]:
            if name not in contractors:
                contractors[name] = [Job(name, i, invoice_count)]
            else:
                contractors[name].append(Job(name, i, invoice_count))
        # Otherwise job completion events
        else:
            current_jobs =  [job for job in contractors[name] if job.completion_line == 0]

            # Convert ids to ints
            invoices = [int(invoice_str) for invoice_str in event_splits[1:]]

            # Create vector of True/False for if jobs are shortened jobs
            # Assume they index in order that jobs were started
            shortened_vector = [current_jobs[i].highest_invoice > invoice for i, invoice in enumerate(invoices)]
            print(current_jobs)
            violation = ''
            if any(shortened_vector):
                violation = SUSPICIOUS_BATCH
                
                if all(shortened_vector):
                    violation = SHORTENED_JOB
            
            for job in current_jobs:
                job.completion_line = i
                job.type = violation

                # Add to sorted container 
                bisect.insort(sorted_jobs, job)

            # Assume all previous ids are valid but exclude the same name
            print(sorted_jobs)
            invoice_count = max(invoices)
    
    # Output
    output = []
    for jobs in contractors.values():
        for job in jobs:
            if job.type == SUSPICIOUS_BATCH:
                output.append(str(job))
            elif job.type == SHORTENED_JOB:
                output.append(str(job))
        
    return output
        

lines = sys.stdin.readlines()
print(findViolations(lines[1:]))