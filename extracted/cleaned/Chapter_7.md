### Propagation in a nonuniform medium: the equation of radiative transfer

## 7.1 Introduction

Virtually every natural and artificial material encountered in our environment is optically nonuniform on scales appreciably larger than molecular. The atmosphere is a mixture of several gases, submicroscopic aerosol particles of varying composition, and larger cloud particles. Sands and soils typically consist of many different kinds and sizes of mineral particles separated by air, water, or vacuum. Living things are made of cells, which themselves are internally inhomogeneous and are organized into larger structures, such as leaves, skin, or hair. Paint consists of white scatterers, typically TiO2 particles, held together by a binder containing the dye that gives the material its color. These examples show that if we wish to interpret the electromagnetic radiation that reaches us from our surroundings quantitatively, it is necessary to consider the propagation of light through nonuniform media.

Although the equations for this problem can be formally written down (Ishimaru, 1978), theirsolution to produce useful, practical answersis another matter. The exact solution of Maxwell's equations for this class of problems is possible today only for ensembles of a small number of particles of relatively simple shapes, even with the help of modern high-speed computers. Several persons have obtained direct solutions of Maxwell's equations for a few interacting spheres (e.g., Liang and Lo, 1967; Bruning and Lo, 1971a, b; Fuller and Kattawar, 1988a, b; Xu, 1995). Lumme *et al.* (1997) used the discrete dipole approximation to synthesize scattering by several particles. Mishchenko and his colleagues have calculated scatterings by rotationally averaged systems of multiple spheres using the T-matrix method (e.g., Mishchenko *et al.*, 1995, 2007;Mishchenko andMackowski, 1996;Mishchenko and Liu, 2007).While these studies have been invaluable in illuminating the electromagnetic interactions between particles, they are hardly realistic models of regoliths and powders. Hence, we must resort to approximate methods whose validity must be judged by the accuracy with which they describe and predict observations. Two of these methods are effective-medium theories and the equation of radiative transfer.

## 7.2 Effective-medium theories

One such approximate method is known as *effective-medium theory*, which attempts to describe the electromagnetic behavior of a geometrically complex medium by a uniform dielectric constant that is a weighted average of the dielectric constants of all the constituents. The various approaches differ chiefly in their specifications of the weighting factors. Examples are the models of Maxwell-Garnett (1904), Bruggeman (1935), Stroud and Pan (1978), and Niklasson *et al.* (1981); see also Bohren and Huffman (1983) and Bohren (1986).

One of the most widely used is the Maxwell-Garnett model, which will be summarized briefly. It is assumed that the medium consists of a vacuum of dielectric constant *Ke*1 = 1, in which approximately spherical particles of radius *a* and complex dielectric constant *Ke*2 are suspended. Both the particles and their separations are assumed to be small compared with the wavelength. Radiation having an electric field of strength **E***e* is incident on the medium and induces a dipole moment **p***e* in each particle that radiates coherently with the incident light. Consider an element of volume in the medium a small fraction of a wavelength in size. From the equations in Section 2.3.1 the electric displacement in that volume element is given by

$$\mathbf{D}_e = \varepsilon_{e0} \mathbf{K}_e \mathbf{E}_e = \varepsilon_{e0} \mathbf{E}_e + \mathbf{P}_e, \tag{7.1}$$

where **E***e* is the external field, *Ke* is the average dielectric constant to be determined, **P***e* is the electric polarization or dipole moment per unit volume, given by **P***e* = *N***p***e*, *N* is the number of particles per unit volume, **p***e* is their induced dipole moment, **p**e = ζ*e*ε*e*0**E**loc, where ζ*e* is the electric polarizability, and **E**loc is the local electric field. At any particle, **E**loc is the sum of the applied field plus the fields due to the surrounding particles.

To calculate **P***e*, the Clausius–Mossotti/Lorentz–Lorenz model (Section 2.3.2), which was originally derived to describe intermolecular fields, is also assumed to be a valid description of the fields between the larger particles. Then,

$$\mathbf{P}_e = N\alpha_e \varepsilon_{e0} \mathbf{E}_e / (1 - N\alpha_e / 3). \tag{7.2}$$

The electric dipole moment of a sphere is given by equation (6.16),

$$\mathbf{p}_e = 4\pi a^3 \varepsilon_{e0} \mathbf{E}_{loc} (K_{e2} - 1) / (K_{e2} + 2).$$

(As discussed in Chapter 6, this expression also results from the first term in the Mie solution for scattering of a plane wave by a sphere.) Hence,

$$\alpha_e = 4\pi a^3 (K_{e2} - 1)/(K_{e2} + 2).$$
 (7.3)

Combining equations (7.2) and (7.3) gives

$$\mathbf{P}_{e} = \varepsilon_{e0} \mathbf{E}_{e} \frac{N4\pi a^{3} [(K_{e2} - 1)/(K_{e2} + 2)]}{1 - \frac{1}{3} N4\pi a^{3} [(K_{e2} - 1)/(K_{e2} + 2)]},$$

and inserting this into (7.1) we obtain

$$\overline{K_e} = 1 + \frac{3\phi \left[ (K_{e2} - 1) / (K_{e2} + 2) \right]}{1 - \phi \left[ (K_{e2} - 1) / (K_{e2} + 2) \right]},\tag{7.4}$$

where  $\phi = N4\pi a^3/3$  is the total fraction of the volume occupied by the particles and is called the *filling factor*. The quantity  $1 - \phi$  is the *porosity*. If, instead of a vacuum, the particles are embedded in a matrix of dielectric constant  $K_{e1} \neq 1$  then  $K_{e2}$  and  $K_e$  are the dielectric constants relative to  $K_{e1}$ , so that

$$K_{\varepsilon} = K_{e1} + \frac{3\phi K_{e1} \left[ (K_{e2} - K_{e1}) / (K_{e2} + 2K_{e1}) \right]}{1 - \phi \left[ (K_{e2} - K_{e1}) / (K_{e2} + 2K_{e1}) \right]}.$$
 (7.5)

Equation (7.5) is the Maxwell-Garnett effective-medium expression.

Unfortunately, effective-medium theories have two major difficulties. The first is that they deal only with media of particles much smaller than the wavelength. The second is that they are not capable of explaining an observation familiar to every child the world over: the color and brightness of the clear sky. The reason is that scattering by the individual particles is neglected.

This neglect is often justified by the following argument. Suppose the radiation is observed exactly from the direction into which it is propagating. Then the scattered radiation combines coherently with the incident light to produce a wave characterized by a modified dielectric constant. If the medium is observed at some other angle, all the particles in any increment of volume small compared with the wavelength radiate toward the observer. However, a second volume along the line of sight can always be found whose distance differs from that of the first volume by exactly one-half wavelength. The particles in the second volume also radiate toward the observer, but the contributions of the two volume elements are exactly out of phase and cancel.

The fallacy in this argument is that it is valid only if the density of particles is perfectly uniform. However, if the various volume elements do not contain equal numbers of particles, they will not radiate equally, and the coherent cancellation will be incomplete. Let the average number of particles in a volume element be  $\langle N \rangle$ , and the actual number of particles in the jth volume element be  $N_j = \langle N \rangle + \delta N_j$ . Let the phase of the wave at the observer radiated by the jth element be  $\phi_j$ . Then, if the density deviations are uncorrelated from place to place, the part of the scattered

intensity that is incompletely canceled is proportional to

$$\left| \sum_{j} \delta N_{j} e^{i\phi_{j}} \right|^{2} = \sum_{j} \left( \left( \delta N_{j} \right)^{2} + \left| \sum_{k \neq j} \delta N_{k} \delta N_{j} e^{(i(\phi_{k} - \phi_{j}))} \right| \right)$$

$$= \sum_{j} \left( \left( \delta N_{j} \right)^{2} + \delta N_{j} \sum_{k \neq j} \delta N_{k} \right) = \sum_{j} (\delta N_{j})^{2}, \quad (7.6)$$

where the sum is taken over all the volume elements along the line of sight. The sum over  $\delta N_k$  is zero, because, by definition, the average value of  $\delta N_k$  is zero.

Although the summation in equation (7.6) is over the entire line of sight, the critical distance is the wavelength of light. The medium may be conceptually divided into compartments whose dimensions are  $\lambda/2$ . Then, if the medium is perfectly uniform, the light scattered by the particles in one compartment will be exactly canceled by light scattered in a close neighbor along the line of sight. However, if the medium is inhomogeneous, the cancellation will be incomplete. The variations in particle density are equivalent to variations in the local dielectric constant or refractive index. Thus, the properties of the medium are effectively controlled by the root-mean-square (rms) average of the fluctuations in the local index of refraction over a volume element whose dimensions are of the order of the wavelength.

In gaseous media the density fluctuations can be described by a Poisson distribution in which the mean-square deviation is

$$\left\langle (\delta N_j)^2 \right\rangle = N_j,\tag{7.7}$$

so that, in this case, the scattered intensity is proportional to the number of particles along the line of sight. Because the scattering efficiency of a small particle is inversely proportional to the fourth power of the wavelength, blue light is scattered more efficiently than red, thus accounting for the color of the sky.

These concepts also have applications to the study of gases near their critical points, where they are known as *theories of critical opalescence* (e.g., Kocinski and Wojtczak, 1978). However, they are deficient on two counts: they fail to describe how the scattered intensity is modified by further scattering as it propagates through the medium, and they break down completely when the particles are larger than the wavelength.

## 7.3 The transport of radiation in a particulate medium 7.3.1 Concepts and definitions

In most applications of reflectance spectroscopy we are interested in the quantitative amount of light scattered by an infinitely thick layer of large particles. One way of

calculating this is to consider the microscopic processes that occur when a typical particle interacts with the radiation field inside the medium. Collimated light incident on the medium is partly absorbed and partly scattered by direct encounter with particles in the upper layers. The light that passes between these particles and the light scattered by them illuminates the given particle where it is partly absorbed and scattered into all directions. The particle is heated by the light it absorbs and emits thermal radiation. Some of the radiation scattered or emitted by the particle into an upward-going direction, passes between particles and escapes from the medium. It is the combined light from all the particles that escapes from the upper surface of the medium that we wish to calculate.

In order to determine the amount of radiation escaping into a particular direction several questions must be answered. (1) What is the transmissivity of the medium; i.e., what fraction of radiation survives after traveling a certain distance through the medium? (2) What is the appropriate particle phase function? (3) How can the component of light scattered several times within the medium be calculated?

We begin by defining a number of quantities commonly used in radiative transport problems. Consider a medium of identical particles much larger than the wavelength separated by distances that are random, but that are, on the average, large compared with the particle sizes. An example might be a cloud. Consider a slab of the medium of area ς*A* and thickness ς*s*, through which radiance *I* propagates (Figure 7.1). The volume of the slab ς*s*ς*A* is assumed to be large compared with the volume of an individual particle in such a way that ς*A* is much larger than the geometric cross-sectional area of an individual particle, but ς*s* is so small that no particle

<!-- IMAGE: _page_4_Picture_5.jpeg -->

Figure 7.1 Extinction by a sparsely packed distribution of particles in an optically thin slab.

shields another within the incremental volume element. Assume that the particles are randomly oriented and positioned. Let *N* be the number of particles per unit volume, σ be the particle geometric cross-sectional area averaged over all orientations, and *QE* be their extinction efficiencies, as defined in Chapters 5 and 6. Because the spacing between the particles is large their properties may be considered to be the same as if they were isolated.

There is a total of *N*ς*s*ς*A* particles in the slab, so that as the light travels through it the radiant power intercepted by the particles in the volume decreases by an amount *dPE* = ς*I (s)*ς*A* = !*I (s)N*ς*s*ς*A*σ*QE*, where *I (s)* is the radiance. Assuming that ς*I* and ς*s* can be made sufficiently small, we can pass to the limit, and this equation becomes

$$\frac{dI(s)}{ds} = -I(s)N\sigma Q_E, \tag{7.8}$$

which can be integrated

$$I(s) = I(0) \exp(-N\sigma Q_E s), \tag{7.9}$$

or if *N* varies with position,

$$I(s) = \exp(-\int_{0}^{s} N(s')\sigma Q_{S}ds').$$
 (7.10)

The last two equations are forms of Beer's law similar to equation (2.95a) which describes the decrease of intensity in a continuous absorbing medium. This suggests that a quantity *E* called the *extinction coefficient*, analogous to the absorption coefficient ζ, may be defined for a particulate medium by

$$E = N\sigma Q_E. (7.11)$$

More generally, suppose the slab contains a mixture of different types of particles with *Nj* particles of type *j* per unit volume, geometric cross sections averaged over all orieintations σ*j* , volumes (*j* , and extinction, scattering and absorption efficiencies *QEj* , *QAj* , and *QSj* , respectively. The particles may differ in such properties as size, composition, shape, and structure, denoted by subscript *j* . Then the total number of particles per unit volume is

$$N = \sum_{j} N_j, \tag{7.12}$$

and the average distance between particles is

$$L = N^{-1/3}. (7.13)$$

The fraction of space within the medium occupied by particles is the *filling factor*

$$\phi = \sum_{j} N_{j} \upsilon_{j} = N \upsilon \tag{7.14}$$

where ( =φ*/N* is the average volume of a particle. The quantity 1–φ is the *porosity*. The *volume-average particle cross-sectional area* is

$$\sigma = \left(\sum_{j} N_{j} \sigma_{j}\right) / N. \tag{7.15}$$

Define the *average particle size* as the diameter of an equivalent sphere with the average cross-sectional area σ,

$$D = \sqrt{4\sigma/\pi}. (7.16)$$

Putting these definitions together, the *volume extinction coefficient* of a particulate medium is

$$E = \sum_{j} N_{j} \sigma_{j} Q_{Ej} = N \sigma Q_{E}, \qquad (7.17a)$$

where

$$Q_E = E/n\sigma \tag{7.17b}$$

is the *volume-average extinction efficiency*. Since extinction is the sum of absorption and scattering, the *volume-average absorption and scattering coefficients* and *efficiencies* can be defined similarly as, respectively,

$$A = \sum_{j} N_{j} \sigma_{j} Q_{Aj} = N \sigma Q_{A}, \tag{7.18a}$$

where

$$Q_A = A/N\sigma, (7.18b)$$

and

$$S = \sum_{j} N_{j} \sigma_{j} Q_{Sj} = N \sigma Q_{S}, \qquad (7.19a)$$

where

$$Q_S = S/N\sigma. (7.19b)$$

Since *QEj* = *QAj* + *QSj*, *QE* = *QA* + *QS*, and *E* = *A* + *S*; *QA* and *QS* are the *volume-average absorption and scattering efficiencies* respectively.

The *volume angular scattering coefficient* is defined as

$$G(g) = \sum_{j} N_{j} \sigma_{j} Q_{sj} \Pi_{j}(g) = N \sigma Q_{S} p(g) = Sp(g),$$
 (7.20a)

where  $\Pi_i(g)$  is the phase function of the jth type of particle and

$$p(g) = G(g)/S \tag{7.20b}$$

is the *volume-average single-particle phase function*. Since each  $p_j(g)$  must satisfy the normalization condition, equation (5.13), S is the integral of G(g):  $S = (1/2) \int_0^{\pi} G(g) \sin g dg$ , and  $(1/2) \int_0^{\pi} p(g) \sin g dg = 1$ .

The volume-average single scattering albedo is

$$w = S/E. (7.21a)$$

It is convenient to define a related quantity called the albedo factor

$$\gamma = \sqrt{1 - w}.\tag{7.21b}$$

The volume-average asymmetry factor is

$$\xi = \langle \cos \theta \rangle = -\sum_{j} \frac{1}{2} \int_{0}^{\pi} p(g) \cos g \sin g dg.$$
 (7.22)

The extinction mean free path  $\Lambda_E$  is the average distance a photon travels through the medium before being extinguished by either absorption or scattering,

$$\Lambda_E = \left(\int_0^\infty s' \ e^{-Es'} ds'\right) / \left(\int_0^\infty e^{-Es'} ds'\right) = 1/E; \tag{7.23}$$

similarly the absorption and scattering mean free paths  $\Lambda_A$  and  $\Lambda_S$  are the reciprocals of their respective coefficients. Finally, two other quantitties frequently encountered are the transport coefficient

$$S_T = S(1 - \xi),$$
 (7.24a)

and, its reciprocal, the transport mean free path,

$$\Lambda_T = 1/S(1-\xi).$$
 (7.24b)

If the distribution of properties in these definitions is continuous the summations are replaced by integrations. In general, each of these quantities may depend on both location and direction of the incident radiance, although this has not been indicated explicitly.

Thus, with these definitions a discontinuous medium of randomly positioned and oriented particles may be described as if it were a quasi-continuous medium. However, defining the various coefficients in this way results in a subtle, but major, change in the physical interpretation of the propagation of radiation through a medium. In a continuous medium the absorbers and scatterers are smoothly distributed. That is, the radiation encounters them everywhere, so that the intensity

is reduced equally across the wave front. However, in the nonuniform medium, the absorbers and scatterers are localized, so that the local intensity is drastically perturbed. The part of the wave front traversing a layer that passes between the particles is relatively unchanged, but the parts that encounter particles are extinguished. Even if the particles are smaller than the wavelength, the energy is no longer distributed uniformly across the wave front of the transmitted light. It is the intensity averaged over an area of the wave front whose dimensions are much larger than both the particle separation and the wavelength that must be considered to be exponentially attenuated.

If the medium consists of several different types of particles the various quantities defined above must be averaged over distances that not only are greater than the particle sizes and separations but are large enough to contain a representative sample of the medium. In a gas the fluctuations in the molecular density are proportional to the number of molecules per unit volume and are uncorrelated; hence, these definitions may be used to calculate radiative transport in atmospheres, as well as in clouds of well-separated larger particles.

### 7.3.2 The equation of radiative transfer in a quasi-continuous medium

The formalism that is commonly used to calculate how the processes of emission, absorption, and scattering control the propagation of electromagnetic waves within a complex medium is a form of the Boltzmann transport equation known as the *equation of radiative transfer*. The fundamental assumption of this formalism is that the medium can be treated as if it were a continuous fluid, each incremental portion of which interacts with other portions independently and incoherently through the processes of absorption, scattering, and emission. The photons are treated as if they were particles diffusing through the medium in a manner similar to gas diffusing through a complicated structure or neutrons diffusing through a nuclear reactor. The theory is not applicable to a medium consisting of particles that are uniformly spaced and regularin shape. However, Mishchenko (2002) hasshown thatfor media of widely spaced discrete particles the radiative transfer equation can be derived from statistical electromagnetic theory. Hence, this equation can be directly applied to one of the two media that are of greatest interest in remote sensing: planetary atmospheres. The theory's applicability to the other type of medium, powders and planetary regoliths where the particles are close together, has not been rigorously established. Nevertheless, as will be seen, models based on the assumption that the radiative transfer equation is valid for these media as well enjoy considerable experimental support, and, therefore, will be the principal type of model used in this book.

In the first part of this chapter the discussion will be confined to continuous media and media of particles sufficiently far apart that equations (7.9) or (7.10) are valid. The various changes that must be made in order to describe media in which the particles are close together will be discussed later. Let *I (s,*.*)* be the radiance at position *s*, propagating into direction . within a continuous or quasi-continuous medium that both scatters and absorbs. The units of *I (s,*.*)* are power per unit area per unit solid angle. In general, unless stated otherwise, *I (s,*.*)* will also be a function of wavelength or frequency; however, in the interest of economy of notation, this dependence usually will not be denoted explicitly. Suppose *s* lies on the base of a right cylinder of area *dA*, length *ds*, and volume *dsdA*, where *ds* points in the direction of . (Figure 7.2). Then the radiant power at *s* passing through the base contained in a cone of solid angle *d*. about . is *I (s,*.*)dAd*.. Similarly, the power emerging from the top of the cylindrical volume into *d*. is *I (s* + *ds,*.*)dAd*. = {*I (s,*.*)* + [/*I (s,*.*)/*/*s*]*ds*}*dAd*.. The difference between the power emerging from the top and that entering at the

<!-- IMAGE: _page_9_Picture_2.jpeg -->

Figure 7.2 Changes in the radiance as it travels a distance *ds* through an absorbing and scattering medium.

<!-- IMAGE: _page_10_Picture_2.jpeg -->

Figure 7.3 Schematic diagram of the changes in the radiance as it traverses the cylindrical volume *dsdA*.

bottom is  $\Delta P = (\partial I/\partial s) ds dA d\Omega$ . More generally,  $\partial I/\partial s$  is the divergence of I (see Appendix A) in the direction of  $\Omega$ :  $\frac{\partial I}{\partial s} = \Omega \cdot \text{div } I$ .

This change in radiant power is due to various processes occurring in the cylinder that add or subtract energy from the beam. In this book we will be concerned with three such processes: absorption, scattering, and thermal emission, as illustrated schematically in Figure 7.3. Fluorescent emission will not be considered.

Since the medium is continuous, it is assumed that both the absorption and scattering can be described by a relation of the form of Beer's law,  $I(s_2) = I(s_1)T(s_1, s_2)$ , where T is the *transmissivity function* in the medium,

$$T(s_1, s_2) = \exp\left[-\int_{S_1}^{s_2} E(s, \Omega) ds\right].$$
 (7.25)

Later in the chapter it will be shown that this equation must be modified for media of closely packed particles; however, for now it will be assumed to be valid. Then the decrease in power due to extinction as the radiance propagates through the volume element is

$$\Delta P_E = -E(s, \Omega)I(s, \Omega)dsdAd\Omega. \tag{7.26}$$

Scattering increases as well as decreases the power in the beam, because light of intensity  $I(s, \Omega')$  propagating through the volume element dsdA in a direction  $\Omega'$ 

can be scattered into the direction .. The power *(*/*PSC/*/.*)d*.% passing through *dsdA* into a cone of solid angle *d*.% about direction .% that is scattered into a cone *d*. about direction . is

$$\frac{\partial P_{SC}}{\partial \Omega} d\Omega' = \frac{1}{4\pi} S(s, \Omega) p(s, \Omega', \Omega) I(s, \Omega') ds dA d\Omega' d\Omega. \tag{7.27}$$

To find the total amount of power ς*PSC* scattered into the beam, the contribution of intensities traveling through the volume in all directions .% must be added together, so that

$$\Delta P_{SC} = \int_{4\pi} \frac{\partial P_{SC}}{\partial \Omega} d\Omega' = ds dA d\Omega \frac{S(s,\Omega)}{4\pi} \int_{4\pi} I(s,\Omega') p(s,\Omega',\Omega) d\Omega'. \quad (7.28)$$

Turning next to emission, define the *volume emission coefficient F(s,*.*)* as the power emitted per unit volume by the element at position *s* into unit solid angle about direction .. Then the contribution of the emitted radiation to the change in power is

$$\Delta P_F = F(s, \Omega) ds dA d\Omega. \tag{7.29}$$

In general, there are at least four processes that contribute to the volume emission: singly scattered incident irradiance from a source, thermal emission, fluorescence and luminescence, and stimulated emission. Fluorescence and luminescence are outside of the scope of this book. Stimulated emission is important in gaseous media that are not in thermodynamic equilibrium, but usually not in particulate media. It can be effectively included by adding a negative component to the volume absorption coefficient. Hence, only single scattering and thermal emission will be considered in detail; their volume coefficients will be denoted by *FS(s,*.*)* and *FT (s,*.*)* respectively. Then

$$F(s,\Omega) = F_s(s,\Omega) + F_T(s,\Omega). \tag{7.30}$$

Single scattering will be discussed first. In a large number of problems the medium is illuminated by highly collimated radiation *J (*.ι*)*incident on the top surface from a point source that may be considered to be located effectively at an infinite distance above the medium in a direction .0 from the medium making an angle *i* from the zenith. The vector .*i* points in the exact opposite direction to .0. At any point *s* below the surface of the medium the irradiance that has not been extinguished is *J* Ψ*(*. ! .*i)*exp[!∫∞ *s E(s*% *,*.*)ds*% ], where Ψ is the delta function. The irradiance that is scattered once by the medium is a source of diffuse radiance that contributes an amount

$$F_{s}(s,\Omega) = \frac{1}{4\pi} \int_{4\pi}^{\pi} J\delta(\Omega' - \Omega_{i}) \exp\left[-\int_{s}^{\infty} E(s',\Omega)ds'\right] G(s,\Omega',\Omega)d\Omega'$$

$$= \frac{J}{4\pi} S(s,\Omega) p(s,\Omega_{i},\Omega) \exp\left[-\int_{s}^{\infty} E(s',\Omega_{i})ds'\right]$$
(7.31)

to the volume emission coefficient. The second emission process, thermal radiation  $F_T(s,\Omega)$ , will be considered in detail in Chapter 13. Equating the sum of all the contributions  $(\Delta P_{SC} + \Delta P_E + \Delta P_F)$  to  $(\delta I/\partial s)dsdAd\Omega$  and dividing by  $dsdAd\Omega$  gives

$$\frac{\partial I(s,\Omega)}{\partial s} = -E(s,\Omega)I(s,\Omega) + \frac{S(s,\Omega)}{4\pi} \int_{4\pi} I(s,\Omega')p(s,\Omega',\Omega)d\Omega' + F(s,\Omega). \tag{7.32}$$

Equation (7.32) is the general form of the equation of radiative transfer.

In most applications of interest the medium is horizontally stratified. Let the positive z-axis point in the vertical direction, and let ds make an angle  $\vartheta$  with dz, so that  $ds = dz/\cos\vartheta$  (Figure 7.1). Making this substitution in (7.34) and dividing through by  $E(z,\Omega)$  gives

$$\frac{\cos\vartheta}{E(z,\Omega)} \frac{\partial I(z,\Omega)}{\partial z} = -I(z,\Omega) + \frac{1}{E(z,\Omega)} \frac{1}{4\pi} \int_{4\pi} I(z,\Omega') G(z,\Omega',\Omega) d\Omega' + \frac{F(z,\Omega)}{E(z,\Omega)}.$$
 (7.33)

Define the source function,

$$F(z,\Omega) = F(z,\Omega)/E(z) = \frac{J}{4\pi} \exp\left[-\int_{s}^{\infty} E(s')ds'\right] \frac{S(s,\Omega)p(z,\Omega_{I},\Omega)}{E(z)} + F_{T}(z,\Omega)$$
(7.34)

where

$$F_T = F_T / E. (7.35)$$

In many applications, including the important case of an ensemble of randomly oriented particles, S, A, and E are independent of  $\Omega$  and p depends only on the angle between  $\Omega'$  and  $\Omega$ , rather than on the two directions separately. Let  $\theta'$  be the scattering angle between the directions into which  $\Omega'$  and  $\Omega$  are pointing, and g' be the phase angle between the directions from which the radiance is coming and into which it is scattered. Then the angular scattering phase function can be equivalently described by  $p(s,\theta')$  or by p(s,g'), as convenient. In what follows it will be assumed that the medium is horizontally stratified and isotropic.

Define the optical depth  $\tau$ ,

$$\tau = \int_{z}^{\infty} E(z')dz' = \int_{s}^{\infty} E(s')ds'/\cos\vartheta, \tag{7.36}$$

so that

$$d\tau = -E(z)dz = -E(s)ds/\cos\vartheta. \tag{7.37}$$

The optical depth τ is a dimensionless vertical distance expressed in units of the extinction length 1*/E*. The altitude *z* can be expressed equivalently in terms of τ . Radiance emitted vertically upward at altitude *z* within the scattering medium is reduced by a factor *e*!τ by extinction as it propagates to the top of the medium. Conversely, light incident vertically on the top of the medium will be reduced in intensity by the same factor *e*!τ as it penetrates to the altitude corresponding to τ .

Making these substitutions and remembering that the volume single-scattering albedo is *w(z)* = *S(z)/E(s)*, the equation of radiative transfer for a horizontally stratified medium may be written

$$-\cos\vartheta \frac{\partial I(\tau,\Omega)}{\partial \tau} = -I(\tau,\Omega) + \frac{w(\tau)}{4\pi} \int_{4\pi} I(\tau,\Omega') p(\tau,g') d\Omega'$$
$$+ J \frac{w(\tau)}{4\pi} p(\tau,g) e^{-\tau/\cos i} + F_T(\tau,\Omega), \tag{7.38}$$

where *g* is the phase angle between .0 and .. Note that none of the quantities *E, A, S, G*, or φ appear explicitly in the radiative-transfer equation when it is written in this form, only ratios in the form of *w* and *p*. The advantage of writing the equation in the form of (7.38) is that in many applications the parameters A, *S*, *G*, and *E* all have the same dependence on altitude through being proportional to a common function of *z*, such as the density of the medium. In these cases the ratios *w* and *p* are independent of *z* or τ , which simplifies the problem considerably.

## 7.4 Radiative transfer in a medium of arbitrary particle separation 7.4.1 Introduction

If the medium consists of well-separated particles the transmissivity function is given by equation (7.25) and, to a good approximation, *p(*τ*,*g*)* can be taken to be the same as that of an isolated particle. It is often assumed that this is also true when the particles are touching. However, it will be seen that several major changes in the nature of the scattering phenomena occur as the particles move close together. These include the following: the Fraunhofer diffraction pattern in the single-particle phase function no longer exists; the transmissivity function is altered; and coherent and collective effects between particles become important. These changes will be discussed in this section.

### 7.4.2 Fresnel diffraction in particulate media

The diffraction pattern of a particle is one of the most misunderstood concepts in the theory of the reflectance of a particulate medium. In order to calculate the multiply scattered component of the reflectance it is necessary to compute the radiance scattered by one particle that falls on another located a *short* distance away, not the radiance at infinity. A common assumption is that the Fraunhofer diffraction pattern (Figure 5.8) is unchanged. However, this assumption is incorrect on two counts. First, the radiant power in the Fraunhofer pattern comes from the portion of the wave that passes by the particle. In a close-packed medium much of the space around the particle is blocked by other particles, which decreases the intensity available for diffraction. To assume that the Fraunhofer pattern is unchanged violates the law of conservation of energy.

Second, the diffraction pattern is caused by interference between the Huygens wavelets generated by the part of the wavefront passing by the particle. In order to evaluate the integral over the wavelets the Fraunhofer formalism depends on a number of mathematical approximations that are valid only if both the source of radiation and the detector are located an infinite distance from the particle. If the particles are sufficiently far apart in a sparse medium these approximations are valid, but they break down completely when the particles are close together. The most obvious manifestation of this breakdown is that Fraunhofer diffraction predicts that shadows do not exist!

Diffraction when the source and detector are at arbitrary distances from an obstacle was investigated in the nineteenth century by Augustin-Jean Fresnel, and is known as *Fresnel diffraction*. Fraunhofer diffraction is a special case of Fresnel diffraction that is valid only if the *Fresnel condition*,

$$\frac{D^2}{4\lambda} \left( \frac{1}{l_S} + \frac{1}{l_D} \right) << 1, \tag{7.39}$$

is met, where D is the average particle size, and  $l_S$  and  $l_D$  are the distances from the particle to the source and detector, respectively. For multiply scattered light in a particulate medium the "source" is the light scattered by one particle that illuminates a second particle, and the "detectors" are the layers of other particles behind the second particle on which the diffracted light falls. Thus  $l_S \sim l_D \sim L$ , so the Fresnel condition becomes

$$\frac{L}{D} >> \frac{D}{4\lambda} = \frac{X}{4\pi},\tag{7.40}$$

where X is the average size parameter. If X = 100 the particles must be separated by more than 8 particle diameters. Fresnel developed graphical methods of carrying out the summation over all the Huygens wavelets, but today with modern computers it is more convenient to evaluate the integrals numerically. Several programs are available for this on the internet.

Figure 7.4 illustrates how the diffraction pattern of an opaque disk changes with distance and with viewing conditions. These figures were calculated using

<!-- IMAGE: _page_15_Figure_0.jpeg -->

Figure 7.4 (a) Fresnel diffraction pattern 100 disk diameters behind an opaque disk viewed by a detector that accepts only light directly scattered by the disk. Compare with the Fraunhofer diffraction pattern, Figure 5.8. (b) Fresnel diffraction pattern of light 100 diameters behind an opaque disk viewed by a detector that accepts both the incident and the diffracted light. This is the diffraction pattern of a particle that would fall on a screen or on another particle 100 diameters away. (c) Fresnel diffraction one disk diameter directly behind an opaque disk illuminated by a source one disk diameter in front of the disk. Note the shadow. This is the diffraction pattern of a particle that would fall on a screen or on another particle located one diameter behind the first.

<!-- IMAGE: _page_16_Figure_2.jpeg -->

Figure 7.4 (*cont*.)

the Fresnel Diffraction Explorer program created by D. Dauger (see Section 7.7). Figure 7.4a is the diffraction pattern of an opaque disk illuminated by light from a point source at a distance of 100 particle diameters viewed by a detector at a distance of 100 diameters. In this figure the detector is assumed to be well collimated so that it views only the light diffracted by the particle and excludes the incident irradiance. Compare with Figure 5.8. However, if the incident irradiance is included, as would be the case for multiply scattered light falling on layers of other particles in a sparsely packed medium, the total intensity pattern is shown in Figure 7.4b. The reason for the differences between the two figures is that the peak is superposed coherently onto the incident irradiance. By contrast Figure 7.4c shows the diffraction pattern when the source and screen are both at distances of one diameter from the plane of the disk, which would be a typical interparticle separation in a closely spaced powder. The main feature is a shadow behind the particle. The edges of the shadow are not sharp but have a pronounced ripple structure. There is also a very thin central spike. As the distance from the disk increases, the ripples and central peak broaden and fill in the shadow.

The change in the nature of the diffraction with distance is not the only effect of decreasing the filling factor. Even the diffraction pattern of light from a distant source scattered once by particles in a regolith and viewed by a distant detector is drastically altered. To understand this, recall the discussion in freshman physics class of interference by light passing through two narrow slits. The diffraction pattern of one slit is just a narrow line. Adding a second slit changes the pattern completely: the single lobe disappears and is replaced by a series of parallel lines. Adding a third slit changes the pattern again into something completely different. Similarly the presence of adjacent particles completely eliminates the Fraunhofer pattern of a single particle. This is discussed extensively in Hapke (1999), who showed that the only Fraunhofer diffraction peak existing in a system of particles is that of the system as a whole and that it has an angular width of the order of the wavelength divided by the size of the entire system. For a powder in the laboratory this is the width of the sample, not the diameter of a single particle. For a planetary regolith this is the diameter of the planet. In both cases the resulting peak is so narrow as to be unobservable in practice.

These arguments are supported by results published in a number of papers on scattering by ensembles of several particles (Mishchenko, 1995; Mishchenko *et al.*, 1995; Mackowski and Mishchenko, 1996; Lumme *et al.*, 1997; Kolokolova *et al.*, 2006). In all cases the central peak of the Fraunhofer patterns had angular widths approximately equal to the ratio of the wavelength to the diameter of the ensemble, not the diameter of the constituent particles. The loss of the Fraunhofer peak of the individual particles is also demonstrated by observations of the Moon. If the diffraction peaks of the individual particles of the lunar regolith existed the crescent Moon should be brighter per unit area than the full Moon. In fact, however, the Moon is difficult to observe when less than a day from new and has never been reported at less than 7° from new.

It would appear to be a hopeless task to calculate the exact Fresnel diffraction pattern behind all of the irregularly shaped particles in a layer of close-packed powder. However, it may be assumed that particles randomly located behind the layer are statistically equally illuminated by all the different parts of the diffraction pattern. Thus, a reasonable approximation is to average the transmitted light over the whole pattern of shadows and ripples and replace it by a uniform wave front that is reduced from the incident intensity in proportion to the fraction of area occupied by the open spaces between the particles. This is equivalent to removing the diffraction pattern from  $\Pi(g)$  and renormalizing the undiffracted remainder according to equation (5.13). Similarly,  $Q_d = 1$  must be subtracted from  $Q_S$  and  $Q_E$ , and w recalculated, so that now

$$w = \frac{Q_s}{Q_s + Q_A}. (7.41)$$

For particles much larger than the wavelength  $Q_E = Q_s + Q_A \approx 1$ , so  $w \approx Q_s$ . In the remainder of this book it will be assumed that  $Q_d = 0$  whenever we are dealing with a close-packed powder.

### 7.4.3 Coherent effects in a close-packed medium

As discussed in Section 5.3, when light is incident on a particle the space outside the surface within roughly a wavelength contains near and evanescent fields. If the filling factor of the medium is low these fields do not carry energy away from a particle. However, if two particles are so close that portions of their surfaces are nearly touching then, as discussed in Chapter 4, the near fields of one particle can induce charges and currents on the adjacent surface of the other particle and transfer energy from one particle to the other, which constitutes a form of scattering. As the porosity decreases chains and clumps of particles begin to act collectively like a single, larger particle. These effects are illustrated in several papers giving exact solutions of scattering by many-particle systems using the T-matrix method (Mishchenko, 1995; Mackowski and Mishchenko, 1996; Tishkovets et al., 1997, 2004; Mishchenko et al., 2007).

From the definitions in Section 7.3.1 the average center-to-center spacing between particles is L. Thus the statistical condition for particles in a close-packed medium to be within about a wavelength of each other is  $L - D < \lambda$ , where D is the average particle size. Dividing by D and cubing gives

$$\left(\frac{L}{D}\right)^3 = \frac{1}{ND^3} = \frac{\pi/6}{\phi} < \left(1 + \frac{\lambda}{D}\right)^3,$$

or

$$\phi > \frac{\pi/6}{(1+\lambda/D)^3} = \frac{0.524}{(1+\lambda/D)^3}.$$
 (7.42)

Equation (7.42) is plotted in Figure 7.5. It shows that when  $D >> \lambda$  collective effects might be expected to occur when the filling factor is greater than about 50%, but should be important in all close-packed media in which particles of the order of the wavelength and smaller are abundant. Below the line the medium may be considered to be a nearly continuous void containing some solid particles. Above the line the optical properties begin to change over to those of a nearly continuous solid containing some void spaces.

Another coherent phenomenon called weak localization or coherent backscattering also occurs in particulate media. This will be discussed in detail in Chapter 9.

### 7.4.4 The transmissivity of a particulate medium

It was seen in Section 7.3 that the transmissivity function in a sparsely packed particulate medium is (equation 7.25),  $T(s) = I(s)/I(0) = \exp(-Es)$ , where E =

<!-- IMAGE: _page_19_Figure_2.jpeg -->

Figure 7.5 Critical filling factors vs.*D/*λ, showing the regions where collective and coherent interference effects are important and where the medium becomes opaque to directly transmitted radiance.(Reproduced from Hapke [\[2008\]](#page-0-0), copyright 2008, with permission of Elsevier.)

*N*σ*QE* is the extinction coefficient. However, in a medium where the particles are close together this expression is incorrect.

Ishimaru and Kuga (1982) measured the extinction coefficient as a function of filling factor for colloidal suspensions of latex spheres of sizes ranging from about λ*/*6 to 26λ. The results are shown in Figure 7.6, which plots the ratio of the extinction coefficients measured at various filling factors to the coefficient when the suspension is dilute. As expected from the discussion of the previous section, the coefficient for particles comparable and smaller than the wavelength decreases with increasing filling factor φ as collective effects become more and more important. However, for particles larger than the wavelength the extinction coefficient increases as the particles come closer together.

The reason that equation (7.25) is incorrect is that it assumes that the fraction of light blocked by particles in a thin slab of thickness *ds* is negligible compared with the fraction of open space. While this is a valid assumption for a sparsely packed medium it is not true when the particles are close together. In Hapke (1986, 1993) it was proposed that *E* be replaced by !*Eln(*1–φ*)/*φ. However, this expression is only approximate. A more rigorous expression can be derived as follows.

<!-- IMAGE: _page_20_Figure_2.jpeg -->

Figure 7.6 Ratio of the extinction coefficients of colloidal suspensions of latex spheres with varying filling factors to that in a low-density medium vs. filling factor  $\phi$ . The numbers give the ratio of particle diameter to wavelength. The solid line is the theoretical expression (7.45b). (Data from Ishimaru and Kuga [1982].)

According to the discussion in Section 7.3.1 a particulate medium may be thought of as being made up of a lattice of imaginary cubes with edges of length L, with the center of each particle located somewhere inside each cube. In order that the particles do not overlap each cube can contain only one particle. Consider a wave of radiance I(s) propagating through the medium as it passes through a slab of area A and thickness L containing a representative distribution of particles and oriented perpendicularly to the direction of propagation. The slab contains NAL particles with extinction cross sections  $\sigma Q_E$ , where N is the number of particles per unit volume. Then the amount of light that encounters particles in the volume and is extinguished is  $A\Delta I_E = I(NAL)\sigma Q_E = AIEL$ . The amount that is transmitted between the particles is  $A\Delta I_T = A1 - A\Delta I_E = AI(1-EL)$ . Hence, the fraction of the radiance incident on the slab that is unobstructed and transmitted is  $\Delta I_T/I = 1-EL$ .

Assuming that the particles are randomly positioned within each box, the probability of transmission through several layers is the product of the individual probabilities. Hence, the fraction of light remaining after traversing a distance s consisting of N = s/L layers is

$$T(s) = (1 - EL)^N = \exp[N \ln(1 - EL)] = \exp(-KEs),$$
 (7.43)

where

$$K = -\ln(1 - EL)/EL. \tag{7.44}$$

is the *porosity coefficient*. Equation (7.43) is illustrated in Figure 7.7, where it is seen to be a discontinuous stair function. The physical meaning of *T (s)* is that the radiance on a particle located anywhere between *s* = *NL* and *s* = *(N* + 1*)L* is *I (*0*)(*1–*EL)N* , where *I (*0*)* is the radiance incident on the first layer.

The quantity *K* is ≥ 1 everywhere. Expanding *K* in a Taylor series,

$$K = 1 + \frac{1}{2}EL + \frac{1}{3}(EL)^2 + \cdots$$

shows that *K* → 1 only when the medium is so sparsely packed that *EL* . 1. For comparison, Figure 7.7 also plots the transmissivity of a sparse continuous medium, equation (7.25). Note that although the transmissivity of a continuous medium falls off less rapidly, the upper layers of a particulate medium actually receive more

<!-- IMAGE: _page_21_Figure_8.jpeg -->

Figure 7.7 Transmissivities vs. number of the layer *N* = *s/L*for the case *EL* = 0*.*4. The discontinuous stair function, equation (7.43), is plotted as the solid line, and its continuous approximation, equation (7.46), as the dashed line. For comparision the transmissivity of a continuous medium, equation (7.25), is shown as the dotted line.(Reproduced from Hapke \[2008], copyright 2008, with permission of Elsevier Publishing Co.)

illumination than the same thickness of a continuous medium. Now,

$$EL = N\sigma Q_E L = N^{2/3}\sigma Q_E = \left[N(\sigma Q_E)^{3/2}\right]^{2/3} = \left[\sum_j N_j v_j \frac{(\sigma_j Q_{Ej})^{3/2}}{v_j}\right]^{2/3}.$$

If the particles are equant  $[\sigma_j^{3/2}/v_j]^{2/3} \approx [\pi^{3/2}/(4\pi/3)]^{2/3} = 1.209$ , and for particles large compared to the wavelength,  $Q_{Ei} \approx 1$ . Thus

$$EL \approx 1.209 \left( \sum_{j} N_{j} v_{j} \right)^{2/3} = 1.209 \phi^{2/3},$$
 (7.45a)

and

$$K = \frac{-\ln(1 - 1.209\phi^{2/3})}{1.209\phi^{2/3}}.$$
 (7.45b)

The medium becomes opaque when EL = 1 or  $\phi = 1.209^{-3/2} = 0.752$ , even though the porosity is >0. This limit is shown in Figure 7.5. In the opposite limit of small EL equation (7.43) becomes the continuous exponential function  $\exp(-Es)$ . Equation (7.45b) for K is plotted as the solid line in Figure 7.6.

A convenient approximation to K if the filling factor is not too large is given by

$$K = 1 + EL/2 + (EL)^{2}/3 + \cdots$$

$$= \{1 - [EL/2 + (EL)^{2}/3 + \cdots] + [EL/2 + (EL)^{2}/3 + \cdots]^{2} + \cdots\}^{-1}$$

$$= \{1 - EL/2 + (EL)^{2}/12 + \cdots\}^{-1}$$

At the upper limit of  $\phi \approx 0.5$  for coherent limits to be negligible,  $(EL)^2/12 = 3.7\%$ . Thus to within an error of <4%,

$$K \approx 1/(1 - EL/2) = 1/(1 - 0.605\phi^{2/3}).$$
 (7.45c)

### 7.4.5 Radiative transfer in a particulate medium of arbitrary filling factor

If the medium is continuous the equation of radiative transfer takes the form of equation (7.38), in which the various parameters are simply constants of the medium that must be specified. When the medium consists of widely spaced particulates the same form of the equation of radiative transfer may be used, in which the parameters are determined by the properties of the particles making up the medium as defined in Section 7.3.2. However, as the filling factor increases, the radiative transfer equation in its usual form, equation (7.38) is no longer correct.

Consider radiance  $I(z,\Omega)$  propagating through a horizontally stratified, isotropic particulate medium at a depth z in a direction  $\Omega$  making an angle  $\vartheta$  with the vertical z-axis. Thermal radiation will be neglected. Then the changes  $\Delta I(z,\Omega)$  in the radiance as it passes through a monolayer of particles of thickness  $\Delta s = L$  perpendicular to  $\Omega$  are

$$\Delta I(z,\Omega) = -ELI(z,\Omega) + \frac{wEL}{4\pi} \int_{4\pi} I(z,\Omega') p(g') d\Omega' + J \frac{SL}{4\pi} T(z/\cos i),$$

where T(s) is given by equation (7.43). This expression is a difference equation. In order to make it more analytically tractable it is desirable to approximate it by a quasi-continuous medium model. In order to do this we will make two assumptions. This first is that to a sufficient approximation I(s) statistically varies linearly through a layer of thickness L. Then  $\Delta I$  may be written

$$\Delta I(z,\Omega) = \frac{\Delta I(z,\Omega)}{\Delta s} L \approx \frac{\partial I(z,\Omega)}{\partial s} L = \cos\vartheta \frac{\partial I(z,\Omega)}{\partial z} L = -\cos\vartheta \frac{\partial I(z,\Omega)}{\partial \tau} EL.$$

The second assumption is that the discontinuous transmissivity function can be approximated by a continuous one. If s is allowed to be a continuous variable the function  $\exp(-KEs)$  falls off correctly with s; however, this function passes through the left edges of each step, so that the average illumination on any given layer is too low. In order to correct this we replace the simple exponential by  $C \exp(-KEs)$ , where C is a constant determined by requiring that the radiance,  $I(0)(1-EL)^N$ , incident on a particle located between s=NL and s=(N+1)L in the discontinuous function, be equal to the average radiance,  $(I(0)/L)\int_{NL}^{(N+1)L} C \exp(-KEs) ds$ , between these two distances in the continuous function. This gives C=K. Hence, the transmissivity function becomes

$$T(s) = K \exp(-KEs), \tag{7.46}$$

where K is given by (7.44) and T(s) is now assumed to be continuous; if the medium consists of equant particles EL is given by (7.45a). Equation (7.46) is plotted in Figure 7.7, where it is seen to pass through the central points of each step.

If the medium consists of spherical particles all of one size K can also be derived numerically from a quantity called the structure factor using the Percus-Yevic pair correlation function (Mishchenko and Macke, 1997). However, equation (7.43) is much more general and applies to particles of any shape and arbitrary size distribution. It also has the advantage of being analytic.

Making these assumptions the quasi-continuous approximation to the radiative transfer equation (7.38) becomes

$$-\cos\vartheta \frac{\partial I(\tau,\Omega)}{\partial \tau} = -I(\tau,\Omega) + \frac{w}{4\pi} \int_{4\pi} I(\tau,\Omega') p(g') d\Omega' + J \frac{w}{4\pi} p(g) K e^{-K\tau/\mu_0},$$
(7.47)

where g is the phase angle between  $\Omega_0$  and  $\Omega$ , and g' is the phase angle between  $\Omega'$  and  $\Omega$ . This equation has the same form as the usual equation of radiative transfer except for the factors of K in the last term and the implicit lack of a Fraunhofer contribution to w and p(g).

### 7.4.6 Mean free paths in a particulate medium

The extinction mean free path in a particulate medium can be readily computed.

$$\Lambda_{E} = \frac{\int_{0}^{\infty} sT(s)ds}{\int_{0}^{\infty} T(s)ds} = \frac{\sum_{N=0}^{\infty} \int_{N}^{N+1} s(1-EL)^{N} ds}{\sum_{N=0}^{\infty} \int_{N}^{N+1} (1-EL)^{N} ds} = \frac{\sum_{n=0}^{\infty} (N+1/2)L(1-EL)^{N}}{\sum_{N=0}^{\infty} (1-EL)^{N}}$$

$$= \frac{L(1-EL)[1+2(1-EL)+(1-EL)^{2}+\cdots]+(1/2)[1+(1-EL)+(1-EL)^{2}+\cdots]}{1+(1-EL)+(1-EL)^{2}+\cdots}$$

$$= \frac{L(1-EL)[1-(1-EL)]^{-1}}{[1-(1-EL)]^{-1}} + \frac{1}{2} = \frac{1-EL/2}{E}.$$
(7.48a)

Thus, in a particulate medium the extinction mean free path is reduced by a factor of (1-EL/2) over that of a continuous medium. If the quasi-continuous approximation to the transmissivity, equation (7.46), is used to compute  $\Lambda_E$ , the expression

$$\Lambda_E = \frac{\int_0^\infty sK \exp(-KEs)ds}{\int_0^\infty K \exp(-KEs)ds} = \frac{1}{KE}$$
 (7.48b)

is obtained. Equations (7.45) shows that (7.48a) and (7.48b) are equal to within an error of < 4%. For internal consistency, equation (7.48b) will be used whenever the quasi-continuous approximation is employed.

The absorption, scattering, and transport mean free paths are given by relations identical to (7.48b). In particular the transport mean free path is

$$\Lambda_T = 1/KS(1 - \xi). \tag{7.48c}$$

## 7.5 Methods of solution of radiative-transfer problems 7.5.1 Introduction

The equation of radiative transfer is a linear integrodifferential equation. In spite of the fact that it is one of the most important equations in astrophysics and remote sensing, it has proved to be remarkably intractable, and no exact analytic solution in closed form has been obtained. Therefore, numerical computer methods must be used if a high degree of accuracy is desired; otherwise one must be satisfied with approximate analytic solutions. It must be emphasized again that when equation

(7.38) is used to find the radiance in particulate media the solutions implicitly apply to averages over dimensions in the media that are large compared with both the wavelength and the particle separation and assume that the particles are well separated.

A large number of different methods have been developed to obtain solutions of the radiative transfer equation of varying degrees of accuracy. These are reviewed in Lenoble (1985) and utilized in many references, including Ambartsumian (1958), Chandrasekhar (1960), Kourganoff (1963), Hansen and Travis (1974), Sobolev (1975), Ishimaru (1978), Van de Hulst (1980), Gerstl and Zardecki (1985a), and Mishchenko *et al.* (1999). The reader is referred to those works for details of a particular method. In this section I will outline a few that are widely used.

### 7.5.2 The Monte Carlo method

This numerical method is potentially the most accurate, especially for complicated geometries (including spherical atmospheres) and highly anisotropic particle phase functions, but requires large amounts of computer time. Photons are injected into the medium, and at each computational step they are presented with a probability of being scattered through a given angle or absorbed. Each photon is followed until it either is absorbed or leaves the medium. The process is continued until adequate statistics are built up for all directions of scattering. Photons that contribute to the observed brightness can be calculated as if they travel either from the source to the detector or in the opposite direction, as convenient.

Although the accuracy of this method is high, in order to use it one must specify the detailed position, orientation, and shape of each object in addition to its scattering properties. This is seldom known in either remote-sensing or laboratory applications, where a statistical description of the properties of the scatterers is usually all that is available.

### 7.5.3 The radiosity method

The radiosity (Borel *et al.*, 1991) of a differential area is defined as the sum of the radiance emitted and reflected from that area, plus the total radiance scattered and transmitted onto the area from other differential areas. An energy-balance equation is set up for each object in the medium. This gives *N* coupled differential equations, where *N* is the number of objects. The same advantages and disadvantages as in the Monte Carlo method also applies to this technique.

### 7.5.4 The doubling method

This numerical method was pioneered by Van de Hulst (1980) and is widely used in calculations of radiative transfer in planetary atmospheres (e.g., Hansen and Travis, 1974) and other horizontally stratified media. It is efficient in computer time and is especially useful when the particle phase function is anisotropic. The polarization as well as the intensity can be readily calculated. The concept is simple, although its practical realization may be complicated. Suppose the amount of light scattered into all angles by a layer of finite optical thickness illuminated from all directions is known. The method uses a general algorithm that calculates the amount of light scattered into all angles by two identical layers of known reflectance and transmittance, when the top layer is illuminated from a single direction above it.

The calculation starts with a layer that is so thin that its reflectance and transmittance into all angles from sources incident on it from all directions can be written down by inspection. A typical optical thickness might be  $2^{-25}$ . A second, identical layer is added, and the reflectance and transmittance of the combined layers are calculated using the algorithm. This layer is again doubled and the process continues until the desired thickness is obtained. For instance, if the properties of a layer of optical thickness  $2^{+25}$  are desired, only 50 repetitions of the algorithm are required. The technique is readily modified to allow calculations of layers of differing properties.

### 7.5.5 The Eddington approximation

In this method the solution of the radiative-transfer equation is assumed to be of the form  $I(\tau,\Omega) = I_0(\tau) + I_1(\tau)\cos\vartheta$ . This solution is substituted into (7.38), and the resulting equation is integrated over solid angle, giving one equation in  $I_0(\tau)$  and  $I_1(\tau)$ . Next this solution is multiplied by  $\cos\vartheta$ , substituted into (7.38), and integrated over  $\Omega$ , giving a second equation for  $I_0(\tau)$  and  $I_1(\tau)$ . The resulting equations are

$$-\frac{1}{3}\frac{dI_{1}(\tau)}{d\tau} = -I_{0}(\tau) + w[I_{0}(\tau) + \xi I_{1}(\tau)] + Jwe^{-\tau/\cos i} + 4\pi F_{T}(\tau)$$

and

$$-\frac{1}{3}\frac{dI_{0}(\tau)}{d\tau} = -\frac{1}{3}I_{1}(\tau) + Jw\xi e^{-\tau/\cos i},$$

where  $\xi$  is the cosine asymmetry factor. The two equations may then be solved simultaneously.

### 7.5.6 Integral equation formulation

The partial differential equation (7.38) can be converted into an integral equation as follows. The term on the left plus the first term on the right-hand side of the equation can be put into the form:

$$-\cos\vartheta \frac{\partial I(\tau,\Omega)}{\partial \tau} + I(\tau,\Omega) = -\cos\vartheta e^{\tau/\cos\vartheta} \frac{\partial}{\partial \tau} [e^{-\tau/\cos\vartheta} I(\tau,\Omega)].$$

Hence, the radiative-transfer equation can be written

$$\frac{\partial}{\partial \tau} \left[ e^{-\tau/\cos\vartheta} I(\tau,\Omega) \right] = -\frac{e^{-\tau/\cos\vartheta}}{\cos\vartheta} \left[ \frac{w(\tau)}{4\pi} \int_{4\pi} I(\tau,\Omega') p(\tau,\Omega',\Omega) d\Omega' + F(\tau,\Omega) \right].$$

To find the radiance at optical depth  $\tau$  both sides must be integrated between 0 and  $\infty$ 

For  $\cos\theta < 0$  the radiance is traveling in the downward direction so that it all comes from levels between 0 and  $\tau$ , and the boundary condition is that there are no sources of multiply scattered radiance above  $\tau = 0$ . For  $\cos\theta > 0$  the radiance is traveling in the upward direction and it all comes from levels between  $\tau$  and  $\infty$ ; the boundary condition is that the radiance remains finite as  $\tau \to \infty$ . This gives

$$\begin{split} I(\tau,\Omega) &= -\left\{\frac{e^{\tau/\cos\vartheta}}{\cos\vartheta} \int_0^\tau \left[\frac{w(\tau')}{4\pi} \int_{4\pi} I(\tau',\Omega') p(\tau',\Omega',\Omega) d\Omega' + F(\tau',\Omega)\right] e^{-\tau'/\cos\vartheta} d\tau'\right\}_{\cos\theta < 0} \\ &+ \left\{\frac{e^{\tau/\cos\vartheta}}{\cos\vartheta} \int_\tau^\infty \left[\frac{w(\tau')}{4\pi} \int_{4\pi} I(\tau',\Omega') p(\tau',\Omega',\Omega) d\Omega' + F(\tau',\Omega)\right] e^{-\tau'/\cos\vartheta} d\tau'\right\}_{\cos\theta > 0}. \end{split}$$

This may be solved using the method of successive approximations. A trial solution for  $I(\tau', \Omega')$  is inserted into the double integral on the right-hand side of (7.38), and a new solution is calculated, either analytically or numerically. This procedure is repeated until the desired accuracy is obtained.

### 7.5.7 The multistream method

The multistream method, also called the discrete ordinates method, can be as accurate as computer time allows. An example is the DISORT program (Stamnes et al., 1988). However, it is also useful for obtaining approximate solutions of the radiative transfer equation. The sphere of all propagation directions  $\Omega$  is broken up into  $\mathcal N$  regions of solid angle  $\Delta\Omega_j$ , which need not be equal. The equation of radiative transfer, equation (7.38), is integrated in solid angle over each of the regions  $\Delta\Omega_j$  and each resulting equation divided by  $\Delta\Omega_j$ , giving N equations of the form

$$-\frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} \frac{\partial I(\tau, \Omega)}{\partial \tau} \cos \vartheta d\Omega = -\frac{1}{\Delta\Omega_{j}} \frac{\partial}{\partial \tau} \int_{\Delta\Omega_{j}} I(\tau, \Omega) \cos \vartheta d\Omega$$

$$= -\frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} I(\tau, \Omega) d\Omega + \frac{w}{4\pi} \frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} \int_{4\pi} p(g') I(\tau, \Omega') d\Omega' d\Omega \quad (7.49)$$

$$+ J \frac{w}{4\pi} e^{-\tau/\cos i} \frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} p(g) d\Omega + \frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} F_{T}(\tau) d\Omega.$$

Define the following average quantities for the *j*th zone:

$$I_{j}(\tau) = \frac{1}{\Delta\Omega_{j}} \int_{\Delta\Omega_{j}} I(\tau, \Omega) d\Omega, \tag{7.50}$$

$$\mu_j = \frac{1}{\Delta\Omega_j} \int_{\Delta\Omega_j} \cos\vartheta \ d\Omega, \tag{7.51}$$

$$p_{kj} = \frac{1}{\Delta\Omega_k} \frac{1}{\Delta\Omega_j} \int_{\Delta\Omega_k} \int_{\Delta\Omega_j} p(g') \, d\Omega' d\Omega, \tag{7.52}$$

$$F_{I_j}(\tau) = \frac{1}{\Delta\Omega_j} \int_{\Delta\Omega_j} F_T(\tau, \Omega) d\Omega.$$
 (7.53)

Note that  $p_{kj}$  is the fraction of the radiance traveling in the direction of the center of region k that is scattered into region j.

In (7.49),  $I(\tau, \Omega)$  is replaced by its average value  $I_j(\tau)$ , which may then be taken out of the integrals over angle. Then the equation for the intensity in the jth directional region becomes

$$\mu_{j}dI_{j}(\tau)/d\tau = -I_{j}(\tau) + (w/4\pi) \sum_{k=1}^{N} \Delta\Omega_{k} p_{kj} I_{k}(\tau) + J \frac{w}{4\pi} p_{mk} e^{-\tau/\cos i} + F_{Tj}(\tau), \qquad (7.54)$$

where the region  $\Omega_m$  contains the direction to the collimated source, and j takes all integer values between 1 and N. Thus, the partial integrodifferential equation (7.38) is replaced by a series of N linear, first-order, coupled differential equations that are amenable to well-established numerical solution. In principle, the mesh can be made as fine as computer time allows, and the calculations can approximate the exact solution as closely as desired.

If N is small enough, the equations can be solved analytically. In particular, if N = 2, the method is known as the two-stream or Schuster–Schwarzschild method (Schuster, 1905). It will be used extensively in this book.

The multistream method was used by Chandrasekhar (1960) in his classic treatise on radiative transfer. The directional sphere is divided into N regions in polar angle  $\vartheta$ , where N is an even integer. The boundaries are chosen to be the zeros of  $P_{\mathcal{N}}(\cos\vartheta)$ , the Legendre polynomial of order N. It was shown by Gauss that this choice of fixing the boundaries results in an approximation that is accurate to order 2N, and the technique is known as the method of Gaussian quadratures.

For example, for isotropic scatterers [p(g) = 1] and  $F_T = 0$ , in each region equation (7.49) has a solution of the form  $I(\tau, \Omega) = Ae^{-a\tau}/[1 + a\cos\vartheta] + Be^{-\tau/\cos i}/(1 + \cos\vartheta/\cos i)$ . However, this solution cannot be made to satisfy the boundary conditions if the quantities A, B, and a are the same for all directions.

In Chandrasekhar's method the solution is forced to be of this form within each Gaussian region, but the "constants" are different in different regions.

### 7.5.8 The method of invariance

The method of invariance was pioneered by Ambartsumian (1958) in his classic treatise on radiative transfer. Although it is not derived directly from the equation of radiative transfer, Chandrasekhar (1960) showed that it gives the same answer. It allows one to obtain exact expressions for the reflectance and emittance of a horizontally stratified, semi-infinite particulate medium without explicitly solving the radiative-transfer equation. It relies on the fact that the reflectance of, or thermal emission from, an infinitely thick medium is not changed by adding a thin identical layer to the top of the original surface.

Denote the direction from the surface of the medium to a distant source by  $\Omega_0=\Omega(i,\psi_0)$ , and the direction to a distant detector by  $\Omega=\Omega(e,\psi_e)$ . The direction of the incident ray is exactly opposite the direction to the source and is denoted by  $\Omega_i=\Omega\iota(i_i=\pi-i,\psi\iota=\pi+\psi_0)$ . Then the bidirectional reflectance of the medium can be denoted by  $r(\Omega_0,\Omega)$  or  $r(\Omega_i,\Omega)$ , and the volume-average phase function by  $p(\Omega_0,\Omega)$  or  $p(\Omega_i,\Omega)$ , as convenient. Let a thin layer of identical material of thickness  $\Delta z$  be added to the top of the medium. Assume that its optical thickness  $\Delta \tau=-E\Delta z$  is so small that interactions of light with the layer involving powers of  $\Delta \tau$  greater than 1 can be ignored. Then the layer will cause five distinct changes that are each proportional to  $\Delta \tau$  in the scattered light. These changes are shown schematically in Figure 7.8.

(1) Light passing through the added layer is reduced by extinction (Figure 7.8a), once by a factor  $\exp(-\Delta \tau/\cos i)$  on the way in, and once by a factor  $\exp(-\Delta \tau/\cos e)$  on the way out. Thus, if this effect were the only one operating the emergent radiance would be

$$\begin{split} I = &J \exp \left[ -\Delta \tau \left( \frac{1}{\cos i} + \frac{1}{\cos e} \right) \right] r(\Omega_i, \Omega) \\ \simeq &J \left[ 1 - \Delta \tau \left( \frac{1}{\cos i} + \frac{1}{\cos e} \right) \right] r(\Omega_i, \Omega). \end{split}$$

Let  $\mu = \cos e$  and  $\mu_0 = \cos i$ . Then the first-order change in the emergent radiance is

$$\Delta I_1 = -J \Delta \tau \left(\frac{1}{\mu_0} + \frac{1}{\mu}\right) r(\Omega_i, \Omega)$$
 (7.55a)

<!-- IMAGE: _page_30_Figure_2.jpeg -->

Figure 7.8 Schematic diagram of the five first-order changes in the scattered radiance caused by adding a thin layer of optical thickness ςτ to the top of an infinitely thick medium of bidirectional reflectance *r*.

(2) The added layer scatters an additional amount of light toward the detector (Figure 7.8b). Consider a cylindrical volume coaxial with a scattered ray emerging from the layer in the direction toward the detector with unit cross-sectional area and length ς*z/µ*. Then there are *N*ς*z/µ* particles in the volume. Incident light *J* will be scattered by any particle with its center in this volume, and this scattered radiance will be added to the emergent radiance scattered by the lower medium. The increase in radiance due to this effect for particles having

<!-- IMAGE: _page_31_Figure_2.jpeg -->

Figure 7.8 (cont.)

a general phase function is

$$\Delta I_2 = JN\sigma Q_S \frac{\Delta z}{\mu} \frac{p(\Omega_i, \Omega)}{4\pi} = J \frac{wp(\Omega_i, \Omega)}{4\pi} \frac{\Delta \tau}{\mu}.$$
 (7.55b)

(3) Light scattered by the added layer in the downward direction is an additional source of illumination of the lower medium (Figure 7.8c). Consider a volume within the layer of unit cross-sectional area and length  $\Delta z/|\mu_i'|$  about a direction  $\Omega_i'(\mu_i',\psi_i)$ , where  $\mu_i'=\cos i_i'$  containing  $N\Delta z/|\mu_i'|$  particles. The radiance scattered by these particles into a downward direction incident on the lower

<!-- IMAGE: _page_32_Figure_2.jpeg -->

Figure 7.8 (cont.)

medium within a small increment of solid angle  $d\Omega_i' = \sin i_i' di_i' d\psi_i'$  about  $\Omega_i'$  is  $dI_i' = J[wp(\Omega_i, \Omega_i')/4\pi][\Delta \tau/|\mu_i'|]d\Omega_i'$ . An amount  $dI_i'r(\Omega_i', \Omega)$  is scattered by the lower medium into a direction toward the detector. To find the total additional light reflected, this quantity must be integrated over all  $\Omega_i'$  in the downward-going hemisphere. Hence,

$$\Delta I_3 = \int_{\Omega_i'} r\left(\Omega_i', \Omega\right) dI_i' = \int_{\Omega_i'} r(\Omega_i', \Omega) J \frac{wp(\Omega_i, \Omega_i')}{4\pi} \frac{\Delta \tau}{|\mu_i'|} d\Omega_i'.$$
 (7.55c)

(4) Light scattered upward by the lower medium illuminates the added layer (Figure 7.8d), which scatters some of this light toward the detector. The light scattered by the medium into an increment of solid angle  $d\Omega' = \sin e' de' d\psi'$  around a direction  $\Omega'$  is  $dI'_e = Jr(\Omega_i, \Omega')d\Omega'$ . This light illuminates a cylindrical volume of unit cross-sectional area containing  $N\Delta z/\mu$  particles in the layer coaxial with direction  $\Omega$ . The light scattered within the volume toward the detector is  $dI'_e[wp(\Omega', \Omega)/4\pi][(\Delta \tau/\mu]$ . Integrating this over all  $\Omega'$  in the upward-going hemisphere gives

$$\Delta I_4 = \int_{\Omega'} \frac{wp(\Omega', \Omega)}{4\pi} \frac{\Delta \tau}{\mu} dI'_e = \int_{\Omega'} Jr(\Omega_i, \Omega') \frac{wp(\Omega', \Omega)}{4\pi} \frac{\Delta \tau}{\mu} d\Omega'. \quad (7.55d)$$

(5) Light scattered upward by the lower medium is scattered back down by the added layer and provides an additional source of illumination of the lower

medium (Figure 7.8e). An amount of light  $dI'' = Jr(\Omega_i, \Omega'')d\Omega''$  is scattered by the lower medium upward into solid angle  $d\Omega'' = \sin e'' de'' d\psi''$  about a direction  $\Omega''$ . This light illuminates a cylindrical volume in the added layer containing  $N\Delta z/|\mu_i''|$  particles in the layer coaxial with direction  $\Omega_i''$  that scatter light downward toward the lower medium and illuminate it with light of intensity  $dI_{ie} = dI_e'' [wp(\Omega'', \Omega_i'')/4\pi] [\Delta \tau/|\mu_i''|] d\Omega_i''$  where  $d\Omega_i'' = \sin i_i'' di_i'' d\psi_i''$ . An amount of light  $dI_{ie}r(\Omega_i'', \Omega)$  is scattered into a direction toward the detector. The total amount of light due to this effect is

$$\Delta I_{5} = \int_{\Omega''} \int_{\Omega''_{i}} r\left(\Omega''_{i}, \Omega\right) dI_{ie}$$

$$= \int_{\Omega''_{i}} \int_{\Omega''} Jr(\Omega_{i}, \Omega'') \frac{wp(\Omega'', \Omega''_{i})}{4\pi} \frac{\Delta \tau}{|\mu''_{i}|} r(\Omega''_{i}, \Omega) d\Omega'' d\Omega''_{i}, \quad (7.55e)$$

where  $\Omega''$  is integrated over the entire upward-going hemisphere and  $\Omega''_i$  is integrated over the entire downward-going hemisphere.

The sum of the changes  $\Delta I_1$  through  $\Delta I_5$  must be zero. Hence,

$$\frac{\mu_{0} + \mu}{\mu_{0}\mu} r(\Omega_{i}, \Omega) = \frac{wp(\Omega_{i}, \Omega)}{4\pi \mu} + \int_{\Omega'_{i}} r(\Omega'_{i}, \Omega) \frac{wp(\Omega_{i}, \Omega'_{i})}{4\pi |\mu'_{i}|} d\Omega'_{i} + \int_{\Omega'} r(\Omega_{i}, \Omega') \frac{wp(\Omega', \Omega)}{4\pi \mu} d\Omega' + \int_{\Omega_{i}} \int_{\Omega''} r(\Omega_{i}, \Omega'') \frac{wp(\Omega'', \Omega''_{i})}{4\pi |\mu''_{i}|} r(\Omega''_{i}, \Omega) d\Omega'' d\Omega''_{i}.$$
(7.56)

Let  $\Omega_0'$  and  $\Omega_0''$  be the directions opposite to  $\Omega_i'$  and  $\Omega_I''$ , respectively. Then  $|\mu_i'| = \mu_0'$  and  $|\mu_i''| = \mu_0''$ . Define the function  $L(\Omega_i, \Omega)$  by

$$r(\Omega_i, \Omega) = \frac{w}{4\pi} \frac{\mu_0}{\mu_0 + \mu} L(\Omega_i, \Omega). \tag{7.57a}$$

Making these substitutions, equation (7.56) can be put into the form

$$L(\Omega_{i}, \Omega) = p(\Omega_{i}, \Omega) + \frac{w}{4\pi} \mu \int_{\Omega_{i}'} p(\Omega_{i}, \Omega_{i}') \frac{L(\Omega_{i}', \Omega)}{\mu_{0}' + \mu} d\Omega_{i}'$$

$$+ \frac{w}{4\pi} \mu_{0} \int_{\Omega'} \frac{L(\Omega_{i}, \Omega')}{\mu_{0} + \mu'} p(\Omega', \Omega) d\Omega'$$

$$+ \left(\frac{w}{4\pi}\right)^{2} \mu_{0} \mu \int_{\Omega_{i}''} \int_{\Omega''} \frac{L(\Omega_{i}, \Omega'')}{\mu_{0} + \mu''} p(\Omega'', \Omega_{i}'') \frac{L(\Omega_{i}'', \Omega)}{\mu_{0}'' + \mu} d\Omega'' d\Omega_{i}''. \quad (7.57b)$$

Equations (7.57a) are the general form of the Ambartsumian invariance relation. They can be solved numerically for L and r.

## 7.6 Computer programs

The computer program Fresnel Diffraction Explorer created by Dean Dauger computes both Fresnel and Fraunhofer diffraction patterns for a variety of disk shapes. It can be downloaded at [http://daugerresearch. com/fresnel/index.shtml.](http://http://daugerresearch.com/fresnel/index.shtml)

The DISORT program uses the discrete ordinate method to compute the radiance within and emerging from a horizontally stratified medium. The properties of the layers can be different. It can be downloaded at ftp://climate1.gsfc.nasa. [gov/wiscombe/.](http://ftp://climate1.gsfc.nasa.gov/wiscombe/)

Mishchenko *et al.* (1999) have developed a code based on the invariance principle that calculates the reflectance of a medium consisting of spherical particles of arbitrary size and refractive index. It can be downloaded at [www.giss.nasa.gov/](http://www.giss.nasa.gov/~crimm/publications/) [crimm/publications/.](http://www.giss.nasa.gov/~crimm/publications/)