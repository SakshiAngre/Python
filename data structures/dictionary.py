"""Dictionaries store key-value pairs."""

maths={"sakshi":59,"harry":45,"lily":49}

print(maths,type(maths))

#Accessing & Modifying Values
print(maths["sakshi"])
maths["harry"]=60
print(maths)

maths["subject"]="marks"
print(maths)

#dictionary marks
print(maths.keys())
print(maths.values())
print(maths.items())
maths.pop("harry") 
maths.clear()

#Dictionary Comprehensions
table_5= {i: 5*i      for i in range(1,11)}
print(table_5)

#when to use each data structure
"""Data Structure	Features	          Best For
   List	           Ordered, Mutable	      Storing sequences, dynamic data
   Tuple	       Ordered, Immutable	  Fixed collections, dictionary keys
   Set	          Unordered,Unique(data)  Removing duplicates, set operations
   Dictionary	   Key-Value Pairs	      Fast lookups, structured data"""