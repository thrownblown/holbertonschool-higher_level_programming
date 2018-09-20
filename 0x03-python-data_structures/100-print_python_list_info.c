#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - C func that prints basic info about Python lists
 * @p: ptr python object
 * Return: nope void
 */

void print_python_list_info(PyObject *p)
{
	size_t len, i = 0;
	const char *pytype = NULL;

	len = PyList_Size(p);
	i = 0;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while (i < len)
	{
		pytype = Py_TYPE(PyList_GetItem(p, i))->tp_name;
		printf("Element %ld: %s\n", i++, pytype);
	}
}
