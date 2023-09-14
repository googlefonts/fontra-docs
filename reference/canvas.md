---
title     : Canvas
layout    : default
permalink : /reference/canvas/
draft     : true
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../reference">Reference</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>


* Table of Contents
{:toc}

The canvas is where both *font previewing* and *glyph editing* takes place.


Navigation
----------

#### User interface inspired by map apps

The Fontra workspace and the UI in general are inspired by map applications such as Google Maps. 

Users of Fontra can zoom in and out of the canvas using the same [navigation tools] also found in map apps.

If you get lost in a large canvas, click on the origin point icon to bring the current glyph back to the center of the view, or to center the text preview in the canvas if no glyph is selected.

#### Other ways to zoom in and out

Zooming in and out is also possible with the usual keyboard shortcuts ⌘ + and ⌘ -, and with the mouse wheel or trackpad.

#### Navigating through the designspace

When working with designspace, you can jump quickly from one source to another using the short keys ⌘ ↑ (previous source) and ⌘ ↓ (next source).


Glyph selection
---------------

Individual glyphs can be selected and deselected by clicking with the [pointer tool]. Only one glyph can be selected at a time.

Attributes of the selected glyph are visible in the [glyph info panel] (name, width, unicode, components) and in the [designspace panel] (axes, sources).


Type preview
------------

The preview string can be edited in the [preview text panel]. Unicode characters and line breaks are supported.


Display options
---------------

#### Displaying other sources

...

#### Displaying a reference font

...

#### Light and dark color schemes

...

#### Full screen mode

...


Glyph editing
-------------

#### Activating editing mode

Double-click a glyph to activate the *editing mode* for that glyph. In place of a 'black' preview shape, you will now see an outline representation of the bézier contours with points and handles.

#### Measuring distances

The [measurement tool] can be used to measure distances of certain aspects of the shapes in real-time.

<div class="alert alert-warning" role="alert" markdown='1'>
<i class="bi bi-exclamation-circle me-1"></i> If you don't need the measurement line anymore, you can disable it in the [options panel].
{: .mb-0 }
</div>

#### Editing contours and components

Use the [pointer tool] to select and move contours, segments points, handles, components.

Use the [pen tool] to draw new contours and add points to existing contours.

Fontra supports cubic and quadratics outlines. Quadratic outlines can be activated in the [options panel].

You can use the standard keyboard shortcuts ⌘ Z to undo the last actions, and ⇧ ⌘ Z to redo them.

<div class="alert alert-warning" role="alert" markdown='1'>
<i class="bi bi-exclamation-circle me-1"></i> Fontra does not have a *save* command – every change is saved!
{: .mb-0 }
</div>

#### Editing glyph metrics

The width of the glyph can be changed in the [glyph info panel].

<div class="alert alert-warning" role="alert" markdown='1'>
<i class="bi bi-exclamation-circle me-1"></i> It is currently not possible to change glyph margins interactively.
{: .mb-0 }
</div>

<div class="alert alert-warning" role="alert" markdown='1'>
<i class="bi bi-exclamation-circle me-1"></i> 
The name and unicode value of a glyph also cannot be changed.
{: .mb-0 }
</div>

#### Editing components

Component functions are available from the [contextual menu], for example creating new components or decomposing existing ones.

#### Editing anchors

<div class="alert alert-warning" role="alert" markdown='1'>
<i class="bi bi-exclamation-circle me-1"></i> Editing anchors is supported in Fontra yet. Existing anchors are not displayed.
{: .mb-0 }
</div>


#### Creating a new source for the current glyph

...


[preview text panel]: #
[glyph info panel]: # 
[designspace panel]: #
[options panel]: # 
[navigation tools]: #
[pointer tool]: #
[pen tool]: #
[measurement tool]: #
[contextual menu]: #
