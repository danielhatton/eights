# This is file Single_part.py

# This is an example script intended to be distributed as part of a
# software library centred on file eights.py

# Single_part.py and eights.py were written by Dr. Daniel C. Hatton

# Copyright (C) 2017 University of Plymouth Higher Education
# Corporation

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
# License [in file ../COPYING.txt], and the GNU General Public License
# which it incorporates [in file ../COPYING_ANNEX.txt], along with
# this program.  If not, see <https://www.gnu.org/licenses/>.

# Daniel Hatton thanks Dr. Justin E. Rigden, Specialist Intellectual
# Property Advisor, for authorizing, on behalf of the University of
# Plymouth Higher Education Corporation, the release of this program
# under the licence terms stated above.

# Daniel Hatton can be contacted on <daniel.hatton@plymouth.ac.uk>
# or at
# Autonomous Marine Systems Group,
# School of Engineering,
# University of Plymouth,
# Plymouth,
# UK.
# PL4 8AA

import FreeCAD
import Part
import eights

pagesize = 'A3'
pageorientation = 'Landscape'
creator = 'Joe D. Draftsman'
longtitle = 'A very important part'
legalowner = 'Acme Design Company'
approver = 'Jane C. Manager'
doctype = 'part drawing'
docstatus = 'for review'
sheetnum = 1
totalsheets = 3
inversescale = 2
partnumber = 'C1'
partlist = partnumber
drawingnum = 'TRY1'
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

C1side = 100.0
C1posn = FreeCAD.Vector(0.0,0.0,0.0)
theshape = Part.makeBox(C1side,C1side,C1side,C1posn)
scale = 1.0/inversescale
drawingxposn = 100.0
drawingyposn = 40.0

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

drawings_adder = eights.first_angle_projection(partnumber, theshape,
                                               drawingviewspacing,
                                               drawingxposn,
                                               drawingyposn,
                                               scale,thepage)

dummythree = drawings_adder.fap('putanyoldrubbishhere')

Gui.getDocument("try_it").show("try_this_bit")