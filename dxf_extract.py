import sys
import ezdxf
#from sqlalchemy import create_engine , text
import sys
import psycopg2
from  shapely.geometry import Polygon

database_name = "planmasse"
database_user = "postgres"
database_password = "password"
database_host = "192.168.1.26"
database_port = "30432"

conn = psycopg2.connect(
    database=database_name,
    user=database_user,
    password=database_password,
    host=database_host,
    port=database_port
)

cursor = conn.cursor()

try:
    doc = ezdxf.readfile("plan-masse1.dxf")
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

msp = doc.modelspace()
#text_list = msp.query('TEXT[layer=="z value TN"]')
#for text in text_list:
#    x = str(text.dxf.insert.x)
#    y = str(text.dxf.insert.y)
#    z = str(text.dxf.text)
#    cursor.execute("INSERT INTO point (x, y, z) VALUES (%s, %s, %s);", (x, y, z))
#conn.commit()
#conn.close()

polyline = msp.query('LWPOLYLINE[layer=="surface"]').first
with polyline.points("xy") as points:
    print(points)
polygon = Polygon(points)
area = polygon.area

print (f" l'aire est de : {area}")


#print(polyline.last.lwpoints.values)
#print
#lines:
#    #print(f"{line}")
#    print(f"{line.dxf.start.xyz[0]},{line.dxf.start.xyz[1]}")
#    print(f"{line.dxf.end.xyz[0]},{line.dxf.end.xyz[1]}")