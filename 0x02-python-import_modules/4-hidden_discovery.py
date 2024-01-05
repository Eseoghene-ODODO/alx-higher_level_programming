#!/usr/bin/python3

import importlib.util
import uncompyle6

if __name__ == "__main__":
    # Decompile pyc file
    with open('hidden_4_decompiled.py', 'w') as f:
        uncompyle6.decompile_file('hidden_4.pyc', f)

    # Import decompiled module
    spec = importlib.util.spec_from_file_location('hidden_4',
                                                  'hidden_4_decompiled.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Print names from module
    names = set()
    for name in dir(module):
        if not name.startswith("__"):
            names.add(name)

    for name in sorted(names):
        print(name)
