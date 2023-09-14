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


### Gestures

| gesture              | description          |
|----------------------|----------------------|
| swipe with 2 fingers | pan canvas           |


### Short keys 

| keys | description          |
|------|----------------------|
| ⌘ +  | zoom in              |
| ⌘ -  | zoom out             |
| ⌘ 0  | fit current glyph    |
| ⌘ A  | select all points    |


<!--
Navigation
----------

The Fontra workspace and the UI in general are inspired by map applications such as Google Maps. Users can zoom in and out of the canvas using the same tools and gestures which are commonly used in map apps.

Zooming in and out is also possible with the usual keyboard shortcuts ⌘ + and ⌘ -, or with the mouse wheel or trackpad.



Glyph selection
---------------

Use the [pointer tool] to select / deselect glyphs.

Only one glyph can be selected at a time. Attributes of the glyph are loaded into the [glyph info panel](#) and into the [designspace panel](#).


Type preview
------------

The preview string can be edited in the [preview text panel]. 


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

Use the [measurement tool] to measure distances between points along the contour.

#### Editing contours and components

Use the [pointer tool] to select and move contours, segments points, handles, components.

Use the [pen tool] to draw new contours and add points to existing contours.

Fontra supports cubic and quadratic outlines. Quadratic outlines can be activated in the [options panel].

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

#### Editing glyph attributes

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


Designspace
-----------

#### Navigating through the designspace

When working with designspace, you can jump quickly from one source to another using the short keys ⌘ ↑ (previous source) and ⌘ ↓ (next source).



[preview text panel]: #
[glyph info panel]: # 
[designspace panel]: #
[options panel]: # 
[navigation tools]: #
[pointer tool]: #
[pen tool]: #
[measurement tool]: #
[contextual menu]: #

-->