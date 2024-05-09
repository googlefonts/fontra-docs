---
title     : Anchors
layout    : default
permalink : /reference/canvas/glyph-editor/anchors
draft     : true
order     : 211
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../../reference">Reference</a></li>
    <li class="breadcrumb-item"><a href="../../canvas/">Canvas</a></li>
    <li class="breadcrumb-item"><a href="../glyph-editor/">Glyph editor</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

*Anchors* have a specific location (x/y) and are identified via a name. They are used usually as a reference point for components.
{: .lead }

<div class="alert alert-primary mt-3" role="alert" markdown='1'>
#### Pro tips
{: .alert-heading}
- Add/edit anchors works with **multi-source-editing**
- **Select all anchors** by entering multiple times the short cut `⌘` + `a` for Mac (or `Ctrl` + `a` for Windows)
- **Show/hide anchor names** via panel [Options](/reference/panels/options)
- **Show coordinates** via panel [Options](/reference/panels/options)
{: .mb-0 }
</div>


![]({{ site.url }}/images/canvas-glyph-editor-anchor.png){: .img-fluid }

#### Add anchor
1. **right click** where you want to add an anchor
2. select **add anchor**
3. enter name 
  - optinal: modify x and/or y
4. click **add**

![]({{ site.url }}/images/canvas-glyph-editor-anchor-add.png){: .img-fluid }

#### Edit anchor
1. **double click** the anchor
2. edit name, x or y value
3. click **edit**

![]({{ site.url }}/images/canvas-glyph-editor-anchor-edit.png){: .img-fluid }

#### Delete anchor
1. select one or more anchors
2. delete via keyboard or right click context-menu **delete selection**


#### Show/hide anchor names
1. go to panel [Options](/reference/panels/options)
2. click checkbox **Anchor names**

![]({{ site.url }}/images/canvas-glyph-editor-anchor-names.png){: .img-fluid }


#### Show/hide anchor coordinates
1. go to panel [Options](/reference/panels/options)
2. click checkbox **Coordinates**
3. select anchor(s)

![]({{ site.url }}/images/canvas-glyph-editor-anchor-coordinates.png){: .img-fluid }

Actions
-------

<table class='table table-hover'>
<tr>
<th width='35%'>action</th>
<th width='65%'>description</th>
</tr>
<tr>
<td>right click + add anchor</td>
<td>adds an anchor</td>
</tr>
<tr>
<td>right click + add anchor (multi-source-editing)</td>
<td>adds an anchor to all sources, relative to the advance width</td>
</tr>
<tr>
<td>double click an anchor</td>
<td>edit anchor</td>
</tr>
<tr>
<td>double click anchor (multi-source-editing)</td>
<td>edit anchor in all sources, eg. change anchor name in entire glyph</td>
</tr>
</table>

**Anchors** introduction
-------
<video src="{{ site.url }}/videos/canvas-glyph-editor-anchor.mp4" controls="controls" style="width: 100%; max-width: 600px">
</video>

Position **Anchors** (multi source editing)
-------
with the help of *Align and distribute objects* 
<video src="{{ site.url }}/videos/canvas-glyph-editor-anchor-position.mp4" controls="controls" style="width: 100%; max-width: 600px">
</video>

