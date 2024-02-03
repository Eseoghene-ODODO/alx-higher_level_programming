#include <Python.h>

/**
 * print_python_string - Print Python string if valid
 * @p: PyObject pointer to a Python object
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        const char *str = PyUnicode_AsUTF8(p);
        
        if (str)
	{
            printf("Python String: %s\n", str);
        }
	else
	{
            PyErr_Print();
        }
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Invalid Python string");
        PyErr_Print();
    }
}
