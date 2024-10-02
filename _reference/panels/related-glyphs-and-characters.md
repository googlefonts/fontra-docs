---
title     : Related Glyphs & Characters
layout    : default
permalink : /reference/panels/related-glyphs-and-characters
draft     : true
order     : 509
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../../reference">Reference</a></li>
    <li class="breadcrumb-item"><a href="../panels">Panels</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

<div class='row'>
<div class='col-md' markdown='1'>
![]({{ site.url }}/images/panel-related-glyphs-and-characters-dark.png){: .img-fluid .py-2 }
</div>
<div class='col-md' markdown='1'>
If you select a glyph you get different relationships.

Alternate glyphs
: ^
  - Looks for glyphs which have the same glyph name, but with a different extension.

Glyphs using this glyph as a component
: ^
  - These are glyphs within this font which use the selected glyph as a component
  - example: a -> aacute, abreve, aring, adieresis, ...

Characters that decompose with this character
: ^
  - We look at unicode decomposition information
  - Can a character be represented as a sequence of other characters?!

Components used by this glyph
: ^
  - The components as defined in the font (based on glyph information) 
  - example: onequarter -> one.numerator, four.numerator, fraction

Character decomposition
: ^
  - Based on unicode information 
  - example: onequarter -> one, four, fraction

</div>
</div>


- - -

*Related Glyphs & Characters Panel* introduction
-------
<video src="{{ site.url }}/videos/related-glyphs-and-characters.mp4" controls="controls" style="width: 100%; max-width: 600px">
</video>