#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
	with open(filename, "r+", encoding="utf-8") as file_pos:
		lines = [line for line in file_pos]
		for idx, line in enumerate(lines):
			if search_string in line:
				lines.insert(idx+1, new_string)
		file_pos.writelines(lines)
