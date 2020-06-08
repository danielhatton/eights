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

import FreeCAD
import Part
import Drawing

class create_eights_drawing_sheet:

        # The purpose of this class is to provide the method
        # "create_it", which adds, to an existing FreeCAD document, a
        # Drawing::FeaturePage object ("the sheet") whose formatting
        # is intended to be consistent with the BS 8888:2011 standard
        # for a drawing sheet, and populates the title block of the
        # sheet, again in a way intended to be consistent with BS
        # 8888:2011.

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
                thesheet = self.document.addObject("Drawing::FeaturePage",
                                                self.shorttitle)

                # BS 8888:2011 inherits most of its style requirements
                # for drawing sheets from ISO7200, so FreeCAD's built-in
                # ISO7200 templates are a good starting point.

                thesheet.Template = FreeCAD.getResourceDir()\
                        +"Mod/Drawing/Templates/"+self.pagesize\
                        +"_"+self.orientation+"_ISO7200.svg"
                
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
                # FreeCAD., so it's necessary to detect the FreeCAD
                # version number here.

                versionnumber = float(FreeCAD.Version()[0])\
                                +0.01*float(FreeCAD.Version()[1])

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
                else:
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
                self.document.recompute()

class add_first_angle_projection_symbol:

        # The purpose of this class is to provide the method
        # "put_it_in", which adds the standard BS 8888:2011 symbol,
        # indicating that a set of drawings are in first angle
        # projection ("the symbol"), to an existing
        # Drawing::FeaturePage object ("the sheet").  The method
        # put_it_in also creates a new FreeCAD Document ("the dummy
        # document"), containing various objects that are created as
        # intermediate steps on the way to adding the symbol to the
        # sheet, but which do not need to exist in the same document
        # as the sheet.  The method put_it_in also modifies the parent
        # document of the sheet, by adding to it two
        # Drawing::FeatureViewPart objects, which are intermediate
        # steps on the way to adding the symbol to the sheet, and
        # which have to exist _in the same document as the sheet_ in
        # order to add the symbol to the sheet.

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
                minusxview\
                        = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                               title
                                                               +" from negative x")
                reflectedone = dummydoc.addObject("Part::Mirroring",
                                                  "reflectedone")
                reflectedone.Source = featurepart
                reflectedone.Normal = FreeCAD.Vector(0.0,0.0,1.0)
                reflectedone.Base = FreeCAD.Vector(0.0,0.0,0.0)
                minusxview.Source = reflectedone
                minusxview.Direction = FreeCAD.Vector(-1.0,0.0,0.0)

                # BS 8888:2011 does not specify the exact position of
                # the symbol on the sheet, so that position is taken
                # from user input.

                minusxview.X = self.xpos
                minusxview.Y = self.ypos
                minusxview.Scale = 1.0
                minusxview.Rotation = 270.0
                minusxview.ShowHiddenLines = False
                minusxview.LineWidth = thick
                minusxview.HiddenWidth = thin
                self.drawing_page.addObject(minusxview)
                minusyview\
                        = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                               title
                                                               +" from negative y")
                minusyview.Source = featurepart
                minusyview.Direction = FreeCAD.Vector(0.0,-1.0,0.0)
                minusyview.X = self.xpos+depth+spacing
                minusyview.Y = self.ypos
                minusyview.Scale = 1.0
                minusyview.Rotation = 90.0
                minusyview.ShowHiddenLines = False
                minusyview.LineWidth = thick
                minusyview.HiddenWidth = thin
                self.drawing_page.addObject(minusyview)
                self.drawing_page.Document.recompute()

                # Leaving the dummy document open is a waste of RAM
                # and clutters up the GUI, so ideally, one would like
                # to close it.  Unfortunately, attempting to close the
                # dummy document causes a segfault, at least under
                # FreeCAD 0.16 on Scientific Linux 7.3 and FreeCAD
                # 0.16 on Fedora 28, so the following command is
                # commented out.

                # FreeCAD.closeDocument("Dummy")

class first_angle_projection:

        # The purpose of this class is to provide the method "fap",
        # which takes any object ("the shape") which can be assigned
        # to the "Shape" property of a Part::Feature object, and adds
        # a set of axonometric drawings ("the views") of the shape in
        # first angle projection to an existing Drawing::FeaturePage
        # object ("the sheet"), following the conventions in BS
        # 8888:2011.  The method fap also creates a new FreeCAD
        # Document ("the dummy document"), containing various objects
        # that are created as intermediate steps on the way to adding
        # the views to the sheet, but which do not need to exist in
        # the same document as the sheet.  The method fap also
        # modifies the parent document of the sheet, by adding to it
        # six Drawing::FeatureViewPart objects, which are intermediate
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
                minuszview\
                        = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                               self.title
                                                               +" from negative z")
                minuszview.Source = featurepart
                minuszview.Direction = FreeCAD.Vector(0.0,0.0,-1.0)

                # BS 8888:2011 does not specify the exact spacing
                # between the individual views, so that spacing is
                # taken from user input; similarly for the position on
                # the sheet of the overall set of views.

                minuszview.X = self.xpos+self.scale*depth+self.spacing
                minuszview.Y = self.ypos
                minuszview.Scale = self.scale
                minuszview.Rotation = 180.0
                minuszview.ShowHiddenLines = True
                minuszview.LineWidth = thick
                minuszview.HiddenWidth = thin
                self.drawing_page.addObject(minuszview)
                minusxview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                  self.title
                                                                  +" from negative x")
                reflectedone = dummydoc.addObject("Part::Mirroring",
                                                  "reflectedone")
                reflectedone.Source = featurepart
                reflectedone.Normal = FreeCAD.Vector(0.0,0.0,1.0)
                reflectedone.Base = FreeCAD.Vector(0.0,0.0,0.0)
                minusxview.Source = reflectedone
                minusxview.Direction = FreeCAD.Vector(-1.0,0.0,0.0)
                minusxview.X = self.xpos
                minusxview.Y = self.ypos+self.scale*(depth
                                                     +height)+self.spacing
                minusxview.Scale = self.scale
                minusxview.Rotation = 270.0
                minusxview.ShowHiddenLines = True
                minusxview.LineWidth = thick
                minusxview.HiddenWidth = thin
                self.drawing_page.addObject(minusxview)
                minusyview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                  self.title
                                                                  +" from negative y")
                minusyview.Source = featurepart
                minusyview.Direction = FreeCAD.Vector(0.0,-1.0,0.0)
                minusyview.X = self.xpos+self.scale*depth+self.spacing
                minusyview.Y = self.ypos+self.scale*(depth
                                                     +height)+self.spacing
                minusyview.Scale = self.scale
                minusyview.Rotation = 90.0
                minusyview.ShowHiddenLines = True
                minusyview.LineWidth = thick
                minusyview.HiddenWidth = thin
                self.drawing_page.addObject(minusyview)
                plusxview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                 self.title
                                                                 +" from positive x")
                reflectedtwo = dummydoc.addObject("Part::Mirroring",
                                                  "reflectedtwo")
                reflectedtwo.Source = featurepart
                reflectedtwo.Normal = FreeCAD.Vector(0.0,0.0,1.0)
                reflectedtwo.Base = FreeCAD.Vector(0.0,0.0,0.0)
                plusxview.Source = reflectedtwo
                plusxview.Direction = FreeCAD.Vector(1.0,0.0,0.0)
                plusxview.X = self.xpos+self.scale*(2.0*depth
                                                    +width)\
                        +2.0*self.spacing
                plusxview.Y = self.ypos+self.scale*(depth
                                                    +height)+self.spacing
                plusxview.Scale = self.scale
                plusxview.Rotation = 90.0
                plusxview.ShowHiddenLines = True
                plusxview.LineWidth = thick
                plusxview.HiddenWidth = thin
                self.drawing_page.addObject(plusxview)
                plusyview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart",
                                                                 self.title
                                                                 +" from positive y")
                plusyview.Source = featurepart
                plusyview.Direction = FreeCAD.Vector(0.0,1.0,0.0)
                plusyview.X = self.xpos+self.scale*(2.0*depth
                                                    +2.0*width)\
                        +3.0*self.spacing
                plusyview.Y = self.ypos+self.scale*(depth
                                                    +height)+self.spacing
                plusyview.Scale = self.scale
                plusyview.Rotation = 270.0
                plusyview.ShowHiddenLines = True
                plusyview.LineWidth = thick
                plusyview.HiddenWidth = thin
                self.drawing_page.addObject(plusyview)
                pluszview = self.drawing_page.Document.addObject("Drawing::FeatureViewPart"
                                                                 ,self.title
                                                                 +" from positive z")
                pluszview.Source = featurepart
                pluszview.Direction = FreeCAD.Vector(0.0,0.0,1.0)
                pluszview.X = self.xpos+self.scale*depth+self.spacing
                pluszview.Y = self.ypos+self.scale*(2.0*depth
                                                    +height)\
                                                    +2.0*self.spacing
                pluszview.Scale = self.scale
                pluszview.Rotation = 0.0
                pluszview.ShowHiddenLines = True
                pluszview.LineWidth = thick
                pluszview.HiddenWidth = thin
                self.drawing_page.addObject(pluszview)
                self.drawing_page.Document.recompute()

                # Leaving the dummy document open is a waste of RAM
                # and clutters up the GUI, so ideally, one would like
                # to close it.  Unfortunately, when this method is
                # being used to add views of a second shape to a sheet
                # that already contains views of one shape, attempting
                # to close the dummy document causes a segfault, at
                # least under FreeCAD 0.16 on Scientific Linux 7.3, so
                # the following command is commented out.

                # FreeCAD.closeDocument("Dummy")
