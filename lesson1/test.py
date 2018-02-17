new_list = {"Kate": {"city": "Moscow", "temperature": 20, "wind": "east"}, 
			"Anna": {"city": "Lipetsk", "temperature": 23, "wind": "north"}, 
			"Paul": {"city": "St. Petersburg", "temperature": 24, "wind": "west"}
			}

print(new_list)

name = input('name')
print(new_list.get(name))
