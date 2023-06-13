#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - function that prints some basic
 * info about Python lists.
 * @p: pointer to structure.
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int si;

	si = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", si);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < si; i++)
	{
		printf("Element %d: %s\n",
				i, Py_TYPE((PyList_GetItem(p, i))->tp_name);
	}
}
