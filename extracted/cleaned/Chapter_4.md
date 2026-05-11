**4**

# Specular reflection

## 4.1 Introduction

In this chapter the specular or mirror-like reflection that occurs when a plane electromagnetic wave encounters a plane surface separating two regions with different refractive indices is discussed quantitatively, along with the accompanying transmission, or refraction, through the interface. Specular reflection is important to the topic of this book for several reasons. First, it is an important tool for investigating properties of materials in the laboratory. Second, it occurs in remote-sensing applications when light is reflected from smooth parts of a planetary surface, such as the ocean. Third, it is one of the mechanisms by which light is scattered from a particle whose size is large compared with the wavelength, so that an understanding of this phenomenon is necessary to an understanding of diffuse reflectance from planetary regoliths.

## 4.2 Boundary conditions in electromagnetic theory

Whenever a volume contains a boundary separating regions of differing electric or magnetic constants, the components of **D***e* and **B***m* perpendicular to the surface and the components of **E***e* and **H***m* tangential to the surface must be continuous across the boundary. If the fields constitute an electromagnetic wave propagating through the surface from one medium to another, the amplitudes of the fields are different within the two regions. Therefore, the continuity conditions cannot be satisfied unless there is another wave propagating backward from the surface into the first medium, in addition to the wave propagating forward from the surface into the second medium. That is, the boundary partly transmits and partly reflects the incident wave. These two additional waves may be thought of as arising because the incident wave induces charges and currents on the surface and in the interior that in turn generate new waves that are coherent with the original wave and travel in both directions away from the interface. The fractions of the energy reflected, transmitted, or refracted, can be found from solutions of the electromagnetic wave equation that satisfy these boundary conditions.

## 4.3 The Fresnel equations

### 4.3.1 Introduction

The equations describing the reflection and transmission of a wave by a plane boundary were first derived by A. J. Fresnel and are known as the Fresnel equations.

It was shown in Chapter 2 that at any point  $\mathbf{r}$  the fields of a plane electromagnetic wave traveling in a direction parallel to a unit propagation vector  $\mathbf{u}_p$  can be described by

$$\mathbf{E}_{e} = \mathbf{E}_{e0} \exp[2\pi i (n\mathbf{u}_{p} \cdot \mathbf{r}/\lambda - \nu \mathbf{t})]$$
 (4.1)

and

$$\mathbf{H}_{m} = \mathbf{H}_{m0} \exp[2\pi i (n\mathbf{u}_{p} \cdot \mathbf{r}/\lambda - \nu t)], \tag{4.2}$$

where  $\nu$  is the frequency,  $\lambda$  is the wavelength in free space, and n is the refractive index, which may be complex. From (2.62),  $\mathbf{E}_e$  and  $\mathbf{H}_m$  are related by

$$\mathbf{H}_m = n\mathbf{u}_p \times \mathbf{E}_e/\mu_m c_0 \text{ or } \mathbf{E}_e = -\mu_m c_0 \mathbf{u}_p \times \mathbf{H}_m/n, \tag{4.3}$$

where  $\mu_m$  is the permeability, and  $c_0 = \lambda v$  is the speed of light in vacuum. In the spirit of the preceding chapters, in which all propagation parameters were lumped together into a complex index of refraction, it will be assumed in the remainder of this chapter that  $\mu_m = \mu_{m0}$  everywhere and that the media on opposite sides of the boundary differ only in n.

The geometry and notation relevant to the processes of reflection and transmission are shown in Figure 4.1. The boundary separates a medium with refractive index  $n_1 = n_{1r} + in_{1i}$  from one with  $n_2 = n_{2r} + in_{2i}$ . A plane wave is incident on the surface from medium 1 into medium 2. The normal to the surface pointing into the first medium is parallel to the unit vector  $\mathbf{u}_n$ . The incident wave has electric field  $\mathbf{E}_e$  and magnetic intensity  $\mathbf{H}_m$  and propagates in a direction parallel to the unit vector  $\mathbf{u}_p$ , which makes an angle  $\vartheta$  with  $\mathbf{u}_n$ . Similar quantities with single primes denote the transmitted wave, and those with double primes the reflected wave.

Let n denote the refractive index of the second medium relative to the first,

$$n = n_2/n_1. (4.4)$$

If either or both  $n_1$  and  $n_2$  are complex, the relative refractive index is given by

$$n = n_r + n_i = \frac{n_{2r} + in_{2i}}{n_{1r} + n_{1i}} = \frac{n_{1r}n_{2r} + n_{1i}n_{2i} + i(n_{1r}n_{2i} - n_{2r}n_{1i})}{n_{1r}^2 + n_{1i}^2},$$

<!-- IMAGE: _page_2_Picture_2.jpeg -->

Figure 4.1 Geometry of specular reflection and transmission.

so that

$$n_r = (n_{1r}n_{2r} + n_{1i}n_{2i})/(n_{1r}^2 + n_{1i}^2), \tag{4.5}$$

$$n_i = (n_{1r}n_{2i} - n_{2r}n_{1i})/(n_{1r}^2 + n_{1i}^2).$$
(4.6)

The electric fields in the three waves are described by the following equations:

incident: 
$$\mathbf{E}_e = \mathbf{E}_{e0} \exp[2\pi i (n_1 \mathbf{u}_p \cdot \mathbf{r}/\lambda - \nu t)],$$
 (4.7)

refracted: 
$$\mathbf{E}'_{e} = \mathbf{E}'_{e0} \exp[2\pi i (n_{2}\mathbf{u}'_{p} \cdot \mathbf{r}/\lambda - \nu t)],$$
 (4.8)

reflected: 
$$\mathbf{E}_{e}^{"} = \mathbf{E}_{e0}^{"} \exp[2\pi i (n_1 \mathbf{u}^{"}_p \cdot \mathbf{r}/\lambda + \nu t)].$$
 (4.9)

The associated magnetic fields are given by (4.3). The coefficients  $E_{e0} = |\mathbf{E}_{e0}|$ ,  $E_{e0}' = |\mathbf{E}_{e0}'|$ , and  $E_{e0}'' = |\mathbf{E}_{e0}''|$  are the amplitudes of the waves, and the exponents are the phases.

### 4.3.2 Reflection and transmission at normal incidence

The case when the incident wave is traveling perpendicular to the boundary surface will be considered first as a prelude to the more complicated case of incidence from an arbitrary direction. In this case the reflected and refracted waves also travel perpendicularly to the surface, which means that all of the electric and magnetic fields

must be parallel to the surface. Then for all points on the surface,  $\mathbf{r}$  is perpendicular to the propagation vectors so that  $\mathbf{u}_p \cdot \mathbf{r} = \mathbf{u}'_p \cdot \mathbf{r} = \mathbf{u}''_p \cdot \mathbf{r} = 0$ .

The electric field  $\mathbf{E}_e$  of the incident wave induces electric dipoles on the surface. As shown in Figure 4.2 below, the fields generated by these dipoles are pointed in the opposite direction to  $\mathbf{E}_e$ . Thus, for continuity of the fields across the surface,

$$E_{e0} \exp(-2\pi i \nu t) - E_{e0}^{"} \exp(2\pi i \nu t) = E_{e0}^{'} \exp(-2\pi i \nu t).$$

This equation indicates that the electric field vectors increase, decrease, and reverse with period  $1/\nu$  with the relative phases given by the exponents. The fields are maximum and equal to their amplitudes at t=0 (and at integer multiples of  $1/\nu$ ) when the exponentials = 1. Hence, the relation between the amplitudes are given by

$$E_{e0} - E_{e0}^{"} = E_{e0}^{'}. (4.10)$$

Similarly, the continuity of  $\mathbf{H}_m$  requires

$$H_{m0} + H_{m0}^{"} = H_{m0}^{'},$$

or

$$n_1 E_{e0} / \mu_{m0} c_0 + n_1 E_{e0}'' / \mu_{m0} c_0 = n_2 E_{e0}' / \mu_{m0} c_0.$$
 (4.11)

Solving the simultaneous equations (4.10) and (4.11) gives

$$E'_{e0} = \frac{2}{n_2/n_1 + 1} E_{e0} = \frac{2}{n+1} E_{e0}$$
 (4.12)

and

$$E_{e0}^{"} = \frac{1 - n_2/n_1}{n_2/n_1 + 1} E_{e0} = \frac{n - 1}{n + 1} E_{e0}.$$
 (4.13)

Note that the electric vector of the reflected wave points oppositely to that of the incident wave, as shown in the figure. The sign reversal may also be thought of as the reflection causing a phase shift of 180°.

Figures 4.2a and 4.2b illustrate the case when the light is traveling from a medium with a lower refractive index to one of higher. Then the electric vector of the reflected field points oppositely to the incident and refracted vectors. For the opposite case where n < 1 the quantity (n-1)/(n+1) is negative, indicating that the reflected electric field vector is opposite to that shown in Figure 4.2. Thus the field points in the same direction as the other two vectors.

If the incident light is circularly polarized it induces a separation of positive and negative charges on the surface, and the direction of the line separating the charges rotates along with the incident field. Thus, if the incident light is right-handed the charge-separation vector rotates CW when seen looking into the same direction as the incident light is propagating, as shown in the top of Figure 4.3. This generates a reflected wave whose electric vector is rotating in the same direction. However,

<!-- IMAGE: _page_4_Figure_2.jpeg -->

Figure 4.2 (a) Schematic diagram of the charges and fields induced on the surface by the incident wave and the fields in the incident, transmitted, and reflected waves. (b) Reflected and transmitted sinusoidal waves.

when seen looking in the direction into which the reflected wave is propagating, as shown in the bottom of Figure 4.3, the electric vector appears to rotate CCW so that the reflected wave is left-handed. Thus, reflectance reverses the helicity of a circularly polarized wave. This is true regardless of whether *nr* is smaller or larger than 1.

It was shown in Chapter 2 (equation [2.94]) that the irradiance is proportional to the square of the absolute value of the electric field. Hence, the reflection coefficient,

<!-- IMAGE: _page_5_Picture_2.jpeg -->

Figure 4.3 Helicity reversal of a circularly polarized wave by reflection. The top figure shows a right-handed circularly polarized wave incident normally on a surface, as seen by an observer above the surface looking in the direction of propagation. The bottom figure shows the reflected wave as seen by an observer located just below the surface looking in the direction of propagation.

the ratio of reflected to incident intensity, is

$$R = \left| \frac{E_{e0}^{"}}{E_{e0}} \right|^2 = \left| -\frac{n-1}{n+1} \right|^2 = \frac{(n_r - 1)^2 + n_i^2}{(n_r + 1)^2 + n_i^2}.$$
 (4.14)

The transmission coefficient, the ratio of transmitted to incident light, is

$$T = \text{Re} \left[ n * \left| \frac{E_{e0}''}{E_{e0}} \right|^2 \right] = n_r \left| \frac{2}{n+1} \right|^2 = \frac{4n_r}{(n_r+1)^2 + n_i^2}.$$
 (4.15)

It may be readily verified that T = 1 - R, as it must, because the boundary does not absorb or create energy. If  $n_2 = n_1$  then R = 0 and T = 1; thus, if there is no change in refractive index, the boundary is invisible.

If the first medium is a vacuum, so that  $n_1 = 1 + i0$ ; then  $n_r = n_{2r}$  and  $n_i = n_{2i}$ . If  $n_{2i} = 0$ , then

$$R = \left(\frac{n_r - 1}{n_r + 1}\right)^2,\tag{4.16}$$

an equation familiar to all students in introductory mineralogy courses. However, if either medium has losses, then

$$R = \frac{(n_r - 1)^2 + n_i^2}{(n_r + 1)^2 + n_i^2}. (4.17)$$

This equation increases monotonically with  $n_i$  from a value of  $R = [(n_r - 1)/(n_r + 1)]^2$  at  $n_i = 0$  to  $R \to 1$  when  $n_i \gg 1$ . Thus, an imaginary component of the refractive index increases the reflectivity of the boundary. This is why metals appear bright when seen in reflected light.

At first sight it may appear contradictory that an imaginary component of the refractive index that is associated with absorption of radiation (as we saw in Chapter 2) also causes an increase in the reflected light. The incident fields may be thought of as inducing dipoles and currents at the surface and in the interior, and they generate radiation that propagates in both directions from the surface. The radiation traveling backward constitutes the reflected light; that traveling forward combines coherently with the incident fields and reduces the intensity of the transmitted light. If  $n_i = 0$ , the induced dipole moments are relatively small in most substances, so that the radiation generated by them is weak. Hence R is small and T is large. In order to affect the reflectance appreciably,  $n_i$  must be of the order of 1. However, an imaginary component this large implies a large conductivity (equation [2.79]), which means that the charges are highly mobile. The induced dipoles and the radiation they generate are strong, resulting in a high reflectivity. Most of the radiation is reflected, rather than being absorbed, as a consequence of the ability of the charges to rearrange themselves in such a manner as to inhibit the fields from entering the second medium.

### 4.3.3 Reflection and transmission at arbitrary angles

4.3.3.1 Snell's law

We now consider the more general case when  $\theta \neq 0$ . Let the point described by  $\mathbf{r}$  lie in the boundary surface. The tangential components of both  $\mathbf{E}_e$  and  $\mathbf{H}_m$  must be continuous across this surface. This can be true only if the spatial parts of the

phases are equal,

$$n_1 \mathbf{u}_p \cdot \mathbf{r}/\lambda = n_2 \mathbf{u}'_p \cdot \mathbf{r}/\lambda = n_1 \mathbf{u}''_p \cdot \mathbf{r}/\lambda. \tag{4.18}$$

This equation implies that  $\mathbf{u}_n$ ,  $\mathbf{u}_p$ ,  $\mathbf{u}_p'$ , and  $\mathbf{u}_p''$  are coplanar. To see this, suppose that  $\mathbf{r}$  is a vector in the surface and perpendicular to the plane containing both  $\mathbf{u}_p$  and  $\mathbf{u}_n$ , so that  $\mathbf{u}_p \cdot \mathbf{r} = 0 = \mathbf{u}_n \cdot \mathbf{r}$ . But the only nontrivial way that  $\mathbf{u}_p' \cdot \mathbf{r}$  and  $\mathbf{u}_p'' \cdot \mathbf{r}$  can also be zero is if all three propagation vectors and  $\mathbf{u}_n$  lie in the same plane.

By definition, for any vector  $\mathbf{r}$  in the surface,  $\mathbf{u}_n \cdot \mathbf{r} = 0$ . Thus, using vector identity (A.5),

$$\mathbf{u}_n \times (\mathbf{u}_n \times \mathbf{r}) = (\mathbf{u}_n \cdot \mathbf{r}) \, \mathbf{u}_n - (\mathbf{u}_n \cdot \mathbf{u}_n) \, r = -\mathbf{r},$$

so that, using vector identity (A.6),

$$\mathbf{u}_p \cdot \mathbf{r} = -\mathbf{u}_p \cdot [\mathbf{u}_n \times (\mathbf{u}_n \times \mathbf{r})] = -(\mathbf{u}_p \times \mathbf{u}_n) \cdot (\mathbf{u}_n \times \mathbf{r}).$$

Similar expressions hold for  $\mathbf{u}'_p$  and  $\mathbf{u}''_p$ . Hence, equation (4.9) can be put in the forms

$$(n_1/\lambda)\left(\mathbf{u}_p \times \mathbf{u}_n\right) \cdot (\mathbf{u}_n \times \mathbf{r}) = (n_1/\lambda)\left(\mathbf{u}_p'' \times \mathbf{u}_n\right) \cdot (\mathbf{u}_n \times \mathbf{r}) \tag{4.19}$$

and

$$(n_1/\lambda) \left( \mathbf{u}_p \times \mathbf{u}_n \right) \cdot \left( \mathbf{u}_n \times \mathbf{r} \right) = (n_2/\lambda) \left( \mathbf{u}_p' \times \mathbf{u}_n \right) \cdot \left( \mathbf{u}_n \times \mathbf{r} \right). \tag{4.20}$$

Equation (4.19) shows that  $\theta'' = \theta$ . This is most easily seen by supposing that  $\mathbf{r}$  is a vector in the surface and also in the common plane of the propagation vectors. Then  $\mathbf{u}_n \times \mathbf{r}$  is perpendicular to the propagation plane and parallel to  $\mathbf{u}_p \times \mathbf{u}_n$  and  $\mathbf{u}_p'' \times \mathbf{u}_n$ . In this case, (4.19) becomes  $(n_1 r/\lambda) \sin \theta = (n_1 r/\lambda) \sin \theta''$ , from which it follows that  $\theta'' = \theta$ .

Similarly, equation (4.20) shows that  $\theta$  and  $\theta'$  are related by  $n_1 \sin \theta = n_2 \sin \theta'$ , or

$$\sin \theta = n \sin \theta',\tag{4.21}$$

which is Snell's law.

To proceed further, it is convenient to resolve the field vectors into two components parallel and perpendicular to the plane of propagation and consider them separately. Let subscript " $\bot$ " denote the component with  $\mathbf{E}$  perpendicular to the plane containing the propagation vectors, in which case  $\mathbf{H}$  is in that plane; let subscript " $\|$ " denote the component with  $\mathbf{E}$  in the same plane as the propagation vectors, in which case  $\mathbf{H}$  is perpendicular to that plane. The first case is called the *transverse electric* case and the second the *transverse magnetic* case.

### 4.3.3.2 Ee perpendicular to the plane of propagation

In the transverse electric case the electric vectors are all perpendicular to  $\mathbf{u}_n$  and parallel to the boundary surface. The conditions that the tangential components of  $\mathbf{E}_e$  and  $\mathbf{H}_m$  be continuous across the boundary can be written, respectively,

$$\mathbf{u}_n \times (\mathbf{E}_e + \mathbf{E}_e'') = \mathbf{u}_n \times \mathbf{E}_e' \tag{4.22}$$

and, from (4.2),

$$n_1 \mathbf{u}_n \times \left( \mathbf{u}_p \times \mathbf{E}_e / \mu_{m0} c_0 + n_1 \mathbf{u}_p'' \times \mathbf{E}_e'' / \mu_{m0} c_0 \right) = n_2 \mathbf{u}_n \times (\mathbf{u}_p' \times \mathbf{E}_e' / \mu_{m0} c_0),$$

$$(4.23)$$

where the fields are given by (4.4), and  $\mathbf{r}$  lies in the surface. Because spatial parts of the phases must all be equal on the surface, (4.22) becomes

$$E_{e0} + E_{e0}^{"} = E_{e0}^{'}. (4.24)$$

Using vector relation (A.5) gives

$$\mathbf{u}_n \times (\mathbf{u}_p \times \mathbf{E}_e) = (\mathbf{u}_n \cdot \mathbf{E}_e) \mathbf{u}_p - (\mathbf{u}_n \cdot \mathbf{u}_p) \mathbf{E}_e = -(\mathbf{u}_n \cdot \mathbf{u}_p) \mathbf{E}_e,$$

since  $\mathbf{u}_n \cdot \mathbf{E}_e = 0$ . Similar expressions hold for  $\mathbf{E}'_e$  and  $\mathbf{E}''_e$ . Hence, (4.23) is

$$n_1 \left( \mathbf{u}_n \cdot \mathbf{u}_p \right) \mathbf{E}_e + n_1 \left( \mathbf{u}_n \cdot \mathbf{u}_p'' \right) \mathbf{E}_e'' = n_2 \left( \mathbf{u}_n \cdot \mathbf{u}_p' \right) \mathbf{E}_e',$$

or

$$-n_1 E_{e0} \cos \theta + n_1 E_{e0}'' \cos \theta'' = -n_2 E_{e0}' \cos \theta'.$$

Because  $\theta'' = \theta$ , and  $n = n_2/n_1$ , this becomes

$$E_{e0}\cos\theta - E_{e0}''\cos\theta = nE_{e0}'\cos\theta'. \tag{4.25}$$

Solving the simultaneous equations (4.24) and (4.25) gives

$$\frac{E'_{e0}}{E_{e0}} = \frac{2\cos\theta}{\cos\theta + n\cos\theta'} \tag{4.26}$$

and

$$\frac{E_{e0}^{"}}{E_{e0}} = \frac{\cos\theta - n\cos\theta'}{\cos\theta + n\cos\theta'}.$$
 (4.27)

### 4.3.3.3 Ee parallel to the plane of propagation

In the transverse magnetic case the magnetic vectors are perpendicular to  $\mathbf{u}_n$  and parallel to the surface. Hence, the boundary condition that the magnetic intensity be continuous across the surface is

$$\mathbf{u}_n \times (\mathbf{H}_m + \mathbf{H}_m'') = \mathbf{u}_n \times \mathbf{H}_m',$$

so that

$$H_{m0} + H_{m0}^{"} = H_{m0}^{'}. (4.28)$$

The condition that the tangential component of the electric field be continuous is, from (4.2),

$$\mathbf{u}_n \times \left(\mu_{m0}c_0\mathbf{u}_p \times \mathbf{H}_m/n_1\right) + \mathbf{u}_n \times \left(\mu_{m0}c_0\mathbf{u}_p'' \times \mathbf{H}_m''/n_1\right) = \mathbf{u}_n \times \left(\mu_{m0}c_0\mathbf{u}_p' \times \mathbf{H}_m'/n_2\right).$$

Because  $\mathbf{u}_n \cdot \mathbf{H}_m = 0$ ,

$$\mathbf{u}_{n} \times (\mathbf{u}_{n} \times \mathbf{H}_{m}) = (\mathbf{u}_{n} \cdot \mathbf{H}_{m}) \mathbf{u}_{p} - (\mathbf{u}_{n} \cdot \mathbf{u}_{p}) \mathbf{H}_{m} = -(\mathbf{u}_{n} \cdot \mathbf{u}_{p}) \mathbf{H}_{m};$$

thus.

$$\mu_{m0}c_0\left(\mathbf{u}_n\cdot\mathbf{u}_p\right)\mathbf{H}_m/n_1+\mu_{m0}c_0\left(\mathbf{u}_n\cdot\mathbf{u}_p''\right)\mathbf{H}_m''/n_1=\mu_{m0}c_0\left(\mathbf{u}_n\cdot\mathbf{u}_p'\right)\mathbf{H}_m'/n_2,$$

or

$$mH_{m0}\cos\theta - mH_{m0}^{"}\cos\theta = H_{m0}^{'}\cos\theta'. \tag{4.29}$$

Combining (4.28) and (4.29) gives

$$\frac{H'_{m0}}{H_{m0}} = \frac{2n\cos\theta}{n\cos\theta + \cos\theta'}$$

and

$$\frac{H_{m0}^{"}}{H_{m0}} = \frac{n\cos\theta - \cos\theta'}{n\cos\theta + \cos\theta'},$$

or, using (2.63),

$$\frac{E'_{e0}}{E_{e0}} = \frac{2\cos\theta}{n\cos\theta + \cos\theta'},\tag{4.30}$$

$$\frac{E_{e0}^{"}}{E_{e0}} = \frac{n\cos\theta - \cos\theta'}{n\cos\theta + \cos\theta'}.$$
 (4.31)

These results have been obtained using only the tangential components of  $\mathbf{E}_e$  or  $\mathbf{H}_m$ , as appropriate. Using a similar procedure, it can be shown that the continuity conditions on the normal components of  $\mathbf{D}_e$  and  $\mathbf{B}_m$  have also been satisfied.

### 4.3.4 Reflection and transmission when n is real

The reflection and transmission coefficients and their properties when  $n_1$  and  $n_2$  are real will be discussed first. According to (2.94) the irradiance is proportional to Re $(n|E_e|^2)$ . Hence, the reflectivities  $R_{\perp}$  and  $R_{\parallel}$  when  $E_e$  is perpendicular and

parallel, respectively, to the plane of propagation are given by

$$R_{\perp} = \left[\frac{\cos\theta - n\cos\theta'}{\cos\theta + n\cos\theta'}\right]^2,\tag{4.32}$$

$$R_{\rm p} = \left[ \frac{n \cos \theta - \cos \theta'}{n \cos \theta + \cos \theta'} \right]^2, \tag{4.33}$$

where Ψ# is given by Snell's law

$$\sin \theta = n \sin \theta'. \tag{4.34}$$

The corresponding transmission coefficients are given by

$$T_{\perp} = \frac{4n\cos^2\theta}{(\cos\theta + n\cos\theta')^2} = (1 - R_{\perp})\frac{\cos\theta}{\cos\theta'},\tag{4.35}$$

$$T_{\parallel} = \frac{4n\cos^2\theta}{(n\cos\theta + \cos\theta')^2} = \left(1 - R_{\parallel}\right) \frac{\cos\theta}{\cos\theta'} \tag{4.36}$$

Expressions (4.32)–(4.36) are the Fresnel equations for *n* real. The factor cos Ψ*/*cos Ψ # in the transmission coefficients arises because the flux of energy crossing an area *A* perpendicular to **u***p* in the incident wave illuminates an area *A*secΨ on the surface; the light transmitted through this area is contained in area *A*secΨ cos Ψ # in the second medium (Figure 4.4).

It is left as an exercise for the reader to show that (4.32) and (4.33) can be put in the following equivalent forms:

$$R_{\perp} = \left[ \frac{\cos \theta - \sqrt{n^2 - \sin^2 \theta}}{\cos \theta + \sqrt{n^2 - \sin^2 \theta}} \right]^2 = \left[ \frac{\sin (\theta - \theta')}{\sin (\theta + \theta')} \right]^2, \tag{4.37}$$

<!-- IMAGE: _page_10_Picture_13.jpeg -->

Figure 4.4 Continuity of the flux through the surface.

<!-- IMAGE: _page_11_Figure_2.jpeg -->

Figure 4.5 Fresnel reflection coefficients for n = 1.50 + i0 versus the angle of incidence.

and

$$R_{\parallel} = \left[ \frac{n^2 \cos \theta - \sqrt{n^2 - \sin^2 \theta}}{n^2 \cos \theta + \sqrt{n^2 - \sin^2 \theta}} \right]^2 = \left[ \frac{\tan \left( \theta - \theta' \right)}{\tan \left( \theta + \theta' \right)} \right]^2. \tag{4.38}$$

The reflectivities  $R_{\perp}$  and  $R_{\parallel}$  versus  $\theta$  are plotted in Figure 4.5 for a case where n>1. Equation (4.21) shows that in this case  $\theta>\theta'$ . When  $\theta=0$ ,  $R_{\perp}(0)=R_{\parallel}(0)=[(n-1)/(n+1)]^2$ , which is identical with (4.16). When  $\theta=\pi/2$ ,  $R_{\perp}(\pi/2)=R_{\parallel}(\pi/2)=1$ . As  $\theta$  increases from zero,  $R_{\perp}$  increases monotonically. However,  $R_{\parallel}$  first decreases and becomes zero at the angle  $\theta=\theta_B$  where  $\theta_B+\theta'=\pi/2$  so that  $\tan(\theta_B+\theta')\to\infty$  in (4.38), following which  $R_{\parallel}$  increases to unity at  $\theta=\pi/2$ .

At the angle  $\theta_B$ , known as *Brewster's angle*,  $\sin \theta_B = n \sin(\pi/2 - \theta_B) = n \cos \theta_B$ , so that

$$an \theta_B = n \tag{4.39}$$

Equation (4.39) provides a method of measuring n by determining the angle at which  $R_p$  vanishes. Other techniques for measuring n include the Becke-line method (e.g., Bloss, 1961), in which small grains of the sample are immersed in oils of different refractive indices until a match is found, indicated by the disappearance of the edge of the grain.

The case where n < 1 is illustrated in Figure 4.6. This situation occurs when  $n_1 > n_2$ . For example, the interface may be between two materials of different

<!-- IMAGE: _page_12_Figure_2.jpeg -->

Figure 4.6 Fresnel reflection coefficients for n = 1/1.50 + i0 versus the angle of incidence.

refractive index, or between water and air, or between air and a medium with  $n_r < 1$  in the anomalous dispersion region of a strong absorption band. When  $\theta = 0$ ,

$$\frac{E'_{e0}}{E_{e0}} = \frac{1 - 1/n}{1 + 1/n} = \frac{n - 1}{n + 1}.$$

Thus, at small angles the reflectivities are equal to the case where  $n_r > 1$ ; that is, they have the value  $R_{\perp}(0) = R_{\parallel}(0) = |(n-1)/(n+1)|^2$ , and  $R_{\perp}$  increases monotonically, while  $R_{\parallel}$  first decreases to zero at the Brewster angle, given by (4.39), and then increases. However,  $\theta'$  increases more rapidly than  $\theta$ . When  $\theta' = \pi/2$ ,  $\theta$  is equal to the *critical angle*  $\theta_c$ . At the critical angle Snell's law is

$$\sin \theta_c = n,\tag{4.40}$$

and  $R_{\perp}(\theta_c) = R_{\parallel}(\theta_c) = 1$ . Because  $\theta'$  cannot exceed  $\pi/2$ , the reflectivities are unity for all  $\theta$  between  $\theta_c$  and  $\pi/2$ .

When  $\theta > \theta_c$ ,  $R_{\perp} = R_p = 1$  and  $T_{\perp} = T_{\parallel} = 0$ . For these angles the boundary completely reflects all incident radiation, and the system is said to exhibit *total internal reflection*. A detailed analysis shows that the fields actually penetrate a short distance into the medium of lower refractive index, but that waves propagating away from the surface do not exist. Instead a system of moving fields, called an *evanescent wave*, is generated that propagates along the surface, and whose amplitude is appreciable in the lower refractive index medium only within about

a wavelength from the interface. If another medium with a higher refractive index is brought close to the first interface the oscillating fields in the evanescent wave will cause the motion of charges along the second interface and generate a wave propagating away from the surface. The incident wave is no longer totally reflected and has partially "tunneled through" the gap separating the two media.

### 4.3.5 Polarization

The reflection and transmission coefficients are different for the two directions of the electric vector. Thus, if the incident light is unpolarized, the reflected and transmitted light will both be partially polarized. For the reflected light the reflected power is always greater when the electric vector is perpendicular to the plane of propagation, and for the transmitted light, when parallel to this plane.

Choosing a coordinate system in which the x-axis is perpendicular and the y-axis is parallel to the plane of propagation, the *linear polarization ratio* or *polarization* (Section 2.6) of the irradiance is

$$P = (J_{\perp} - J_{\parallel})/(J_{\perp} + J_{\parallel}), \tag{4.41}$$

where, as usual, the subscript " $\perp$ " denotes the electric vector perpendicular to the plane of propagation, and the subscript " $\parallel$ " denotes the electric vector parallel to this plane; P is a scalar. If the incident radiation J is unpolarized, then  $J_{\perp} = J_{\parallel} = J/2$ . Hence the polarization of the reflected light is

$$P = (R_{\perp} - R_{\parallel})/(R_{\perp} + R_{\parallel}),$$

and that of the transmitted light is

$$P = (T_{\perp} - T_{\parallel})/(T_{\perp} + T_{\parallel}) = -(R_{\perp} - R_{\parallel})/(2 - R_{\perp} - R_{\parallel}).$$

The polarization is shown in Figure 4.7. Note that it is always positive for reflected light and becomes +100% at the Brewster angle. The polarization is always negative for transmitted light but nowhere reaches -100%.

If the incident light is linearly polarized in an arbitrary direction it can be resolved into transverse electric and transverse magnetic components vibrating in phase with each other. As the angle of incidence increases from zero the unequal reflection coefficients of the two components cause the plane of polarization to rotate until at the Brewster angle the plane of polarization of the reflected light is entirely perpendicular to the scattering plane.

If the incident light is circularly polarized the two components are 90° out of phase. As the angle of incidence increases the unequal reflection coefficients cause the light to become elliptically polarized. At the Brewster angle the ellipse is perfectly flat and the reflected light is linearly polarized.

<!-- IMAGE: _page_14_Figure_2.jpeg -->

Figure 4.7 Polarization of the reflected and transmitted light for n = 1.5 + i0 versus the angle of incidence.

### 4.3.6 Reflection and refraction when n is complex

When  $n_1$  or  $n_2$  is complex, the amplitude ratios  $E''_{e0}/E_{e0}$ , given by (4.27) and (4.31) for the directions of **E**, are complex also. Denote the amplitude reflection coefficients, that is, the ratio of the amplitudes of the fields, by

$$r_{\perp} = \frac{\cos \theta - n \cos \theta'}{\cos \theta + n \cos \theta'} = \eta_{\perp} e^{i\phi_{\perp}}, \tag{4.42a}$$

$$r_{\parallel} = \frac{n\cos\theta - \cos\theta'}{n\cos\theta + \cos\theta'} = \eta_{\parallel}e^{i\phi_{\rm p}}.$$
 (4.42b)

where the  $\eta s$  are the amplitudes and the  $\phi s$  are the phases of the reflection coefficients. The physical meaning of  $\phi_{\perp}$  and  $\phi_{\parallel}$  is that shifts of this amount in the phase of the wave occur upon reflection. Transmission is similarly accompanied by phase shifts.

The bending of a ray of light upon refraction is caused by the change in the velocity of propagation,  $c_0/n_r$  (equation [2.88]). Hence, in media with complex refractive indices Snell's law is

$$n_{1r}\sin\theta = n_{2r}\sin\theta'. \tag{4.43}$$

Straightforward, but tedious, algebra gives the following equations:

$$R_{\perp} = |r_{\perp}|^2 = \eta_1^2 = \frac{[\cos \theta - G_1]^2 + G_2^2}{[\cos \theta + G_1]^2 + G_2^2},\tag{4.44}$$

$$\tan \phi_{\perp} = \frac{2G_2 \cos \theta}{G_1^2 + G_2^2 - \cos^2 \theta},\tag{4.45}$$

$$R_{\parallel} = |r_{\parallel}|^2 = \eta_2^2 = \frac{[(n_r^2 - n_i^2)\cos\theta - G_1]^2 + [2n_r n_i \cos\theta - G_2]^2}{[(n_r^2 - n_i^2)\cos\theta + G_1]^2 + [2n_r n_i \cos\theta + G^2]^2}, \quad (4.46)$$

$$\tan \phi_{\parallel} = 2\cos\theta \frac{2n_r n_i G_1 - (n_r^2 - n_i^2) G_2}{(n_r^2 + n_i^2)^2 \cos^2\theta - (G_1^2 + G_2^2)},$$
(4.47)

where

$$G_1^2 = \frac{1}{2} \left\{ \left[ n_r^2 - n_i^2 - \sin^2 \theta \right] + \left[ (n_r^2 - n_i^2 - \sin^2 \theta)^2 + 4n_r^2 n_i^2 \right]^{1/2} \right\}, \quad (4.48)$$

$$G_2^2 = \frac{1}{2} \left\{ -\left[ n_r^2 - n_i^2 - \sin^2 \theta \right] + \left[ (n_r^2 - n_i^2 - \sin^2 \theta)^2 + 4n_r^2 n_i^2 \right]^{1/2} \right\}. (4.49)$$

At  $\theta = 0$  the reflectivities are  $R_{\perp}(0) = R_{\parallel}(0) = [(n_r - 1)^2 + n_i^2]/[(n_r + 1)^2 + n_i^2]$ , which is the same as (4.17). As  $\theta$  increases, the component of the reflectivity perpendicular to the plane of propagation increases monotonically to 1 at  $\theta = \pi/2$ . The parallel component first decreases to a minimum and then increases to 1 at  $\theta = \pi/2$ ; however, the minimum never becomes zero, as it does at the Brewster angle when  $n_i = 0$ . The reflectivities are plotted versus  $\theta$  in Figure 4.8 for a medium with a complex refractive index.

In two special cases equations (4.46) - (4.49) can be simplified somewhat. When  $n_i \ll 1$ ,

$$n_r^2 - n_i^2 \simeq n_r^2$$
,  $G_1 \simeq \left(n_r^2 - \sin^2\theta\right)^{1/2}$ ,  $G_2 \simeq n_r n_i / (n_r^2 - \sin^2\theta)^{1/2}$ . (4.50)

At the opposite extreme, when  $|n_r^2 - n_i^2| \gg 1$ ,

$$G_1 \simeq n_r$$
,  $G_2 \simeq n_i$ , (4.51)

and, after a little algebra, the reflectivities become

$$R_{\perp} = \frac{(n_r - \cos\theta)^2 + n_i^2}{(n_r + \cos\theta)^2 + n_i^2},\tag{4.52}$$

$$R_{\parallel} = \frac{(n_r - 1/\cos\theta)^2 + n_i^2}{(n_r + 1/\cos\theta)^2 + n_i^2}.$$
 (4.53)

When  $n_i \neq 0$  and the incident light is unpolarized, the different phase shifts for the two reflection coefficients cause the reflected light to be partially circularly polarized.

<!-- IMAGE: _page_16_Figure_2.jpeg -->

Figure 4.8 Fresnel reflection coefficients for  $n = 1.50 + i \cdot 1.0$  versus the angle of incidence.

## 4.4 The Kramers–Kronig reflectivity relations

At  $\theta = 0$  the complex amplitude reflection coefficient for the two directions of polarization ([4.42a] and [4.42b]) are equal and can be written

$$r(0) = r_{\perp}(0) = r_{\parallel}(0) = (n_r - 1 + in_i)/(n_r + 1 + in_i) = \eta e^{i\phi}, \tag{4.54}$$

where  $\eta$  is the amplitude of the reflection coefficient and  $\phi$  is its phase.

Because  $n_r$  and  $n_i$  are both functions of frequency  $\nu$ ,  $\eta$  and  $\phi$  are also functions of  $\nu$ . Taking the logarithm of (4.54) gives

$$\ln[\mathbf{r}(0,\nu)] = \ln[\eta(\nu)] + i\phi(\nu). \tag{4.55}$$

The reflectivity must obey causality. Thus, as discussed in Chapter 3, the expression for the amplitude reflectivity possesses crossing symmetry; that is,  $r(0, -\nu) = r^*(0, \nu)$ . Hence, according to the discussion in AppendixB,  $\eta(\nu)$  and  $\phi(\nu)$  must obey relations of the form of (B.14) and (B.15):

$$\ln[\eta(\nu)] = \frac{2}{\pi} \int_0^\infty \frac{v'\phi(\nu')}{\nu'^2 - \nu^2} d\nu', \tag{4.56}$$

$$\phi(\nu) = -\frac{2\nu}{\pi} \int_0^\infty \frac{\ln[\eta(\nu')]}{\nu'^2 - \nu^2} d\nu'. \tag{4.57}$$

Equations (4.56) and (4.57) are the Kramers–Kronig reflectivity relations. They can be used to calculate the complex dielectric constant from measurements of the normal reflectivity as a function of frequency,  $\eta(\nu) = \sqrt{R(0,\nu)}$ . The normal reflectivity is measured over as wide a range of frequencies as practical. A suitable theory, such as the Drude or Lorentz model (Chapter 3), is then used to extrapolate the measurements to  $\nu = 0$  and  $\nu = \infty$ , and these values are inserted into (4.57) to calculate  $\phi(\nu)$ . From  $\eta(\nu)$  and  $\phi(\nu)$  the components of the refractive index can be found by solving (4.54):

$$n_r = (1 - \eta^2)/(1 - 2\eta\cos\phi + \eta^2). \tag{4.58}$$

and

$$n_i = 2\eta \sin \phi / (1 - 2\eta \cos \phi + \eta^2).$$
 (4.59)

A more detailed discussion of this technique has been provided by Wooten (1972). One limitation of this method of measuring  $n_i$  is that it can be used only for materials that are highly absorbing. For reasonable measurement errors,  $n_i$  should be large enough to make a difference of at least 10% in R(0), which for  $n_r = 1.5$  means  $n_i \ge 0.15$ . From (2.95) it may be seen that this requires that the absorption coefficient be so large that the irradiance propagating through the medium is reduced by a factor of e over a distance of less than half a wavelength.

## 4.5 Absorption bands in reflectivity

The spectral reflectivity at normal incidence of a material having an absorption band given by a classical Lorentz oscillator with the same parameters as in Figures 3.1 and 3.2 is shown in Figure 4.9. The material is assumed to be in air, so that  $n = n_2 = n_r + in_i$ . Note that the peak of the reflectivity occurs at a higher frequency than the band center  $\nu_0$  and that the band is broadened. The reason the frequency of the band center shifts is the anomalous dispersion of the real part of the refractive index, which, as can be seen in Figure 3.2, decreases with frequency throughout the main region of the absorption band.

If the material has only one absorption band, and is in vacuum, then Figure 3.2 shows that  $n_r = 1$  only at  $\nu_0$ , the band center. However, if the continuum refractive index  $n_c$  is > 1,  $n_r$  will also = 1 at a second frequency on the high-frequency side of  $\nu_0$ . This second frequency at which  $n_r = 1$  is known as the *Christiansen frequency*, denoted by  $\nu_C$ , and the corresponding wavelength is the Christiansen wavelength  $\lambda_C$ .

The Christiansen wavelength provides a method for making a narrow-bandwidth transmission filter. Small crystals of suitable material are embedded in a second medium whose refractive index is chosen to make  $n_r = 1$  at the desired frequency, which also must be away from the center of any strong absorption bands in either

<!-- IMAGE: _page_18_Figure_2.jpeg -->

Figure 4.9 Spectrum of the Fresnel reflection coefficient at normal incidence for a material having the Lorentz dielectric constant and refractive index shown in Figures 3.1 and 3.2. Note that the reflectivity peak is much broader than, and is displaced to the high-frequency side of the dielectric-constant peak.

<!-- IMAGE: _page_18_Picture_4.jpeg -->

Figure 4.10 Isolating the frequencies in a restrahlen band by multiple reflections.

material. Rays of light whose frequencies are close to the Christiansen frequency will pass undeviated through the surfaces between the two materials, but rays of other frequencies will be bent out of the beam by refraction.

The peak in reflectivity near the center of a strong absorption band provides another method of obtaining a nearly monochromatic beam of radiation without using a prism or diffraction grating. Light from a source giving off a broad range of wavelengths is arranged to be reflected many times from the polished surfaces of an appropriate material, as shown in Figure 4.10. After several reflections the beam consists almost entirely of light of a narrow range of wavelengths around the reflectivity maximum. Before long-wavelength diffraction gratings were widely available, this technique was commonly used to isolate wavelengths in the infrared. The narrow bands of wavelengths produced in this manner are known as *Reststrahlen*, a German word literally translated as "residual rays." For this reason the strong vibrational bands of solids in the infrared are often called *Reststrahlen bands*.

## 4.6 Criterion for optical flatness

Even highly polished surfaces have myriads of small scratches and other imperfections, and all surfaces are rough on the scale of the size of atoms, a few angstroms. Thus, an important question arises: under what circumstances are the equations of this chapter valid? That is, when may a surface be considered smooth?

This question may be answered with the aid of Figure 4.11, which shows schematically a wave incident at angle  $\theta$  on a surface whose vertical deviations from a perfect plane are characterized by a height h. The portions of the wave front indicated by the two rays have been reflected from parts of the surface differing in elevation by h. As indicated in the figure, the path difference over which the two rays have traveled is  $\Delta L = 2h\cos\theta$ , so that the portions of the wave front they represent differ in phase by  $\Delta \phi = 2\pi \Delta L/\lambda = 4\pi h\cos\theta/\lambda$ .

If  $\Delta \phi \ll 2\pi$ , say  $\Delta \phi < 2\pi/10$ , then the roughness will have negligible effect on the reflected wave. Thus, one criterion for the surface to be considered smooth would be  $h < \lambda \sec \theta/20$ . The so-called *Rayleigh criterion* is somewhat less stringent than this and assumes that the effect of roughness will be negligible if  $\Delta \phi < \pi/2$ ,

<!-- IMAGE: _page_19_Figure_7.jpeg -->

Figure 4.11 Schematic diagram of two parts of a wave reflected from a rough surface.

leading to

$$h < \lambda \sec \theta / 8 \tag{4.60}$$

as the criterion for a surface to be considered smooth.

On the other hand, if the two portions of the wave front differ in phase by π or more, then they will certainly interfere with each other, either constructively or destructively, so that the surface will act as a rough scatterer if

$$h > \lambda \sec \theta / 4. \tag{4.61}$$

Note that the roughness criteria depend on Ψ. A surface may be rough for normal incidence but smooth for glancing incidence.

The transition between rough- and smooth-surface scattering has been studied experimentally by Schaber, Berlin, and Brown (1976) as a method for measuring the surface relief of a terrain using radar.