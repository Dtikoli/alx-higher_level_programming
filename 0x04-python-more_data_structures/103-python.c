#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, idx, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);

	for (idx = 0; idx < lim; idx++)
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 256 + str[idx]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int size, idx;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < size; idx++)
	{
		obj = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
