# UC-XROMM

The RCC is working with [Callum Ross](http://pondside.uchicago.edu/oba/faculty/ross_c.html) and [his lab](http://rosslab.uchicago.edu/) to streamline the
the collection and publication of [XROMM](http://www.xromm.org/) (X-ray Reconstruction of Moving Morphology) datasets.  The Ross Lab would like to send trial data from their [motion capture station](http://www.xcitex.com/procapture-motion-capture-systems.php) to Midway for cataloging in a locally-hosted [XMA (X-ray Motion Analysis) Portal](http://xmaportal.org/).

Our initial efforts will be focused on the [packaging](packaging.md) of study/trial data (both data files and associated metadata) and towards streamling the transfer of such "datapackages" to Midway.  See [this poster](https://github.com/rcc-uchicago/uc-xromm-poster/blob/master/poster.pdf?raw=true) for a quick, high-level overview of the project and its objectives.

The RCC will is hosting a testbed instance of the XMA Portal at [`xromm.rcc.uchicago.edu`](http://xromm.rcc.uchicago.edu/)


## Background

XROMM is a 3D imaging technology for visualizing and analyzing rapid skeletal movement *in vivo*. It combines three-dimensional models of bone morphology with motion data from biplanar x-ray video to create highly accurate re-animations of skeletal movement.

Bone motion data comes from two high-speed, biplanar x-ray movies.  Bone morphology data comes from a 3D computer model of the bone surfaces (derived from CT, laser scanning, or MRI). This motion and shape data can then be used together to generate an XROMM animation.  Rigid body kinematics inferred from the x-ray movies are applied to the skeletal models to re-animate the actual movement that was performed by the individual subject at the time of recording.

See Brown's [XROMM site](http://www.xromm.org/) for additional details on this particular method of analyzing skeletal kinematics.

See our [notes](portal.md) for an overview of the XMA portal.

The XMA Portal source files are available via [a private repo](https://github.com/rcc-uchicago/xma-portal).  Contact [@joyrexus](https://github.com/joyrexus) for access.


**xhub** is a simple web service currently being used to persist [uc-xromm](https://github.com/rcc-uchicago/uc-xromm)-related study data.  It functions as a web service for the [`xpub`](https://github.com/rcc-uchicago/xpub) client, storing/retrieving the JSON-encoded metadata sent/requested by the client.

## Players

#### Ross Lab

* [Callum Ross](http://pondside.uchicago.edu/oba/faculty/ross_c.html) (PI and Project Lead)
* [Fritzie Arce](http://rosslab.uchicago.edu/Members/fritziearce/fritzie-arces-home-page) (Postdoc)
* [Kazutaka Takahashi](http://home.uchicago.edu/~kazutaka/) (Postdoc)
* Courtney Orsbon

#### RCC

* [Jason Voigt](https://github.com/joyrexus) (current point man, working remotely as of Aug 16)
* [Simon Jacobs](https://github.com/sdjacobs) (local point man)
* Richard Williams (will work in close liaison with the Ross Lab)
* [Robin Weiss](https://github.com/RobinWeiss)

#### Brown / XMA Portal

* Kia Huffman ([XMA Portal](http://xmaportal.org/) admin)
