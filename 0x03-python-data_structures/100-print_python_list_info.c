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

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE((PyList_GetItem(p, i))->tp_name);
}
