"""
A meeting is stored as a tuple ↴ of integers (start_time, end_time). 
These integers represent the number of 30-minute blocks past 9:00am.

Write a function merge_ranges() that takes a list of multiple meeting 
time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 
Your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming 
from multiple teams.

Write a solution that's efficient even when we can't put a nice upper 
bound on the numbers representing our time ranges. Here we've simplified 
our times down to the number of 30-minute slots past 9:00 am. But we 
want the function to work even for very large numbers, like Unix timestamps. 
In any case, the spirit of the challenge is to merge meetings where 
start_time and end_time don't have an upper bound.

"""

def merge_schedules(meetings):
    
    sorted_meetings = sorted(meetings)

    merged_meetings = list(sorted_meetings[0])

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]


    if (current_meeting_start <= last_merged_meeting_end):
        merged_meetings[-1] = (last_merged_meeting_start, 
                                max(last_merged_meeting_end, 
                                current_meeting_end)
                                )

    else:
        merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

"""
Complexity
O(nlg{n})O(nlgn) time and O(n)O(n) space.

Even though we only walk through our list of meetings once to merge them,
we sort all the meetings first, giving us a runtime of O(nlg{n})O(nlgn). 
It's worth noting that if our input were sorted, we could skip the sort 
nd do this in O(n)O(n) time!

We create a new list of merged meeting times. In the worst case, none of 
the meetings overlap, giving us a list identical to the input list. Thus 
we have a worst-case space cost of O(n)O(n).
"""



