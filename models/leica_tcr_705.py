#! /usr/bin/env python
# -*- coding: utf-8 -*-
# filename: leica_tcr_705.py
# Copyright 2009 Luca Bianconi <luxetluc@yahoo.it>
# Copyright 2009 Stefano Costa <steko@iosa.it>
# Under the GNU GPL 3 License

from generic import *


class ModelConnector(Connector):
    def __init__(self, port):
        Connector.__init__(self, port=port, baudrate=19200)


class ModelParser(Parser):
    
    def is_point(self,line):
        
        tokens = line.split(",")
        is_point = True
	
        try:

            float(tokens[1])
            float(tokens[2])
            float(tokens[3])
	    
	    
        except (ValueError, IndexError):
            is_point = False
	    
        #else:
            #di questo controllo che segue FORSE non gliene frega un beliscimu
            #if tokens[4]=="MEAS":
            #    is_point = True
            #else:
            #    is_point = False
        
        return is_point
        
    def get_point(self,line):
        
        tokens = line.split(",")
        
        if len(tokens)> 4:
            text = str(tokens[4])
        else:
            text = ""
        
        p = Point(str(tokens[0]), float(tokens[1]), float(tokens[2]), float(tokens[3]), text)
	
        return p

