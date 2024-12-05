---
title     : Axes
layout    : default
permalink : /reference/menu/font/axes
draft     : true
order     : 642
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="{{ site.url }}/reference">Reference</a></li>
    <li class="breadcrumb-item"><a href="{{ site.url }}/reference/menu">Menu</a></li>
    <li class="breadcrumb-item"><a href="{{ site.url }}/reference/menu/font">Font</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

Fontra's approach is *variable-first*, therefore it's most likey that you will add at least one font axis. The most common one is probably *Weight*. Add a new axis via the *New axis...* button. 
{: .lead }

<div class="alert alert-primary mt-3" role="alert" markdown='1'>
#### Pro tips: 
{: .alert-heading}
- Before you create a new axis we recommend to have a look at **[Designspace](/explanations/designspace/)**, first.
- Change the order of the axes via *drag and drop*.
{: .mb-0 }
</div>

![]({{ site.url }}/images/font-axes.png){: .img-fluid }

Names
-------

<table class='table table-hover'>
<tr>
<th width='35%'>Entry</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Name<a href="#marker_1">¹</a></td>
<td>The axis name identifies the axis</td>
</tr>
<tr>
<td>OT tag</td>
<td>The axis tag <b>must be 4 characters</b> long. <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags' target="_blank">Registered OT tags</a>. Non-registered tags must be written in all uppercase.</td>
</tr>
<tr>
<td>UI Name<a href="#marker_1">¹</a></td>
<td>UI Name is <b>the Label how it will be visible</b> to the end user</td>
</tr>
</table>


<span id='marker_1'>¹Note: **Name** and **UI Name** are often the same.</span>
{% comment %}
For more please see: https://github.com/googlefonts/fontra-docs/pull/77#issuecomment-2518494551
{% endcomment %}

Range
-------

<table class='table table-hover'>
<tr>
<th width='35%'>Entry</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Axis Type</td>
<td>Either <b>Continuous<a href="#marker_2">²</a></b> or <b>Discrete<a href="#marker_3">³</a></b></td>
</tr>
</table>

<span id='marker_2'>²Range: Axis type *Continuous*</span>
-------

<table class='table table-hover'>
<tr>
<th width='35%'>Entry</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Minimum</td>
<td>the minimum value of the axis (for example: <b>100 for Thin</b> in a Weight axis)</td>
</tr>
<tr>
<td>Default</td>
<td>the default value of the axis (for example: <b>400 for Regular</b> in a Weight axis)</td>
</tr>
<tr>
<td>Maximum</td>
<td>the maximum value of the axis (for example: <b>900 for Black</b> in a Weight axis)</td>
</tr>
</table>

<span id='marker_3'>³Range: Axis type *Discrete*</span>
-------

<table class='table table-hover'>
<tr>
<th width='35%'>Entry</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Values</td>
<td>a list of values for the axis (for example: <b>0 for Upright</b> and <b>1 for Italic</b> for Italic axis)</td>
</tr>
<tr>
<td>Default</td>
<td>the default value of the axis (for example: <b>0 for Upright</b> in the Italic axis)</td>
</tr>
</table>

Mapping graph
-------

The mapping graph visualizes the axis mapping.

Mapping list
-------

Specify a new mapping of the axis values (also known as avar-mapping). Add a new mapping with the plus-button or remove a mapping with the minus-button.


Axis Values
-------

Add a new axis value with plus-button or remove it via minus-button (keyword: STAT table).

<table class='table table-hover'>
<tr>
<th width='35%'>Entry</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Name</td>
<td>The name of a specifed style (for example <b>Regular</b>)</td>
</tr>
<tr>
<td>Value</td>
<td>The value of a style (for example <b>400</b> for Regular)</td>
</tr>
<tr>
<td>Min</td>
<td>The minumum value of a style (for example <b>350</b> for Regular)</td>
</tr>
<tr>
<td>Max</td>
<td>The maximum value of a style (for example <b>450</b> for Regular)</td>
</tr>
<tr>
<td>Linked</td>
<td>The linked value of a style (for example <b>700</b> for Regular, so it's <b>linked with Bold</b>)</td>
</tr>
<tr>
<td>Elidable</td>
<td>A checkbox which shows that the name should not be displayed (<b>Upright might be an elidable</b> name in the Italic axis)</td>
</tr>
</table>



### Links

- [Google Fonts: Axis (in variable fonts)](https://fonts.google.com/knowledge/glossary/axis_in_variable_fonts)
