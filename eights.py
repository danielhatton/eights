# This is file eights.py

# This is a Python module intended for use with the open-source 3D
# computer-aided design package FreeCAD.  This module automates the
# construction of a sheet of 2D axonometric drawings in first angle
# projection, in a style consistent (to the best of the module
# author's ability) with the BS 8888:2011 standard.

# eights.py was written by Dr. Daniel C. Hatton

# Material up to and including release 0.2 copyright (C) 2015-2018
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
# License [in file LICENSE] along with this program.  If not, see
# <https://www.gnu.org/licenses/>.

# Daniel Hatton thanks Dr. Justin E. Rigden, Specialist Intellectual
# Property Advisor, for authorizing, on behalf of the University of
# Plymouth Higher Education Corporation, the release of this program
# under the licence terms stated above.

# Daniel Hatton can be contacted on <dan.hatton@physics.org>

import sys
import FreeCAD
import Part

# As of FreeCAD version 0.16, the Drawing toolbox has been deprecated,
# and replaced by a toolbox called TechDraw.  However, it's not until
# FreeCAD version 0.19 that TechDraw::DrawPage objects have an
# assignable ViewObject.ShowFrames property, which is essential for BS
# 8888:2011 compliance.  Anywhere this script tests whether the
# FreeCAD version number is less than 0.19, it's in order to decide
# whether to use the Drawing toolbox or the TechDraw toolbox.

versionnumber = float(FreeCAD.Version()[0])\
        +0.01*float(FreeCAD.Version()[1])
if(versionnumber < 0.19):
        import Drawing
else:
        import TechDraw

class create_eights_drawing_sheet:

        # The purpose of this class is to provide the method
        # "create_it", which adds, to an existing FreeCAD document, a
        # TechDraw::DrawPage or Drawing::FeaturePage object ("the
        # sheet") whose formatting is intended to be consistent with
        # the BS 8888:2011 standard for a drawing sheet, and populates
        # the title block of the sheet, again in a way intended to be
        # consistent with BS 8888:2011.

        def __init__(self, document_in, shorttitle_in, pagesize_in,
                     orientation_in, creator_in, longtitle_in, legalowner_in,
                     approver_in, doctype_in, docstatus_in, sheetnum_in,
                     totalsheets_in, inverse_scale_in, partlist_in,
                     drawingnum_in, year_in, month_in, day_in, revision_in):
               self.document = document_in
               self.shorttitle = shorttitle_in
               self.pagesize = pagesize_in
               self.orientation = orientation_in
               self.creator = creator_in
               self.longtitle = longtitle_in
               self.legalowner = legalowner_in
               self.approver = approver_in
               self.doctype = doctype_in
               self.docstatus = docstatus_in
               self.sheetnum = sheetnum_in
               self.totalsheets = totalsheets_in
               self.inverse_scale = inverse_scale_in
               self.partlist = partlist_in
               self.drawingnum = drawingnum_in
               self.year = year_in
               self.month = month_in
               self.day = day_in
               self.revision = revision_in 

        def create_it(self,dummy):
                versionnumber = float(FreeCAD.Version()[0])\
                        +0.01*float(FreeCAD.Version()[1])
                if (versionnumber < 0.19):
                        thesheet =\
                                self.document.addObject("Drawing::FeaturePage",
                                                        self.shorttitle)
                        # BS 8888:2011 inherits most of its style
                        # requirements for drawing sheets from
                        # ISO7200, so FreeCAD's built-in ISO7200
                        # templates are a good starting point.
                        thesheet.Template = FreeCAD.getResourceDir()\
                                +"Mod/Drawing/Templates/"+self.pagesize\
                                +"_"+self.orientation+"_ISO7200.svg"
                else:
                        thesheet =\
                                self.document.addObject("TechDraw::DrawPage",
                                                        self.shorttitle)
                        thetemplate =\
                                self.document.addObject\
                                ("TechDraw::DrawSVGTemplate","Standard")
                        # BS 8888:2011 inherits most of its style
                        # requirements for drawing sheets from
                        # ISO7200, so FreeCAD's built-in ISO7200
                        # templates are a good starting point.  The
                        # "TD" version of the TechDraw template has a
                        # title block that better matches the examples
                        # in BS 8888:2011 than the "Pep" version.
                        thetemplate.Template = FreeCAD.getResourceDir()\
                                +"Mod/TechDraw/Templates/"+self.pagesize\
                                +"_"+self.orientation+"_ISO7200TD.svg"
                        thesheet.Template = self.document.Standard
                        # TechDraw's view frames are incompatible with
                        # BS 8888:2011
                        thesheet.ViewObject.ShowFrames = False
                
                # However, there are several fields listed in BS
                # 8888:2011 as "mandatory" for inclusion in a title
                # block, which are not present by default in the
                # FreeCAD ISO7200 title block template.  This method
                # includes them using three of the the six
                # "supplementary information" fields in the FreeCAD
                # template.

                # Unfortunately, the mapping of actual title block
                # fields to array element numbers in the
                # "EditableTexts" property of a Drawing::FeaturePage
                # object is different between different versions of
                # FreeCAD, so it's necessary to do things differently
                # depending on the FreeCAD version number here.  In
                # addition, the TechDraw::DrawPage class doesn't
                # directly have an "EditableTexts" property, it only
                # has it as a sub-property of the "Templates"
                # property, and treats it as a hash, not a
                # straightforward list.  Not only that, the Python
                # "unicode" function has been renamed to "str" as of
                # Python 3, so it's necessary to detect the (major
                # part of the) Python version number as well.

                pythonversionnumber = float(sys.version_info.major)

                if (pythonversionnumber > 2.5):
                        def unicode(firstarg,secondarg):
                                return str(firstarg)
                
                if (versionnumber < 0.155):
                        thesheet.EditableTexts\
                                = [unicode(self.creator, 'utf-8'),
                                   unicode(self.longtitle, 'utf-8'),
                                   unicode('Legal owner: '+self.legalowner,
                                           'utf-8'),
                                   unicode('To be approved by: '+self.approver,
                                           'utf-8'),
                                   unicode('Document type: '+self.doctype,
                                           'utf-8'),
                                   unicode('Document status: '
                                           +self.docstatus, 'utf-8'),
                                   unicode(self.pagesize, 'utf-8'),
                                   unicode('%d' % (self.sheetnum)+' / '
                                           +'%d' % (self.totalsheets),
                                           'utf-8'),
                                   unicode('1 : '+'%d' % (self.inverse_scale),
                                           'utf-8'),
                                   unicode(self.partlist, 'utf-8'),
                                   unicode(self.drawingnum, 'utf-8'),
                                   unicode('%04d' % (self.year)+'-'
                                           +'%02d' % (self.month)
                                           +'-'+'%02d' % (self.day), 'utf-8'),
                                   unicode(self.revision, 'utf-8'),]
                elif(versionnumber < 0.19):
                        thesheet.EditableTexts\
                                = [unicode(self.creator, 'utf-8'),
                                   unicode(self.longtitle, 'utf-8'),
                                   unicode('Legal owner: '+self.legalowner,
                                           'utf-8'),
                                   unicode('To be approved by: '+self.approver,
                                           'utf-8'),
                                   unicode('Document type: '+self.doctype,
                                           'utf-8'),
                                   unicode('Document status: '
                                           +self.docstatus, 'utf-8'),
                                   unicode(' ', 'utf-8'),
                                   unicode(' ', 'utf-8'),
                                   unicode(self.pagesize, 'utf-8'),
                                   unicode('%d' % (self.sheetnum)+' / '
                                           +'%d' % (self.totalsheets),
                                           'utf-8'),
                                   unicode('1 : '+'%d' % (self.inverse_scale),
                                           'utf-8'),
                                   unicode(self.partlist, 'utf-8'),
                                   unicode(self.drawingnum, 'utf-8'),
                                   unicode('%04d' % (self.year)+'-'
                                           +'%02d' % (self.month)
                                           +'-'+'%02d' % (self.day), 'utf-8'),
                                   unicode(self.revision, 'utf-8'),]
                else:
                        texts = thesheet.Template.EditableTexts
                        texts["AUTHOR_NAME"]\
                                = unicode(self.creator, 'utf-8')
                        texts["DRAWING_TITLE"]\
                                = unicode(self.longtitle, 'utf-8')
                        texts["SI-1"]\
                                = unicode('Legal owner: '+self.legalowner,
                                          'utf-8')
                        texts["SI-2"]\
                                = unicode('To be approved by: '+self.approver,
                                          'utf-8')
                        texts["FreeCAD_DRAWING"]\
                                = unicode('Document type: '+self.doctype,
                                          'utf-8')
                        texts["SI-4"]\
                                = unicode('Document status: '
                                          +self.docstatus, 'utf-8')
                        texts["FC-SI"]\
                                = unicode(self.pagesize, 'utf-8')
                        texts["FC-SH"]\
                                = unicode('%d' % (self.sheetnum)+' / '
                                          +'%d' % (self.totalsheets),
                                          'utf-8')
                        texts["FC-SC"]\
                                = unicode('1 : '+'%d' % (self.inverse_scale),
                                          'utf-8')
                        texts["PN"]\
                                = unicode(self.partlist, 'utf-8')
                        texts["DN"]\
                                = unicode(self.drawingnum, 'utf-8')
                        texts["FC-DATE"]\
                                = unicode('%04d' % (self.year)+'-'
                                          +'%02d' % (self.month)
                                          +'-'+'%02d' % (self.day), 'utf-8')
                        texts["FC-REV"]\
                                = unicode(self.revision, 'utf-8')
                        thesheet.Template.EditableTexts =  texts
                self.document.recompute()

class add_first_angle_projection_symbol:

        # The purpose of this class is to provide the method
        # "put_it_in", which adds the standard BS 8888:2011 symbol,
        # indicating that a set of drawings are in first angle
        # projection ("the symbol"), to an existing TechDraw::DrawPage
        # or Drawing::FeaturePage object ("the sheet").  The method
        # put_it_in also creates a new FreeCAD Document ("the dummy
        # document"), containing various objects that are created as
        # intermediate steps on the way to adding the symbol to the
        # sheet, but which do not need to exist in the same document
        # as the sheet.  The method put_it_in also modifies the parent
        # document of the sheet, by adding to it two
        # TechDraw::DrawViewPart or Drawing::FeatureViewPart objects,
        # which are intermediate steps on the way to adding the symbol
        # to the sheet, and which have to exist _in the same document
        # as the sheet_ in order to add the symbol to the sheet.

        def __init__(self, H_in, h_in, d_in, xpos_in, ypos_in,
                     drawing_page_in):
                self.H = H_in
                self.h = h_in
                self.d = d_in
                self.xpos = xpos_in
                self.ypos = ypos_in
                self.drawing_page = drawing_page_in

        def put_it_in(self,dummy):
                title = "first_angle_projection_symbol"
                thick = 0.7 # The wider of the two line widths suggested in\
                             # BS 8888:2011
                thin = 0.35 # The narrower of the two line widths suggested\
                            # in BS 8888:2011

                # BS 8888:2011 does not specify the exact dimensions
                # of the truncated cone, axonometric projections of
                # which form the symbol, so those dimensions are taken
                # from user input.

                base_radius = 0.5*self.h
                top_radius = 0.5*self.H
                spacing = 3.0*self.d
                depth = self.H
                height = self.H
                width = self.H
                top_centre = FreeCAD.Vector(top_radius,0.0,top_radius)
                depth_wise_direction = FreeCAD.Vector(0.0,1.0,0.0)
                part = Part.makeCone(base_radius,top_radius,self.H,
                                     top_centre,depth_wise_direction)
                dummydoc = FreeCAD.newDocument("Dummy")
                part_in_tree = dummydoc.addObject("Part::Feature", title)
                part_in_tree.Shape = part
                featurepart = dummydoc.getObject(title)
                versionnumber = float(FreeCAD.Version()[0])\
                        +0.01*float(FreeCAD.Version()[1])
                if(versionnumber < 0.19):
                        plusxview\
                                = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                       title
                                                                       +" from positive x")
                else:
                        plusxview\
                                = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                       title
                                                                       +" from positive x")
                plusxview.Source = featurepart
                plusxview.Direction = FreeCAD.Vector(1.0,0.0,0.0)

                # BS 8888:2011 does not specify the exact position of
                # the symbol on the sheet, so that position is taken
                # from user input.

                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        plusxview.X = self.xpos
                        plusxview.Y = self.ypos
                else:
                        plusxview.ScaleType = u"Custom"
                plusxview.Scale = 1.0
                if(versionnumber < 0.19):
                        plusxview.Rotation = 270.0
                        plusxview.ShowHiddenLines = False
                        plusxview.LineWidth = thick
                        plusxview.HiddenWidth = thin
                        self.drawing_page.addObject(plusxview)
                        minusyview\
                                = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                       title
                                                                       +" from negative y")
                else:
                        plusxview.Rotation = 0.0
                        plusxview.HardHidden = False
                        plusxview.ViewObject.LineWidth = thick
                        plusxview.ViewObject.HiddenWidth = thin
                        plusxview.Label = ""
                        self.drawing_page.addView(plusxview)
                        plusxview.X = self.xpos+0.5*depth
                        plusxview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos
                        minusyview\
                                = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                       title
                                                                       +" from negative y")
                        
                minusyview.Source = featurepart
                minusyview.Direction = FreeCAD.Vector(0.0,-1.0,0.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        minusyview.X = self.xpos+depth+spacing
                        minusyview.Y = self.ypos
                else:
                        minusyview.ScaleType = u"Custom"
                minusyview.Scale = 1.0
                if(versionnumber < 0.19):
                        minusyview.Rotation = 90.0
                        minusyview.ShowHiddenLines = False
                        minusyview.LineWidth = thick
                        minusyview.HiddenWidth = thin
                        self.drawing_page.addObject(minusyview)
                else:
                        minusyview.HardHidden = False
                        minusyview.ViewObject.LineWidth = thick
                        minusyview.ViewObject.HiddenWidth = thin
                        minusyview.Label = ""
                        self.drawing_page.addView(minusyview)
                        minusyview.X = self.xpos+depth+0.5*width+spacing
                        minusyview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos
                                
                self.drawing_page.Document.recompute()

                # Leaving the dummy document open is a waste of RAM
                # and clutters up the GUI, so ideally, one would like
                # to close it.  Unfortunately, attempting to close the
                # dummy document causes a segfault, at least under
                # FreeCAD 0.16 on Scientific Linux 7.3 and FreeCAD
                # 0.16 on Fedora 28, so the following command operates
                # only if the FreeCAD version is 0.18.4 or later.
                # (I've checked, and the segfault doesn't happen under
                # FreeCAD 0.18.4 on Ubuntu 20.04.)

                if (versionnumber >= 0.184):
                        FreeCAD.closeDocument("Dummy")

class first_angle_projection:

        # The purpose of this class is to provide the method "fap",
        # which takes any object ("the shape") which can be assigned
        # to the "Shape" property of a Part::Feature object, and adds
        # a set of axonometric drawings ("the views") of the shape in
        # first angle projection to an existing TechDraw::DrawPage or
        # Drawing::FeaturePage object ("the sheet"), following the
        # conventions in BS 8888:2011.  The method fap also creates a
        # new FreeCAD Document ("the dummy document"), containing
        # various objects that are created as intermediate steps on
        # the way to adding the views to the sheet, but which do not
        # need to exist in the same document as the sheet.  The method
        # fap also modifies the parent document of the sheet, by
        # adding to it six TechDraw::DrawViewPart or
        # Drawing::FeatureViewPart objects, which are intermediate
        # steps on the way to adding the views to the sheet, and which
        # have to exist _in the same document as the sheet_ in order
        # to add the views to the sheet.

        def __init__(self, title_in, part_in, spacing_in, xpos_in, ypos_in,
                     scale_in, drawing_page_in):
            self.title = title_in
            self.part = part_in
            self.spacing = spacing_in
            self.xpos = xpos_in
            self.ypos = ypos_in
            self.scale = scale_in
            self.drawing_page = drawing_page_in

        def fap(self,dummy):
                thick = 0.7 # The wider of the two line widths suggested in\
                            # BS 8888:2011
                thin = 0.35 # The narrower of the two line widths suggested\
                            # in BS 8888:2011

                # Measure the dimensions of the shape, in order to know how
                # much space is needed on the sheet for the views.

                width = self.part.BoundBox.XLength
                depth = self.part.BoundBox.YLength
                height = self.part.BoundBox.ZLength
                dummydoc = FreeCAD.newDocument("Dummy")
                part_in_tree = dummydoc.addObject("Part::Feature",
                                                  self.title)
                part_in_tree.Shape = self.part
                featurepart = dummydoc.getObject(self.title)
                versionnumber = float(FreeCAD.Version()[0])\
                        +0.01*float(FreeCAD.Version()[1])
                if(versionnumber < 0.19):
                        minuszview\
                                = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                       self.title
                                                                       +" from negative z")
                else:
                        minuszview\
                                = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                       self.title
                                                                       +" from negative z") 
                minuszview.Source = featurepart
                minuszview.Direction = FreeCAD.Vector(0.0,0.0,-1.0)

                # BS 8888:2011 does not specify the exact spacing
                # between the individual views, so that spacing is
                # taken from user input; similarly for the position on
                # the sheet of the overall set of views.

                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        minuszview.X = self.xpos+self.scale*depth+self.spacing
                        minuszview.Y = self.ypos
                else:
                        minuszview.ScaleType = u"Custom"
                minuszview.Scale = self.scale
                if(versionnumber < 0.19):
                        minuszview.Rotation = 180.0
                        minuszview.ShowHiddenLines = True
                        minuszview.LineWidth = thick
                        minuszview.HiddenWidth = thin
                        self.drawing_page.addObject(minuszview)

                        minusxview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                          self.title
                                                                          +" from negative x")
                else:
                        minuszview.Rotation = 0.0
                        minuszview.HardHidden = True
                        minuszview.ViewObject.LineWidth = thick
                        minuszview.ViewObject.HiddenWidth = thin
                        minuszview.Label = ""
                        self.drawing_page.addView(minuszview)
                        minuszview.X = self.xpos+self.scale*(depth+0.5*width)\
                                +self.spacing
                        minuszview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-0.5*self.scale*depth

                        minusxview = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                          self.title
                                                                          +" from negative x")
                
                minusxview.Source = featurepart
                minusxview.Direction = FreeCAD.Vector(-1.0,0.0,0.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        minusxview.X = self.xpos+self.scale*(2.0*depth
                                                    +width)\
                                                    +2.0*self.spacing
                        minusxview.Y = self.ypos+self.scale*(depth
                                                             +height)\
                                                             +self.spacing
                else:
                        minusxview.ScaleType = u"Custom"
                minusxview.Scale = self.scale
                if(versionnumber < 0.19):
                        minusxview.Rotation = 90.0
                        minusxview.ShowHiddenLines = True
                        minusxview.LineWidth = thick
                        minusxview.HiddenWidth = thin
                        self.drawing_page.addObject(minusxview)

                        minusyview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                          self.title
                                                                          +" from negative y")
                else:
                        minusxview.Rotation = 0.0
                        minusxview.HardHidden = True
                        minusxview.ViewObject.LineWidth = thick
                        minusxview.ViewObject.HiddenWidth = thin
                        minusxview.Label = ""
                        self.drawing_page.addView(minusxview)
                        minusxview.X = self.xpos+self.scale*(1.5*depth+width)\
                                +2.0*self.spacing
                        minusxview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-self.scale*(depth+0.5*height)\
                                -self.spacing

                        minusyview = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                          self.title
                                                                          +" from negative y")
                
                minusyview.Source = featurepart
                minusyview.Direction = FreeCAD.Vector(0.0,-1.0,0.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        minusyview.X = self.xpos+self.scale*depth+self.spacing
                        minusyview.Y = self.ypos+self.scale*(depth
                                                             +height)\
                                                             +self.spacing
                else:
                        minusyview.ScaleType = u"Custom"
                minusyview.Scale = self.scale
                if(versionnumber < 0.19):
                        minusyview.Rotation = 90.0
                        minusyview.ShowHiddenLines = True
                        minusyview.LineWidth = thick
                        minusyview.HiddenWidth = thin
                        self.drawing_page.addObject(minusyview)

                        plusxview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                         self.title
                                                                         +" from positive x")
                else:
                        minusyview.HardHidden = True
                        minusyview.ViewObject.LineWidth = thick
                        minusyview.ViewObject.HiddenWidth = thin
                        minusyview.Label = ""
                        self.drawing_page.addView(minusyview)
                        minusyview.X = self.xpos+self.scale*(depth+0.5*width)\
                                +self.spacing
                        minusyview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-self.scale*(depth+0.5*height)\
                                -self.spacing

                        plusxview = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                         self.title
                                                                         +" from positive x")
                
                plusxview.Source = featurepart
                plusxview.Direction = FreeCAD.Vector(1.0,0.0,0.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        plusxview.X = self.xpos
                        plusxview.Y = self.ypos+self.scale*(depth
                                                            +height)\
                                                            +self.spacing
                else:
                        plusxview.ScaleType = u"Custom"
                plusxview.Scale = self.scale
                if (versionnumber < 0.19):
                        plusxview.Rotation = 270.0
                        plusxview.ShowHiddenLines = True
                        plusxview.LineWidth = thick
                        plusxview.HiddenWidth = thin
                        self.drawing_page.addObject(plusxview)

                        plusyview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                         self.title
                                                                         +" from positive y")
                else:
                        plusxview.Rotation = 0.0
                        plusxview.HardHidden = True
                        plusxview.ViewObject.LineWidth = thick
                        plusxview.ViewObject.HiddenWidth = thin
                        plusxview.Label = ""
                        self.drawing_page.addView(plusxview)
                        plusxview.X = self.xpos+self.scale*0.5*depth
                        plusxview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-self.scale*(depth+0.5*height)\
                                -self.spacing

                        plusyview = self.drawing_page.Document.addObject("TechDraw::DrawViewPart",
                                                                         self.title
                                                                         +" from positive y")
                
                plusyview.Source = featurepart
                plusyview.Direction = FreeCAD.Vector(0.0,1.0,0.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        plusyview.X = self.xpos+self.scale*(2.0*depth
                                                            +2.0*width)\
                                                            +3.0*self.spacing
                        plusyview.Y = self.ypos+self.scale*(depth
                                                            +height)\
                                                            +self.spacing
                else:
                        plusyview.ScaleType = u"Custom"
                plusyview.Scale = self.scale
                if (versionnumber < 0.19):
                        plusyview.Rotation = 270.0
                        plusyview.ShowHiddenLines = True
                        plusyview.LineWidth = thick
                        plusyview.HiddenWidth = thin
                        self.drawing_page.addObject(plusyview)

                        pluszview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart"
                                                                         ,self.title
                                                                         +" from positive z")
                else:
                        plusyview.Rotation = 0.0
                        plusyview.HardHidden = True
                        plusyview.ViewObject.LineWidth = thick
                        plusyview.ViewObject.HiddenWidth = thin
                        plusyview.Label = ""
                        self.drawing_page.addView(plusyview)
                        plusyview.X = self.xpos+self.scale*(2.0*depth
                                                            +1.5*width)\
                                                            +3.0*self.spacing
                        plusyview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-self.scale*(depth+0.5*height)\
                                -self.spacing

                        pluszview = self.drawing_page.Document.addObject("TechDraw::DrawViewPart"
                                                                         ,self.title
                                                                         +" from positive z")
                
                pluszview.Source = featurepart
                pluszview.Direction = FreeCAD.Vector(0.0,0.0,1.0)
                if(versionnumber < 0.19):
                        
                        # The "addView" method of a TechDraw::DrawPage
                        # object appears to change the "X" and "Y"
                        # properties of the TechDraw::DrawViewPart
                        # object that's being added, so it's only when
                        # the Drawing toolbox, rather than the
                        # TechDraw toolbox, is being used that there's
                        # any point setting the "X" and "Y" properties
                        # (of the Drawing::FeatureViewPart object) here.
                        # In any case, the "X" and "Y" properties have
                        # to take different values when the TechDraw
                        # toolbox is in use, since the TechDraw toolbox
                        # measures Y in the opposite direction from the
                        # Drawing toolbox, and the TechDraw toolbox
                        # measures X and Y at the centre of a
                        # DrawViewPart object, whereas the Drawing
                        # toolbox measures X and Y at one corner of a
                        # FeatureViewPart object.
                        pluszview.X = self.xpos+self.scale*depth+self.spacing
                        pluszview.Y = self.ypos+self.scale*(2.0*depth
                                                            +height)\
                                                            +2.0*self.spacing
                else:
                        pluszview.ScaleType = u"Custom"
                pluszview.Scale = self.scale
                pluszview.Rotation = 0.0
                        
                if(versionnumber < 0.19):
                        pluszview.ShowHiddenLines = True
                        pluszview.LineWidth = thick
                        pluszview.HiddenWidth = thin
                        self.drawing_page.addObject(pluszview)
                else:
                        pluszview.HardHidden = True
                        pluszview.ViewObject.LineWidth = thick
                        pluszview.ViewObject.HiddenWidth = thin
                        pluszview.Label = ""
                        self.drawing_page.addView(pluszview)
                        pluszview.X = self.xpos+self.scale*(depth+0.5*width)\
                                +self.spacing
                        pluszview.Y = float(self.drawing_page.Template.Height)\
                                -self.ypos-self.scale*(1.5*depth+height)\
                                -2.0*self.spacing
                        
                self.drawing_page.Document.recompute()

                # Leaving the dummy document open is a waste of RAM
                # and clutters up the GUI, so ideally, one would like
                # to close it.  Unfortunately, when this method is
                # being used to add views of a second shape to a sheet
                # that already contains views of one shape, attempting
                # to close the dummy document causes a segfault, at
                # least under FreeCAD 0.16 on Scientific Linux 7.3, so
                # the following command operates only if the FreeCAD
                # version is 0.18.4 or later.  (I've checked, and the
                # segfault doesn't happen under FreeCAD 0.18.4 on
                # Ubuntu 20.04.)

                if (versionnumber >= 0.184):
                        FreeCAD.closeDocument("Dummy")
