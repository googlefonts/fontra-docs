---
title     : Designspace
layout    : default
permalink : /explanations/designspace/
draft     : true
order     : 901
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../explanations">Explanations</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

We recommend to spend some time with setting up your designspace, before start a new typeface.
{: .lead }

Question you may ask yourself before you start with a new typeface:
- What axes do your font project will end up with?
  - [Registerd axes](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags) like *Weight*, *Width*, *Italic*, *Optical size*
  - or even a non-registered axes?
- What ranges will these axes have?
  - maybe *Weight* from 100 to 900 (Thin to Black)
  - maybe *Width* from 75 to 100 (Consended to Normal)
- Do you plan to have *Italics*?
  - Are the *Italics* real *Italics*
  - or are they interpolatable with the uprights, like Slanted?
- etc.

Once you have sketched out your designspace, you're ready to create your [font axes]({{ site.url }}/reference/menu/font/axes).


### Links

- [Google Fonts: Designspace](https://fonts.google.com/knowledge/glossary/designspace)
- [fonttools: designspaceLib](https://fonttools.readthedocs.io/en/latest/designspaceLib/)
