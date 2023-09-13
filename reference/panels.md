---
title: Panels
layout: default
permalink: /reference/panels/
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../reference">Reference</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

### Overview

<table class="table table-hover mb-4">
<tr>
<th>icon</th>
<th>tool</th>
<th>description</th>
<th>short key</th>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/texttool.svg"></td>
<td>preview text</td>
<td>edit the glyph preview string</td>
<td></td>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/magnifyingglass.svg"></td>
<td>find glyph</td>
<td>search and choose specific glyphs in the font</td>
<td>⌘ f</td>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/sliders.svg"></td>
<td>designspace</td>
<td>access variation axes and sources in the designspace</td>
<td></td>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/gear.svg"></td>
<td>options</td>
<td>adjust various app settings</td>
<td></td>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/reference.svg"></td>
<td>reference font</td>
<td>choose a reference font to display in the background</td>
<td></td>
</tr>
<tr>
<td><img height="30" src="{{ site.url }}/images/icons/info.svg"></td>
<td>glyph info</td>
<td>view and edit glyph attributes</td>
<td>⌘ i</td>
</tr>
</table>

<!--
| icon | panel             | description                                          |
|------|-------------------|------------------------------------------------------|
|      | preview text      | edit the glyph preview string                        |
|      | find glyph        | search and choose specific glyphs in the font        |
|      | designspace       | access variation axes and sources in the designspace |
|      | options           | adjust various app settings                          |
|      | reference font    | choose a reference font to display in the background |
|      | glyph info        | view and edit glyph attributes                       |
{: .table .table-hover .mb-4 }
-->

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

clipboard format
: ^
  - GLIF (Gliph Interchange Format)
  - SVG (Scaleable Vector Graphics)
  - JSON (JavaScript Object Notation)

experimental features
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