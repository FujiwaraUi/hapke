## Single-particle scattering: irregular particles

## 6.1 Introduction

The scattering of electromagnetic radiation by perfect, uniform, spherical particles was described in Chapter 5. However, such particles are rarely found in nature. Most pulverized materials, including planetary regoliths, volcanic ash, laboratory samples, and industrial substances, have particles that are irregular in shape, have rough surfaces, and are not uniform in either structure or composition. Even the liquid droplets in clouds are not perfectly spherical, and they contain inclusions of submicroscopic particles around which the liquid has condensed, so that they are not perfectly uniform. At the present state of our computational and analytical capabilities it is possible to find exact solutions of scattering by such particles only by the expenditure of considerable computer time and memory (to say nothing of the effort of writing detailed programs), so that approximate models remain extremely useful.

The objective of any model of single-particle scattering is to relate the microscopic properties of the particle (its structure and complex refractive index) to the macroscopic properties (the scattering and extinction efficiencies and the phase function) that, in principle, can be measured by an appropriate scattering experiment. This chapter describes a variety of models that have been proposed to describe the scattering of light by irregular particles. This is not an exhaustive survey; rather, it is a commentary on those models that are most often encountered in remote-sensing applications or that offer some particular insight into the problem.

The organization of this chapter is as follows. First, the quantities defined in Chapter 5 for spherical particles are extended to particles that are nonspherical in shape. Next, some empirical models that are widely used in remote sensing are introduced. Theoretical approaches to the formidable problem of scattering by irregular particles are summarized. Laboratory measurements of the efficiencies and phase functions are described. The experimental and theoretical results are then summarized. Finally, the equivalent-slab approximation introduced in Chapter 5 for spheres is generalized to irregular particles and further extended to coated particles.

## 6.2 Extension of definitions to nonspherical particles

The physical meanings of the particle scattering parameters defined in Chapter 5, including the cross sections and phase functions, are intuitively clear for a particle that is spherically symmetric. However, if a particle is not spherical, the proper interpretation of these quantities is not obvious. Unless explicitly stated otherwise, in this book it will always be assumed that we are dealing with ensembles of particles whose orientations are random. Thus, the power extinguished by a particle of arbitrary shape is defined to be the average of the power removed from the beam of light as the particle is randomly oriented in all directions. Similar definitions apply for the power scattered and absorbed. The geometric cross section σ of a particle is the average area of the geometric shadow cast by the particle as it is oriented at random in all directions. The equivalent particle radius and diameter are defined as

$$a = \sqrt{\sigma/\pi},\tag{6.1a}$$

$$D = 2a = 2\sqrt{\sigma/\pi}. (6.1b)$$

With this understanding of implicitly averaging over all orientations, the quantities defined in Section 5.2 have physical meanings for nonspherical particles as well as spherical ones. These meanings are intuitively clear and internally consistent. Note that the scattering properties defined in this way are azimuthally symmetric, so that the normalization condition, equation (5.13) on #*(g)* holds.

Some workers define the effective particle radius *a* to be the radius of a sphere of the same volume as the particle under consideration. With such a definition the power absorbed by the particle is the same as that absorbed by the equivalent sphere if the particle is optically thin, but not if the particle is opaque. In this book the definition of the equivalent radius *a* in terms of a sphere of the same mean geometric cross-sectional area is preferred, because this leads to unambiguous meanings for the efficiencies and phase functions. Also, the power absorbed by an optically thick irregular particle and that absorbed by its equivalent sphere are equal.

## 6.3 Empirical scattering functions 6.3.1 The Allen approximation for Fraunhofer diffraction

It was shown in Chapter 5 that the light scattered by Fraunhofer diffraction around a sphere is identical with that diffracted through a circular aperture of the same radius in an opaque screen, and consists of a strong central peak surrounded by a series of weaker fringes. A noncircular opening has a qualitatively similar diffraction pattern, but the main peak and the fringes are not azimuthally symmetric. For instance, the angular size and spacing of the diffraction pattern of a rectangular slit is wider along the direction perpendicular to the long edge of the slit than along the direction perpendicular to the short edge of the slit. Jenkins and White (1950) give a number of examples of the diffraction patterns of openings of various shapes. Dauger has created a computer program that calculates the Fraunhofer diffraction pattern of an object of arbitrary cross section (see end of chapter).

Ensembles of large, irregular particles have narrow, forward-scattered main diffraction peaks, but the fringes and asymmetries tend to be averaged out, so that the diffracted intensity decreases monotonically from the center of the pattern and approximates the envelope of the diffraction pattern of a sphere. Allen (1946) has pointed out that a good empirical fit to the envelope of the diffraction fringes is provided by the function.

$$\Pi_d(g) = \frac{X^2}{1 + 0.470X^3(\pi - g)^3},\tag{6.2}$$

where the coefficient of *X*3 in the denominator comes from normalizing #*d (g)*. This function is mathematically more convenient than equation (5.26). The exact and approximate diffraction functions are compared in Figure 6.1.

<!-- IMAGE: _page_2_Figure_6.jpeg -->

Figure 6.1 Allen approximation to the Fraunhofer diffraction function (dashed line) compared with the exact expression (solid line).

### 6.3.2 Legendre polynomial representation of $\Pi(g)$

It is often convenient to represent  $\Pi(g)$  as a series of Legendre polynomials:

$$\Pi(g) = \sum_{j=0}^{\infty} b_j P_j(g), \tag{6.3}$$

where the  $b_j$ s are constants, and the  $P_j$  (g)s are Legendre polynomials of order j. The properties of these functions are reviewed and illustrated in Appendix C. This representation of  $\Pi(g)$  is most useful when the departures from isotropic scattering are not very large, so that only a few terms are necessary. Thus (6.3) is most often used to represent the nondiffractive portion of  $\Pi(g)$ . It has been used by many authors, including Hapke (1981) and Mustard and Pieters (1989).

From the normalization condition on  $\Pi(g)$ , equation (5.13), the series must satisfy

$$\frac{1}{4\pi} \int 4\pi \sum_{j} b_{j} P_{j}(g) d\Omega = \frac{1}{4\pi} \int_{0}^{\pi} \sum_{j} b_{j} P_{j}(g) 2\pi \sin g dg = 1.$$

But, from the orthogonality of the Legendre polynomials, the only nonvanishing integral is that for j=0, which equals  $4\pi b_0$ . Hence,  $b_0=1$ . No general model exists to specify the other coefficients. A constraint on the  $b_j$ 's is that  $\Pi(g)$  cannot be negative anywhere. For example, if it is desired to represent the phase function by a first-order expansion,  $\Pi(g)=1+b_1\cos g$ , then  $b_1$  is restricted to the range  $-1 \le b_1 \le +1$ . A first-order expansion is adequate if the phase function is single-lobed. However, the phase functions of most real, nonopaque particles are double-lobed, which requires at least a second-order expansion:  $\Pi(g)=1+b_1P_1(g)+b_2P_2(g)$ .

The cosine asymmetry factor (equation 5.14) is

$$\xi = -\langle \cos g \rangle = -\frac{1}{4\pi} \int_{0}^{\pi} \sum_{j=0}^{\infty} P_{j}(g) \cos g 2\pi \sin g dg$$

$$= -\frac{1}{2} \int_{0}^{\pi} b_{1} P_{1}(g) \cos g \sin g dg = -\frac{1}{2} \int_{0}^{\pi} b_{1} \cos^{2} g \sin g dg = -b_{1}/3, \quad (6.4)$$

where we have again used the orthogonality property, which implies that all terms except j = 1 in the sum vanish. Hence,  $b_1 = -3\xi$ .

<!-- IMAGE: _page_4_Figure_2.jpeg -->

Figure 6.2 Henyey–Greenstein particle phase function for several values of the asymmetry parameter  $\xi$  .

### 6.3.3 Henyey-Greenstein function representation of $\Pi(g)$

Henyey and Greenstein (1941) introduced the single-parameter empirical phase function

$$\Pi_{\text{HG1}}(\theta) = \frac{1 - \xi^2}{(1 - 2\xi \cos \theta + \xi^2)^{3/2}},$$

or equivalently,

$$\Pi_{\text{HGI}}(g) = \frac{1 - \xi^2}{(1 + 2\xi \cos g + \xi^2)^{3/2}}.$$
(6.5)

The function is illustrated for several values of  $\xi$  in Figure 6.2. It is widely used in planetary reflectance work (e.g., Lumme and Bowell, 1981b; Buratti, 1985; Helfenstein *et al.*, 1988).

This versatile function has the following useful properties, which are left as an exercise for the reader to prove. It is normalized:  $(1/4\pi)\int_{4\pi}\Pi_{\rm HG1}(g)d\Omega=1$ . The Henyey–Greenstein parameter  $\xi$  is the cosine asymmetry factor,  $\xi=\langle\cos\theta\rangle=-\langle\cos g\rangle$ . The function is isotropic  $(\Pi_{\rm HG1}(g)=1)$  when  $\xi=0$ . At g=0 and  $\pi$ ,  $\Pi_{\rm HG1}(g)$  has the values  $(1-\xi)/(1+\xi)^2$  and  $(1+\xi)/(1-\xi)^2$ , respectively. If  $\xi>0$ ,  $\Pi_{\rm HG1}(g)$  increases monotonically between 0 and  $\pi$ , and decreases monotonically if  $\xi<0$ . The shape of the peak depends on  $\xi$ , becoming higher and narrower as  $|\xi|$  increases. In the limiting case, as  $\xi\to1$  (or -1),  $\Pi_{\rm HG1}(g)\to0$  everywhere except at  $g=\pi$  (or 0), where it becomes infinite in such a way that its integral equals  $4\pi$ . Hence, this function is often used to represent the diffraction peak.

The expansion of the Henyey-Greenstein function in Legendre polynomials is (Kattawar, 1975)

$$\Pi_{\text{HG1}}(g) = \sum_{j=0}^{\infty} (2j+1)(-\xi)^j P_j(g). \tag{6.6}$$

However, equation (6.5) has only one lobe, whereas the phase functions of most particles are double-lobed. In order to represent a double-lobed phase function, two Henyey-Greenstein functions of opposite symmetry are required. The double-lobed Henyey-Greenstein function can be formulated using either two or three parameters; the two-parameter function is:

$$\Pi_{\text{HG2}}(g) = \frac{1+c}{2} \frac{1-b^2}{(1-2b\cos g + b^2)^{3/2}} + \frac{1-c}{2} \frac{1-b^2}{(1+2b\cos g + b^2)^{3/2}}; \quad (6.7a)$$

and the three-parameter function is:

$$\Pi_{\text{HG3}}(g) = \frac{1+c}{2} \frac{1-b_1^2}{(1-2b_1\cos g + b_1^2)^{3/2}} + \frac{1-c}{2} \frac{1-b_2^2}{(1+2b_2\cos g + b_2^2)^{3/2}}. \quad (6.7b)$$

In these experessions the first term describes the backward lobe and the second the forward lobe; the relative strengths of the lobes are determined by c, and their shapes by b, or  $b_1$  and  $b_2$ . The b-parameters are constrained to lie in the range  $0 \le b$ ,  $b_1$ ,  $b_2 \le 1$ ; there is no constraint on c except that  $\Pi_{HG}(g) \ge 0$  everywhere. The mean cosines of the two functions are:

two-parameter 
$$\xi = -bc$$
; (6.8a)

three-parameter 
$$\xi = -\frac{1+c}{2}b_1 + \frac{1-c}{2}b_2$$
. (6.8b)

The disadvantage of the two-parameter function is that the shapes of the lobes of the particle being described cannot be too different; the advantage is that it has only two parameters to be fitted instead of three. (1997)

and Hartman and Domingue (1998) investigated the relative ability of the two- and three-parameter functions to fit phase angle measurements of several types of real materials. They concluded that, although slightly better fits were obtained with the three-parameter function, the improvement was marginal and not sufficient to justify a third parameter.

### 6.3.4 Lambert and Lommel–Seeliger sphere phase functions for nondiffractive scattering

Suppose an element of area dA on the surface of a sphere is illuminated by collimated light of irradiance J making an angle i with the normal to dA and observed

from a direction making an angle e with the surface normal. The phase angle g is the angle between the directions to the source and detector as seen from the particle. Suppose each element of the surface scatters the incident light into unit solid angle described by a surface reflectance function dI = JY(i, e, g)dA. Then the nondiffractive scattering efficiency  $Q_s$  and phase function of an opaque sphere, each of whose surface elements scatters light as described by Y(i, e, g), may be calculated as follows.

It is assumed that the particle is sufficiently absorbing that internally transmitted light can be neglected. Choose a spherical coordinate system with the origin at the center of the particle and such that the great circle through the sub-source point and the sub-observer point forms the equator of the sphere, with the central meridian of longitude passing through the sub-observer point. The sub-observer point and sub-source point are separated in longitude by an angle equal to the phase angle g. The geometry is shown in Figure 6.3. The element of area  $dA = a^2 \cos L dL d\Lambda$  is located on the surface of the sphere at longitude  $\Lambda$  and latitude L, where a is the radius of the particle. The outward normal to the surface makes an angle i with the incident illumination, and an angle e with the direction to the observer.

From the law of cosines for spherical triangles,  $\cos i = \cos(\Lambda + g)\cos L$ , and  $\cos e = \cos \Lambda \cos L$ . Then the radiance scattered from the sphere into the direction toward the observer is the integral of Y(i, e, g) over all areas of the surface that are

<!-- IMAGE: _page_6_Picture_5.jpeg -->

Figure 6.3

both visible and illuminated:

$$I = \int_{\Lambda = -\pi/2}^{\pi/2 - g} \int_{L = -\pi/2}^{\pi/2} JY(i, e, g) dA.$$
 (6.9)

Two widely used surface reflectance functions are Lambert's law,

$$Y_{\rm L}(i, e, g) = \frac{1}{\pi} \cos i \cos e, \tag{6.10}$$

and the Lommel–Seeliger law,

$$Y_{LS}(i, e, g) = \frac{1}{4\pi} \frac{\cos i \cos e}{\cos i + \cos e}.$$
 (6.11)

These functions are discussed more fully in Chapter 8. Note that both are independent of *g*.

Inserting (6.10) into (6.9) gives

$$I = \int_{\Lambda = -\pi/2}^{\pi/2 - g} \int_{L = -\pi/2}^{\pi/2} \frac{J}{\pi} \cos i \cos e \, dA$$
$$= \frac{J}{\pi} a^2 \int_{\Lambda = -\pi/2}^{\pi/2 - g} \int_{L = -\pi/2}^{\pi/2} \cos(\Lambda + g) \cos \Lambda \cos^3 L dL d\Lambda.$$

Using the identity cos*x* cos*y* = [cos*(x* +*y)*+cos*(x* !*y)*]*/*2, this integral becomes

$$I = \frac{J}{2\pi}a^2 \left\{ \int_{\Lambda = -\pi/2}^{\pi/2 - g} [\cos(g + 2\Lambda) + \cos g] d\Lambda \right\} \cdot \left\{ \int_{L = -\pi/2}^{\pi/2} \cos^3 L dL \right\},$$

which is readily evaluated and gives

$$I = Ja^{2} \frac{1}{\pi} \frac{2}{3} [\sin g + (\pi - g)\cos g]. \tag{6.12}$$

By definition, *I* = *J* σ*Qs*[#*(g)/*4ζ], where σ = ζ*a*2. However, because we are assuming that radiation does not penetrate into the sphere, there is no absorption, so that *Qs* = 1. Hence, the phase function of a *Lambert sphere* is

$$\Pi_{L}(g) = \frac{8}{3} \frac{\sin g + (\pi - g)\cos g}{\pi}.$$
(6.13)

This expression was first derived by Schönberg (1929) and is known as the Schönberg function. It may readily be verified that this phase function satisfies the normalization condition, equation (5.13). It is plotted in Figure 6.4.

Similarly, inserting the Lommel–Seeliger law (6.11) into (6.9) gives

$$I = \int_{\Lambda = -\pi/2}^{\pi/2 - g} \int_{L = -\pi/2}^{\pi/2} \frac{J}{4\pi} \frac{\cos(\Lambda + g)\cos L \cos \Lambda \cos L}{\cos(\Lambda + g)\cos L + \cos \Lambda \cos L} dA$$
$$= \frac{J}{4\pi} a^2 \int_{\Lambda = -\pi/2}^{\pi/2 - g} \int_{L = -\pi/2}^{\pi/2} \frac{\cos(\Lambda + g)\cos \Lambda}{\cos(\Lambda + g) + \cos \Lambda} \cos^2 L dL d\Lambda.$$

<!-- IMAGE: _page_8_Figure_2.jpeg -->

Figure 6.4 Phase functions of Lambert and Lommel–Seeliger spheres.

The integral over *L* is readily evaluated. The integral over Ψ may be evaluated by putting *x* = Ψ+*g/*2, so that cos*(*Ψ+*g)* = cos*(x* +*g/*2*)* and cosΨ = cos*(x* !*g/*2*)*, giving

$$I = \frac{J}{16}a^2 \int_{x=-\pi/2+g/2}^{\pi/2-g/2} \left[ \sec\frac{g}{2}\cos x - \sin\frac{g}{2}\tan\frac{g}{2}\sec x \right] dx$$
$$= \frac{J}{8}a^2 \left[ 1 - \sin\frac{g}{2}\tan\frac{g}{2}\ln\left(\cot\frac{g}{4}\right) \right] = J\pi a^2 \frac{p(g)}{4\pi}.$$

Hence,

$$\Pi_{\mathrm{LS}}(g) = \frac{1}{2} \left[ 1 - \sin \frac{g}{2} \tan \frac{g}{2} \ln \left( \cot \frac{g}{4} \right) \right].$$

However, this phase function is not normalized. To normalize #*(g)*, set

$$\frac{C}{4\pi} \int_0^{\pi} \frac{1}{2} \left[ 1 - \sin \frac{g}{2} \tan \frac{g}{2} \ln \left( \cot \frac{g}{4} \right) \right] 2\pi \sin g \ dg = 1,$$

where *C* is the normalization constant. This integral may be evaluated by letting *y* = cos*(g/*2*)*, noting that

$$\ln\left[\cot\left(g/4\right)\right] = \ln\left[\left(1+y\right)/\left(1-y\right)\right],$$

and integrating by parts. This gives the phase function of a *Lommel–Seeliger sphere,*

$$\Pi_{LS}(g) = \frac{3}{4(1 - \ln 2)} \left[ 1 - \sin \frac{g}{2} \tan \frac{g}{2} \ln \left( \cot \frac{g}{4} \right) \right]. \tag{6.14}$$

This function is plotted in Figure 6.4 along with the Lambert sphere.

Note that both the Lambert and Lommel-Seeliger functions are strongly backscattering.

### 6.3.5 Other functions

Several other semi-empirical scattering functions have been introduced in the literature to describe various aspects of scattering by large irregular particles. One of the simplest is that used by Hapke and Nelson (1975) in connection with a study of the clouds of Venus. For the diffracted component of the intensity they used a delta function. They assumed that the nondiffracted part of the phase function is isotropic and that the scattering efficiency could be described by

$$Q_s = S_e + (1 - S_e)e^{-\alpha D}, (6.15)$$

where  $S_e$  is the integral of the Fresnel reflection coefficient given by (5.36).

For large particles, Pollack and Cuzzi (1980) described diffraction by an approximation to the circular-hole equation, and external surface scattering by the Fresnel equations. They represented the internally refracted light by a simple expression of the form  $ce^{(1-bg)}$ , where c and b are empirical constants.

## 6.4 Theoretical and experimental studies of nonspherical particles 6.4.1 Theory for particles small compared with the wavelength

Although Mie theory is strictly valid only for spherical particles, it still serves as a valuable starting point in discussing scattering by irregular particles. Suppose that the condition  $|n|X \ll 1$  is satisfied, where  $n = n_r + in_i$  is the complex index of refraction relative to its surroundings, and  $X = 2\pi a/\lambda$  is the particle size parameter. Then the change in phase of the applied internal field across the particle is  $n_r X$ , and the attenuation of the field across the particle is  $n_i X$ , both of which are small. At any given time the entire particle sees electric and magnetic fields that are essentially uniform, and the instantaneous fields in the vicinity of the particle are essentially the same as if only static fields are applied. Thus, the fields are given, to a good approximation, by solutions of the appropriate electrostatic and magnetostatic equations. That this is indeed the case may be verified for small spherical particles as follows.

The dipole moment induced by a uniform, static, external field  $E_{e0}$  on a sphere of radius a and dielectric constant  $K_e$  is (see any textbook on advanced electrodynamics, e.g., Stratton (1941)):

$$p_{e0} = 4\pi a^3 \varepsilon_{e0} E_{e0}(K_e - 1) / (K_e + 2). \tag{6.16}$$

If |n|X=1, then the electric field seen by a sphere illuminated by a plane electromagnetic wave of irradiance  $J=(\varepsilon_{e0}/\mu_{m0})^{1/2}E_{e0}^2/2$  and frequency  $\nu$  is  $E_{e0}e^{2\pi i\nu t}$ , and the induced electric dipole of the sphere is  $p_{e0}e^{2\pi i\nu t}$ .

It can also be shown (Stratton, 1941) that the power radiated into a vacuum by an oscillating electric dipole of moment  $p_e = p_{e0}e^{2\pi i\nu t}$  and frequency  $\nu$  is given by

$$p_e = 4\pi^3 v^4 \varepsilon_{e0}^{1/2} \mu_{m0}^{3/2} |p_{e0}|^2 / 3.$$
 (6.17)

Inserting (6.16) into (6.17) and equating the result to  $J\pi a^2 Q_S$ , where  $Q_S$  is the scattering efficiency, gives

$$Q_S = \frac{8}{3}X^4|(K_e - 1)/(K_e + 2)|^2.$$
(6.18)

Since  $K_e = n^2$ , equation (6.18) is identical with (5.11) for the scattering efficiency of a small particle.

Now, a static electric field will induce a dipole moment in any particle, regardless of shape. This suggests that small particles of any shape will scatter light similar to a sphere, resulting in equations similar to (5.16) and (5.17) for a sphere. Figure 6.5

<!-- IMAGE: _page_10_Figure_9.jpeg -->

Figure 6.5 Measured angular scattering coefficient of a cube of X = 3.75 and n = 1.57 + i0.006 (circles), compared with the predictions of Mie theory for a sphere of the same size (lines), for the two polarized components of incident radiation. (Reproduced from Zerull [1976], copyright 1976, with permission of Friedrich Vieweg & Sohn.)

shows the measured phase function of a cube compared with the prediction of Mie theory for a sphere of the same size and refractive index.

Hence, electrostatic theory may be employed to calculate  $p_{e0}$ , and the result may be used in (6.17) to calculate  $Q_S$ . The advantage of this method is that it allows a wider variety of particle shapes to be treated analytically than does electrodynamic theory. In particular, scattering by oblate and prolate ellipsoids of rotation may be calculated, which includes disks and needles as special cases, and also triaxial ellipsoids.

Scattering by small ellipsoidal particles is discussed in considerable detail by Bohren and Huffman (1983). The net result is that if a particle is *equant*, that is, if its dimensions are roughly the same in all directions, then its efficiencies are not very different from those of a sphere of similar size. In particular,  $Q_S \propto X^4$  and  $Q_A \propto n_i X$ . However, if the particle is not approximately equidimensional, the particle still scatters and absorbs in a dipole-like manner, but its efficiencies differ quantitatively from (6.18).

### 6.4.2 General theoretical methods

A large number of different types of theoretical approaches to the problem of calculating single-particle scattering have been published, in addition to the direct solution of the wave equation discussed in Chapter 5. Of these, three appear to be the most fruitful and have become dominant in recent years with the advent of high-speed desktop computers. These are the discrete dipole approximation (DDA), the T-matrix method (TMM), and the ray-tracing Monte Carlo approximation (RTMCA). All are capable of handling particles with complex shapes, rough surfaces, and inclusions, as well as systems of several interacting particles. However, they require the detailed specification of the shape and structure of the system. They are highly computer intensive, and the computational requirements increase geometrically with increasing particle size. As the capabilities of computers increase in coming years it is expected that these methods will be able to describe scattering by both larger particles and systems of more particles.

The discrete dipole approximation This method is reviewed by Draine (2000). It was introduced by Purcell and Pennypacker (1973) and further developed by Draine (1988), Draine and Goodman (1993), and Draine and Flatau (1994). Two versions are available for download on the internet.

In the DDA the system under study is replaced by an array of point polarizable electric dipoles that approximate its size and structure as closely as possible. The dipoles interact with the radiation from each other as well as the incident irradiance. For a total of N dipoles this results in 3N coupled linear equations. The smaller the distance d between dipoles is, the more accurate the simulation will be, but

the resulting increase in *N* also increases the CPU time and memory required. The maximum spacing is such that the phase change of the field between dipoles is 2ζ|*n*|*d/*λ *<* 1.

**T-matrix method (T for transition)** This method (also known as the extended boundary condition method) is reviewed by Mishchenko *et al.* (2000b). It was first proposed by Waterman (1965, 1979) and further developed by Mishchenko and his colleagues (Mishchenko *et al.*, 1996, 2002). Scattering and absorption inside a particle due to the incident wave are replaced by charges and currents on the surface of a sphere that completely circumscribes the particle. Mishchenko discovered a way of analytically simplifying scattering from the system if it is averaged over all orientations, thus facilitating the computation of the important problem of scattering by ensembles of randomly oriented particles. He has made his program available for downloading from the internet. In addition to applying the method to a wide range of problems, he has also published a useful list of papers in which the method is applied to scattering problems (Mishchenko *et al.*, 2007).

**Ray-tracing Monte Carlo approximation** It was shown in Chapter 5 that when *X* ' 1, solutions for the scattering of light from a sphere obtained using geometric optics give reasonably good approximations to those using Mie theory. This suggests that ray theory may be used on large, nonspherical particles. In the RTMCArays from a distant source are directed randomly at the system under study, with which they interact according to Fresnel's laws of reflection and refraction. The directions into which they are finally scattered are recorded. In this way the scattering properties are built up after a large number of trials.

This approach has been used by several authors to calculate scattering by particles of regular shape, such as cubes, parallelepipeds, hexagonal cylinders, and other common crystalline forms (e. g., Liou and Coleman, 1980; Liou *et al.*, 1983; Muinonen *et al.*, 1989; Peltoniemi *et al.*, 1989; Vilaplana *et al.*, 2006). It is discussed in detail by Macke (2000) and Muinonen (2000).

### 6.4.3 Other approaches

Various other schemes for calculating scattering have been proposed. Further references and discussions can be found in the works of Schuerman (1980), Bohren and Huffman (1983), and Mishchenko *et al.* (2000a). Most of the models divide the problem into several parts, typically diffraction, external surface scattering, and internal refraction and scattering, and treat each part separately. Often one part is emphasized, and the rest either ignored or treated in an ad hoc fashion.

Leinert *et al.* (1976) fitted observations of the zodiacal light to models in which the particles are large compared with the wavelength. The diffracted radiation was taken to be identical with that from a sphere (equation [\[5.28\]](#page-0-0)), and surface-reflected light was described by the Fresnel reflectances (equation [\[5.34\]](#page-0-0)). Internally refracted light was assumed isotropic and simply adds a constant term to the phase function.

Chylek *et al.* (1976) pointed out that the large resonances displayed by scattering from a perfect sphere, such as peaks in the scattering efficiency and the cloudbows and glories in the phase function, can be attributed to specific terms in the series expansion of the Mie solution. They set these terms equal to zero and assumed that the resulting expression applies to irregular particles. However, though this assumption may be reasonable for particles whose sizes are comparable to the wavelength, it is certainly not true for large, irregular, nonuniform particles.

In general, the scattered wave can be considered as the sum of waves radiating from all the different points within the particle. The amplitudes of these wavelets are proportional to the amplitude of the wave inside the particle and the difference between the scatterer and a vacuum. Several workers have used the so-called *eikonal approximation,* in which the internal wave is replaced by the incident wave phase-shifted along undeviated linear paths. Both Chiappetta (1980) and Perrin and Lamy (1983) used this approach to calculate the intensity forwardscattered into large phase angles, and they used an empirical model to describe the scattering at smaller phase angles. Their models assume that the particles have very rough surfaces. They also assume that the broad backscattered peaks in the particle phase functions are caused by shadows on the surface. Internally refracted light is mainly ignored.

Schiffer and Thielheim (1982a, b) used a geometric-optics approach to calculate the effects of shadows on light reflected from a rough surface. Mukai *et al.* (1982) modeled multiple reflections between facets on the rough surface of a particle using the equation of radiative transfer, although it is not clear that this equation is applicable. Internally refracted light is ignored in the model of Mukai and associates, so that the types of particles to which it may be applicable are extremely limited.

Emslie and Aronson (1973) and Aronson and Emslie (1973, 1975) emphasized the importance of surface roughness to the spectral scattering properties of the particle. In an elaborate numerical model, later extended by Egan and Hilgeman (1978), they assumed a particle with a basic spherical shape. The absorption and scattering of this sphere were calculated using geometric optics. Roughness on the particle surface was assumed to scatter like randomly oriented dipoles distributed over the surface of the sphere. It was also assumed that the rest of the surface scattered light diffusely instead of specularly. This model has had considerable success in explaining features in the reflectance and emittance spectra of powders in the thermal infrared.

### 6.4.4 Laboratory measurements

Most measurements of particle scattering have been done at visible (Hovenier, 2000) and microwave (Gustafson, 2000) wavelengths. The sizes of particles of greatest interest in remote sensing generally tend to be of the order of a few micrometers. Hence, the particles studied using visible light generally are of the order of 1–10µm in size. Particles are levitated electrostatically or in a column of gas. The particle is illuminated by a collimated light source and the light scattered into all directions in the plane containing the source and detector measured. Polarized optics may or may not be used. At radio frequencies the targets are several centimeters in size in order to be analogs of particles interacting with visible light. The large size allows better control over the particle characteristics, as well as convenient handling and support. The particle is illuminated by radiation from a transmitting antenna and the scattered radiation detected by a separate movable receiving antenna.

Experimental studies of scattering by large, irregular particles have been reported by several workers, including Richter (1962), Hodkinson (1963), Zerull and Giese (1974),Zerull(1976),Weiss-Wrana (1983),McGuire and Hapke (1995), Volten *et al.* (2001), Barkey *et al.* (2002), and Munoz *et al.* (2006). The study by McGuire and Hapke is particularly illluminating because they systematically varied the shape, surface roughness, absorption coefficient, and density of internal scatterers in their analog particles, and because theirs is one of the few to investigate the effects of internal scatterers. A catalog of scattering measurements on a variety of types of particles at 633 and 442 nm by the Amsterdam group is available for download on the internet.

### 6.4.5 Summary of theoretical and experimental studies

Based on the studies summarized in the preceding subsections, a number of general inferences concerning the scattering properties of large, irregular particles can be made. The following discussion specifically excludes the Fraunhofer diffraction peak.

(1) A major difference between the scattering properties of irregular particles and perfect spheres is the absence of the large oscillations observed in both the scattering efficiencies of spheres as the size parameter changes and in the resonances in the angular scattering function. The varying dimensions in different directions of the irregularly shaped particles destroys the positive and negative interference effects that cause the resonances. This is illustrated in the study by Hodkinson (1963) of the extinction of visible light by colloidal suspensions of

<!-- IMAGE: _page_15_Figure_2.jpeg -->

Figure 6.6 Measured extinction coefficients of suspensions of irregular nonabsorbing particles (circles and dashed line) versus size parameter, compared with predictions of Mie theory for perfect spheres (solid line). (Reproduced from Hodkinson \[1963], copyright 1963, with permission of Elsevier.)

quartz particles as the size changes. Figure 6.6 shows that, in contrast to perfect spheres, the extinction efficiency of the irregular particles increases smoothly and monotonically with *X* until when *(nr*–1*)X* ! 3 it levels off at *QE* ( 2. Figure 6.7 shows the measured phase function and polarization of irregular particles of olivine compared with those calculated for a perfect sphere. Note that there is no sign of a cloudbow or other resonances.

- (2) If a particle is translucent, that is, if it has few internal scatterers and is not completely opaque, its phase function is dominated by a strong, broad, forwardscattering lobe caused by refracted, singly transmitted rays (Figures 6.7 and 6.8). This lobe is weaker for irregular particles than for spherical ones, but it occurs for particles of any shape or degree of surface roughness. Its amplitude decreases as the absorption coefficient increases.
- (3) At intermediate angles the intensity scattered from a spherical particle is small and independent of absorption coefficient, and the only rays that contribute are those reflected from the surface. In an irregular particle the intensity at intermediate angles is increased markedly, by as much as an order of magnitude,

<!-- IMAGE: _page_16_Figure_2.jpeg -->

Figure 6.7 (a) Measured phase function of crushed olivine particles of size parameter *X* ∼ 38 (dots) compared with predictions of Mie theory for spheres (line). Olivine data from the Amsterdam Data Base (Munoz *et al.*, 2000). (b) Same as Figure 6.7a for the polarization.

<!-- IMAGE: _page_17_Figure_2.jpeg -->

Figure 6.8 (a) Measured phase functions of a large, clear, spherical particle with a smooth surface and the same particle after the surface had been roughened. (b) Measured polarization functions of the particles shown in Figure 6.8a.

over that for a sphere (Figures 6.7 and 6.8). It is sensitive to the absorption coefficient, showing that internally reflected and transmitted light contributes. This is one of the places where Mie theory is grossly incorrect for an irregular particle.

In scattering by an irregular particle, some of the energy that would have gone into the strong, forward-refracted and weaker, backward-internally-reflected peaks if the particle were a sphere is redirected and internally scattered into the

- sideways directions. Although certain regular particles with smooth external surfaces that meet at angles close to 90◦, such as cubes, may display sharp peaks near zero phase because of an internal corner-reflector effect(Liou *et al.*, 1983), such effects are not important for particles of irregular shapes.
- (4) The backscattered twice-transmitted, once-internally-reflected lobe in an irregular particle merges smoothly into the intermediately scattered light and may or may not be a distinguishable peak.
- (5) An irregular or rough-surfaced particle has a higher single-scattering albedo than a sphere of similar size and dielectric constant. The irregularities tend to decrease the mean path length +*D*, of the rays through the particle, thus decreasing the amount of light absorbed and increasing the single-scattering albedo. In doing so, the rays from the forward lobe are redirected into smaller phase angles.
- (6) The light reflected from the surface is positively polarized. In a clear sphere, the polarization can be large, nearly 100% around 90◦ and then drops to a small positive or negative value because the forward-refracted lobe is negatively polarized and dominates the scattering for *g* ! 2ϑ*c*. As seen in Figure 6.8 at large phase angles the polarization of the irregular particle is less than that for the sphere, but still goes to a small negative value, showing that the polarization of the transmitted lobe is decreased, but is not completely random.
- (7) Highly absorbing particles with large imaginary refractive indices and smooth surfaces have phase functions that are slightly forward-scattering and large positive polarizations (Figures 5.6 and 5.7). However, if their surfaces are rough the phase function can be approximately isotropic or even backscattering (Figure 6.9).
- (8) The phase functions of large irregular particles tend to be much more isotropic than perfect spheres and may even be backscattering. There are two reasons for this. First, as the particle size increases, surface irregularities may become large enough to cast shadows, which are more visilble at larger phase angles. The surface elements of large protuberances facing away from the source, with the largest specular reflectances, tend to be less visible than elements with smaller reflectances facing toward the source.

Second, large real paricles tend to be composite and made up of many smaller particles that can act as internal scatterers and may also be absorbing. The presence of internal scatterers causes major departures from the predictions of Mie theory, as can be seen in Figure 6.10. They are of special importance because internal scatterers are abundant in both laboratory samples and in planetary soils. Most natural particles contain smaller inclusions and bubbles. Usually large particles are polycrystalline, and the internal grain boundaries scatter light. The process of grinding inevitably produces cracks and fractures that radiate

<!-- IMAGE: _page_19_Figure_2.jpeg -->

Figure 6.9 (a) Measured phase functions of large steel spheres with smooth and rough surfaces. (b) Polarization functions of the particles shown in Figure 6.9a.

from the surface of a grain into the interior (Tanashchuk and Gilchuk, 1978; Skorobogatov and Usoskin, 1982). The lunar regolith (and presumably the regoliths of other bodies as well) contains large numbers of agglutinate particles, which are welded agglomerates of smaller grains and voids that can act as internal scatterers. A particularly dramatic effect of inclusions may occur if they consist of submicroscopic particles with large imaginary refractive indices. Because such particles are very efficient absorbers, they may increase the

<!-- IMAGE: _page_20_Figure_2.jpeg -->

Figure 6.10 (a) Measured phase functions of large spherical particles filled with internal scatterers. The terms "low," "intermediate," and "high" refer to the relative internal scattering coefficients. (b) Measured polarization functions of the particles shown in Figure 6.10a.

effective absorption coefficients of their host particles by orders of magnitude (Hapke, 2001).

If internal scatterers are present, less light is directly transmitted through the particle, and more is scattered out the back and sides after traveling only a short distance through the particle. If the subparticles are nonabsorbing this increases both the single-scattering albedo and the amplitude of the phase function at small and intermediate angles. If the subparticles are absorbing the albedo and amount of light reaching the forward surface are both decreased. As internal scatterers are added, the amplitude of the forward lobe decreases, and the intensity scattered at intermediate phase angles increases, so that the phase function becomes more isotropic. Further increasing the internal scattering causes the phase function to acquire a strong, broad backscattered lobe. The polarization peaks around 150◦, implying that the polarization of the internally scattered light is random, so that most of the polarization of the light scattered from the particle will be due to the surface-reflected rays.

The particle phase functions of many planetary regoliths appear to be backscattering. It is of interest to note that the only known types of particles that are backscattering are either filled with internal scatterers or have large imaginary refractive indices and rough surfaces.

(9) McGuire and Hapke (1995) found that the phase functions of their particles could be adequately described by a two-parameter double Henyey–Greenstein function (equation [\[6.7a\]](#page-0-0)). In this representation of #*(g)* the parameter *c* describes the relative amplitudes of the forward-and backscattered lobes and *b* determines their shapes. A forward-scattering particle has *c <* 0; increasing *b* increases the amplitudes and decreases the widths of the lobes.

When plotted on a diagram of *b* versus *c* all of the particles were found to fall within an L-shaped region of restricted area clustered around the empirical curve

$$c = \left(\frac{0.05}{b - 0.15}\right)^{3/4} - 1,\tag{6.19}$$

as shown in Figure 6.11. Clear, spheroidal particles have *b* ∼0*.*$5^{-0}$*.*7 and *c* ∼ !0*.*9*.*

Increasing the absorption decreases the single scattering albedo + and decreases *b* slightly, but does not change *c* appreciably. Making the particle more irregular in shape, but still clear, increases +, decreases *b*, and increases *c*; that is, the particle becomes more isotropic and less strongly forward-scattering. Roughening the surface of the particle or making a composite agglomerate adds internal scatterers and increases *c*. As more internal scatterers are added, *c* increases, but *b* remains in the range 0.15–0.35; that is, the particle becomes more strongly backscattering, while the lobes remain low and wide. Increasing the absorption decreases + and causes a particle to move a short distance in a direction away from either end toward the center of the L-shaped area.

Cord *et al.*(2003) and Shepard and Helfenstein (2007)measured the reflectances of a large number of natural substances in powder form and extracted the values of *b* and *c* by fitting a theoretical reflectance model. Most of these parameters were

<!-- IMAGE: _page_22_Figure_2.jpeg -->

Figure 6.11 Empirical two-parameter double Henyey–Greenstein parameters for large silicate, resin, and metal particles of varied shapes, absorption coefficients, and conditions of surface roughness, and containing differing densities of internal scatterers (data from McGuire and Hapke, 1995).

found to lie close to equation (6.19). Thus *b* and *c* are not independent parameters, but appear to be highly correlated.

In summary, almost any change from a perfect, uniform sphere has the effect of increasing +, decreasing *b*, increasing *c*, and generally causing the particle to scatter more isotropically than a Mie sphere. For a particle with internal scatterers *b* is small, and decreasing the absorption increases both + and *c*, but does not affect *b* appreciably. Smooth strongly absorbing particles scatter nearly isotropically, with *b* and *c* both small; roughening their surfaces decreases + and increases *c* but *b* does not change.

## 6.5 The generalized equivalent-slab model 6.5.1 The scattering efficiency

The exact particle scattering models discussed in this chapter require extensive numerical evaluation, and are inconvenient to use. The empirical models of Section 6.3 require the specification of parameters that are not connected in any obvious way to the size, shape, and complex refractive index of the particle. Hence, a general analytic scattering model would appear to be useful, especially in contrast to spheres which are hardly realistic analogs of natural regolith particles. In this section, the equivalent-slab model derived in Chapter 5 for the nondiffractive portion of the scattering efficiency of large spheres will be extended to ensembles of large irregular particles. The parameters of the model are based on experimental data. Although approximate, the model is given in closed analytic form, and its parameters can be related to the fundamental properties of the particle. An expression for the phase function will be derived, and the model will be further extended to include coated particles.

Following the notation in Chapter 5, write *QS* = *Qs* +*Qd* where *Qd* is the portion of the scattering efficiency associated with diffraction, and *Qs* is the nondiffractive portion scattered into smaller phase angles. The diffraction term will be discussed first.

### 6.5.2 Fraunhofer diffraction

We have seen that the diffraction efficiency of a perfect, isolated, large sphere is *Qd* =1. By Babinet's principle (Section 5.4.4.2), the diffraction of a wave around an isolated obstacle is equivalent to that through a hole of identical cross-sectional size and shape in an opaque, infinite screen. Because the total power in the diffraction pattern of the hole is equal to the power passing through the hole, regardless of shape, the diffraction efficiency of the hole is 1. Hence, the average diffraction efficiency of an ensemble of isolated, randomly oriented, irregular particles is also *Qd* = 1. The diffraction pattern has a phase function sharply peaked in the forward direction with an angular width ∼ 1*/X*. For the portion of the phase function associated with diffraction, the Allen function, equation (6.2), may be used.

However, it must be emphasized that Fraunhofer diffraction is only relevant to an isolated particle and does not exist when particles are close together in a regolith or powder.

### 6.5.3 Nondiffractive scattering

*6.5.3.1 The equivalent-slab model for Qs*

The success of the equivalent-slab model in reproducing *Qs* for a sphere suggests that we attempt to generalize it to irregular particles. Hence, we again write equation (5.52a) for *Qs*,

$$Q_s = S_e + (1 - S_e) \frac{1 - S_i}{1 - S_i \Theta} \Theta.$$
 (6.20)

The various quantities in this equation have the same meanings as in Section 5.5.6. That is, *Se* and *Si* are respectively the surface reflection coefficients for light that is externally and internally incident, and , is the internal-transmission factor. The first term of (6.20) represents the light externally scattered from the particle surface. The numerator of the second term corrects for the light transmitted once through the particle, and the denominator represents light multiply internally scattered through the particle. Expressions for each of these quantities for irregular particles will be derived in the following section.

### 6.5.3.2 Exterior-surface reflection

The evaluation of *Se* is simple if the particle is *convex*, with smooth, randomly oriented surface facets. Van de Hulst (1957) defined a convex particle as one that "when illuminated from any direction has a light side and a dark side separated by a closed curve on the surface. Any small surface area *dS* is on the dark side when its outward normal makes an angle *<*90◦ with the direction of propagation of the incident light; it is on the light side when this angle is *>*90◦." A more intuitive description of a convex particle would be to say that it is one that is without any depressions, dimples, or projections on its surface that can cast shadows on another part of the surface. Convex particles include most simple shapes, such as spheres, ellipsoids, cylinders, and euhedral crystals of most minerals.

The normals to the surface facets of an ensemble of randomly oriented, convex particles are distributed isotropically. This distribution is identical with that of the surface elements of a sphere. Therefore, provided each facet is smooth, the light reflected from the surface facets of the ensemble is the same as for a sphere, so that the phase function associated with external reflection is given by the integral of the Fresnel coefficients, equation (5.36).

The effects of surface roughness on the scattering characteristics of the particle depend on the scale of the roughness. The discussion in Section 4.6 implies that under most circumstances a particle surface may be treated as smooth if the scale of the surface roughness is small compared with the wavelength. More sophisticated theoretical analyses (e.g., Berreman, 1970) indicate that small asperities and depressions in a surface will scatter light in a manner similar to dipoles suspended just above the surface. Because a dipole scatters light proportionally to *(*size*/*λ*)*4, if the Rayleigh criterion is satisfied then the effects of a few small surface imperfections usually can be ignored. This conclusion is supported by the microwave experiments of Zerull and Giese (1974), which showed that a sphere with surface roughness elements small compared with the wavelength scatters light in a manner that is virtually indistinguishable from the predictions of Mie theory.

A major exception may occur when the complex refractive index is in the region of anomalous dispersion in the vicinity of a strong absorption band. As discussed in Chapter 5, when *Ke* = *n*2 ( !2, a resonance can occur that may cause the scattering and particularly the absorption efficiencies of small particles to be anomalously large, so that they cannot be ignored. This point has been emphasized by Emslie and Aronson (1973). The effect can be especially important in the thermal infrared, where materials typically have strong restrahlen bands.

A second exception occurs when k is large, as with metals. Figure 6.10 shows that roughening the surface of a metal will markedly decrease the scattering efficiency. The probable explanation is that the scratches and corners on the surface act like Rayleigh absorbers (Section 5.4.2).

The case in which the scale of the roughness is larger than the wavelength is more difficult to treat, because shadowing may be important. Several experimental studies of the effect of well-characterized, large-scale roughness on the reflection from a surface have been carried out, including those by Torrance and Sparrow (1967) and O'Donnell and Mendez (1987). An important conclusion that may be drawn from these studies is that the general character of the scattering remains quasi-specular. That is, the scattering does not change from specular to diffuse, as has been conjectured by many authors. Rather, the reflected light is redirected into a relatively broad peak that is approximately centered in the specular direction. Even at glancing incidence and reflection, the character of the scattering remains quasi-specular. Apparently, a ground or frosted surface scatters light diffusely because of the subsurface fractures created by the grinding process, rather than because of the irregular surface geometry.

Thus, to a first approximation the scattering from the surface of an irregular particle can be treated as quasi-specular, so that the exterior surface reflection coefficient of an irregular particle is  $S_e$ , the same as that of a sphere, equation (5.36). A convenient analytic approximation to  $S_e$  is given by equation (5.37) and plotted in Figure 5.12. Repeating it here for convenience,

$$S_e = 0.0587 + 0.8543R(0) + 0.0870R(0)^2,$$

where

$$R(0) = \frac{(n_r - 1)^2 + n_i^2}{(n_r + 1)^2 + n_i^2}$$

is the normal specular reflection coefficient.

For particles with very rough surfaces containing large numbers of small scattering elements, it can be assumed that the surface asperities and depressions behave like quasi-independent small scattering particles, so that the effective scattering efficiency can be treated like a mixture of large and small particles. Experimental support for this assumption is given in Section 6.5.4. Scattering by mixtures is treated in Chapter 10.

### 6.5.3.3 Internal surface reflection

In a perfect sphere, the angle at which a refracted ray is incident on the inside of the sphere is equal to that with which it is refracted into the sphere, so that  $S_i = S_e$ . However, as emphasized by Melamed (1963), for an ensemble of irregular particles the two angles are uncorrelated, and a refracted ray will have virtually equal probabilities of encountering interior surfaces at all orientations. Thus, a reasonable expression for the interior reflection coefficient is the integral of the internal Fresnel reflection coefficients over all angles:

$$S_{i} = \int_{0}^{\pi/2} [R_{\perp}(\vartheta') + R_{\parallel}(\vartheta')] \cos \vartheta' \sin \vartheta' d\vartheta' y = 2 \int_{0}^{\pi/2} R(\vartheta') \cos \vartheta' \sin \vartheta' d\vartheta',$$
(6.21)

where  $\vartheta'$  is the angle of incidence for the interior rays. This expression is identical in form with (5.36) for  $S_e$ , except that now  $R(\vartheta')$  refers to internally reflected light. The curve for  $S_i$  calculated by numerical integration for n real is shown as a function of n in Figure 6.12.

A convenient approximate analytic expression for  $S_i$  may be derived as follows. As may be seen in Figure 4.5, when  $0 < \theta < \theta_c$  the average of the internal polarized reflectivities is nearly constant and equal to its value R(0) at  $\theta = 0$ . It then rises abruptly to 1 at  $\theta = \theta_c$ , and is equal to 1 for  $\vartheta'_c < \vartheta' < \pi/2$ . Hence,  $S_i$  can be

<!-- IMAGE: _page_26_Figure_6.jpeg -->

Figure 6.12 Surface reflection coefficient for light internally incident on the surface of the particle versus the real part of the refractive index for  $n_i << 1$ . The solid line is the exact expression, equation (6.21); the dashed line is the approximation, equation (6.23).

approximated by

$$S_i \simeq 2 \left[ \int_0^{\vartheta_c'} R(0) \cos \theta \sin \theta d\theta + \int_{\vartheta_c'}^{\pi/2} \cos \theta \sin \theta d\theta \right], \tag{6.22}$$

Carrying out this integration gives

$$S_i \simeq 1 - \sin^2 \theta_c [1 - R(0)],$$

where  $\sin \theta_c = 1/n_r$ , and  $n_r$ , is the real part of the refractive index of the particle relative to the surrounding medium. Empirically, it was found that a better fit can be obtained if equation (5.37) for  $S_e$  is substituted for R(0), which gives

$$S_i = 1 - \frac{1}{n_r^2} [0.9413 - 0.8543R(0) - 0.0870R(0)^2].$$
 (6.23)

This expression for  $S_i$  is plotted in Figure 6.12 for n real, where it is compared with the exact expression, equation (6.21). In practice, it is seldom necessary to calculate  $S_i$  when  $n_i$  is large enough to affect R(0), because then the particle is opaque and the refracted wave is absorbed before it reaches the far surface.

### 6.5.3.4 The internal-transmission factor

One might try to estimate  $\Theta$  by carrying out ray-tracing calculations on a variety of models of specific shapes, hoping that the results would have some resemblance to the transmission of irregular particles. However, this approach is of questionable value, particularly if it is realized that accounting for effects of particle shape is not the only difficulty: often the particles of interest are not clear, but are full of internal scatterers. Instead of that approach, we will consider several possible general models and use the results of experiments to choose the best one. Four models for  $\Theta$  will be considered: exponential, Melamed, internal scattering, and double exponential. These are illustrated schematically in Figure 6.13.

<!-- IMAGE: _page_27_Picture_11.jpeg -->

Figure 6.13 Schematic diagram of the various models for the scattering efficiency.

**The exponential model** It was shown in Chapter 5 that for a sphere the internal-transmission factor can be approximated by an exponential function. Hence, the first and simplest model to be considered is of the form

$$\Theta = e^{-\alpha \langle D \rangle},\tag{6.24}$$

where  $\langle D \rangle$  is the average distance traveled by all transmitted rays during one traverse of the particle. If the particle is spherical,  $\langle D \rangle \simeq 0.9D$ . However, if the particle is irregular, then  $\langle D \rangle$  can be quite different from D and in general will be smaller.

The Melamed model Another possibility for  $\Theta$  was suggested by Melamed (1963). In his model, the external reflection coefficient is assumed to be  $S_e$ , and Melamed was the first to introduce the idea that the internal reflection coefficient should be  $S_i$ , which we have adopted here.

To calculate  $\Theta$  Melamed assumes a clear particle of spherical shape and diameter D=2a. Radiance emerging from any point of an inner surface after being either transmitted or reflected is assumed to have an angular distribution given by Lambert's law,  $(1/\pi)\cos\vartheta'$ , where  $\vartheta'$  is the angle between the surface normal and the direction of the radiance (see Figure 6.14). An incremental area dA a

<!-- IMAGE: _page_28_Picture_7.jpeg -->

Figure 6.14 Melamed model for the internal-transmission factor.

distance  $x = D\cos\vartheta'$  away on the inner surface of the sphere subtends a solid angle  $dA\cos\vartheta'/x^2$  from the point. The radiance is attenuated by a factor  $e^{-\alpha x}$  in traveling from the point to dA. Thus, the total fraction of light emitted from the point that reaches all areas on the interior surface of the particle is

$$\Theta = \int_{\psi=0}^{\pi} \frac{1}{\pi} \cos \vartheta' e^{-\alpha x} \frac{dA \cos \vartheta'}{x^2},$$

where  $dA = 2\pi a^2 \sin \psi d\psi$ , and  $\psi = \pi - 2\vartheta'$ . It is readily seen that  $x = a \sin \psi$ , so that  $dA = 2\pi x dx$ . Hence,

$$\Theta = \int_0^D e^{-\alpha x} \frac{2x}{D^2} dx = \frac{2}{(\alpha D)^2} \left[ 1 - e^{-\alpha D} (1 + \alpha D) \right].$$

Generalizing to irregular particles by replacing D by  $\langle D \rangle$  gives

$$\Theta = \frac{2}{(\alpha \langle D \rangle)^2} \left[ 1 - e^{-\alpha D} (1 + \alpha \langle D \rangle) \right]. \tag{6.25}$$

The internal-scattering model The importance of internal scatterers in natural particles has already been emphasized. One approach to investigating their effects on  $\Theta$  would be to attempt to find the radiance inside a spherical absorbing particle containing embedded scatterers. In order to do that it would be necessary to solve the equation of radiative transfer in a spherical geometry. The radiative-transfer equation will be introduced in Chapter 7, with exact and approximate solutions obtained in subsequent chapters. However, the solution of this equation is a formidable problem that requires numerical solution by a computer for reasonable accuracy. Thus, we seek a simpler approximate analytic model.

We have seen that the transmission factor of a perfect sphere can be approximated quite well by  $\exp(-a\langle D\rangle)$ , which is equivalent to the transmission of a slab of thickness  $\langle D\rangle$ . This suggests that the transmission of an absorbing slab containing embedded scatterers might provide a suitable approximation. Consider the following model: diffuse radiation is assumed to be incident from above on a plane slab of thickness L, refractive index n, absorption coefficient  $\alpha$ , and with distributed scattering coefficient s, which describes the scattering by the internal embedded scattering centers. These are assumed to scatter light isotropically. The physical meaning of s is similar to that of  $\alpha$ : the intensity is attenuated by a factor of  $e^{-1}$  after traveling a distance 1/s, but the attenuation is by scattering, rather than by absorption. As with the other models, the slab is assumed to have external reflection coefficient  $S_e$  and internal reflection coefficient  $S_i$ . It will also be assumed

that any radiation transmitted through or reflected from an internal surface has a diffuse angular distribution.

The problem of the radiation field inside such a slab and the intensity emerging from the top and bottom surfaces will be solved in Chapter 10 using a method known as the two-stream approximation to the equation of radiative transfer. It will be shown that  $Q_{sB}$ , the efficiency for scattering light into the back direction, and  $Q_{sF}$ , the efficiency for scattering into the forward direction, are given by the relations

$$Q_{sB} + Q_{sF} = Q_s$$

and

$$Q_{SB} - Q_{SF} = \Delta Q_{S}$$

where the scattering efficiency  $Q_s$  is given by equation (6.20), with

$$\Theta = \frac{r_i + \exp\left(-\sqrt{\alpha(\alpha+s)}2L\right)}{1 + r_i \exp\left(-\sqrt{\alpha(\alpha+s)}2L\right)},\tag{6.26}$$

and

$$r_i = \frac{1 - \sqrt{\alpha/(\alpha + s)}}{1 + \sqrt{\alpha/(\alpha + s)}},\tag{6.27}$$

and the scattering efficiency difference  $\Delta Q_s$  is

$$\Delta Q_s = S_e + (1 - S_e)(1 - S_i) \frac{\Psi}{1 - S_i \Psi}, \tag{6.28}$$

with

$$\Psi = \frac{r_i - \exp\left(-\sqrt{\alpha(\alpha+s)}2L\right)}{1 - r_i \exp\left(-\sqrt{\alpha(\alpha+s)}2L\right)}.$$
(6.29)

If the slab is clear, with s=0, then  $\Theta=-\Psi=\exp(-a2L)$ , which is identical with equations (5.52a), (5.52b), and (5.56) for a sphere if 2L is replaced by  $\langle D \rangle$ . This shows that the mean path length through the slab is  $2L=\langle D \rangle$ , where  $\langle D \rangle$  is to be interpreted as the length of the average ray that traverses the particle once without being scattered. This gives that the internal-transmission factor of the equivalent slab is

$$\Theta = \frac{r_i + \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}{1 + r_i \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)},\tag{6.30}$$

and the scattering efficiency difference factor is

$$\Psi = \frac{r_i - \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}{1 - r_i \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}.$$
 (6.31)

**The double-exponential model** It was suggested in the discussion of  $S_e$  that surface asperities might scatter as quasi-independent particles, so that  $Q_s$  can be treated as a mixture of particles of two different sizes. Internal scattering elements located just under the surface might also behave in this manner. Thus, we will consider a model of the form

$$Q_{s} = S_{e} + (1 - S_{e})(1 - S_{i}) \left[ (1 - f) \frac{e^{-\alpha \langle D \rangle}}{1 - S_{i}e^{-\alpha \langle D \rangle}} + f \frac{e^{-\alpha \Delta D}}{1 - S_{i}e^{-\alpha \Delta D}} \right], \quad (6.32)$$

where  $\langle D \rangle$  is the mean absorption path through the main particle,  $\Delta D$  is the mean path associated with scattering by the surface asperities or subsurface fractures, and f is the fraction of light scattered by these small "particles."

### 6.5.4 Experimental choice of models for $\Theta$

The scattering efficiencies corresponding to these four models for  $\Theta$  are illustrated in Figure 6.15. For very small values of  $\alpha$ , all models attenuate light exponentially; that is,  $\Theta \simeq \exp(-\alpha \langle D \rangle)$ . At large values of  $\alpha \langle D \rangle$  the scattering efficiencies all approach  $S_e$ , but for the last three models they do so more slowly than for the exponential model, so that  $Q_s$  is larger at intermediate values of  $\alpha \langle D \rangle$ .

<!-- IMAGE: _page_31_Figure_7.jpeg -->

Figure 6.15 Scattering efficiency of a particle of refractive index  $n_r = 1.50$  vs.  $\alpha \langle D \rangle$  for the four internal-transmission models considered in the text. For the internal-scattering model,  $s \langle D \rangle = 5$ , and for the double-exponential model, f = 0.2 and  $\Delta D = 0.05 \langle D \rangle$ .

The exponential and Melamed models have only one free parameter,  $\langle D \rangle$ ; the internal-scattering model has two,  $\langle D \rangle$  and s; and the double-exponential model has three,  $\langle D \rangle$ ,  $\Delta D$ , and f.

In order to verify equation (6.20) for  $Q_s$  and choose the best expression for  $\Theta$ , the results of measurements on comminuted materials will be used. This is justified because most laboratory powders and planetary regoliths are the products of grinding and crushing.

In a series of measurements on crushed-glass powders (Hapke and Wells, 1981), silicate glass doped with  $CoCl_2$  was synthesized, and its absorption coefficient was measured as a function of wavelength in the near ultraviolet, visible, and near infrared by transmission of polished thin sections. The remainder of the batch was ground and separated into several size ranges by wet-sieving. Each size fraction was washed to remove clinging fines. The bidirectional reflectances of the powder fractions were measured over the same wavelength range as the transmission measurements and  $Q_s$  as a function of wavelength found using the reflectance theory to be derived in Chapters 8–11. Because  $\alpha(\lambda)$  was known,  $Q_s(\lambda)$  could be converted to  $Q_s$  as a function of  $\alpha$ . The four models for  $\Theta$  were then fitted to the data. The resultant experimental values and fitted curves for each size range are shown in Figures 6.16. (To avoid clutter, curves for all of the models are not shown in all of the figures.)

From these figures several conclusions may be drawn:

- (1) The general expression, equation (6.20), provides a reasonably satisfactory description of  $Q_s$  as a function of  $\alpha \langle D \rangle$  over the range from 0 to 22. However, the goodness of the fit depends on the choice of  $\Theta$ .
- (2) Because all four models behave exponentially when  $\alpha \langle D \rangle$  is small, they all fit the data for the smallest size fraction, <37  $\mu$ m (Figure 6.16a), for which  $\alpha \langle D \rangle \lesssim 2$ .
- (3) For larger size fractions the exponential model is unsatisfactory. It is too low for  $\alpha \langle D \rangle \gtrsim 2$ .
- (4) The Melamed model is an improvement over the exponential model, but is also too low for the larger size fractions.
- (5) Both the internal-scattering and double-exponential models provide satisfactory fits over the entire range of particle sizes and absorption coefficients measured (Figure 6.16e). The double-exponential model gives a slightly better fit near  $\alpha \sim 2\,\mu\,\text{m}^{-1}$ , which is not surprising because the double-exponential model has three parameters that can be fitted, in contrast to the internal-scattering model, which has only two.
- (6) The mean ray path length  $\langle D \rangle$  is of the same order of magnitude as the particle size, but is smaller than the average particle diameter, as is expected for irregular particles.

<!-- IMAGE: _page_33_Figure_2.jpeg -->

Figure 6.16 (a) Scattering efficiency of crushed cobalt glass of size <37 µm as a function of absorption coefficient. The points show the values calculated from reflectance measurements. The lines show the fit of the various models discussed in the text. The Melamed model with  $\langle D \rangle = 24 \,\mu\text{m}$  and the double-exponential model with  $\langle D \rangle = 18 \,\mu\text{m}$ , f = 0.2, and  $\Delta D = 60 \,\mu\text{m}$  are indistinguishable from the internal-scattering curve. (b) Same as Figure 6.16a for size  $37-49\,\mu m$ . The internal-scattering curve is indistinguishable from the Melamed model with  $\langle D \rangle =$  $35 \,\mu\text{m}$  and the double-exponential model with  $\langle D \rangle = 29 \,\mu\text{m}$ , f = 0.2, and  $\Delta D =$  $6.0\,\mu\text{m}$ . (c) Same as Figure 6.16a for size  $37-74\,\mu\text{m}$ . The internal-scattering curve is indistinguishable from the double-exponential model with  $\langle D \rangle = 45 \,\mu\text{m}$ , f =0.2, and  $\Delta D = 4.5 \,\mu\text{m}$ . (d) Same as Figure 6.16a for size 74–150  $\mu\text{m}$ . The internalscattering curve is indistinguishable from the double-exponential model with  $\langle D \rangle$  =  $80 \,\mu\text{m}$ , f = 0.2, and  $\Delta D = 5.6 \,\mu\text{m}$ . (e) Same as Figure 6.16a for size  $> 150 \,\mu\text{m}$ . The exponential and Melamed models fall well below the measured points. This is the only example for which the internal-scattering and double-exponential models are noticeably different.

<!-- IMAGE: _page_34_Figure_0.jpeg -->

Figure 6.16 (*cont.*)

- (7) The excellent fit provided by the double-exponential model over the entire range of  $\alpha$  supports the hypothesis that surface asperities and subsurface scatterers can be treated as separate small particles in their effects on  $Q_s$ . For the particles of ground silicate glass whose scattering efficiencies are shown in Figure 6.13, the surface imperfections evidently scatter about 15% of the light and behave as particles whose effective sizes are approximately 5  $\mu$ m.
- (8) The best fit value of the internal scattering coefficient is  $s = 600 \,\mathrm{cm}^{-1}$  for these silicate glass particles. It is likely that both of the successful models, the double-exponential and internal-scattering models, are describing the same phenomenon, the scattering by surface asperities and subsurface fractures, but in mathematically different ways. Hence, the decision as to which one to use is arbitrary. We will adopt the internal-scattering model, equation (6.30), because this model contains the minimum number of free parameters that can still adequately describe  $Q_s$ . Note that the exponential model is included as a special case when s = 0. If it is desired to use the double-exponential model, this can easily be done using the single-exponential model for  $\Theta$  and the theory for intimate mixtures that is discussed in Chapter 10.

Some additional properties of the internal-scattering model should be noted. When  $\alpha \langle D \rangle \ll 1$ ,  $\Theta \simeq \exp(-\alpha \langle D \rangle)$  independently of s. Thus, to first order,  $Q_s \simeq S_e + (1 - S_e)e^{-\alpha \langle D \rangle}$ , which is of the same form as expression (6.16), that was used by Hapke and Nelson (1975) to describe Venus cloud particles.

When  $\alpha$  is small, the critical path length inside the particle that governs the behavior of  $Q_s$  is  $\langle D \rangle$ , which is a distance somewhat less than the mean diameter of the particle. As  $\alpha$  increases,  $\Theta$  is influenced more and more by s, until, when  $\alpha \langle D \rangle \gg 1$ ,  $\Theta \simeq s/4\alpha$ , and

$$Q_s \simeq S_e + (1 - S_e)(1 - S_i) \frac{s}{4\alpha}.$$
 (6.32)

In this case,  $Q_s$  is very nearly independent of  $\langle D \rangle$ , and the critical internal path is the scattering length 1/s. That is, the portion of the light that has been refracted into the particle and scattered back out has traveled a mean distance of the order of 1/s. Because  $\alpha\langle D \rangle \gg 1$ , the particle is nearly opaque, so that most of the refracted light interacts only with a layer of the order of 1/s thick on the side of the particle facing the source. Hence, s does not necessarily refer to the scattering coefficient throughout the whole interior of the particle, but characterizes the imperfections close to the surface. For this reason, s will be referred to as the *near-surface scattering coefficient*. This term is intended to be inclusive and not exclude the possibility that the scatterers are distributed throughout the volume of the particle.

A caveat concerning this model for  $Q_s$  must be emphasized, in that it is based on measurements on one type of particle, pulverized silicate glass. The extent to

<!-- IMAGE: _page_36_Figure_2.jpeg -->

Figure 6.17 Absorption efficiency vs.  $\alpha \langle D \rangle$  calculated using (6.20) and (6.26) with s=0. On the log-log plot the dashed line has unit slope, showing that  $Q_A \propto \alpha$  for  $\alpha \langle D \rangle \lesssim 0.1$ .

which these particles are representative has not been experimentally explored. Of particular interest is the appropriate value of *s* for other types of particles

### 6.5.5 The espat function

In Chapter 5 a quantity called the *espat function* was introduced. We will now consider its properties in detail. When  $n_i=1$ , the amount of light absorbed must be proportional to the product of the absorption coefficient and the volume of the particle, so that  $Q_A$  must be proportional to  $\alpha\langle D\rangle$ . In Figure 6.17 the quantity  $Q_A=1-Q_s$  calculated from (6.20) and (6.26) is plotted versus  $\alpha\langle D\rangle$  for s=0. This figure shows that  $Q_A$  is indeed linearly proportional to  $\alpha$ , but that the linear region is only in the range  $0<\alpha\langle D\rangle\lesssim 0.1$ .

However, consider the quantity

$$W \equiv \frac{Q_A}{Q_S} = \frac{Q_E - Q_S}{Q_S} = \frac{1 - \varpi}{\varpi}.$$
 (6.33)

For a large isolated particle  $Q_E \simeq 2$ . However, it will be argued in Chapter 7 that when the particles are close enough together to touch, as in a powder or regolith, Fraunhofer diffraction does not exist. In that case  $Q_d = 0$ ,  $Q_E \approx 1$ ,  $Q_S = Q_S = \varpi$ ,

and  $W = (1 - Q_s)/Q_s$ . Inserting expression (6.20) for  $Q_s$  into (6.33), W becomes

$$W = \frac{1 - S_e}{1 - S_i} \frac{1/\Theta - 1}{1 + [S_e/(1 - S_i)](1/\Theta - 1)}.$$
(6.34)

Using (6.26) for  $\Theta$ , the quantity  $1/\Theta - 1$  may be expanded for small  $a\langle D \rangle$  to give

$$1/\Theta - 1 \simeq (\alpha \langle D \rangle) + \frac{1}{2} \left[ 1 - \frac{1}{6} (s \langle D \rangle) \right] (\alpha \langle D \rangle)^2 + L. \tag{6.35}$$

Hence, to first order in  $\alpha \langle D \rangle$ ,

$$W \simeq \frac{1 - S_e}{1 - S_i} \alpha \langle D \rangle. \tag{6.36}$$

In Figure 6.18 W is plotted versus  $[(1-S_i)/(1-S_i)]\alpha\langle D\rangle$  for n=1.50 and several values of  $s\langle D\rangle$ . This figure shows that when  $s\langle D\rangle$  is not too large, W is approximately linearly proportional to  $\alpha$  over a much larger range of  $\alpha\langle D\rangle$  than  $Q_A$ . There is no physical reason for this quasi-linear behavior when  $\alpha\langle D\rangle$  is larger than 0.1; it is simply a serendipitous mathematical coincidence. However, as  $\alpha\langle D\rangle$  becomes large, the slope of W decreases until W saturates at

$$W = (1 - S_e)/S_e. (6.37)$$

<!-- IMAGE: _page_37_Figure_10.jpeg -->

Figure 6.18 Espat function W of a particle calculated using (6.30) for several values of s < D >. The solid lines show the calculated values of W. The dashed lines show the straight-line approximations to W. The slopes of the straight lines are as indicated.

When  $\alpha\langle D\rangle$  is small, Figure 6.18 shows that W approximates, although it is not exactly equal to, a straight line that is proportional to  $[(1-S_e)/(1-S_i)]\alpha\langle D\rangle$ . However, the constant of proportionality and the length of the linear region both depend on s. When  $s\langle D\rangle=1$ , the constant of proportionality is about 4/3, and the quasi-linear region extends out to  $[(1-S_e)/(1-S_i)]\alpha\langle D\rangle\simeq 6$ , or  $\alpha\langle D\rangle\simeq 3$ . As s increases, the constant and the length decrease until when  $s\langle D\rangle=10$ , the constant is 3/4 and the length of the quasi-linear region is less than 1.

In the quasi-linear region we may write

$$W \simeq \alpha D_e$$
, (6.38a)

where  $D_e$  is an effective particle size given by

$$D_e = C \frac{1 - S_e}{1 - S_i} \langle D \rangle, \tag{6.38b}$$

and C is a constant that depends on s, but  $C \sim 1$ . Thus, the W function is an absorption optical thickness. Hence, this quantity will be called the effective single-particle absorption thickness function, or *espat function*.

Except in regions of anomalous dispersion,  $n_r$  is very nearly independent of wavelength, so that  $D_e$  is approximately constant also. For many substances of interest in remote sensing,  $D_e/\langle D \rangle$  is somewhat greater than 2, while  $\langle D \rangle/D$  is somewhat less than 1, where D is the particle size. Hence, in the absence of more definite information, a rough estimate of  $D_e$  is

$$D_e \simeq 2D. \tag{6.39}$$

The effective particle size  $D_e$  decreases with increasing  $s\langle D \rangle$ . The espat function is most useful when the medium consists of particles that are sufficiently small that  $s\langle D \rangle \lesssim 3$ .

In Figure 6.19 W is plotted against  $\alpha$  for four size fractions of the Co glass. The linear regions are prominent in each figure. The values of  $D_e$  for best fit to the data in the linear region are given in the figures. As  $\alpha$  increases, W departs from linearity. Also shown for each data set is the theoretical espat function calculated from the internal-scattering model with the same values of s and  $\langle D \rangle$  used in Figure 6.16.

Combining relations (6.33) and (6.38) provides a simple approximation for  $Q_s$  that is valid within the quasi-linear region:

$$Q_s = \frac{1}{1+W} \simeq \frac{1}{1+\alpha D_e}.$$
 (6.40)

Because W is not independent of  $s\langle D \rangle$ , the range in  $\alpha(D)$  over which this expression is valid depends on the particle size. However, even for the largest particles of Figure 6.19, W is linear for  $\alpha D_e \lesssim 3$ , or  $\varpi = Q_s \gtrsim 0.25$ . It can be calculated

<!-- IMAGE: _page_39_Figure_2.jpeg -->

Figure 6.19 Espat function W vs. absorption coefficient for four size fractions of the cobalt silicate glass. W is calculated from the measured bidirectional reflectance of the powdered glass;  $\alpha$  is measured from transmission. Also given in each figure is the effective particle size  $D_e$  calculated from the slope of the linear part of the curve, and the average path length  $\langle D \rangle$  and internal scattering coefficient s calculated from fitting the internal-scattering model to the data. (Reproduced from Hapke and Wells [1981], copyright 1981 by the American Geophysical Union.)

from the reflectance expressions that will be derived in later chapters that  $\varpi \simeq 0.25$  corresponds to particulate media with reflectances of the order of 0.07. Thus, expression (6.40) for  $Q_s$  may be used if the reflectance is greater than about 7%, provided that the density of internal scatterers is not too high.

<!-- IMAGE: _page_40_Figure_2.jpeg -->

Figure 6.19 (*cont.*)

In addition to providing a simple expression for *Qs* the espat function can be very useful for extracting absorption coefficients from reflectance measurements. This will be discussed in more detail in Chapter 14. However, it can be used only if neither ς*(D)* nor *s*+*D*, is large. It will also be seen in Chapter 14 that the linear relation between *W* and ς does not hold in general for mixtures of different types of particles.

### 6.5.7 The particle phase function of the equivalent-slab model

From the relations *Qs* = *QsB* + *QsF* and /*Qs* = *QsB*–*QsF*, the fractions of *Qs* scattered in the back and forward directions are, respectively

$$\frac{Q_{sB}}{Q_s} = \frac{Q_s + \Delta Q_s}{2Q_s},\tag{6.41a}$$

and

$$\frac{Q_{sF}}{Q_s} = \frac{Q_s - \Delta Q_s}{2Q_s}.\tag{6.41b}$$

Based on the results ofMcGuire and Hapke (1995),Domingue and Verbiscer(1997), Hartman and Domingue (1998),Cord *et al.*(2003), and Shepard and Helfenstein (2007), the two-parameter double Henyey–Greenstein function, #HG2*(g)*(equation [\[6.7a\]](#page-0-0)), appears to be able to describe a wide variety of particles, and so will be used in the general equivalent-slab model. The parameters in the function can be obtained by equating the strength of the backscattering term with *QsB/Qs* and the forwardscattering term with *QsF/Qs*, giving *QsB/Qs* =*(*1+*c)/*2 and *QsF/Qs* =*(*1°*c)/*2. Solving these for *c* gives

$$c = \frac{Q_{sB}}{Q_s} - \frac{Q_{sF}}{Q_s} = \frac{\Delta Q_s}{Q_s}.$$
 (6.42)

The lobe shape parameter *b* can then found by using the McGuire–Hapke relation, equation (6.19), between *b* and *c*. Solving this equation for *b* gives

$$b = 0.15 + \frac{0.05}{(1+c)^{4/3}} = 0.15 + \frac{0.05}{(1+\Delta Q_s/Q_s)^{4/3}}.$$
 (6.43)

### 6.5.8 Coated particles

Coated particles are common in nature. They are often produced by weathering processes operating on rocks and soil grains on the surfaces of a planet. To account for the effects of coatings the equivalent-slab model can be extended with the following assumptions: (1) the coatings are irregular in thickness so that no interference effects occur; (2) the coatings absorb light but are sufficiently thin that internal scattering within them is negligible.

Notation: let *Sjk* be the Fresnel reflection coefficients averaged over angle for rays incident from medium *j* reflected from the interface between mediums *j* and *k*. If *nrj < nrk* then *Sjk* is calculated using equation (5.37) for external incidence; if *nrj > nrk* then *Sjk* is calculated using equation (6.23) for internal incidence. Let subscript 0 denote values of quantities in the medium in which the coated particle is imbedded (usually air or vacuum); let subscript 1 denote the coating; and subscript 2 denote the host coated particles. Let the average ray path length through the coating be *<l>* and the average path length through the coated particle be *<D>*.

Using the same formalism as was used in Chapter 5 to derive *Qs* (Figure 5.15), but keeping the reflected and transmitted parts separate, it may readily be shown that the coefficient for the reflection of light from the surface of the coating on the back side of the particle for light incident from outside is

$$R_B = S_{01} + (1 - S_{01})(1 - S_{12}) \frac{S_{12} \exp(-2\alpha_1 < l >)}{1 - S_{10}S_{12} \exp(-2\alpha_1 < l >)}$$
(6.44a)

and the transmission coefficient is

$$T_B = (1 - S_{21})(1 - S_{10}) \frac{\exp(-2\alpha_1 < l >)}{1 - S_{10}S_{12}\exp(-2\alpha_1 < l >)}.$$
 (6.44b)

Similarly, the reflection coefficient of the coating on the forward side of the particle for light incident from inside the particle is

$$R_F = S_{21} + (1 - S_{21})(1 - S_{12}) \frac{S_{10} \exp(-2\alpha_1 < l >)}{1 - S_{12}S_{10} \exp(-2\alpha_1 < l >)},$$
(6.45a)

and the transmission coefficient is

$$T_F = (1 - S_{21})(1 - S_{10}) \frac{\exp(-2\alpha_1 < l >)}{1 - S_{12}S_{10}\exp(-2\alpha_1 < l >)}.$$
 (6.45b)

Then the equations for the scattering efficiency and phase function of the equivalentslab approximation of an uncoated particle can be used for a coated particle by making the following substitutions: *Se* → *RB, (*1–*Se)* → *TB, Si* → *RF , (*1–*Si)* → *TF* , giving

$$Q_s = R_B + T_B T_F \frac{\Theta}{1 - R_F \Theta},\tag{6.46a}$$

$$\Delta Q_s = R_B + T_B T_F \frac{\Psi}{1 - R_F \Psi},\tag{6.46b}$$

where , and 0 refer to the interior of the coated particle and are the same as equations (6.30) and (6.31), respectively. The phase function is the two-parameter double Henyey–Greenstein function, equation (6.7a) with *c* = /*Qs/Qs* and *b* given by equation (6.43).

This completes the derivation of the equivalent-slab model.

### 6.5.9 Summary of the equivalent-slab model for irregular particles

For convenience, the equations of the equivalent-slab model for *X <*∼ 1 are collected here. The radiance scattered by a single particle is given by

$$I(g) = J\sigma Q_s \frac{\Pi(g)}{4\pi}.$$
 (6.46)

When *X* % 1, the dipole expressions for spheres (Chapter 5.4.2) may be used to calculate *Qs* and #*(*g*)*. In the region where *X* ! 1, the irregular particle shapes and the fact that most natural assemblages of particles have wide size distributions cause the optical parameters to approach their large X values smoothly and monotonically, without the large oscillations seen in spheres. Similarly, resonances in  $\Pi(g)$  such as cloudbows and glories do not occur.

When the particle is large the quantity  $Q_s\Pi(g)$  can be divided into diffractive and nondiffractive components  $Q_s\Pi(g)=Q_s\Pi_s(g)+Q_d\Pi_d(g)$ . The scattering coefficient is  $Q_S=Q_d+Q_s$ , where  $Q_d$  is the part of  $Q_S$  associated with diffraction, and  $Q_d=1$  for an isolated particle. The diffractive phase function associated with  $Q_d$  can be approximated by the Allen function, equation (6.2). However, if the particle is not isolated the diffraction is changed both qualitatively and quantitatively. This will be discussed in Chapter 7.

The portion of the scattering not associated with diffraction is given by three quantities: the scattering efficiency  $Q_s$ , the scattering efficiency difference  $\Delta Q_s$ , and the particle phase function  $\Pi(g)$ . The scattering efficiency is given by

$$Q_{s} = S_{e} + (1 - S_{e}) \frac{1 - S_{i}}{1 - S_{i}\Theta}\Theta, \tag{6.47}$$

where the transmission function of the particle is

$$\Theta = \frac{r_i + \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}{1 + r_i \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)},\tag{6.48a}$$

$$r_i = \frac{1 - \sqrt{\alpha/(\alpha + s)}}{1 + \sqrt{\alpha/(\alpha + s)}},$$
(6.48b)

$$S_e = 0.0587 + 0.8543R(0) + 0.0870R(0)^2, (6.49a)$$

$$R(0) = \frac{(n_r - 1)^2 + n_i^2}{(n_r + 1)^2 + n_i^2},$$
 (6.49b)

and

$$S_i \simeq 1 - \frac{1}{n_r} [0.9413 - 0.8543R(0) - 0.0870R(0)^2].$$
 (6.50)

The scattering efficiency difference is given by

$$\Delta Q_s = S_e + (1 - S_e)(1 - S_i) \frac{\Psi}{1 - S_i \Psi}, \tag{6.51}$$

where

$$\Psi = \frac{r_i - \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}{1 - r_i \exp\left(-\sqrt{\alpha(\alpha+s)}\langle D\rangle\right)}.$$
 (6.52)

The particle phase function is described by the two-parameter double Henyey–Greenstein function

$$\Pi(g) = \Pi_{\text{HG2}}(g) = \frac{1+c}{2} \frac{1-b^2}{(1-2b\cos g + b^2)^{3/2}} + \frac{1-c}{2} \frac{1-b^2}{(1+2b\cos g + b^2)^{3/2}},$$
(6.53)

where

$$c = \frac{\Delta Q_s}{Q_s},\tag{6.54}$$

$$b = 0.15 + \frac{0.05}{(1 + \Delta Q_s/Q_s)^{4/3}}. (6.55)$$

The scattering efficiency and phase function of coated particles can be calculated using the formalism in section 6.5.8.

A useful approximation for the scattering efficiency, which may be used if the particle is not too absorbing and if the near-surface internal scattering density s is not too large, is

$$Q_s = \frac{1}{1+W} \simeq \frac{1}{1+\alpha D_e}.$$
 (6.56)

where  $D_e$  is a size of the order of twice the particle diameter.

## 6.6 Computer programs and databases

Useful computer programs are available at the following internet sites:

the Dauger program for calculating the diffraction pattern of an object of arbitrary cross-section: daugerresearch.com/fresnel/index.shtml;

the DDSCAT program for the DDA method: www.astro.princeton.edu/~draine/DDSCAT;

the Amsterdam program for the DDA method: www.science.uva.nl/reserch/scs/software/adda/index.html:

the Mishchenko *et al.* program for the T-matrix method: www.gis.nasa.gov/~ crimm.

A catalog of particle scattering measurements by the Amsterdam group (Munoz *et al.*, 2000) may be downloaded at www.laa.es/scattering/.