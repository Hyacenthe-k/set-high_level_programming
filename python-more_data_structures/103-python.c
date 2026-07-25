#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		size = 10;
	else
		size++;

	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02hhx", string[i]);
	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	size = ((PyVarObject *)p)->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
