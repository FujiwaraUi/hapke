## The absorption of light

## 3.1 Introduction

The differential reflection and scattering of light as a function of wavelength form the basis of the science of reflectance spectroscopy. This chapter discusses the absorption of electromagnetic radiation by solids and liquids. The classical descriptions of absorption and dispersion are derived first, followed by a brief discussion of these processes from the point of view of quantum mechanics and modern physics. Finally, the various types of mechanisms by which light is absorbed are summarized.

## 3.2 Classical dispersion theory

### 3.2.1 Conductors: the drude model

The simplest model for absorption and dispersion by a solid isthat of Drude (1959). This model assumes that some of the electrons are free to move within the lattice, while the ions are assumed to remain fixed. These approximate the conditions within a metal. The average electric-charge density associated with the semifree electrons is equal to the average of that associated with the lattice ions, so that the total electric-charge density ρ*e* = 0. Because the quantum-mechanical wave functions of the conduction electrons are not localized in a metal, the local field *E*loc seen by the electrons is equal to the macroscopic field **E***e*. Thus, the force on each electron is –*e*0**E***e* ,where *e*0 is the charge of an electron. Assume that **E***e* is parallel to the *x*-axis.

In addition to the electric field, there is a force due to collisions of each electron with the lattice, resulting in nonradiative loss of energy. This force, which is proportional to the velocity *d***x***/dt* of the electron, but opposite in direction, may be characterized by a parameter ζ, defined such that the average collisional force on the electron is given by !2πζ*med***x***/dt,* where *me* is the mass of the electron, and **x** is the displacement of the electron relative to the lattice. Physically, it can be shown that ζ = 1*/*2π*t ,* where *t* is the mean time between collisions of the electron with the lattice;  $\Xi$  is called the *collision frequency*. The equation of motion of an electron is then

$$m_e d^2 \mathbf{x}/dt^2 + 2\pi \,\Xi m_e d\mathbf{x}/dt = -e_0 \mathbf{E}_e. \tag{3.1}$$

Assume that  $\mathbf{E}_e$  is a periodic wave described by  $\mathbf{E}_e = \mathbf{E}_{e0}e^{-2\pi ivt}$ , where  $\nu$  is the frequency, and we seek periodic solutions of (3.1) of similar form,  $\mathbf{x} = \mathbf{x}_0 e^{-2\pi ivt}$ . Substituting this form of  $\mathbf{x}$  into (3.1) gives

$$-4\pi^{2}v^{2}m_{e}\mathbf{x}_{0} - 4\pi^{2}im_{e}\Xi v\mathbf{x}_{0} = -e_{0}\mathbf{E}_{e0},$$
(3.2)

or

$$\mathbf{x}_0 = \frac{e_0/4\pi^2 m_e}{v^2 + i \Xi v} \mathbf{E}_{e0}.$$
 (3.3)

The amount  $\mathbf{x}_0$  by which the electron is offset from the ion lattice induces an electric dipole moment

$$\mathbf{p}_{e} = -e_{0}\mathbf{x}_{0} = -\frac{e_{0}^{2}/4\pi^{2}m_{e}}{v^{2} + i\Xi v}\mathbf{E}_{e} = \alpha_{e}\varepsilon_{e0}\mathbf{E}_{e0},$$
(3.4)

where  $\alpha_e$  is the electric polarizability. Thus,

$$\alpha_e = -\frac{e_0^2}{4\pi^2 m_e \varepsilon_{e0}} \frac{1}{\nu^2 + i \Xi \nu}.$$
 (3.5)

The electric susceptibility is  $\chi_e = N_e \alpha_e$ , where  $N_e$  is the free-electron density. Hence, the dielectric constant is

$$K_e = 1 + \chi_e = 1 - \frac{N_e e_0^2}{4\pi^2 m_e \varepsilon_{e0}} \frac{1}{\nu^2 + i \Xi \nu}.$$
 (3.6)

The factor  $N_e e_0^2/4\pi^2 m_e \varepsilon_{e0}$  has the dimensions of reciprocal time squared, and the square root of this quantity is called the *plasma frequency*  $v_p$ ,

$$v_p = (N_e e_0^2 / 4\pi^2 m_e \varepsilon_{e0})^{1/2}.$$
(3.7)

Thus the dielectric constant may be written

$$K_e = 1 - v_p^2 / (v^2 + i \Xi v).$$
 (3.8)

The real and imaginary parts of  $K_e$  are, respectively,

$$K_{er} = n_r^2 - n_i^2 = 1 - v_p^2 / (v^2 + \Xi^2)$$
 (3.9)

and

$$K_{ei} = 2n_r n_i = \frac{v_p^2}{v^2 + \Xi^2} \frac{\Xi}{v},$$
 (3.10)

where  $n = n_r + in_i = \sqrt{K_e}$  is the refractive index and can be found from equations (2.84) and (2.85).

In most metals,  $\Xi \ll \nu_p$ , so that the real part of  $K_e$  becomes zero at or close to the plasma frequency. When this happens, the phase velocity becomes infinite. The physical meaning of a dielectric constant of zero is that true electromagnetic waves cannot propagate. The only disturbances that can occur in the medium are standing waves; these are called *plasma oscillations*.

If  $\nu \gg \nu_p$ , then  $K_{er} \to 1$  and  $K_{ei} \ll 1$ , so that the metal becomes transparent. Conversely, when  $\nu \ll \nu_p$ , both  $K_{er}$  and  $K_{ei}$  are large, and the material is opaque. In the limit of small  $\nu$ ,  $K_{ei} \simeq (\nu_p^2/\Xi\nu) = N_e e_0^2/4\pi^2 m_e \varepsilon_{e0} \Xi \nu$ . From equation (2.78),  $K_{ei}$  is related to the electrical conductivity  $\sigma_e$  by  $K_{ei} = \sigma_e/2\pi \nu \varepsilon_{e0}$ . When  $\nu$  is very small,  $\sigma_e$  is the direct-current (DC) conductivity  $\sigma_{DC}$ . Thus,

$$\Xi = 2\pi v_p^2 \varepsilon_{e0} / \sigma_{DC} = N_e e_0^2 / 2\pi m_e \sigma_{DC}.$$
 (3.11)

The plasma frequency  $\nu_p$  can be measured by noting where the metal becomes transparent, or it can be calculated by estimating  $N_e$  as the number of atoms per unit volume times the number of free electrons per atom, and using (3.7). The collision frequency  $\Xi$  can be measured from the DC conductivity, using (3.11).

### 3.2.2 Absorption in insulators: the Lorentz model

In nonconducting solids the electrons are not free to move through the lattice, but are localized by being bound to individual atoms. Because the wave functions of the electrons are localized in insulators,  $\mathbf{E}_{loc}$  must be used rather than  $\mathbf{E}_e$ . The equations of motion of the electrons contain all the terms of (3.1), plus a force describing the bonding of the electrons to lattice sites. The Lorentz model (Lorentz, 1952) assumes that this force is proportional to the displacement  $\mathbf{x}$  and is characterized by a parameter  $v_0$ , defined such that the restoring force is  $-4\pi^2 m_e v_0^2 \mathbf{x}$ . Then the equation of motion of an electron is

$$m_e d^2 \mathbf{x}/dt^2 + 2\pi m_e \Xi d\mathbf{x}/dt + 4\pi^2 m_e v_0^2 \mathbf{x} = -e_0 \mathbf{E}_{loc}.$$
 (3.12)

This equation is identical with that of a mass moving in a potential well of parabolic shape, and the Lorentz model is sometimes referred to as the parabolic-well model of electron oscillations.

The periodic solution to (3.9) with both  $\mathbf{E}_{loc}$  and  $\mathbf{x}$  proportional to  $e^{-2\pi i v t}$  is

$$-4\pi^{2}\nu^{2}m_{e}\mathbf{x}_{0} - 4\pi^{2}im_{e}\Xi\nu\mathbf{x}_{0} + 4\pi^{2}m_{e}\nu_{0}^{2}\mathbf{x}_{0} = -e_{0}\mathbf{E}_{loc0},$$
 (3.13)

which gives

$$\mathbf{x}_0 = \frac{e_0}{4\pi^2 m_e} \frac{1}{v_0^2 - v^2 - i\,\Xi \nu} \mathbf{E}_{\text{loc}0}.$$
 (3.14)

As in the Drude model, this gives

$$X_e = N_e \alpha_e = \frac{N_e e_0^2}{4\pi^2 m_e \varepsilon_{e0}} \frac{1}{\nu_0^2 - \nu^2 - i \Xi \nu} = \frac{\nu_p^2}{\nu_0^2 - \nu^2 - i \Xi \nu}.$$
 (3.15)

If  $\mathbf{E}_{loc} \neq \mathbf{E}_e$ , but the Clausius–Mossotti relation is valid,

$$(K_e - 1)/(K_e + 2) = N_e \alpha_e/3 = (v_p^2/3)/(v_0^2 - v^2 - i \Xi v),$$
 (3.16)

or

$$K_e = [1 + (2\nu_p^2/3)/(\nu_0^2 - \nu^2 - i\,\Xi\nu)]/[1 - (\nu_p^2/3)/(\nu_0^2 - \nu^2 - i\,\Xi\nu)]. \tag{3.17}$$

Usually in the Lorentz model it is assumed, without particular justification, that  $\mathbf{E}_{loc} = \mathbf{E}_{e}$ . In that case,

$$K_e = 1 + \chi_e = 1 + N_e \alpha_e = 1 + \frac{N_e e_0^2}{4\pi^2 m_e \varepsilon_{e0}} \frac{1}{\nu_0^2 - \nu^2 - i \Xi \nu} = 1 + \frac{\nu_p^2}{\nu_0^2 - \nu^2 - i \Xi \nu}.$$
(3.18)

Then

$$K_{er} = n_r^2 - n_i^2 = 1 + \frac{\nu_p^2 (\nu_0^2 - \nu^2)}{(\nu_0^2 - \nu^2)^2 + \Xi^2 \nu^2},$$
(3.19)

and

$$K_{ei} = 2n_r n_i = \frac{v_p^2 \Xi \nu}{(v_0^2 - \nu^2)^2 + \Xi^2 \nu^2}.$$
 (3.20)

Equations (3.19) and (3.20) also describe absorption in solids by ion vibrations instead of electronic oscillations, except that the electron mass  $m_e$ , which occurs in the expression for the plasma frequency, must be replaced by the reduced mass of the negative ions with respect to the positive ions in the molecule. Usually an absorption band is superimposed on a continuum real dielectric constant  $K_{ec}$ . In that case the term equal to 1 in equation (3.19) is replaced by  $K_{ec}$  or  $n_c^2 = K_{ec}$ .

Figures 3.1 and 3.2 give an example of the variations of  $K_{er}$ ,  $K_{ei}$ ,  $n_r$ , and  $n_i$  with  $\nu$  for a solid that obeys the Lorentz model. The dielectric constant and refractive index have a resonance at  $\nu = \nu_0$ . Note that over most of the range of  $\nu$ ,  $K_{er}$  increases as  $\nu$  increases; this is called *normal dispersion*. However, near  $\nu_0$ ,  $K_{er}$  decreases as  $\nu$  increases; this is called *anomalous dispersion*. Note that  $K_{er}$  can be negative in this region, but  $n_r$  and  $n_i$  are positive.

If the absorption band is strong enough,  $n_r$  can be <1 on the high-frequency side of the absorption band. This means that the wave velocity is  $c_0/n_r > c_0$ , which would appear to violate the theory of special relativity. However,  $c_0/n_r$  is the phase velocity, the speed with which the peaks of the wave move. It can be shown that the power and information content conveyed by the wave always move with velocity  $\leq c_0$ .

<!-- IMAGE: _page_4_Figure_2.jpeg -->

Figure 3.1 Real and imaginary parts of the dielectric constant in the vicinity of a strong absorption band, according to the Lorentz model. This example is calculated for ν*p/*ν0 = 1*.*2 and ζ*/*ν0 = 0*.*1*.*

<!-- IMAGE: _page_4_Figure_4.jpeg -->

Figure 3.2 Real and imaginary parts of the refractive index in the vicinity of a strong absorption band for a material with the dielectric constant of Figure 3.1.

The width of the region of anomalous dispersion may be found by setting the derivative of (3.19) to zero,  $dK_{er}/d(v^2)=0$ , to obtain the frequencies  $v_m$  where  $K_e$  is either maximum or minimum. This gives  $v_0^2-v_m^2=\pm\Xi v_0$ . Assuming that the region is narrow,  $v_0^2-v_m^2=(v_0-v_m)(v_0+v_m)\simeq (v_0-v_m)\cdot 2v_0$ . Thus,  $|v_0-v_m|=\Xi/2$ , and the full width of the region of anomalous dispersion is  $\Xi$ .

At  $v = v_0$ ,  $K_{er} = 1$  and  $K_{ei} = v_p^2/\Xi v_0$ ;  $K_{ei}$  has a maximum at  $v_0$ . Assuming  $\Xi \ll v_0$ , when  $v \ll v_0$ ,  $K_{er} \simeq 1 + v_p^2/v_0^2$ , which is constant, and  $K_{ei} \simeq v_p^2 \Xi v/v_0^4$ , so that  $K_{ei}$  goes to zero linearly with v. When  $v \gg v_0$ ,  $K_{er} \simeq 1 - v_p^2/v^2$ , and  $K_{ei} \simeq v_p^2 \Xi/v^3$ . These latter expressions for  $K_{er}$  and  $K_{ei}$  are identical with (3.9) and (3.10) for the Drude model. This result may be interpreted to imply that at high frequencies the electrons are excited into states where they are not bound to discrete atoms and, as in a conductor, are free to move about the lattice.

In many substances electrons are bound to several different lattice sites with strengths characterized by resonant frequencies  $v_j$  and collision frequencies  $\Xi_j$ , and with  $N_{ej}$  electrons per unit volume bound to the *j*th resonance. In that case,

$$K_e = 1 + \frac{e_0^2}{4\pi^2 m_e \varepsilon_{e0}} \sum_j \frac{N_{ej}}{v_j^2 - v^2 - i \Xi_j \nu},$$
 (3.21)

where the  $N_{ej}$ s are subject to the sum rule

$$\sum_{i} N_{ej} = N_e. \tag{3.22}$$

### 3.2.3 Quantum-mechanical dispersion

The quantum-mechanical calculation of dispersion (Sokolov, 1967; Wooten, 1972), equivalent to the Lorentz model is carried out by solving Schrödinger's equation for an electron in a parabolic potential well. As is usual in quantum mechanics, it is found that not all frequencies of oscillation are possible; rather the electrons can exist only in discrete states separated by energies  $\Delta E_j = h_0 v_j$ , where  $h_0$  is Planck's constant. The applied electromagnetic-radiation field perturbs the energy levels, and the probability of an electron jumping from one state to another is calculated from the relative amplitudes of the wave functions associated with the two states. An equation identical with (3.21) is obtained, except that  $N_{ej}$  is replaced by  $N_e f_j$ , where  $f_j$  is the relative probability of a transition between two states separated by  $\Delta E_j$  and is called the *oscillator strength* of the transition. The  $f_j$ s are subject to the sum rule equivalent to (3.23),

$$\sum_{i} f_j = 1. \tag{3.23}$$

## 3.3 Dispersion relations

A dispersion relation is an equation that describes the frequency or wavelength dependence of an optical quantity. One example is equation (2.95), which relates the absorption coefficient to the imaginary part of the reflective index and the wavelength. Although this equation is often called *the* dispersion relation, it is only one of many. Another example is (3.19) and (3.20) for  $K_{er}$  and  $K_{ei}$  versus  $\nu$ , which, together with (2.84) and (2.85), can be used to calculate the angular dispersion of white light as it passes through a prism. The latter is, of course, the original meaning of "dispersion."

An important relation may be derived from equation (3.15) for  $K_e$  by mathematically allowing  $\nu$  to be a complex quantity. Then  $K_e-1$  has a singularity (that is, it becomes infinite) only when  $\nu^2+i\,\Xi\nu-\nu_0^2=0$  or  $\nu=[-i\,\Xi\pm(-\Xi^2+4\nu_0^2)^{1/2}]/2$ . If  $\Xi\ll\nu_0$ ,  $\nu\approx i\,\Xi/2\pm\nu_0$ . Because these singularities lie below the real axis,  $K_e-1$  is analytic in the upper half of the complex frequency plane. Also,  $|K_e-1|\to 0$  as  $\nu\to\infty$ . Hence, relation (B.11) from Appendix B is applicable, which gives

$$K_e - 1 = \frac{1}{i\pi} \int_{-\infty}^{\infty} \frac{K_e(\nu') - 1}{\nu' - \nu} d\nu'.$$
 (3.24)

In addition,  $K_e$  has crossing symmetry, so that  $K_{er}(-\nu) = K_{er}(\nu)$  and  $K_{ei}(-\nu) = -K_{ei}(\nu)$ ; hence, equations (B.14) and (B.15) from Appendix B are also applicable, so that

$$K_{er}(\nu) - 1 = \frac{2}{\pi} \int_0^\infty \frac{\nu' K_{ei}(\nu')}{\nu'^2 - \nu^2} d\nu', \tag{3.25}$$

and

$$K_{ei}(\nu) = -\frac{2\nu}{\pi} \int_0^\infty \frac{K_{er}(\nu') - 1}{\nu'^2 - \nu^2} d\nu'.$$
 (3.26)

Equations (3.25) and (3.26) are known as the Kramers–Kronig dispersion relations. They show that the real and imaginary parts of the dielectric constant are not independent, but that one can be calculated from the other.

Although we have used the Lorentz model to derive these dispersion relations, it can be shown (e.g., Wooten, 1972) that they are much more general and are independent of the particular model for the dielectric constant. In fact, these dispersion relations follow from the requirement of causality, that is, that the system cannot have a response before the event that excites the response occurs.

Numerous other dispersion relations and sum rules exist. They have been discussed by many authors, including Wooten (1972) and Smith (1985).

## 3.4 Mechanisms of absorption

The mechanisms by which electromagnetic radiation interacts with condensed matter may be classified into four broad categories: rotational, vibrational, electron excitation, and free carrier. Each will be discussed qualitatively in this section. More detailed, rigorous descriptions of the modern theory of the solid state, on which this section is based, can be found in books on modern physics, solid-state physics, and optical physics, such as those by Sproull and Phillips (1980), Kittel (1976), and Garbuny (1965). A succinct and clear summary of absorption mechanisms, particularly in the visible and infrared, has been provided by Hunt (1980). Further discussion and references may be found in the work of Salisbury (1993). See also Egan and Hilgeman (1979) and Gaffey *et al.* (1989). Although the emphasis here will be on absorption by solids, many of the mechanisms are also applicable to liquids. Tabulated values of optical constants for a variety of materials have been provided by Palik (1991).

### 3.4.2 Molecular rotation

Molecules possessing permanent electric-dipole moments contribute to the complex dielectric constant by changing their orientations when acted on by an electric field. The molecules in gases and liquids are able to rotate in an applied field, and their permanent dipole moments can cause a large electric polarizability. In a solid, the ability of a molecule to rotate depends on its shape and the strength of its interactions with its environment. In general, the more nearly spherical the molecule and the smaller its dipole moment, the more easily it rotates. Molecules often have several stable orientations in the solid, and they may flip from one orientation to another during an interval called the *relaxation time*.

If the period of the applied field is long compared with the relaxation time, the alignments saturate, and the dielectric constant is large. Conversely, if the ratio of the period to the relaxation time is small, the molecules do not have time to rotate, and the dielectric constant is small. Thermal agitation tends to randomize the orientations of the molecules, so that the portion of the dielectric constant associated with rotational transitions decreases with increasing temperature.

A substance of considerable interest in planetary remote sensing is water  $H_2O$ . In liquid water at room temperature, the relaxation time is on the order of  $3\times 10^{-11}$  sec, corresponding to a wavelength of 1 cm. Consequently, the real part of the dielectric constant of water for wavelengths shorter than 1 cm is around 80, whereas the value in the visible part of the spectrum is 1.77. However, in ice at  $-20\,^{\circ}C$  the relaxation time is around 1 msec, so that the microwave dielectric constant of ice is

<!-- IMAGE: _page_8_Figure_2.jpeg -->

Figure 3.3 Dielectric constant of fresh water at 20◦C*.* Data from Fung and Ulaby (1983).

1.78. Figure 3.3 shows the dielectric constant of liquid water in the microwave region.

The ubiquitous occurrence of water on the surface of the Earth and its high dielectric constant effectively prevent the penetration of microwaves very far into the surface. However, because the Earth appears to be the only body in the solar system where H2O occurs in the liquid state on the surface, this limitation does not apply to microwave sensing of other planets.

### 3.4.3 Lattice vibrations

A solid can be considered to be made up of positive and negative ions arranged in a periodic array, with each ion able to vibrate about its equilibrium position. The mathematical description of lattice vibrations is found by setting up the equations of motion of the ions and seeking solutions having the form of periodic waves propagating through the array. In the quantum-mechanical description the lattice vibrations are considered to be made up of waves, called *phonons*, with discrete, quantized energy levels.

In general, in both classical and quantum-mechanical physics two classes of solutions are found. One type describes motions in which the positive and negative ions move together so that there is no net dipole moment associated with the vibrations, and hence they are not able to interact with an electromagnetic wave. This class is called the *acoustical branch* of the vibrational spectrum because it describes the propagation of pressure and shear waves.

The second class, or branch, of waves describes vibrations in which the positive and negative ions move out of phase with each other, so that there is a net dipole moment associated with the motions. These types of waves are able to emit or absorb electromagnetic waves, and hence this is called the *optical branch* of lattice vibrations. The strongest interactions between the electromagnetic and lattice waves occur when the relative ionic displacements result in transverse dipole moments. Radiation can be absorbed by causing the lattice to jump from one vibrational state to another of higher energy. The system may return to the lower state by a radiationless transition in which phonons are generated, the absorbed energy ultimately appearing as heat.

The strong absorption bands associated with fundamental lattice vibrations generally occur in the thermal infrared, although overtone and combination bands often extend to shorter wavelengths.

Figure 3.4 shows the measured vibrational absorption spectrum of quartz. The figure also shows the fit of classical dispersion theory, equation (3.21), to the data.

### 3.4.4 Electronic transitions

### 3.4.4.1 The band model of electrons in a solid

Absorption in the near ultraviolet, visible, and near infrared can occur by several different mechanisms, but most can be classed as transitions in which single electrons are induced by the radiation to jump from a state of lower energy to one of higher energy. These transitions can be described in terms of the band model of electrons in a solid.

Aclassical oscillating system has a well-defined resonant frequency.An example is the pendulum, in which the resonant frequency is determined by the length. Two isolated, identical pendulums will have the same resonant frequency, but if the pendulums are coupled, the resonances will split, so that the system as a whole will have two resonant frequencies. The stronger the coupling, the greater the splitting.

Similarly, electrons in isolated atoms or ions have well-defined, discrete energy states, which (in principle) can be calculated from the Schrödinger equation. As the ions are brought together in a solid, the wave functions of the outer electrons overlap and perturb one another. The result of the perturbations is to split the energy levels, so that the system of many atoms has a large number of states that are closely spaced in energy. The quantum-mechanical energy levels overlap because they have a finite width. As a result, the system has several wide, continuous bands in which the electrons can exist, separated by gaps in which no solution of the wave equation is possible.

<!-- IMAGE: _page_10_Figure_2.jpeg -->

Figure 3.4 Transmission spectrum of quartz for the ordinary and extraordinary rays. The lines show classical dispersion theory fitted to the data. (Reproduced from Spitzer and Kleinman \[1961], copyright 1961 by the American Physical Society.)

The highest energy band, in which all electron states are occupied, is called the *valence band*. The wave functions of electrons in the valence band generally are localized on discrete ions or atoms. The lowest energy band in which all states are not occupied, is called the *conduction band*, which may be partially filled or completely empty. (To be sure, states of lower energy than the valence band and of higher energy than the conduction band exist and may also properly be called valence and conduction bands. However, these other bands usually play no role in absorption and so may be ignored.) Electrons in the conduction band are not bound to any specific atom or ion, but are free to move about the solid lattice, where they contribute to both the electrical and thermal conductivities. The width of the gap between the valence and conduction bands typically is several electronvolts. The bands are illustrated schematically in Figure 3.5.

If an electron is excited from the valence band to the conduction band, it leaves an ion with an excess of positive charge behind it. This positively charged electron vacancy is called a *hole*. A hole can jump from one ion to another when an electron 0

<!-- IMAGE: _page_11_Picture_2.jpeg -->

Figure 3.5 Schematic diagram of the band structure of electrons in a solid.

from the second ion tunnels to the hole site through the potential barrier separating the two ions. Thus, holes can be mobile and behave like positively charged particles.

This general picture of bands occupied by electrons and holes gives rise to a rich variety of ways by which light can be absorbed. These will be described next.

### 3.4.4.2 Color centers

All real solids have many different types of lattice imperfections, including *vacancies*, where an ion is missing from the lattice, *interstitials*, where an extra ion is forced into the space between ions of the lattice, and *substitutional* impurities, where a lattice ion is replaced by one of a different species. Generally an excess charge of one sign accompanies the imperfection, so that to preserve overall electrical neutrality a second imperfection having a charge of the opposite sign also exists near the first.

An electron can orbit a positively charged imperfection and a hole a negatively charged one to form systems analogous to the hydrogen atom. Such a system is called a *color center*, and absorption can be regarded as taking place when the electron or hole jumps to a higher energy level in this hydrogen-like system. The wavelengths of absorption bands due to color centers usually are in the visible and near infrared. Figure 3.6 shows color centers induced in soda-silica glass by x-ray irradiation.

Color centers have been extensively studied in alkali halides and a number of metal oxides. Detailed discussions can be found in the works of Schulman and Compton (1962) and Fowler (1968).

<!-- IMAGE: _page_12_Figure_2.jpeg -->

Figure 3.6 Absorption bands in a soda-silica glass irradiated by x-rays. The upper curve is the absorption spectrum; the lower curves show the spectrum deconvolved into individual bands of Gaussian shapes. (Reproduced from Cohen and Janezic [\[1983\]](#page-0-0), copyright 1983 with permission of Akademie-Verlag GmbH.)

### 3.4.4.3 Crystal-field effects in transition elements

Transition elements have partly filled *d* or *f* shells in both the neutral atoms and their common oxidation states. In an isolated ion the orbital states in the partly filled shell are degenerate, so that electrons have equal probabilities of residing in any state. However, when the ion is in a solid, the electric field due to the surrounding ions is not isotropic. This anisotropy removes the degeneracies, so that the orbitals in the shell have different energy levels, an effect known as *crystal-field splitting*. Light can be absorbed when an electron jumps from an orbital of lower energy to one of higher energy in the same shell. This mechanism is called *crystal-field absorption*.

The probability of a transition between the orbital energy levels is subject to certain selection rules. One is the spin-multiplicity rule, which states that transitions may take place only between states that have the same number of unpaired electrons. A second is the Laporte rule, which forbids transitions between orbitals of the same type and quantum number. Thus, in the isolated ion, crystal-field transitions would be strictly forbidden even if the energy levels were not degenerate. In a crystal lattice these selection rules are relaxed by various effects, including spinorbit coupling and departure of the environment of the ion from perfect symmetry. However, the transition probabilities are relatively low, so that the absorptions are weak. Transitions within the *d* shell of an ion in octahedral coordination are

<!-- IMAGE: _page_13_Figure_2.jpeg -->

Figure 3.7 Absorption spectrum of enstatite ([Mg, Fe]SiO3*)* showing crystal-field bands of Fe2+ at 900 and 1800 nm. (Reproduced from White and Keester [\[1966\]](#page-0-0), copyright 1966 with permission of the Mineralogical Society of America.)

Laporte-forbidden and thus are very weak. However, if the ion is in tetrahedral coordination, which lacks a center of symmetry, the transition probability is roughly 100 times larger.

Absorption bands due to crystal-field transitions typically occur in the visible and near infrared. The crystal-field absorption spectrum of Fe2+ in octahedral coordination with O2° in enstatite is shown in Figure 3.7. An excellent discussion of crystal-field absorption has been provided by Burns (1970, 1993). See also Adams (1975) and Vaughan (1990). The Fe2+ bands near 1000 and 2000 nm and the Fe3+ band near 860 nm have important applications in geochemical remote sensing.

### 3.4.4.4 Charge transfer

Absorption by charge transfer occurs when an electron jumps from a state localized on one ion to another on a nearby ion. Because the transition is not spin- or Laporte-forbidden, charge-transfer bands are strong. Theoretical prediction of the wavelength at which charge-transfer absorption will occur is difficult because both ions and their neighbors must all be considered as one system in calculating the electronic energy levels.

Charge-transfer bands generally are in the near ultraviolet, visible, and near infrared spectral region. Figure 3.8 shows the Fe2+ ! Ti4+ charge-transfer bands

<!-- IMAGE: _page_14_Figure_2.jpeg -->

Figure 3.8 Reflectance spectrum of powdered silicate glass. The spectrum shows the Fe2+ !Ti4+ charge-transfer bands at 340 and 420 nm, and the weak crystal-field bands of Fe2+ near 1000 and 2000 nm.

at 340 and 420 nm in a silicate glass (Wells and Hapke, 1977). This spectrum also exhibits the Fe2+ crystal-field bands.

In certain minerals, such as magnetite *(*Fe3O4*)* and the ilmenite–hematite *(*FeTiO3!Fe2O3*)* series, charge-transfer mechanisms are thought to cause electron delocalization (Burns *et al.*, 1980). The electrons behave as nearly free carriers, with the result that the minerals are opaque over a wide spectral region.

### 3.4.4.5 Excitons

When an electron is excited into the conduction band, a hole is left in the valence band. The positively charged hole can attract an unbound electron and form a hydrogen-like system, called an *exciton*, which can absorb light by transitions between levels within the system. The energies of excitonic transitions are slightly smaller than the valence–conduction band gap, so that the wavelengths corresponding to them usually lie in the far ultraviolet. An exciton transition in forsterite is illustrated in Figure 3.9.

### 3.4.4.6 Interband and impurity transitions

If the wavelength is short enough, absorption may occur when the radiation excites an electron directly from the valence band to the conduction band. Generally this type of transition occurs in the far ultraviolet, but for a few materials, called intrinsic semiconductors, thermal phonons are sufficient. Elemental Ge and Si are examples of intrinsic semiconductors. Absorption associated with interband transitions is extremely strong. Figure 3.9 shows the interband absorption spectrum of forsterite.

Often electrons of impurity ions have energy levels within the forbidden gap between the valence and conduction bands. In that case, transitions may occur in

<!-- IMAGE: _page_15_Figure_2.jpeg -->

Figure 3.9 Refractive index of forsterite (Mg2 SiO4*)* showing the exciton band at about 9 eV. (Reproduced from Nitsan and Shankland \[1976], copyright 1976 with permission of the Royal Astronomical Society.)

which an electron is excited from the valence band to an impurity level, or from impurity level to conduction band.

### 3.4.5 Free carriers

Free carriers of charge, including both electrons and holes, can absorb light in a solid when they are stimulated to move by the electric field of the incident radiation and then collide with the lattice, converting some of the energy of the radiation into lattice vibrations. According to quantum theory, an electron can propagate without loss through a perfect periodic structure; hence, the absorption actually takes place by collisions with lattice imperfections. The imperfections can be of many types, including dislocations, grain boundaries, vacancies, interstitials, impurities, and random displacements of the ions from their average positions due to thermal motions. The latter can be described quantum-mechanically as phonons, and absorptions associated with this type of imperfection are sometimes referred to as electron-phonon losses.

Free-carrier loss is the main source of absorption in the visible and near infrared in metals and semiconductors. Unlike the other mechanisms discussed in this section, free-carrier absorption occurs over a broad range of wavelengths and not in well-defined bands. It is described approximately by the Drude theory at long wavelengths, but not at short, where other absorption mechanisms dominate. Electromagnetic-wave propagation and losses in metals have been discussed by Abeles (1966) and Sokolov (1967).

## 3.5 Band shape and temperature effects

It has been shown in this chapter that an absorption band due to charged particles oscillating in a parabolic potential well has a Lorentzian shape described by equations (3.19) and (3.20). For all of the loss mechanisms considered in the preceding section the assumption of parabolic shapes is a reasonable first approximation, and measured infrared absorption bands associated with lattice vibrations can be described adequately by Lorentzian shapes (Figure 3.4).

However, the shorter-wavelength electronic bands are better described empirically by Gaussian shapes of the form Ψ = *A*exp[!*(*ν !ν0*)*2*/B*]*,* where *A* and *B* are constants (Figure 3.6). The reasons for this have been discussed by Lax (1954) and Dexter (1956). Essentially it occurs because the widths of the electronic potential wells are affected by the distances to the nearest neighbor ions. These distances differ from their averages because the lattice may be distorted by a variety of effects, including dislocations, impurities, and interstitials and because the ions are in constant thermal vibration. The effect of these distortions averaged over a large

<!-- IMAGE: _page_16_Figure_6.jpeg -->

Figure 3.10 Absorption spectrum of forsterite illustrating the effect of temperature on the crystal-field band. The number next to each curve is the temperature in degrees Celsius. (Reproduced from Sung *et al.* [\[1977\]](#page-0-0), copyright 1977 with permission of Pergamon Press Ltd.)

number of systems in the solid is to smear out the band shapes from Lorentzians to Gaussians and to cause the bands to become wider with increasing temperature.

Raising the temperature usually causes a solid to expand, increasing the average distance between the ions in the lattice and the widths of the electronic potential wells. The wavelength of an electron wave function varies directly with the width of the potential well, so that the energies of the electron states become less negative. The lower energy levels are raised more than the higher ones, so that the transition energy and thus the frequency of the center of an absorption band decrease with increasing temperature. This effect is illustrated in Figure 3.10, which shows the increase in the central wavelength of the Fe2+ crystal-field band in olivine with increasing temperature.

## 3.6 Spectral databases

Reflectance and emittance spectra of substances of interest in the geological and planetary sciences can be found on the following websites.

**<speclib.jpl.nasa.gov>** The Jet Propulsion Laboratory, US Geological Survey and Johns Hopkins University spectral libraries, vis-midIR. **<speclab.asu.edu>** The Arizona State University spectral library, mid-IR. lf314-rlds.geo.brown.edu also planetary.brown.edu/relabdata - vis/nearIR/midIR.

The Wagner *et al.* (1987) spectral atlas 90 nm – 1.8µm can be obtained in digital form by email request from Jeffrey K. Wagner, [j](%20)kwagn@<bgsu.esu.>