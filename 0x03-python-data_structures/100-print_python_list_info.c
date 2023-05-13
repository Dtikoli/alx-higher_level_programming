#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n",
		       i,
		       (PY_TYPE(PyList_GetItem(p, i)))->tp_name);
	}
}
