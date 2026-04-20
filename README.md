# Resume_auto_filler
Liam's Resume Autotyper

This is a small set of python scripts to type in information from my resume, using a keybind as opposed to having to manually type the info. When applying to jobs, the format of my Resume sometimes clashes with the autofill feature that many websites use. I created this to remediate that problem.

I currently have created 6 keybinds that are as follows:

k.add_hotkey('z', chooser, args= ([1]))

    -This bind types out a job title

k.add_hotkey('x', chooser, args= ([2]))

    -This bind types out another job title

k.add_hotkey('a', chooser, args= ([3]))

    -This bind types the company name related to the first keybind

k.add_hotkey('s', chooser, args= ([4]))

    -This bind types out the company name related to the second keybind

k.add_hotkey('d', chooser, args= ([5]))

    -This types out the job description related to the second/fourth bind

k.add_hotkey('c', chooser, args= ([6]))

    -This types out the job description related to the first/third bind


This is not a repo for Professional use/purposes. It contains code that I created to quickly solve a common issue that I face while applying to jobs.
