---
title: Panels
layout: default
permalink: /reference/panels
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="/">Index</a></li>
    <li class="breadcrumb-item"><a href="../reference">Reference</a></li>
    <li class="breadcrumb-item active" aria-current="page">Panels</li>
  </ol>
</nav>

### Overview

| icon | panel             | description                                          |
|------|-------------------|------------------------------------------------------|
|      | preview text      | edit the glyph preview string                        |
|      | find glyph        | search and choose specific glyphs in the font        |
|      | designspace       | access variation axes and sources in the designspace |
|      | options           | adjust various app settings                          |
|      | reference font    | choose a reference font to display in the background |
|      | glyph info        | view and edit glyph attributes                       |
{: .table .table-hover .mb-4 }

### Preview text

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-text.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
preview string
: type some text to be used in the preview

text alignment
: choose between left-, center-, or right-aligned text
</div>
</div>

### Find glyph

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-glyphs.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
search string
: type a string to search in glyph names

glyph list
: a list of all glyphs in the font or designspace
</div>
</div>

### Designspace

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-designspace.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
variation axes
: move the sliders to navigate around the font's designspace 

restore defaults
: click the icon to restore all axes to their default location

edit local axes
: open a pop-up window with options to adjust local axes (?)

- - -

sources
: a list of all sources available for the current glyph

on
: uncheck to remove source from the interpolation for this glyph

bg
: check to show a preview of this source in the background

plus
: add a new source at a new location for the current glyph

minus
: delete current glyph in the selected source 
</div>
</div>

### Options

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-options.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
glyph editor appearance
: ^
  - Units-per-em grid
  - Reference font
  - Sidebearings for non-editing glyphs
  - CJK design frame
  - Baseline
  - Drag crosshair
  - Drag "ghost" path
  - Show coordinates
  - Power ruler

vlipboard format
: ^
  - GLIF (Gliph Interchange Format)
  - SVG (Scaleable Vector Graphics)
  - JSON (JavaScript Object Notation)

rxperimental features
: ^
  - Scaling edit tool behavior
  - Pen tool draws quadratics

theme settings
: ^
  - Automatic (use OS setting)
  - Light
  - Dark

version info
: ^
  - Server info
  - Fontra version
  - Startup time
  - View plugins
  - Project manager

</div>
</div>



### Reference font

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-reference.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
reference fonts
: drag and drop binary fonts to add them to list

custom character
: ...

language code
: ...
</div>
</div>



### Glyph info

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-info.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
glyph info
: ^
  - glyph name
  - unicode value
  - unicode character
  - advance width

dimensions
: ^
  - glyph bounds

components info
: ^
  - base glyph
  - transformation matrix
</div>
</div>