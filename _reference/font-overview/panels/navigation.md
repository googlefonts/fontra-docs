---
title     : Navigation Font Overview
layout    : default
permalink : /reference/font-overview/panels/navigation
draft     : true
order     : 4111
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="{{ site.url }}/reference">Reference</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/font-overview-navigation.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>

##### Search Glyphs

Search for glyphs containing the entered text, for example *grave* shows *Agrave*, *Egrave*, *Igrave*, etc.

- - -

##### Location

Dropdown
: Choose a **font source** to navigate to a location in the design space

Slider(s)
: Use the sliders to navigate continuously within the design space


- - -

##### Group by

Organize the glyphs of the font by one or many of the following categories.

Script
: Group by **script** (a script is not a language: Cyrillic ≠ Bulgarian) 

Block
: sort by **unicode blocks**

Case
: sort by **uppercase** (followed by *lowercase*) glyphs

Category
: sort by **category**, for example: Letter, Number, Punctuation, etc.

Sub-category
: sort by **sub-category**, for example: Superscript, Fraction, Quote, etc.

Glyph name extension
: sort by **extension**, for example **.case**, **.numerator**, etc.


<div class="alert alert-primary mt-3" role="alert" markdown='1'>
#### Pro tip: 
{: .alert-heading}
- Try: Group by **Category** + **Sub-Category**.
{: .mb-0 }
</div>

- - -

##### Project glyph sets

Project specific glyph sets (activate one or many via checkboxes).

This font's glyphs
: shows **all glyphs** of the font project

<img height="30" src='{{ site.url }}/images/icons/plus.svg' />*
: add a new glyph set to this specific font project

- - -

##### My glyph sets

Fontra specific glyph sets (activate one or many via checkboxes).

<img height="30" src='{{ site.url }}/images/icons/plus.svg' />*
: add a new glyph set to your Fontra environment 

<img src='{{ site.url }}/images/icons/pencil.svg' />
: click on the icon to show the **context menu**


- - -

\* a glyph set must be publicly available (for example via github)