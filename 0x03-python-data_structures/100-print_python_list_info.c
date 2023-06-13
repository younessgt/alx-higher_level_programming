#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info -  function that prints some
 * basic info about Python lists.
 * @p: pointer to structure
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int size_py = PyList_Size(p);
	int i;
	Py_ssize_t allocate;

	allocate = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %i\n", size_py);
	printf("[*] Allocated = %ld\n", allocate);
	for (i = 0; i < size_py; i++)
		printf("Element %d: %s\n",i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
