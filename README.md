# About this documentation file

This is file `README.md`

`README.md` is the documentation for a software library centred
on file `eights.py` (see "Description" section below).

`README.md` was written by Dr. Daniel C. Hatton

Material up to and including release 0.2 copyright (C) 2017-2018
University of Plymouth Higher Education Corporation

Changes since release 0.2 copyright (C) 2020 Dr. Daniel C. Hatton

This program, including this documentation file, is free software: you
can redistribute it and/or modify it under the terms of the GNU Lesser
General Public License as published by the Free Software Foundation:
version 3 of the License.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License, and the GNU General Public License
which it incorporates, for more details.

You should have received a copy of the GNU Lesser General Public
License [in file `LICENSE`] along with this program.  If not, see
<https://www.gnu.org/licenses/>.

Daniel Hatton thanks Dr. Justin E. Rigden, Specialist Intellectual
Property Advisor, for authorizing, on behalf of the University of
Plymouth Higher Education Corporation, the release of this program
under the licence terms stated above.

# Contact

Daniel Hatton can be contacted on <dan.hatton@physics.org>.

# Description

File `eights.py` is a Python module intended for use with the
open-source 3D computer-aided design package FreeCAD (FreeCAD version
0.15 user manual, n.d.).  The module automates the construction of a
page of 2D axonometric drawings in first angle projection, in a style
consistent (to the best of the module author's ability) with the BS
8888:2011 standard (Technical product documentation and specification
BS 8888, 2011).

# Statement of need

The creative process behind detailed engineering design now typically
takes place in 3D CAD packages (Quintana et al., 2010). However, for
this creative process actually to lead to an embodiment of the design
being manufactured, this creative process must be followed by
communication of the content of the design to a manufacturing
facility. There are two necessary requirements for success: firstly,
the communication must include information on all those aspects of the
design that are necessary to complete manufacture, and to verify by
inspection that the completed, manufactured artefact matches the
design (Quintana et al., 2010); secondly, the communication must be in
a well-defined (usually graphical) language, so that it can be
understood at the manufacturing facility in a way that permits
successful manufacturing and inspection (Quintana et al., 2010;
Dobelis et al., 2018). The drive to meet both of these requirements
has led to the development of published standards for design
communication (Dobelis et al., 2018), of which BS 8888:2011 (Technical
product documentation and specification BS 8888, 2011) is one. These
standards are in a very advanced state of maturity for 2D engineering
drawings, but despite efforts in recent years to develop similar
standards for 3D models, the standards for 3D models remain somewhat
less mature (Quintana et al., 2010). As a result, 2D drawings remain a
crucial medium for communication of design information to
manufacturing facilities, and possessing the capability for automated
generation of standards-compliant 2D drawings from a 3D model is an
important criterion by which the technical quality of 3D CAD software
packages is assessed (Kannan & Vinay, 2008; Hughes, 2013). Hence, by
automating the process of producing certain standards-compliant 2D
drawings, the eights module offers the opportunity for the FreeCAD CAD
package (FreeCAD version 0.15 user manual, n.d.) to be more favourably
assessed against this criterion in future.

One automated tool, for generating 2D drawings in first angle
projection from a 3D model in FreeCAD, already exists: the FreeCAD
Automatic Drawing Macro (Macro Automatic Drawing, 2016). A full
analysis of the relative advantages and disadvantages of the Automatic
Drawing Macro, and the eights module announced here, can be found in
the "Comparison and contrast with other software of similar purpose"
section of this documentation file.  For the purposes of this
statement of need, it is sufficient to mention two of the relative
disadvantages of the Automatic Drawing Macro:

* the Automatic Drawing Macro does not attempt to comply with BS 8888
  as regards the format of the drawing sheet and its title block;
* the Automatic Drawing Macro does not offer the ability to include
  first angle pro jection sets for multiple 3D objects on the same
  drawing sheet.

It is not only in the manufacturing sector that standardized
axonometric drawings have proved important to clear communication:
scholarly research has also benefited from this language. For example,
in the study of human anatomy, standardization of axonometric drawing
sets to the BS 8888 standard has been used to reduce both cumulative
uncertainty in position co-ordinates and difficulty of interpretation
associated with the presentation, in published papers, of geometric
data on the human skeleton (Magee et al., 2012); and in archaeology,
the standard first-angle projection set has been used to facilitate
unambiguous description of the laboratory methods used to infer
manufacturing methods from surface profilometry of ancient monumental
artefacts (Moitinho de Almeida & Barceló, 2014). In scholarly research
in physics, one finds a cautionary tale concerning the consequences
when no standardized language is available for engineering drawings:
in foundational seventeenth-century experimental research in
hydrostatics, the discovery of effects, in the force balance on
columns of water and air, due to the solubility of air in water and to
adhesion between water and solid surfaces, was for some time hotly
contested due to a lack of reproducibility of results between subtly
different sets of apparatus (Shapin & Schaffer, 2011). In the absence
of a standard for engineering drawings, attempts to communicate
between different research groups, using a combination of text and
schematic diagrams, what the differences between their respective
apparatus were, proved fruitless, and consensus on the experimental
facts was eventually achieved only by the long-range transport of
actual experimental rigs, across international borders, for
side-by-side comparison (Shapin & Schaffer, 2011). So deep did the
confusion run that, more than three centuries later, Shapin & Schaffer
(2011) still found themselves with much work to do, in attempting to
understand exactly what were the relevant differences between the
respective experimental rigs.

# Prerequisites

For this module to be useful, it will be necessary to have a working
installation of FreeCAD.  FreeCAD is available in the standard
repositories of most Linux distributions, and for Windows and MAC OS X
systems from <https://www.freecadweb.org/wiki/Download>.  The module
has been most thoroughly tested on FreeCAD 0.16 under Scientific Linux
7.3 and Scientific Linux 7.5, but also to some extent on FreeCAD 0.15
under Windows 7 Enterprise, on FreeCAD 0.16 under Fedora 28, and on
FreeCAD 0.18.4 under Ubuntu 20.04.

# Installation

To install, create a subdirectory called `eights` in your module
directory (`~/.FreeCAD/Mod` on Linux, `%APPDATA%\FreeCAD\Mod` on
Windows), and place the file `eights.py` in that subdirectory.

On some systems (at least, FreeCAD 0.16 under Scientific Linux 7.5),
placing the file `eights.py` in the working directory from which
FreeCAD is to be started can also be an effective installation method,
although there are reports that this method does not work on all
systems.

# Details

The module provides:

* a class "`create_eights_drawing_sheet`", whose purpose is to provide
  the method "`create_it`", which adds, to an existing FreeCAD
  document, a `TechDraw::DrawPage` (if the FreeCAD version under which
  the module is being run is 0.19 or later) or `Drawing::FeaturePage`
  (if the FreeCAD version under which the module is being run is
  earlier than 0.19) object ("the sheet") whose formatting is intended
  to be consistent with the BS 8888:2011 standard for a drawing sheet,
  and populates the title block of the sheet, again in a way intended
  to be consistent with BS 8888:2011;
* a class "`add_first_angle_projection_symbol`", whose purpose is to
  provide the method "`put_it_in`", which adds the standard BS
  8888:2011 symbol, indicating that a set of drawings are in first
  angle projection ("the symbol"), to an existing `TechDraw::DrawPage`
  or `Drawing::FeaturePage` object ("the sheet").  The method
  `put_it_in` also creates a new FreeCAD Document ("the dummy
  document"), containing various objects that are created as
  intermediate steps on the way to adding the symbol to the sheet, but
  which do not need to exist in the same document as the sheet.  The
  method `put_it_in` also modifies the parent document of the sheet,
  by adding to it two `TechDraw::DrawViewPart` (if the FreeCAD version
  under which the module is being run is 0.19 or later) or
  `Drawing::FeatureViewPart` (if the FreeCAD version under which the
  module is being run is earlier than 0.19) objects, which are
  intermediate steps on the way to adding the symbol to the sheet, and
  which have to exist _in the same document as the sheet_ in order to
  add the symbol to the sheet; and
* a class "`first_angle_projection`", whose purpose is to provide the
  method "`fap`", which takes any object ("the shape") which can be
  assigned to the "`Shape`" property of a `Part::Feature` object, and
  adds a set of axonometric drawings ("the views") of the shape in
  first angle projection to an existing `TechDraw::DrawPage` or
  `Drawing::FeaturePage` object ("the sheet"), following the
  conventions in BS 8888:2011.  The method `fap` also creates a new
  FreeCAD Document ("the dummy document"), containing various objects
  that are created as intermediate steps on the way to adding the
  views to the sheet, but which do not need to exist in the same
  document as the sheet.  The method `fap` also modifies the parent
  document of the sheet, by adding to it six `TechDraw::DrawViewPart`
  (if the FreeCAD version under which the module is being run is 0.19
  or later) or `Drawing::FeatureViewPart` (if the FreeCAD version
  under which the module is being run is earlier than 0.19) objects,
  which are intermediate steps on the way to adding the views to the
  sheet, and which have to exist _in the same document as the sheet_
  in order to add the views to the sheet.

# Invocation

The methods provided by this module can be invoked either from the
FreeCAD Python console, or from a Python script opened in FreeCAD.  In
both cases, before invoking the methods from this module, it will be
necessary to invoke

    import FreeCAD
    import Part
    import eights

To create a BS 8888:2011 drawing sheet, as a `TechDraw::DrawPage` (if
the FreeCAD version under which the module is being run is 0.19 or
later) or `Drawing::FeaturePage` (if the FreeCAD version under which
the module is being run is earlier than 0.19) object to be stored in
"`any_var_name`":

    any_var_name = eights.create_eights_drawing_sheet(<doc>, <shorttitle>,
                                                      <pagesize>, <orientation>,
                                                      <creator>,
                                                      <longtitle>,
                                                      <legalowner>,
                                                      <approver>,
                                                      <doctype>,
                                                      <docstatus>,
                                                      <sheetnum>,
                                                      <totalsheets>,
                                                      <inversescale>,
                                                      <partlist>,
                                                      <drawingnum>, <year>,
                                                      <month>, <day>, <rev>)
    any_other_var_name = any_var_name.create_it('putanyoldrubbishhere')

where:

* `<doc>` is the FreeCAD document to which the drawing sheet will be
  added;
* `<shorttitle>` is a string giving a short title (suitable to
  appear in the tree view in the FreeCAD GUI) for the drawing sheet;
* `<pagesize>` is a string indicating the size of paper on which the
  drawing sheet should appear, in the same format used in the
  file names of the SVG files for FreeCAD's built in ISO7200
  templates;
* `<orientation>` is a string indicating the orientation of paper on
  which the drawing sheet should appear, in the same format used in
  the file names of the SVG files for FreeCAD's built in ISO7200
  templates;
* `<creator>` is a string giving the name of the creator of the design
  (suitable to appear in the on-sheet title block) ;
* `<longtitle>` is a string giving a longer title (suitable to appear in
  the on-sheet title block) for the drawing sheet;
* `<legalowner>` is a string identifying the legal owner of the design
  (suitable to appear in the on-sheet title block);
* `<approver>` is a string giving the name of the approval person for
  the design (suitable to appear in the on-sheet title block);
* `<doctype>` is a string identifying the document type (suitable to
  appear in the on-sheet title block);
* `<docstatus>` is a string identifying the document status (suitable to
  appear in  the on-sheet title block);
* `<sheetnum>` is an integer identifying which number sheet this is in
  the overall series of drawing sheets of which it is a member;
* `<totalsheets>` is an integer identifying how many sheets there are in
  total in the series of which this drawing sheet is a member;
* `<inversescale>` is an integer identifying the reciprocal of the scale
  to which the drawings are to be drawn (BS 8888:2011 indicates a
  preference for this number being either 2 or 5);
* `<partlist>` is a string containing a comma-separated list of the part
  identifiers of the parts that will appear on this drawing sheet;
* `<drawingnum>` is a string indicating the drawing identifier of this
  drawing sheet;
* `<year>` is an integer representing the year in which the design was
  created;
* `<month>` is an integer representing the calendar month in which the
  design was created;
* `<day>` is an integer representing the day of the month on which the
  design was created; and
* `<rev>` is a string indicating the revision identifier of the version
  of the design that will appear on this drawing sheet.

To add the first-angle projection symbol to a drawing sheet:

    some_name = eights.add_first_angle_projection_symbol(<largediam>,
                                                         <smalldiam>,
                                                         <spacing>,
                                                         <xpos>, <ypos>,
                                                         <thepage>)
    some_other_name = some_name.put_it_in('putanyoldrubbishhere')

where:

* `<largediam>` is a floating-point number, representing the diameter at
  base of the truncated cone from which the symbol is generated (on the
  systems where the present module has been tested, it's in
  millimetres, but this may depend on some configuration option of
  FreeCAD);
* `<smalldiam>` is a floating-point number, representing the diameter at
  truncation plane of the truncated cone from which the symbol is
  generated (on the systems where the present module has been tested,
  it's in millimetres, but this may depend on some configuration
  option of FreeCAD);
* `<spacing>` is a floating-point number, representing the spacing
  between the two axonometric projections of the truncated cone that
  form the symbol (on the systems where the present module has been
  tested, it's in millimetres, but this may depend on some
  configuration option of FreeCAD);
* `<xpos>` is a floating-point number, representing the horizontal
  position ordinate, on the drawing page, at which the symbol is to be
  placed (on the systems where the present module has been tested,
  it's in millimetres, but this may depend on some configuration
  option of FreeCAD);
* `<ypos>` is a floating-point number, representing the vertical
  position ordinate, on the drawing page, at which the symbol is to be
  placed (on the systems where the present module has been tested,
  it's in millimetres, but this may depend on some configuration
  option of FreeCAD); and
* `<thepage>` is a `TechDraw::DrawPage` or`Drawing::FeaturePage`
  object, representing the drawing sheet to which the symbol is to be
  added.

To add a first angle projection set for a 3D shape to a drawing sheet:

    a_name = eights.first_angle_projection(<partnum>, <theshape>,
                                           <spacing>,
                                           <xpos>, <ypos>,
                                           <scale>, <thepage>)
    
    another_name = a_name.fap('putanyoldrubbishhere')


where:

* `<partnum>` is a string containing a comma-separated list of the
  part identifiers of the parts included in the 3D shape;
* `<theshape>` is an object capable of being assigned to the `Shape`
  property of a `Part::Feature` object, representing the 3D shape to be
  drawn;
* `<spacing>` is a floating-point number, representing the spacing
  between the individual axonometric projections of the 3D shape (on
  the systems where the present module has been tested, it's in
  millimetres, but this may depend on some configuration option of
  FreeCAD);
* `<xpos>` is a floating-point number, representing the horizontal
  position ordinate, on the drawing page, at which the first angle
  projection set is to be placed (on the systems where the present
  module has been tested, it's in millimetres, but this may depend on
  some configuration option of FreeCAD);
* `<ypos>` is a floating-point number, representing the vertical
  position ordinate, on the drawing page, at which the first angle
  projection set is to be placed (on the systems where the present
  module has been tested, it's in millimetres, but this may depend on
  some configuration option of FreeCAD);
* `<scale>` is a floating-point number, representing the scale at which
  the first angle projection set is to be drawn (BS 8888:2011
  indicates a preference for this number being either 0.5 or 0.2); and
* `<thepage>` is a `TechDraw::DrawPage` or `Drawing::FeaturePage`
  object, representing the drawing sheet to which the first angle
  projection set is to be added.

# Example scripts (test cases)

Six example python scripts that make use of this module are provided,
in the directory `EXAMPLES`.  In each case, one can run the example
script by opening it in the FreeCAD GUI and pressing the GUI "Execute
the macro in the editor" button.  The expected functionality of the
example scripts is as follows:

* `Single_part.py` creates a drawing sheet showing, in first angle
  projection, a single part (a cube of side 100 mm), with intended
  output as follows: ![Intended output for single part
  example](EXAMPLES/Single_part_intended_output.png).
* `Two_parts.py` creates a drawing sheet showing, in first angle
  projection, two separate parts (a cube of side 100 mm and a sphere
  of diameter 100 mm), with intended output as follows: ![Intended
  output for two-part
  example](EXAMPLES/Two_parts_intended_output.png).
* `Assembly.py` creates a drawing sheet showing, in first angle
  projection, two parts (a cube of side 100 mm and a sphere of
  diameter 100 mm) fused into an assembly, with intended output as
  follows: ![Intended output for assembly
  example](EXAMPLES/Assembly_intended_output.png).
* `Anisotropic_part.py` creates a drawing sheet showing, in first
  angle projection, a single part (a rectangular parallelepiped of
  sides 50 mm, 100 mm, and 150 mm), with intended output as follows:
  ![Intended output for anisotropic part
  example](EXAMPLES/Anisotropic_part_intended_output.png).
* `Assembly_side.py` creates a drawing sheet showing, in first angle
  projection, the same assembly as in `Assembly.py`, but in a
  different orientation.  This has been added because previously, all
  the test cases had reflection symmetry about the same planes, which
  had caused a particular bug (now fixed) to remain undetected through
  multiple releases.  The intended output is as follows: ![Intended
  output for differently-oriented assembly
  example](EXAMPLES/Assembly_side_intended_output.png).
* `Assembly_back.py` creates a drawing sheet showing, in first angle
  projection, the same assembly as in `Assembly.py` and
  `Assembly_side.py`, but in a different orientation.  This has been
  added because previously, all the test cases had reflection symmetry
  about the same planes, which had caused a particular bug (now fixed)
  to remain undetected through multiple releases.  The intended output
  is as follows: ![Intended output for differently-oriented assembly
  example](EXAMPLES/Assembly_back_intended_output.png).

# Comparison and contrast with other software of similar purpose

The present module is not the only available contributed Python script
for FreeCAD intended to produce a drawing sheet containing a
first-angle projection set: there is also the ["Automatic drawing"
macro](https://www.freecadweb.org/wiki/Macro_Automatic_drawing).
There are a number of differences between the operation of the
Automatic Drawing macro and the operation of the present module.  Some
of these differences can be classified as advantages of the present
module, some can be classified as advantages of the Automatic Drawing
macro, and some are neutral (including differences that may be either
advantages of the present module or advantages of the Automatic
Drawing macro, depending on the use case).

## Advantages of the present module

* The present module has separate methods for the creation of the
  drawing sheet and the addition of a first angle projection set,
  whereas the Automatic Drawing macro performs both tasks in a single
  procedure; this means that only the present module offers the
  ability to include first angle projection sets for multiple 3D
  objects on the same drawing sheet.
* The present module attempts to follow the conventions of BS
  8888:2011 for the format of the drawing sheet and its title block,
  and for the thicknesses of lines in drawings, whereas the Automatic
  Drawing macro does not.
* In the present module, the scale of the drawings is an option that
  can be set by the user, whereas the Automatic Drawing macro
  automatically computes separate scales for its first angle projection
  set and its isometric drawing, in an attempt to produce fixed
  drawing sizes, and neither reports those computed scales to the user,
  nor automatically prints them in the title block of the drawing
  sheet.
* In the present module, the size and orientation of the drawing sheet
  are user-selectable options, whereas in the automatic drawing macro,
  they are fixed and can be changed only by editing the macro source
  code.
* In the present module, the spacing between the individual
  axonometric views is a user-selectable option, whereas in the
  Automatic Drawing module, it is fixed by an algorithm that can be
  changed only by editing the macro source code (and is sometimes
  fixed in such a way that the individual views overlap).
* In the present module, the location on the drawing sheet of the
  first angle projection set is a user-selectable option, whereas in
  the Automatic Drawing module, it is fixed by an algorithm that can
  be changed only by editing the macro source code (so too is the
  location on the drawing sheet of the isometric drawing, and they are
  sometimes fixed in such a way that the first angle projection set
  and the isometric drawing overlap).
* The present module can automatically populate the title block of its
  drawing sheet with user-supplied information, whereas the Automatic
  Drawing macro cannot.
* The present module clearly states the identity of its copyright
  holder and the licence terms under which it is released, whereas the
  Automatic Drawing macro does not.
* The Automatic Drawing macro can only add its drawing sheet to the
  currently active document, whereas the present module can add its
  drawing sheet to any document.
* The Automatic Drawing macro can only produce drawings of the
  currently selected 3D object, whereas the present module can produce
  drawings of any 3D object.

## Advantages of the Automatic Drawing macro

* The Automatic Drawing macro adds fewer extraneous
  `TechDraw::DrawViewPart` or `Drawing::FeatureViewPart` objects to
  the parent document of the drawing sheet than the present module
  (although it still adds some).
* The Automatic Drawing module can be straightforwardly launched
  either from menus and dialogue boxes in the FreeCAD GUI or from
  Python commands, whereas the present module can be straightforwardly
  launched only from Python commands.

## Neutral differences between the present module and the Automatic Drawing macro

* The present module produces a full set of six individual axonometric
  views, whereas the Automatic Drawing macro produces only three.
  This is an advantage of the present module if one is in the sphere
  of influence of the British Standards Institute, since as the author
  of the present module understands it, including all six views in a
  first angle projection set is mandatory in BS 8888:2011.  It is also
  an advantage of the present module if one's design is sufficiently
  asymmetric that it cannot be successfully manufactured from just
  three axonometric projections.  Otherwise, it is an advantage of
  the Automatic Drawing macro, which can thereby produce a less
  cluttered drawing sheet.
* The Automatic Drawing macro, in addition to the first angle
  projection set, adds an isometric drawing to its drawing sheet.
  If one actually _wants_ an isometric drawing, this is an advantage
  of the Automatic Drawing macro; however, the behaviour cannot be
  switched off (other than by editing the macro source code), so if
  one does not want an isometric drawing, it is an advantage of the
  present module.
* In the present module, the dimensions and location on the drawing
  sheet of the first angle projection symbol are user-selectable
  options, whereas in the Automatic Drawing module, they are fixed and
  can be changed only by editing the macro source code.
* The Automatic Drawing macro takes as its input 3D object a
  `Part::Feature` object, whereas the present module takes as its input
  3D object an object capable of being assigned to the `Shape` property
  of a `Part::Feature` object.

# Bugs

This module attempts to implement BS 8888:2011, which is not the
latest edition of the BS 8888 standard.

The drawings produced by the `fap` method in the
`first_angle_projection` class do not include explicit dimensions,
tolerances or labels associating part numbers with the drawings of
particular parts; some of these features may, under some
circumstances, be mandatory in BS 8888:2011.  All of these features
can be added using the GUI of the [FreeCAD Drawing Dimensioning
Workbench](https://github.com/hamish2014/FreeCAD_drawing_dimensioning),
supplied by github user hamish2014; however, the author of the present
module has been unable to find a convenient way of scripting the
Drawing Dimensioning Workbench in Python.

The `create_it` method in the `create_eights_drawing_sheet` class
doesn't trap any attempt by the user to select a combination of paper
size and orientation that doesn't exist in FreeCAD's collection of
ISO7200 templates.  When this happens, the method goes ahead and
creates a `TechDraw::DrawPage` (if the FreeCAD version under which the
module is being run is 0.19 or later) or `Drawing:FeaturePage` (if the
FreeCAD version under which the module is being run is earlier than
0.19) object, to which content can be added by other methods, but
which cannot be viewed in the FreeCAD GUI.  The only
subsequently-visible (to the user) clue as to what's wrong is that
hovering the mouse over the manifestation of the relevant drawing
sheet in the Tree View produces pop-up text "Cannot open file
path\_to\_non-existent\_template\_file.svg".

The `create_it` method in the `create_eights_drawing_sheet` class doesn't
trap any attempt by the user to insert inappropriately typed data into
the fields of the title block (e.g. drawing sheet numbers that are not
integers, creator names that are not strings, ...).

BS 8888:2011 indicates a preference for drawing scales of 1:2 and 1:5
over such intermediate scales as 1:3 or 1:4; however, this module
contains no such preference, instead making it equally easy for the
user to select any drawing scale.

BS 8888:2011 inherits its specifications for the title block of a
drawing sheet from ISO7200.  To implement these specifications, the
`create_it` method in the `create_eights_drawing_sheet` class makes
use of FreeCAD's built-in template for ISO7200 drawing sheets.
However, the layout of the title block in the FreeCAD ISO7200 template
(at least in FreeCAD version 0.15) is not identical to either of the
ISO7200 example layouts given in BS 8888:2011.  It is not clear
whether this represents:

* an error in the FreeCAD template;
* a change in the ISO7200 standard since the publication of BS
  8888:2011; or
* a degree of flexibility in ISO7200.

The `fap` method in the `first_angle_projection` class was written
assuming that the input solid shape would be positioned in such a way
that the solid shape is entirely contained in the positive-_x_,
positive-_y_, positive-_z_ octant of space, but that all three of the
planes bounding that octant are tangent to the solid shape.  When
that's not the case, the method produces sets of projections which are
not _wrong_ in any technical sense, but which do look decidedly odd.

In setting the widths of lines in the drawing to comply with BS
8888:2011, both the `put_it_in` method in the
`add_first_angle_projection_symbol` class and the `fap` method in the
`first_angle_projection` class assume that FreeCAD will interpret
floating-point numbers, assigned to the `LineWidth` and `HiddenWidth`
properties of a `TechDraw::DrawViewPart` or `Drawing::FeatureViewPart`
object, as being in millimetres.  This assumption has so far proved
correct on the systems on which the present module has been tested,
but there may be some FreeCAD configuration option that can render it
incorrect.

(This bug is fixed as long as the module is being run under FreeCAD
version 0.18.4 or later.)  The dummy documents created by the
`put_it_in` method in the `add_first_angle_projection_symbol` class
and by the `fap` method in the `first_angle_projection` class are a
waste of RAM and clutter up the GUI, and ideally should be closed just
before the respective methods exit.  Unfortunately, adding commands to
the end of the methods to close the dummy documents causes a segfault,
at least under FreeCAD 0.16 on Scientific Linux 7.3 (and in some cases
under FreeCAD 0.16 on Fedora 28).  The segfault doesn't happen under
FreeCAD 0.18.4 on Ubuntu 20.04, so the present state of the code is
that the dummy documents are closed in a conditional code segment that
is executed only if the FreeCAD version under which the module is
being run is 0.18.4 or later.

# Citing

If you use the eights module to produce published work, please cite

* Hatton, D. C. (2019). eights: BS 8888:2011 first angle projection
  drawings from FreeCAD 3D model. _J. Open Source Softw._, **4**(33),
  974-1-974-3. doi:`10.21105/joss.00974`

# References

* Dobelis, M., Polinceusz, P., Sroka-Bizon, M., Tytkowski, K.,
  Velichova, D., & Vansevicius, A. (2018). Is the constructional
  drawing an international language for engineers? In L. Cocchiarella
  (Ed.), _ICGG 2018 — proceedings of the 18th international conference
  on geometry and graphics, Advances in intelligent systems and
  computing_ (Vol. 809, pp. 1542–1552). Milan: Springer International
  Publishing. doi:`10.1007/978-3-319-95588-9_137`
* _FreeCAD version 0.15 user manual_. (n.d.). Retrieved from
  <https://github.com/FreeCAD/FreeCAD/releases/download/0.15/FreeCAD-0.15_manual.pdf>
* Hughes, N. (2013). _CAD for the workshop_. CROWOOD metalworking
  guides. Ramsbury: Crowood Press.
* Kannan, G., & Vinay, V. P. (2008). Multi-criteria decision making
  for the selection of CAD/CAM
  system. _Int. J. Interact. Des. Manuf._, **2**(3),
  151–159. doi:`10.1007/s12008-008-0045-5`
* _Macro automatic drawing_. (2016, September). World-Wide Web
  page. Retrieved from
  <https://www.freecadweb.org/wiki/Macro_Automatic_drawing>
* Magee, J., McClelland, B., & Winder, J. (2012). Current issues with
  standards in the measurement and documentation of human skeletal
  anatomy. _J. Anat._, **221**(3), 240–251.
  doi:`10.1111/j.1469-7580.2012.01535.x`
* Moitinho de Almeida, V., & Barceló, J. A. (2014). Measuring and
  describing 3D texture.  In F. Giligny, F. Djindjian, L. Costa,
  P. Moscati, & S. Robert (Eds.), _Proceedings of the 42nd annual
  conference on computer applications and quantitative methods in
  archaeology CAA 2014 — 21st century archaeology_
  (pp. 519–528). Paris: CAA International; Archaeopress.
* Quintana, V., Rivest, L., Pellerin, R., Venne, F., & Kheddouci,
  F. (2010). Will model-based definition replace engineering drawings
  throughout the product lifecycle? A global perspective from
  aerospace industry. _Comput. Ind._, **61**(5), 497–508.
  doi:`10.1016/j.compind.2010.01.005`
* Shapin, S., & Schaffer, S. (2011). _Leviathan and the air-pump:
  Hobbes, Boyle, and the experimental life_. Princeton classics
  (Paperback reissue, with a new introduction.).  Princeton: Princeton
  University Press.
* _Technical product documentation and specification BS
  8888:2011_. (2011). (Sixth edition.).  London: British Standards
  Institution.
