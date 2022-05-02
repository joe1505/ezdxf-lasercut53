#
# Started 27Apr2022.
# This is a simple demo of the proper incantations to create
# a dxf file that can be imported by the LaserCut53 software. 
# 

import ezdxf
from ezdxf import units

# Versions  R2000, R2007, or R2010 all read ok.
dxfVersion='R2000'
#dxfVersion='R2007'
#dxfVersion='R2010'

# Lasercut groups lines by color, so different laser cutting settings
# can be applied to each color.
# Color numbers corresponding to the layer buttons at the bottom
# of the LaserCut53 GUI:
#   black:7 blue:5 red:1 green:3 magenta:0 yellow:2 cyan:4
# More exist, but that's enough for any reasonable application :-).
#             0  1  2  3  4  5  6
lc_colors = [ 7, 5, 1, 3, 0, 2, 4 ] ;

###################################
# Open the document and set units.

doc = ezdxf.new(dxfversion=dxfVersion,setup=True)
msp = doc.modelspace()

# From the documentations:
# https://ezdxf.readthedocs.io/en/stable/concepts/units.html#dxf-units
# Some versions of ezdxf define units.CM , etc. I'll just use the numbers here.
my_units = 1 # Units: 1:inches, 5:centimeters, etc.

# https://ezdxf.readthedocs.io/en/stable/howto/document.html#set-dxf-drawing-units
doc.header['$INSUNITS'] = my_units

# Optional: the next 2 lines prevent an out-of-bounds warning in lasercut5.3 .
# If I leave out these lines and ignore the warning, LaserCut reads the file just fine.
doc.header['$EXTMIN'] = (0,0,0)
doc.header['$EXTMAX'] = (47,35,0)

###################################
# Draw to msp.
# https://ezdxf.readthedocs.io/en/stable/dxfentities/index.html
# for drawing lines, arcs, etc.

xc=3
yc=2
# Vertical and horizontal lines.
msp.add_line(start=(xc,yc-1),end=(xc,yc+1),dxfattribs={'color': lc_colors[0]});
msp.add_line(start=(xc-0.5,yc),end=(xc+0.5,yc),dxfattribs={'color': lc_colors[0]});
# Ellipse.
msp.add_ellipse(center=(xc,yc),major_axis=(0,1.1),ratio=0.55,dxfattribs={'color': lc_colors[1]});
# Circle
msp.add_circle(center=(xc,yc),radius=1.2,dxfattribs={'color': lc_colors[2]});
# Arc on left side
msp.add_arc(center=(xc,yc),radius=1.3,start_angle=110,end_angle=250,dxfattribs={'color': lc_colors[3]});
# Arc on right side
msp.add_arc(center=(xc,yc),radius=1.3,start_angle=-70,end_angle=70,dxfattribs={'color': lc_colors[4]});
# lightweight polyline - triangle.
polypoints= [ (xc-1,yc+1.3), (xc+1,yc+1.3), (xc,yc+1.6), (xc-1,yc+1.3)]
msp.add_lwpolyline(polypoints,dxfattribs={'color': lc_colors[6]});

###################################
# Save the output file.

doc.saveas('dxf4laser-'+dxfVersion+'.dxf')

