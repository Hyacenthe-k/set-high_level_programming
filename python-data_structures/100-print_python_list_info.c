#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A generic PyObject pointer representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
    long int size, allocated, i;
    PyObject *item;

    size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    }
}
