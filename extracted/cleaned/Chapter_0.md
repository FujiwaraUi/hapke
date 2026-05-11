## BRUCE HAPKE

# Theory of Reflectance and Emittance Spectroscopy

<!-- IMAGE: _page_0_Picture_2.jpeg -->

# THEORY OF REFLECTANCE AND EMITTANCE SPECTROSCOPY

Reflectance and emittance spectroscopy have become increasingly important tools in remote sensing, and have been employed in virtually all recent planetary spacecraft missions. They are primarily used to measure properties of disordered materials, especially in the interpretation of remote observations of the surfaces of the Earth and other terrestrial planets.

*Theory of Reflectance and Emittance Spectroscopy* gives a quantitative treatment of the physics of the interaction of electromagnetic radiation with particulate media, such as powders and soils. Subjects covered include electromagnetic wave propagation, single particle scattering, diffuse reflectance, thermal emittance, and polarization. This new edition has been updated and expanded to include: extension of the equivalent slab model of irregular particle scattering to include particle phase functions and coated particles; a quantitative treatment of the effects of porosity; a detailed discussion of the coherent backscatter opposition effect, including polarization; a quantitative treatment of simultaneous transport of energy within the medium by conduction and radiation; and lists of relevant databases and software.

With a strong emphasis on physical insights, this book is an essential reference for research scientists, engineers, and advanced students of planetary remote sensing.

Bruce Hapke is Professor Emeritus of Geology and Planetary Science at the University of Pittsburgh, where he continues to study various bodies of the solar system. He was principal investigator for the analysis of lunar samples and was associated with several other NASA missions, to Mercury, Mars, Saturn, and the outer solar system. He is a Fellow of the American Geophysical Union and was awarded the Kuiper Prize by the Division for Planetary Sciences of the American Astronomical Society for "outstanding contributions to planetary science." He has an asteroid *3549 Hapke* and a mineral *hapkeite* named in his honor.

# THEORY OF REFLECTANCE AND EMITTANCE SPECTROSCOPY

*Second Edition*

## BRUCE HAPKE

*Department of Geology and Planetary Science University of Pittsburgh*

<!-- IMAGE: _page_3_Picture_4.jpeg -->

#### cambridge university press

Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore, São Paulo, Delhi, Tokyo, Mexico City

Cambridge University Press The Edinburgh Building, Cambridge CB2 8RU, UK

Published in the United States of America by Cambridge University Press, New York

[www.cambridge.org](http://www.cambridge.org) Information on this title: [www.cambridge.org/9780521883498](http://www.cambridge.org/9780521883498)

© Bruce Hapke 2012

This publication is in copyright. Subject to statutory exception and to the provisions of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published 2012

Printed in the United Kingdom at the University Press, Cambridge

*A catalogue record for this publication is available from the British Library*

*Library of Congress Cataloging in Publication data* Hapke, Bruce.

Theory of reflectance and emittance spectroscopy / Bruce Hapke. – 2nd ed.

p. cm.

Includes bibliographical references and index.

ISBN 978-0-521-88349-8

1. Reflectance spectroscopy. 2. Emission spectroscopy. 3. Moon–Surface–Spectra. I. Title. QC454.R4H37 2012 522° .67–dc23 2011040517

ISBN 978-0-521-88349-8 Hardback

Cambridge University Press has no responsibility for the persistence or accuracy of URLs for external or third-party internet websites referred to in this publication, and does not guarantee that any content on such websites is, or will remain, accurate or appropriate.

<!-- IMAGE: _page_5_Picture_0.jpeg -->

# Contents

|   | Acknowledgments                                                   | pagexi |
|---|-------------------------------------------------------------------|------------|
| 1 | Introduction                                                      | 1          |
|   | 1.1Scientificrationale                                    | 1          |
|   | 1.2Aboutthisbook                                      | 3          |
| 2 | Electromagneticwavepropagation                            | 5          |
|   | 2.1Maxwell'sequations                                     | 5          |
|   | 2.2Electromagneticwavesinfreespace            | 6          |
|   | 2.3Propagationinalinearnonabsorbingmedium | 11         |
|   | 2.4Propagationinalinearabsorbingmedium    | 17         |
|   | 2.5Interference                                               | 22         |
|   | 2.6Polarization;theStokesvector                   | 23         |
| 3 | Theabsorptionoflight                                  | 27         |
|   | 3.1Introduction                                               | 27         |
|   | 3.2Classicaldispersiontheory                          | 27         |
|   | 3.3Dispersionrelations                                    | 33         |
|   | 3.4Mechanismsofabsorption                             | 34         |
|   | 3.5Bandshapeandtemperatureeffects             | 43         |
|   | 3.6Spectraldatabases                                      | 44         |
| 4 | Specularreflection                                            | 45         |
|   | 4.1Introduction                                               | 45         |
|   | 4.2Boundaryconditionsinelectromagnetictheory  | 45         |
|   | 4.3TheFresnelequations                                | 46         |
|   | 4.4TheKramers–Kronigreflectivityrelations         | 61         |
|   | 4.5Absorptionbandsinreflectivity                  | 62         |
|   | 4.6Criterionforopticalflatness                    | 64         |

viii *Contents*

| 5 | Single-particlescattering:perfectspheres                                              |                                                                                                |     |  |
|---|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----|--|
|   | 5.1                                                                                               | Introduction                                                                                   | 66  |  |
|   | 5.2                                                                                               | Conceptsanddefinitions                                                                 | 66  |  |
|   | 5.3                                                                                               | Scatteringbyaperfect,uniformsphere:Mietheory                       | 72  |  |
|   | 5.4                                                                                               | PropertiesoftheMiesolution                                                     | 73  |  |
|   | 5.5                                                                                               | Otherregularparticles                                                                  | 95  |  |
|   | 5.6                                                                                               | Theequivalent-slabapproximation                                                        | 95  |  |
|   | 5.7                                                                                               | Computerprograms                                                                           | 99  |  |
| 6 | Single-particlescattering:irregularparticles                                          |                                                                                                |     |  |
|   | 6.1                                                                                               | Introduction                                                                                   | 100 |  |
|   | 6.2                                                                                               | Extensionofdefinitionstononsphericalparticles                              | 101 |  |
|   | 6.3                                                                                               | Empiricalscatteringfunctions                                                           | 101 |  |
|   | 6.4                                                                                               | Theoreticalandexperimentalstudiesofnonsphericalparticles               | 109 |  |
|   | 6.5                                                                                               | Thegeneralizedequivalent-slabmodel                                                 | 122 |  |
|   | 6.6                                                                                               | Computerprogramsanddatabases                                                       | 144 |  |
| 7 | Propagationinanonuniformmedium:theequationofradiativetransfer |                                                                                                |     |  |
|   | 7.1                                                                                               | Introduction                                                                                   | 145 |  |
|   | 7.2                                                                                               | Effective-mediumtheories                                                                   | 146 |  |
|   | 7.3                                                                                               | Thetransportofradiationinaparticulatemedium                        | 148 |  |
|   | 7.4                                                                                               | Radiativetransferinamediumofarbitraryparticleseparation        | 158 |  |
|   | 7.5                                                                                               | Methodsofsolutionofradiative-transferproblems                              | 169 |  |
|   | 7.6                                                                                               | Computerprograms                                                                           | 179 |  |
| 8 | The                                                                                               | bidirectionalreflectanceofasemi-infinitemedium                             | 180 |  |
|   | 8.1                                                                                               | Introduction                                                                                   | 180 |  |
|   | 8.2                                                                                               | Reflectances                                                                                   | 180 |  |
|   | 8.3                                                                                               | Geometryandnotation                                                                    | 183 |  |
|   | 8.4                                                                                               | Theradianceatadetectorviewingahorizontallystratifiedmedium | 185 |  |
|   | 8.5                                                                                               | Empiricalreflectanceexpressions                                                        | 187 |  |
|   | 8.6                                                                                               | Thediffusivereflectance                                                                | 189 |  |
|   | 8.7                                                                                               | Thebidirectionalreflectance                                                            | 195 |  |
|   | 8.8                                                                                               | ComparisonoftheIMSAmodelwithmeasurements                               | 210 |  |
|   | 8.9                                                                                               | Bidirectionalreflectanceofamediumofarbitraryfillingfactor      | 216 |  |
| 9 | Theoppositioneffect                                                                       |                                                                                                |     |  |
|   | 9.1                                                                                               | Introduction                                                                                   | 221 |  |
|   | 9.2                                                                                               | Theshadow-hidingoppositioneffect(SHOE)                                         | 224 |  |
|   | 9.3                                                                                               | Thecoherentbackscatteroppositioneffect(CBOE)                               | 237 |  |
|   | 9.4                                                                                               | CombinedSHOE,CBOE,andIMSAmodels                                            | 260 |  |

| 10 | Amiscellanyofbidirectionalreflectancesandrelatedquantities |                                                                                        |            |  |
|----|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------|--|
|    | 10.1                                                                                   | Introduction                                                                           | 263        |  |
|    | 10.2                                                                                   | Somecommonlyencounteredbidirectionalreflectancequantities          | 263        |  |
|    | 10.3                                                                                   | Reciprocity                                                                            | 264        |  |
|    | 10.4                                                                                   | Diffusereflectancefromamediumwithaspecularlyreflecting |            |  |
|    |                                                                                        | surface                                                                                | 266        |  |
|    | 10.5                                                                                   | Orientedscatterers:applicationstovegetationcanopies                | 268        |  |
|    | 10.6                                                                                   | Reflectanceofalayeredmedium                                            | 272        |  |
|    | 10.7                                                                                   | Mixingformulas                                                                     | 282        |  |
| 11 | Integrated                                                                             | reflectancesandplanetaryphotometry                                         | 287        |  |
|    | 11.1                                                                                   | Introduction                                                                           | 287        |  |
|    | 11.2                                                                                   | Integratedreflectances                                                             | 287        |  |
|    | 11.3                                                                                   | Planetaryphotometry                                                                | 295        |  |
|    |                                                                                        |                                                                                        |            |  |
| 12 | 12.1                                                                                   | Photometriceffectsoflarge-scaleroughnessIntroduction               | 303303 |  |
|    | 12.2                                                                                   | Derivation                                                                             | 307        |  |
|    | 12.3                                                                                   | Applicationstoplanetaryphotometry                                          | 323        |  |
|    | 12.4                                                                                   | Summaryoftheroughnesscorrectionmodel                               | 331        |  |
|    | 12.5                                                                                   | Otherplanetaryphotometricmodels                                            | 335        |  |
|    |                                                                                        |                                                                                        |            |  |
| 13 |                                                                                        | Polarizationoflightscatteredbyaparticulatemedium           | 339        |  |
|    | 13.1                                                                                   | Introduction                                                                           | 339        |  |
|    | 13.2                                                                                   | Linearpolarizationofparticulatemedia                                   | 340        |  |
|    | 13.3                                                                                   | Thepositivebranchofpolarization                                        | 344        |  |
|    | 13.4                                                                                   | Thenegativebranchofpolarization                                        | 354        |  |
|    | 13.5                                                                                   | Summary                                                                                | 367        |  |
| 14 | Reflectance                                                                            | spectroscopy                                                                           | 369        |  |
|    | 14.1                                                                                   | Introduction                                                                           | 369        |  |
|    | 14.2                                                                                   | Measurementofreflectances                                                      | 370        |  |
|    | 14.3                                                                                   | Invertingthereflectancetofindthescatteringparameters       | 372        |  |
|    | 14.4                                                                                   | Absorptionbandsinreflectance                                               | 378        |  |
|    | 14.5                                                                                   | Thereflectancespectraofintimatemixtures                            | 388        |  |
|    | 14.6                                                                                   | Absorptionbandsinlayeredmedia                                          | 392        |  |
|    | 14.7                                                                                   | Retrievingtheabsorptioncoefficientfromthesingle-scattering     |            |  |
|    |                                                                                        | albedo                                                                                 | 395        |  |
|    | 14.8                                                                                   | Othermethodologies                                                                 | 400        |  |
|    | 14.9                                                                                   | ParticulatemediawithX"1                                                    | 406        |  |
|    | 14.10                                                                                  | Planetaryapplications                                                              | 407        |  |

x *Contents*

| 15    |                                                                                              | Thermalemissionandemittancespectroscopy                        |     |  |
|-------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----|--|
|       | 15.1                                                                                         | Introduction                                                                   | 412 |  |
|       | 15.2                                                                                         | Black-bodythermalradiation                                             | 413 |  |
|       | 15.3                                                                                         | Emissivity                                                                     | 415 |  |
|       | 15.4                                                                                         | Kirchhoff'slaw                                                             | 425 |  |
|       | 15.5                                                                                         | Combinedreflectanceandemittance                                    | 427 |  |
|       | 15.6                                                                                         | Emittancespectroscopy                                                      | 428 |  |
|       | 15.7                                                                                         | Thethermalshadow-hidingoppositioneffect:thermalbeaming | 435 |  |
| 16    | Simultaneoustransportofenergybyradiationandthermalconduction |                                                                                |     |  |
|       | 16.1                                                                                         | Introduction                                                                   | 440 |  |
|       | 16.2                                                                                         | Equations                                                                      | 440 |  |
|       | 16.3                                                                                         | Sometime-independentapplicationsoftheequations             | 449 |  |
|       | 16.4                                                                                         | Time-dependentradiativeandconductivemodels                     | 460 |  |
|       | Appendix                                                                                     | AAbriefreviewofvectorcalculus                          | 463 |  |
|       | Appendix                                                                                     | BFunctionsofacomplexvariable                               | 467 |  |
|       | Appendix                                                                                     | CThewaveequationinsphericalcoordinates                 | 470 |  |
|       | AppendixDFraunhoferdiffractionbyacircularhole                    |                                                                                |     |  |
|       | Appendix                                                                                     | ETableofsymbols                                                    | 482 |  |
|       | Bibliography                                                                                 |                                                                                | 488 |  |
| Index |                                                                                              |                                                                                | 509 |  |

# Acknowledgments

## From the first edition

Many persons have contributed to this book. Foremost is my wife, Joyce, to whom this book is dedicated. Without her continuing support, to say nothing of pleas, cajoleries, and sometimes even threats, this book would not have been written. My children, Kevin, Jeff, and Cheryl, all managed to launch themselves successfully while this work was under way. In spite of several anxious moments, they have been a joy and an inspiration.

Next are my former students. Their suggestions, criticisms, measurements, and computations made important contributions. Bob Nelson built the goniometric photopolarimeter that took much of the data used in this book. He will be happy to know the instrument is still functional. I am especially grateful to Eddie Wells for his careful measurements and suggestions, and also to Jeff Wagner, Deborah Domingue, and Audrey McGuire.

Over the years I have benefited from conversations with many other persons, particularly Jack Salisbury, Paul Helfenstein, Carle Pieters, Joe Veverka, Roger Clark, Marcia Nelson, Jim Pollack, Ted Bowell, and Kaari Lumme. I also wish to thank Sophia Prybylski of Cambridge University Press. Her careful attention to the manuscript caught many errors of both typography and grammar.

My father was fond of quoting Albert Einstein to the effect that a scientist never really understands his own theories unless he can satisfactorily explain them to an average person. I never was able to verify whether or not Einstein actually said this, but it seemed like a good principle to follow. My colleague and friend Bill Cassidy is an explorer, finder of meteorites, and raconteur extraordinaire, but he has never claimed to be a mathematician, and thus he was an ideal man-on-the-street for my ideas. Many times he watched while I covered a blackboard with equations, and then asked me to explain in English what I had just written. I hope his patience has had a positive effect on the clarity of this book.

The major impetus behind the development of the reflectance models described here has been the desire to provide a tool that will enable planetary scientists to better understand the surfaces of the various bodies we study. I am grateful to the Planetary Geology and Geophysics Program, Solar System Exploration Division, Office of Space Science and Applications of the National Aeronautics and Space Administration (NASA) for their continuing support. I especially wish to thank former NASA program manager Steve Dwornik, who continued to approve my grant proposals even though at times he was not quite sure what I was attempting to do. I also thank the National Research Council of the NationalAcademy of Sciences for a senior research fellowship at NASA's Ames Research Center that supported me while I was working out some of these ideas.

I would be remiss if I did not especially acknowledge Thomas Gold, who may be said to have started it all. I had just finished my graduate studies at Cornell University when President Kennedy announced that we were going to the Moon. As a result, planetary science was suddenly revitalized. I thought that this would be a much more exciting field in which to do research than neutron physics, which was the subject of my doctoral dissertation, and Tommy agreed to accept me for postdoctoral research.

No one knew what the surface of the Moon was like, but Tommy thought that it was covered with a very fine-grained soil, which he referred to by the generic term "dust." At the time, that idea was at odds with the prevailing wisdom, which was divided between those who expected to find volcanic extrusive rock similar to Hawaiian aa and those who expected cobbly gravel, thought to have been generated by meteorite impacts. Tommy returned from a conference at which astronomers from the then Soviet Union had emphasized the strongly backscattering character of the lunar bidirectional refectance function. He was sure that "dust" could have this property and suggested that I build a goniometric photometer to investigate the diffuse reflectances of particulate media.

He assigned a young graduate student, Hugh Van Horn, as my research assistant. Hugh has since gone on to study brighter and denser objects than the Moon.We built the photometer and proceeded to measure the bidirectional reflectance functions of everything we could lay our hands on, including pulverized rocks, but the only material that was as backscattering as the Moon was reindeer moss – hardly a likely candidate. Somewhat in desperation, we began referring to the mysterious shapes that would produce a lunar type of photometric function as "fairy castle structures."

One day we discovered that very fine SiC abrasive powder was strongly backscattering, but that coarse SiC powder was not. There was no obvious reason for that difference in scattering properties, so I went off in search of microscope to see if a magnified inspection of the surface would give me a clue. It was late on Friday afternoon, and most of my colleagues had gone home, so that the only instrument I could borrow was a low-power, stereoscopic microscope. This turned out to be serendipitous. First, I looked through the microscope at the coarse-grained powder. It resembled a pile of gravel and was not very interesting. Then I placed the fine-grained powder on the stage, and there were the fairy castles.

The name we had given the structures turned out not to be facetious at all, but is in fact a rather accurate description of the morphology of a powder in which the surface forces that act between grains exceed the gravitational forces exerted on them by the Earth. As I looked through the microscope, I saw a miniature world of deep, mysterious valleys and soaring towers leaning at crazy angles atop rugged, porous hills, with flying buttresses, and all connected by lacy bridges. Readers can easily verify these features for themselves. The complexity of such a texture is impossible to perceive with a monocular microscope, but it is just what is necessary to produce a lunar-type reflectance function. This discovery, along with Lyot's polarization data, turned out to be among the strongest pre-Apollo evidences that the lunar surface consists of a fine-grained regolith.

After we had solved the problem experimentally, I thought I would see if I could describe it mathematically, and I have been thinking about reflectances, off and on, ever since.

Finally, I wish to thank Ted Bowell for proposing that an asteroid that he discovered be named 3549 Hapke after me. I hope that someday my granddaughter Carley will land on it.

## Preface to the second edition

In the years since the first edition of this book appeared reflectance and emitance spectroscopy have evolved into mature techniques for the remote study of surfaces of bodies of the solar system. The first edition had been generously received by my colleagues, so Cambridge University Press suggested that I write a second edition. Interactions with many colleagues, including those cited above and also Paul Lucey, Jack Mustard, and Mark Robinson, continue to help my understanding of reflectance. I am particularly indebted to my former students Jennifer Piatek and Amy Snyder Hale. The many discussions with them and their research while at the University of Pittsburgh made important contributions to this book. Jen's wizardy with MAC computers and her general programming skills were astonishing to someone who finished his formal schooling with only a slide rule. Bob Nelson has grown from a former graduate student into a respected planetary scientist and personal friend. We continue to collaborate on measurements of the reflectance and polarization of particulate media, and these measurements and his insights have been invaluable.

Finally, I thank Larry Taylor for naming the mineral hapkeite (Fe2Si) after me.