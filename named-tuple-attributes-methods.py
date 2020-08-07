# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:53:57 2019

@author: luan9
"""

from collections import namedtuple

City = namedtuple('City','name country population coordinates')

City._fields #retorna uma tupla cujos campos são os atributos da classe

Latlong = namedtuple('Latlong','lat long')

delhi_data = ('Delhi NCR','IN', 21.935, Latlong(28.6138, 77.2088))

delhi = City._make(delhi_data) #permite criar uma named tuple de um iteravel
delhi._asdict() #returna um collections.OrderedDict de uma instância named tuple

for key, value in delhi._asdict().items():
    print(key + ':', value) 