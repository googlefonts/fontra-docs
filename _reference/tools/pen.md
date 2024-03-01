---
title     : Pen tool
layout    : default
permalink : /reference/tools/pen
draft     : true
order     : 6
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../../reference">Reference</a></li>
    <li class="breadcrumb-item"><a href="../tools/">Tools</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

The *Pen tool* allows you to draw new bézier contours and add points to existing ones.
{: .lead }

To activate the tool, click on the *Pen tool* icon <img height="20" src="{{ site.url }}/images/icons/pointeradd.svg"> in the toolbar, or use the short key `2`.

Actions
-------

#### Draw outline

<table class='table table-hover'>
<tr>
<th width='35%'>action</th>
<th width='65%'>description</th>
</tr>
<tr>
<td>click</td>
<td>Adds new point</td>
</tr>
<tr>
<td>⇧ + click</td>
<td>Adds new point (straight line) snapping to 0/45/90 degrees</td>
</tr>
<tr>
<td>click + drag</td>
<td>Adds new point with handle</td>
</tr>
<tr>
<td>click + drag + ⇧</td>
<td>Adds new point with handle snapping to 0/45/90 degrees</td>
</tr>
<tr>
<td>⇧ + e</td>
<td>Toggles <a href="{{ site.url }}/reference/tools/pen#pen-tool-multi-source-editing">multi source editing</a></td>
</tr>
</table>

*Pen tool* introduction
-------
<video src="{{ site.url }}/videos/pen-tool-introduction.mp4" controls="controls" style="width: 100%; max-width: 600px">
</video>

*Pen tool* multi source editing
-------
<video src="{{ site.url }}/videos/pen-tool-multi-source-editing.mp4" controls="controls" style="width: 100%; max-width: 600px">
</video>


