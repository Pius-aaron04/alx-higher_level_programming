#include "Python.h"
#include <stdio.h>
#include <string.h>


/**
 * print_python_list - Prints info about a python list object
 * @p: pyhton list object (initially a PyObject type)
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int i;
	ssize_t list_size = list->ob_base.ob_size;

	puts("[*] Python list info");
	printf("[*] Size of Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated: %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}


/**
 * print_python_bytes - prints info about a python object
 * @p: pointer to python byte object
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	char *data = bytes->ob_sval;
	int i;
	ssize_t bytes_size = strlen(data);

	puts("[.] bytes object info");
	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", data);

	if (bytes_size > 10)
		bytes_size = 10;
	printf("  first %ld bytes: ", bytes_size);

	for (i = 0; i < bytes_size; i++)
	{
		if (i == bytes_size - 1)
			printf("%x\n", data[i]);
		else
			printf("%x ", data[i]);
	}
}
