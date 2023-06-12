#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - for printing information about python
 * @c: it's a pointer to python object
 * Return: null
 */
void print_python_list_info(PyObject *c)
{
	Py_ssize_t size;
	int i;
	PyListObject *list = (PyListObject *)c;

	size = PyList_Size(c);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
