import os
import time
import json
import xml.etree.ElementTree as et
import xml.dom.minidom as minidom

INPUT_PATH = "./Variflight_SC8404_20230211.json"
OUTPUT_PATH = "./SC8404_20230211.kml"

kml_root = et.Element("kml",
                      {"xmlns": "http://www.opengis.net/kml/2.2",
                       "xmlns:gx": "http://www.google.com/kml/ext/2.2"})

kml_document = et.SubElement(kml_root, "Document")
et.SubElement(kml_document, "name").text = os.path.basename(INPUT_PATH)

track_placemark = et.SubElement(kml_document, "Placemark")
et.SubElement(track_placemark, "name").text = "Aircraft"
gx_track = et.SubElement(track_placemark, "gx:Track")
et.SubElement(gx_track, "extrude").text = "1"
et.SubElement(gx_track, "tessellate").text = "1"
et.SubElement(gx_track, "altitudeMode").text = "absolute"

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    records = json.load(f)
    for record in records:
        et.SubElement(gx_track, "when").text = \
            time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record["updatetime"]))

        et.SubElement(gx_track, "gx:coord").text = \
            f"{record['longitude']} {record['latitude']} {record['height']}"

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(
        minidom.parseString(
            et.tostring(
                kml_root,
                encoding="utf-8",
                short_empty_elements=True,
                xml_declaration=True
            ))
        .toprettyxml(indent="    "))
