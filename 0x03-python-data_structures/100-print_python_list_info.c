#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - prints pyhton list object info
 * @list: Python list object
 */

void print_python_list_info(PyObject *list)
{
	PyListObject *new_list = (PyListObject *)list;
	int i;
	ssize_t list_size = new_list->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", new_list->allocated);
	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: %s\n", i,
				new_list->ob_item[i]->ob_type->tp_name);
	}
}
