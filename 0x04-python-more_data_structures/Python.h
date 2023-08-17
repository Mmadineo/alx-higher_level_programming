#ifndef Py_PYTHON_H
#define Py_PYTHON_H

// Since this is a "meta-include" file, no #ifdef __cplusplus / extern "C" {

// Include Python header files
#include "patchlevel.h"
#include "pyconfig.h"
#include "pymacconfig.h"

#if defined(__sgi) && !defined(_SGI_MP_SOURCE)
#  define _SGI_MP_SOURCE
#endif
