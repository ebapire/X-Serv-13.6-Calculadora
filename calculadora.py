#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) == 4:
    if sys.argv[1] in ["suma", "sum"]:
        print (float(sys.argv[2]) + float(sys.argv[3]))
    elif sys.argv[1] in  ["resta", "rest"]:
        print (float(sys.argv[2]) - float(sys.argv[3]))
    elif sys.argv[1] in ["mult", "*"]:
        print (float(sys.argv[2]) * float(sys.argv[3]))
    elif sys.argv[1] in ["div", "dividir"]:
        print (float(sys.argv[2]) / float(sys.argv[3]))
    else:
        print "Operación invalida"
else:
    print "numero de argumentos incorrecto"
