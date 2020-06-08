# This is file Two_parts.py

# This is an example script intended to be distributed as part of a
# software library centred on file eights.py

# Two_parts.py and eights.py were written by Dr. Daniel C. Hatton

# Material up to and including release 0.2 copyright (C) 2017
# University of Plymouth Higher Education Corporation

# Changes since release 0.2 copyright (C) 2020 Dr. Daniel C. Hatton

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation: version 3 of the
# License.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License, and the GNU General Public License
# which it incorporates, for more details.

# You should have received a copy of the GNU Lesser General Public
# License [in file ../LICENSE] along with this program.  If not, see
# <https://www.gnu.org/licenses/>.

# Daniel Hatton thanks Dr. Justin E. Rigden, Specialist Intellectual
# Property Advisor, for authorizing, on behalf of the University of
# Plymouth Higher Education Corporation, the release of this program
# under the licence terms stated above.

# Daniel Hatton can be contacted on <dan.hatton@physics.org>

import FreeCAD
import Part
import eights

pagesize = 'A3'
pageorientation = 'Landscape'
creator = 'Joe D. Draftsman'
longtitle = 'Some very important parts'
legalowner = 'Acme Design Company'
approver = 'Jane C. Manager'
doctype = 'part drawings'
docstatus = 'for review'
sheetnum = 2
totalsheets = 3
inversescale = 5
firstpartnumber = 'C2'
secondpartnumber = 'S1'
partlist = firstpartnumber+','+secondpartnumber
drawingnum = 'TRY2'
year = 2017
month = 7
day = 11
revision = 'A'

# All distances in millimetres

conelargediameter = 15.0
conesmalldiameter = 7.5
drawingviewspacing = 5.0
symbolviewspacing = drawingviewspacing/3.0
symbolxposition = 190.0
symbolyposition = 280.0

C2side = 100.0
C2posn = FreeCAD.Vector(0.0,0.0,0.0)
thefirstshape = Part.makeBox(C2side,C2side,C2side,C2posn)
S1diam = 100.0
S1posn = FreeCAD.Vector(S1diam/2.0,S1diam/2.0,S1diam/2.0)
thesecondshape = Part.makeSphere(S1diam/2.0,S1posn)
scale = 1.0/inversescale
firstdrawingxposn = 50.0
firstdrawingyposn = 40.0
seconddrawingxposn = 300.0
seconddrawingyposn = 40.0

thedocument = FreeCAD.newDocument("try_it")

pagetitle = "try_this_bit"

page_creator = eights.create_eights_drawing_sheet(thedocument, pagetitle,
                                                  pagesize, pageorientation,
                                                  creator,
                                                  longtitle,
                                                  legalowner,
                                                  approver,
                                                  doctype,
                                                  docstatus,
                                                  sheetnum, totalsheets,
                                                  inversescale, partlist,
                                                  drawingnum, year,
                                                  month, day, revision)
dummyone = page_creator.create_it('putanyoldrubbishhere')

thepage = thedocument.getObject(pagetitle)

symbol_adder = eights.add_first_angle_projection_symbol(conelargediameter,
                                                        conesmalldiameter,
                                                        symbolviewspacing,
                                                        symbolxposition,
                                                        symbolyposition,
                                                        thepage)
dummytwo = symbol_adder.put_it_in('putanyoldrubbishhere')

first_drawings_adder = eights.first_angle_projection(firstpartnumber,
                                                     thefirstshape,
                                                     drawingviewspacing,
                                                     firstdrawingxposn,
                                                     firstdrawingyposn,
                                                     scale,thepage)

dummythree = first_drawings_adder.fap('putanyoldrubbishhere')

second_drawings_adder = eights.first_angle_projection(secondpartnumber,
                                                      thesecondshape,
                                                      drawingviewspacing,
                                                      seconddrawingxposn,
                                                      seconddrawingyposn,
                                                      scale,thepage)

dummyfour = second_drawings_adder.fap('putanyoldrubbishhere')

Gui.getDocument("try_it").show("try_this_bit")
