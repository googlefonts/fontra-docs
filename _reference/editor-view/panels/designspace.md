---
title     : Designspace
layout    : default
permalink : /reference/editor-view/panels/designspace
draft     : true
order     : 4243
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="{{ site.url }}/reference">Reference</a></li>
    <li class="breadcrumb-item"><a href="../panels">Panels</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-designspace.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
##### variation axes

interactive controls for all variation axes in the designspace

sliders
: move the knobs to navigate around the font's designspace 

labels
: slider values indicate the current location at that axis

<img src='{{ site.url }}/images/icons/refresh.svg' /> restore defaults
: click to restore all axes to their default location

<img src='{{ site.url }}/images/icons/tool.svg' /> edit local axes
: open a pop-up window to adjust local axes (?)

- - -

##### sources

a list of all sources available for the current glyph

<img src='{{ site.url }}/images/icons/circle-dot.svg' /> on
: uncheck to remove source from the interpolation for this glyph

<img src='{{ site.url }}/images/icons/bug.svg' /> bug
: indicates that this source is incompatible for interpolation

<img src='{{ site.url }}/images/icons/eye.svg' /> bg (background)
: show/hide this source in the background while editing

<img src='{{ site.url }}/images/icons/antenna-bars-4.svg' /> bars
: displays the influence of this source in the current location

<img src='{{ site.url }}/images/icons/plus.svg' height='20' /> plus
: add a new source at a new location for the current glyph

<img src='{{ site.url }}/images/icons/minus.svg' height='20' /> minus
: delete current glyph in the selected source 
</div>
</div>