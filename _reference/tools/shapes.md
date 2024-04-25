---
title     : Shape tool
layout    : default
permalink : /reference/tools/shapes
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

The *Shape tool* allows you to draw a new bézier based rectanlge or ellipse.
{: .lead }

To activate the tool, click on the *Shape tool* icon <img height="20" src="{{ site.url }}/images/icons/square-plus-2.svg"> in the toolbar, or use the short key `3`.
With *hold click* give you access to the dropdown menu to switch between the *rectangle tool* <img height="20" src="{{ site.url }}/images/icons/square-plus-2.svg"> and the *ellipse tool* <img height="20" src="{{ site.url }}/images/icons/circle-plus-2.svg">.

Actions
-------

#### Draw shape

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


