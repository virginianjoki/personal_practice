# madlibs

#asking for inputs
noun = input("enter a noun: ")
verb = input("enter a verb: ")
adjective = input("enter an adjective: ")
insect = input("enter an insect: ")
place = input("enter a place: ")

#story template with conditions
if adjective.lower() == "pretty":
    story = f"once upon a time there was a {adjective} {noun} who loved {verb}."
else:
    story = f"In the distant land of {place}, there was a {adjective} {noun} who loved to {verb}."

#adding anothe codition based on insect
if insect.lower() == "butterfly":
    story += f" one day she saw a {insect} in the {place}."  
else:
    story += f" One day, they encountered a wild {insect} that tried to stop their quest."    

#displaying the story
print("\n--- Your Mad Libs Story ---")    
print(story)