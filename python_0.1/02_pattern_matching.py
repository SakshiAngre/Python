import re

text="The quick brown fox jumps over the lazy dog;and the brown"

"""match= re.search("brown",text)
if match:
    print("match found!")
    print("start index",match.start())
    print("end index",match.end())"""

"""#find all occurances
matches = re.findall("brown", text, re.IGNORECASE)  # Case-insensitive search
print("Matches:", matches)"""

"""#replece all occurances
new_text=re.sub("fox","cat",text)
print("Newtext:",new_text)
"""
#Compile a regex for efficiency
matches = re.findall("the", text, re.IGNORECASE)
print("Matches:", matches)