---
title     : Installing Fontra Pak on your computer
layout    : default
permalink : /how-tos/installing-fontra-pak/
draft     : true
---

<nav aria-label="breadcrumb">
  <ol class="breadcrumb small">
    <li class="breadcrumb-item"><a href="{{ site.url }}">Index</a></li>
    <li class="breadcrumb-item"><a href="../../how-tos">How-Tos</a></li>
    <li class="breadcrumb-item active" aria-current="page">{{ page.title }}</li>
  </ol>
</nav>

Fontra can be installed locally using [Fontra Pak], a self-contained application which allows you to edit local files in your browser using Fontra. The installer is available only for **macOS** and **Windows**. Linux users can [build Fontra from source].

Follow the steps below to install Fontra on your machine.

1. Sign in to [GitHub] to be able to download.

2. Go to the [Actions] page of the Fontra Pak repository.

3. Click on the topmost “Build Application” link to go the worflow page.

    ![]({{ site.url }}/images/fontra-actions-build.png){: .img-fluid}

4. In the *Artifacts* section of that page, choose the appropriate installer for your platform and click to download.

    ![]({{ site.url }}/images/fontra-download-installer.png){: .img-fluid}

5. Unzip and double-click the package, then drag the Fontra Pak icon into the *Applications* folder to conclude the installation.

    ![]({{ site.url }}/images/fontra-pak-installer.png){: .img-fluid}


[Fontra Pak]: http://github.com/googlefonts/fontra-pak
[build Fontra from source]: ../building-fontra-from-source
[GitHub]: http://github.com
[Actions]: http://github.com/googlefonts/fontra-pak/actions

