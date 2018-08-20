---
title: 'eights: BS 8888:2011 first angle projection drawings from FreeCAD 3D model'
tags:
  - Python
  - computer aided design
  - engineering drawings
  - standards compliance
authors:
  - name: Daniel C. Hatton
    orcid: 0000-0002-4585-3336
    affiliation: "1" # (Multiple affiliations must be quoted)
affiliations:
 - name: Lecturer in Mechanical and Marine Engineering, Autonomous Marine Systems Group, School of Engineering, University of Plymouth
   index: 1
date: "12 August 2018"
bibliography: paper.bib
---

# Summary

eights.py is a Python module intended for use with the open-source
three-dimensional (3D) computer-aided design (CAD) package FreeCAD
[@a:1:FVU].  The module automates the construction of a page of
two-dimensional (2D) axonometric drawings in first angle projection,
in a style consistent (to the best of the module author's ability)
with the BS 8888:2011 standard [@a:2011:TPD].

The module includes:

* a class whose purpose is to provide a method which adds, to an
  existing FreeCAD document, a drawing sheet object whose formatting
  is intended to be consistent with the BS 8888:2011 standard, and
  populates the title block of the sheet, again in a way intended to
  be consistent with BS 8888:2011;
* a class whose purpose is to provide a method which adds the standard
  BS 8888:2011 symbol, indicating that a set of drawings are in first
  angle projection, to an existing FreeCAD drawing sheet object; and
* a class whose purpose is to provide a method which takes any
  existing FreeCAD 3D shape object, and adds a set of axonometric
  drawings of that shape, in first angle projection, to an existing
  FreeCAD drawing sheet object, following the conventions in BS
  8888:2011.

Also supplied with the module are a detailed documentation file, and
three example files illustrating its application to particular 3D CAD
models.

# Statement of need

The creative process behind detailed engineering design now typically
takes place in 3D CAD packages [@Quintana:2010:WMB].  However, for
this creative process actually to lead to an embodiment of the design
being manufactured, this creative process must be followed by
communication of the content of the design to a manufacturing
facility.  There are two necessary requirements for success: firstly,
the communication must include information on all those aspects of the
design that are necessary to complete manufacture, and to verify by
inspection that the completed, manufactured artefact matches the
design [@Quintana:2010:WMB]; secondly, the communication must be in a
well-defined (usually graphical) language, so that it can be
understood at the manufacturing facility in a way that permits
successful manufacturing and inspection [@Quintana:2010:WMB;
@Dobelis:2018:ICD].  The drive to meet both of these requirements has
led to the development of published standards for design communication
[@Dobelis:2018:ICD], of which BS 8888:2011 [@a:2011:TPD] is one.
These standards are in a very advanced state of maturity for 2D
engineering drawings, but despite efforts in recent years to develop
similar standards for 3D models, the standards for 3D models remain
somewhat less mature [@Quintana:2010:WMB].  As a result, 2D drawings
remain a crucial medium for communication of design information to
manufacturing facilities, and possessing the capability for automated
generation of standards-compliant 2D drawings from a 3D model is an
important criterion by which the technical quality of 3D CAD software
packages is assessed [@Kannan:2008:MCD; @Hughes:2013:CW].  Hence, by
automating the process of producing certain standards-compliant 2D
drawings, the eights module offers the opportunity for the FreeCAD CAD
package [@a:1:FVU] to be more favourably assessed against this
criterion in future.

One automated tool, for generating 2D drawings in first angle
projection from a 3D model in FreeCAD, already exists: the FreeCAD
Automatic Drawing Macro [@a:2016:ADM].  A full analysis of the relative
advantages and disadvantages of the Automatic Drawing Macro, and the
eights module announced here, can be found in the documentation file
of the eights module.  For the purposes of this statement of need, it
is sufficient to mention two of the relative disadvantages of the
Automatic Drawing Macro:

* the Automatic Drawing Macro does not attempt to comply with BS 8888
  as regards the format of the drawing sheet and its title block;
* the Automatic Drawing Macro does not offer the ability to include
  first angle projection sets for multiple 3D objects on the same
  drawing sheet.

# Acknowledgements

I would like to thank Dr. Frank Abraham, for guidance on issues of the
interface between 3D CAD and standards-compliant 2D manufacturing
drawings; and Mrs. Barbara Fuller, Dr. Alison Raby, Dr. Richard
Thompson, Prof. Kevin Jones, and Dr. Justin Rigden, for assistance
with navigating through the regulatory and intellectual-property
issues associated with the public release of this software.

# References
