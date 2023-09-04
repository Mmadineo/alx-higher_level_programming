#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	Py_UNICODE* wide_chars;
	Py_ssize_t length;

	fflush(stdout);

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	length = PyUnicode_GET_LENGTH(p);
	wide_chars = PyUnicode_AsUnicode(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %zd\n", length);
	printf("  value: %ls\n", wide_chars);
}

int main()
{
	Py_Initialize();
	PyObject* str_obj = PyUnicode_DecodeUTF8("Hello, world!", 13, "strict");
	print_python_string(str_obj);
	Py_DECREF(str_obj);
	Py_Finalize();

	return (0);
}
