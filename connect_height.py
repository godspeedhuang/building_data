import json

import glob
import pathlib

import xml.etree.cElementTree as ET
from lxml import etree

import re
# tree = ET.ElementTree(
# file="C:\D\Study\大四上\實習\圖資\建物\D202109170001\kmz\kml\94182051-11.kml")

building_data = {
    'NAME': '',
    'BUILD_ID': '',
    'BUILDNAME': '',
    'BUILDTYPE': '',
    'M_SOURCE': '',
    'SOURCE': '',
    'SOURCE_DES': '',
    'MDATE': '',
    'BUILD_H': '',
    'H_SOURCE': '',
    'H_EXTRAC': '',
    'BUILD_NO': '',
    'NO_SOURCE': '',
    'M_MDATE': '',
    'MODEL_LOD': '',
    'COUNTY': '',
    'MODEL_NAME': '',
    'CENT_E_97': '',
    'CENT_N_97': '',
    'C_FRAMEID': ''
}

row_data = {
    "type": "FeatureCollection",
    "name": "building_1017update2",
    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
    "features": []
}

# 找出所有kml檔案
file_dir = r"C:\D\Study\大四上\實習\圖資\建物"
file_ext = r"**\*.kml"

with open("building_1017.geojson", mode='r', encoding='utf-8') as file:
    data = json.load(file)

f = list(pathlib.Path(file_dir).glob(file_ext))

f_list = []
for files in f:
    f_list.append(str(files))
count = 0
for files in f_list:
    # print(files)
    # r=files.find(file_name)
    # if r != -1:
    # print(files)
    tree = etree.parse(files)
    key_data_NAME = tree.xpath('//kml:Placemark/kml:name/text()',
                               namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILD_ID = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILD_ID"]/text()',
                                   namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILDNAME = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILDNAME"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILDTYPE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILDTYPE"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILD_STR = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILD_STR"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_M_SOURCE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="M_SOURCE"]/text()',
                                   namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_SOURCE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="SOURCE"]/text()',
                                 namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_SOURCE_DES = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="SOURCE_DES"]/text()',
                                     namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_MDATE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="MDATE"]/text()',
                                namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILD_H = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILD_H"]/text()',
                                  namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_H_SOURCE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="H_SOURCE"]/text()',
                                   namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_H_EXTRAC = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="H_EXTRAC"]/text()',
                                   namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_BUILD_NO = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="BUILD_NO"]/text()',
                                   namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_NO_SOURCE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="NO_SOURCE"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_M_MDATE = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="M_MDATE"]/text()',
                                  namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_MODEL_LOD = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="MODEL_LOD"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_COUNTY = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="COUNTY"]/text()',
                                 namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_MODEL_NAME = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="MODEL_NAME"]/text()',
                                     namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_CENT_E_97 = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="CENT_E_97"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_CENT_N_97 = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="CENT_N_97"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    key_data_C_FRAMEID = tree.xpath('//kml:Placemark/kml:ExtendedData/kml:SchemaData/kml:SimpleData[@name="C_FRAMEID"]/text()',
                                    namespaces={"kml": "http://www.opengis.net/kml/2.2"})
    select_d = []
    frame = key_data_C_FRAMEID[0]
    print(frame)
    for d in data['features']:
        file_name = d['properties']['layer'][:-2]
        if frame in file_name:
            select_d.append(d)
    for i in range(0, len(key_data_NAME)):
        building_data['NAME'] = key_data_NAME[i]
        for dd in select_d:
            building_name = dd['properties']['Name']
            if building_name == building_data['NAME']:
                dd['properties']['BUILD_ID'] = key_data_BUILD_ID[i]
                dd['properties']['BUILDNAME'] = key_data_BUILDNAME[i]
                dd['properties']['BUILDTYPE'] = key_data_BUILDTYPE[i]
                dd['properties']['M_SOURCE'] = key_data_M_SOURCE[i]
                dd['properties']['SOURCE'] = key_data_SOURCE[i]
                dd['properties']['SOURCE_DES'] = key_data_SOURCE_DES[i]
                dd['properties']['MDATE'] = key_data_MDATE[i]
                dd['properties']['BUILD_H'] = key_data_BUILD_H[i]
                dd['properties']['H_SOURCE'] = key_data_H_SOURCE[i]
                dd['properties']['H_EXTRAC'] = key_data_H_EXTRAC[i]
                dd['properties']['BUILD_NO'] = key_data_BUILD_NO[i]
                dd['properties']['NO_SOURCE'] = key_data_NO_SOURCE[i]
                dd['properties']['M_MDATE'] = key_data_M_MDATE[i]
                dd['properties']['MODEL_LOD'] = key_data_MODEL_LOD[i]
                dd['properties']['COUNTY'] = key_data_COUNTY[i]
                dd['properties']['MODEL_NAME'] = key_data_MODEL_NAME[i]
                dd['properties']['CENT_E_97'] = key_data_CENT_E_97[i]
                dd['properties']['CENT_N_97'] = key_data_CENT_N_97[i]
                dd['properties']['C_FRAMEID'] = key_data_C_FRAMEID[i]
                row_data['features'].append(dd)
                count += 1
                print('success '+str(count))
        # print('success '+building_data['NAME'])
    print("="*30)
    print(files)
    print("="*30)


with open("building_1017update_new.geojson", mode='w', encoding='utf-8') as file:
    json.dump(row_data, file, ensure_ascii=False)
