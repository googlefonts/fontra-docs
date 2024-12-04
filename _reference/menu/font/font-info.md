---
title     : Font Info
layout    : default
permalink : /reference/menu/font/font-info
draft     : true
order     : 641
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

*Font Info* contains various general font informations. You can access it via *Font* -> *Font Info* menu.
{: .lead }

![]({{ site.url }}/images/font-font-info.png){: .img-fluid }

<table class='table table-hover'>
<tr>
<th width='35%'>Font Info</th>
<th width='65%'>Description</th>
</tr>
<tr>
<td>Family Name</td>
<td>The fonts family name as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid1' target="_blank">OT spec Name ID 1</a></td>
</tr>
<tr>
<td>Copyright</td>
<td>The fonts copyright as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid0' target="_blank">OT spec Name ID 0</a></td>
</tr>
<tr>
<td>Trademark</td>
<td>The fonts trademark as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid7' target="_blank">OT spec Name ID 7</a></td>
</tr>
<tr>
<td>Description</td>
<td>The fonts description as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid10' target="_blank">OT spec Name ID 10</a></td>
</tr>
<tr>
<td>Sample Text</td>
<td>The fonts sampel text as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid19' target="_blank">OT spec Name ID 19</a></td>
</tr>
<tr>
<td>Designer</td>
<td>The fonts designer name(s) as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid9' target="_blank">OT spec Name ID 9</a></td>
</tr>
<tr>
<td>Designer URL</td>
<td>The fonts designer URL as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid12' target="_blank">OT spec Name ID 12</a></td>
</tr>
<tr>
<td>Manufacturer</td>
<td>The fonts manufacturer as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid8' target="_blank">OT spec Name ID 8</a></td>
</tr>
<tr>
<td>Manufacturer URL</td>
<td>The fonts manufacturer URL as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid11' target="_blank">OT spec Name ID 11</a></td>
</tr>
<tr>
<td>License description</td>
<td>The fonts license description as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid13' target="_blank">OT spec Name ID 13</a></td>
</tr>
<tr>
<td>License info URL</td>
<td>The fonts license info URL as a string. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/name#nid14' target="_blank">OT spec Name ID 14</a></td>
</tr>
<tr>
<td>Vendor ID</td>
<td>The Vendor ID must be exactly 4 characters long. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/os2#achvendid' target="_blank">OT spec Vendor ID</a></td>
</tr>
<tr>
<td>Major Version</td>
<td>The fonts major version number</td>
</tr>
<tr>
<td>Minor Version</td>
<td>The fonts minor version number</td>
</tr>
<tr>
<td>Units Per Em</td>
<td>The fonts UPM is typically set to 1000, but must be at least a value from 16 to 16384. Please see: <a href='https://learn.microsoft.com/en-us/typography/opentype/spec/head' target="_blank">OT spec head table unitsPerEm</a></td>
</tr>
</table>
