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
<td>Name</td>
<td>The axis <b>Name</b> identifies the axis</td>
</tr>
<tr>
<td>OT tag</td>
<td>The axis tag must be 4 characters long. <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags' target="_blank">Registered OT tags</a>. Non-registered tags must be written in all uppercase.</td>
</tr>
<tr>
<td>UI Name</td>
<td><b>UI Name</b> is the Label how it will be visible to the end user</td>
</tr>
</table>

Note: **Name** and **UI Name** are often the same.
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
<td>Either <b>Continuous</b> or <b>Descrete</b></td>
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
<td>The value of a style (for example 400 for <b>Regular</b>)</td>
</tr>
<tr>
<td>Min</td>
<td>The minumum value of a style (for example 350 for <b>Regular</b>)</td>
</tr>
<tr>
<td>Max</td>
<td>The maximum value of a style (for example 450 for <b>Regular</b>)</td>
</tr>
<tr>
<td>Linked</td>
<td>The linked value of a style (for example 700 for <b>Regular</b>, so it's linked with <b>Bold</b>)</td>
</tr>
<tr>
<td>Elidable</td>
<td>A checkbox which shows that the name should not be displayed (*Upright* might be an elidable name in the *Italic* axis)</td>
</tr>
</table>



### Links

- [Google Fonts: Axis (in variable fonts)](https://fonts.google.com/knowledge/glossary/axis_in_variable_fonts)
