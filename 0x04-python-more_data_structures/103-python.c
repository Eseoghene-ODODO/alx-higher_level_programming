#include "Python.h" 

/**
 * print_list_info - Prints some info about Python lists
 *
 * Return: PyObject* 
 */
static PyObject* print_list_info(PyObject* self, PyObject* args) 
{
  printf("Python lists are dynamic arrays that can contain objects of different types.\n");
  printf("Lists are defined using square brackets and elements are separated by commas.\n"); 
  printf("Ex: [1, 'hello', 3.5]\n");
  
  return Py_BuildValue("");
}

/** 
 * print_bytes_info - Prints some info about Python bytes
 * 
 * Return: PyObject*
 */
static PyObject* print_bytes_info(PyObject* self, PyObject* args)
{
  printf("Python bytes are immutable sequences of integers in the range 0-255.\n");
  printf("They are often used to represent byte-level data like images, files, etc.\n");
  printf("Bytes literals are defined using a b prefix like b'hello'\n");

  return Py_BuildValue(""); 
}

/**
 * Method definitions for the module
 */
static PyMethodDef myMethods[] = {
  {"print_list_info", print_list_info, METH_NOARGS, "Print some info about Python lists"},
  {"print_bytes_info", print_bytes_info, METH_NOARGS, "Print some info about Python bytes"}, 
  {NULL, NULL, 0, NULL}
};

/**
 * Module initialization
 */
PyMODINIT_FUNC PyInit_mymodule(void) 
{
  return PyModule_Create(&(struct PyModuleDef){
    PyModuleDef_HEAD_INIT,
    "mymodule",
    "My module with some C functions",
    -1,
    myMethods
  });
}
