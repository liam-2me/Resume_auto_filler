import pyautogui as p
from enum import Enum

"""
This file handles deciding what needs to be typed, and typing it out
usinf the pyautogui class
"""
#store the info we need as an enum, wanted to use a hash map but didnt want to 
#write out a full hash map myself
class strings(Enum):
    job_title1 = "Technology Development Program Associate"
    job_title2 = "Digital Technology Leadership Intern"
    company1 = 'Optum'
    company2 = 'Pratt and Whitney'
    tdp_asc_desc = "Rotation 1: Software Engineer (Clinical ETL) Built scalable ETL workflows using SQL, Python, and automation frameworks. Led the Optum at Home data pipeline initiative for the Rebel Spies ETL team. Partnered with business teams to gather test cases and ensure validated end to end data output. Rotation 2: Software Engineer (HCC Containers Platform), Developed Chef Cookbooks to extract configuration metadata from distributed Kubernetes clusters. Maintained Kubernetes node health and resolved deployment level issues.• Delivered reusable automation modules for infrastructure teams"
    inter_desc = "Developed enterprise training roadmaps for Agile, DevOps, and modern engineering roles. • Operated in Agile sprints to deliver high visibility transformation materials."


#simple function to differentiate what needs to typed
def chooser(n):
    if n == 1:
        line_writer(strings.job_title1.value)
    elif n == 2:
        line_writer(strings.job_title2.value)
    elif n == 3:
        line_writer(strings.company1.value)
    elif n == 4:
        line_writer(strings.company2.value)
    elif n == 5:
        line_writer(strings.tdp_asc_desc.value)
    elif n == 6:
        line_writer(strings.inter_desc.value)
    else:
        raise ValueError("Unsupported value entered")

#delete the stroke of the keybind, then type the string
def line_writer(line):
    p.press('backspace')
    p.typewrite(line)

