#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in ".?:":
        text = (x + "\n\n").join([line.strip(" ") for line in text.split(x)])
    print(text, end="")
