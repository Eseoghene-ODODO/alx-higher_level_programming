#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

    /*Print first 10 elements*/
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("size: %ld\n", PyBytes_GET_SIZE(p));
    printf("trying string: %s\n", PyBytes_AsString(p));

    /* Print up to 10 bytes*/
    printf("first 10 bytes: ");
    for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; ++i)
    {
        printf("%02hhx ", ((char *)PyBytes_AsString(p))[i]);
    }
    printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a PyObject representing a Python float object
 */
void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("value: %lf\n", PyFloat_AS_DOUBLE(p));
}
