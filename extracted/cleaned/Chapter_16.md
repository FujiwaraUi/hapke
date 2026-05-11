# Simultaneous transport of energy by radiation and thermal conduction

## 16.1 Introduction

The temperature distribution in the regolith of a body of the solar system is important for several reasons. First, the mean temperature is one of the fundamental properties of an object; second, the regolith is the part of the planet studied by remote-sensing methods; and third, the temperature distribution in the upper layers constitutes the boundary condition for thermal models of the deeper interior. The temperatures in the regolith are governed by three energy-transport processes that interact within the medium: visible and near-IR solar radiation, thermal radiation, and heat conduction. However, most models treat the energy as being carried entirely by thermal conduction inside the medium, the interaction with radiation being treated only as a boundary condition. In this chapter all three processes occurring in the medium are treated simultaneously. In doing so it will be seen that radiative conductivity of heat and the solid-state greenhouse effect appear intrinsically without any ad hoc assumptions.

In Section 16.2 the time-dependent, one-dimensional radiative and heat conduction equations are introduced. The time-independent equations are solved analytically for two important cases: a layer of isotropically scattering particles heated from below and radiating into a vacuum, simulating conditions often used in laboratory IR and thermal measurements, and a semi-infinite medium of isotropic scatterers heated by incident visible light and radiating into a vacuum, simulating a planetary regolith in equilibrium with sunlight. In the final section some time-dependent problems are discussed briefly.

## 16.2 Equations 16.2.1 Basic equations

The system that will be considered in this chapter is a semi-infinite, horizontally stratified, particulate medium in a vacuum. As in the rest of this book, it is assumed that the radiance can be adequately described by the equation of radiative transfer. Let a subscript  $\lambda$  on a quantity explicitly denote that the quantity is dependent on wavelength. Then the radiative transfer equation for radiance  $I_{\lambda}(z, \Omega, t)$  of wavelength  $\lambda$  at time t and depth z below the surface, traveling in direction  $\Omega$  making an angle  $\vartheta$  with the normal to the surface is

$$\cos\vartheta \frac{\partial I_{\lambda}(z,\Omega,t)}{\partial z} = -E_{\lambda}(z)I_{\lambda}(z,\Omega,t) + \frac{1}{4\pi} \int_{4\pi} I_{\lambda}(z,\Omega',t)G_{\lambda}(z,\Omega',\Omega)d\Omega' + \frac{J_{\lambda}F(t)}{4\pi}G_{\lambda}(z,\Omega_{i},\Omega)\exp\left[-\frac{1}{\mu_{0}(t)}\int_{z}^{\infty} E_{\lambda}(z')dz'\right] + \frac{A_{\lambda}}{\pi}U_{\lambda}(T), \quad (16.1)$$

where  $E_{\lambda}$  is the extinction coefficient,  $G(z, \Omega, \Omega)$  is the volume angular scattering coefficient,  $J_{\lambda}$  is the incident irradiance, F(t) describes the time-variation of the irradiance,  $\mu_0 = \cos i$ ,  $A_{\lambda}$  is the volume-average absorption coefficient, and  $U_{\lambda}(T)$  is the Planck function, which radiates isotropically.

The temperature T is governed by the heat equation,

$$\rho C \frac{\partial T(z,t)}{\partial t} = \frac{\partial}{\partial z} \left[ k \frac{\partial T(z,t)}{\partial z} \right] + \int_{\lambda} A_{\lambda}(z) J_{\lambda} F(t) \exp \left[ -\frac{1}{\mu_{0}(t)} \int_{z}^{\infty} E_{\lambda}(z') dz' \right] d\lambda$$

$$+ \int_{\lambda} A_{\lambda}(z) \left[ \int_{4\pi} I_{\lambda}(z,\Omega,t) d\Omega \right] d\lambda$$

$$- \int_{\lambda} A_{\lambda}(z) \left[ \int_{4\pi} \frac{1}{\pi} U_{\lambda}(z,t) d\Omega \right] d\lambda,$$
(16.2)

where  $\rho$  is the bulk density, C is the specific heat per unit mass, and k is the solidstate thermal conductivity. The left-hand side of equation (16.2) describes the rate of change of heat content per unit volume in a layer of thickness dz at depth z. The first term on the right-hand side is the difference between the heat conducted into the layer and the heat conducted out. The second term on the right describes the absorption of the incident collimated irradiance that has penetrated to depth zand been absorbed in the layer. The third term is the diffuse radiance absorbed by the layer. The fourth term describes the loss of heat by thermal radiation from the particles in the layer at a temperature T(z,t).

Note that the heat equation is coupled to the radiative-transfer equation only through integrals of the radiance over wavelength, not the spectral radiance. Therefore, solving this equation requires the calculation of the wavelength-integrated radiance. In some situations the only radiation is in the thermal IR region and the wavelength distribution approximates a Planck function. However, in a medium illuminated by a source of visible light, such as the Sun or an incandescent lamp, the radiance is appreciable in two spectral regions, the visual, including the near-UV/visible/near-IR, and the thermal IR. Then the spectrum of the radiance is

bimodal, consisting of two separate wavelength regions: one with a spectrum similar to that of the incident irradiance *J*λ and one with a spectrum similar to *U (TC)* where *U (TC)*is the Planck function of a black body at a temperature *TC* that characterizes the medium. If the two spectra overlap they can still be separated by suitable extrapolation from the nonoverlapping regions. Then the radiative transfer equation can be separated into two discrete equations by integration and/or averaging over these spectral regions.

Let the subscript *V* denote integration or averaging over wavelength over the visual portion of the spectrum and *T* over the thermal IR. Define the following quantities,

$$J(t) = \int_{visual \,\lambda} J_{\lambda}(t) d\lambda,$$

$$I_{V}(z, \Omega, t) = \int_{visual \,\lambda} I_{\lambda}(z, \Omega, t) d\lambda,$$

$$I_{T}(z, \Omega, t) = \int_{thermal \,\lambda} I_{\lambda}(z, \Omega, t) d\lambda,$$

$$V(T) = \int_{thermal \,\lambda} U_{\lambda}(T) d\lambda = \sigma_{0} T^{4}(z, t),$$

where *visual* λ denotes the visual wavelength region where *I*λ is appreciable, and similarly for *thermal* λ. Define the visual value of any parameter *X*λ by

$$X_V(z) = \int_{visual \,\lambda} X_{\lambda}(z) I_{\lambda}(z, \Omega, t) d\lambda / I_V(z, \Omega, t).$$

Assuming that the spectrum of *I*λ is similar to that of *J*λ we can calculate *XV* to a good approximation by

$$X_V(z) \approx \int_0^\infty X_{\lambda}(z) J_{\lambda}(t) d\lambda / J(t).$$

Similarly, for the thermal region define

$$X_{T}(z) = \int_{thermal \, \lambda} X_{\lambda}(z) I_{\lambda}(z, \Omega, t) d\lambda / I_{T}(z, \Omega, t),$$

and to a good approximation

$$X_T(z) \approx \int_0^\infty X_{\lambda}(z) U_{\lambda}(T_C) d\lambda / V(T_C).$$

Integrating over each spectral region, the radiative-transfer equation can be separated into a wavelength-integrated equation for visual radiance

$$\cos\vartheta \frac{\partial I_{V}(z,\Omega,t)}{\partial z} = -E_{V}(z)I_{V}(z,\Omega,t) + \frac{1}{4\pi} \int_{4\pi} I_{V}(z,\Omega',t)G_{V}(z,\Omega',\Omega)d\Omega' + \frac{JF(t)}{4\pi} G_{V}(z,\Omega_{i},\Omega) \exp\left[-\frac{1}{\mu_{0}(t)} \int_{z}^{\infty} E_{V}(z')dz'\right], \quad (16.3)$$

and an equation for thermal IR radiance

$$\cos \vartheta \frac{\partial I_T(z,\Omega,t)}{\partial z} = -E_T(z)I_T(z,\Omega,t) + \frac{1}{4\pi} \int_{A\pi} I_T(z,\Omega',t)G_T(z,\Omega',\Omega)d\Omega' + \frac{A_T}{\pi} V(T). \quad (16.4)$$

Then the heat equation becomes

$$\rho C \frac{\partial T(z,t)}{\partial t} = \frac{\partial}{\partial z} \left[ k \frac{\partial T(z,t)}{\partial z} \right] + A_T(z) \left[ \int_{4\pi} I_T(z,\Omega,t) d\Omega \right] - 4A_T V(T)$$

$$+ A_V(z) JF(t) \exp \left[ -\frac{1}{\mu_0(t)} \int_z^{\infty} E_V(z') dz' \right]$$

$$+ A_V(z) \left[ \int_{4\pi} I_V(z,\Omega,t) d\Omega \right]. \tag{16.5}$$

Equation (16.4) assumes that the incident irradiance is negligible in the thermal IR region. If it is not negligible then an additional term similar to the third term on the right of equation (16.3) must be added to (16.4).

Now

$$\tau_V = \int_z^{\infty} E_V dz, \text{ or } d\tau_V = -E_V dz,$$

$$\tau_T = \int_z^{\infty} E_T dz, \text{ or } d\tau_T = -E_T dz,$$

$$G_V(z, \Omega', \Omega) = S_v(z) p_V(z, \Omega', \Omega),$$

$$G_T(z, \Omega', \Omega) = S_T(z) p_T(z, \Omega', \Omega),$$

$$w_V = S_V / E_V, w_T = S_T / E_T,$$

where the Ss are the volume-scattering coefficients and the ws are the volume particle single-scattering albedos. It was shown in Chapter 15 that

$$A_{\lambda} = \varepsilon_T E_{\lambda} = \gamma_T^2 E_{\lambda}$$

where )*T* is the volume particle emissivity and γ*T* = √1°*wT* . Then the separated equations become

$$-\cos\vartheta \frac{\partial I_{V}(\tau_{V},\Omega,t)}{\partial \tau_{V}} = -I_{V}(\tau_{V},\Omega,t)$$

$$+ \frac{w_{V}(\tau_{V})}{4\pi} \int_{4\pi} I_{V}(\tau_{V},\Omega',t) p_{V}(z,\Omega',\Omega) d\Omega'$$

$$+ JF(t) \frac{w_{V}(\tau_{V})}{4\pi} \exp\left[-\frac{\tau_{V}}{\mu_{0}(t)}\right], \qquad (16.6)$$

$$-\cos\vartheta \frac{\partial I_{T}(\tau_{T},\Omega,t)}{\partial \tau_{T}} = -I_{T}(\tau_{T},\Omega,t)$$

$$+ \frac{w_{T}(\tau_{T})}{4\pi} \int_{4\pi} I_{T}(\tau_{T},\Omega',t) p_{T}(\tau_{T},\Omega',\Omega) d\Omega'$$

$$+ \frac{\varepsilon_{T}(\tau_{T})}{\pi} V(T), \qquad (16.7)$$

$$\rho C \frac{\partial T(\tau_{T},t)}{\partial t} = E_{T}(\tau_{T}) \frac{\partial}{\partial \tau_{T}} \left[E_{T}(\tau_{T})k \frac{\partial T(\tau_{T},t)}{\partial \tau_{T}}\right]$$

$$+ A_{T}(\tau_{T}) \int_{4\pi} I_{T}(\tau_{T},\Omega,t) d\Omega - 4A_{T}(\tau_{T})V(T)$$

$$+ A_{V}(\tau_{T})JF(t) \exp\left[-\frac{\eta \tau_{T}}{\mu_{0}(t)}\right]$$

$$+ A_{V}(\tau_{T}) \int_{4\pi} I_{V}(\tau_{T},\Omega,t) d\Omega, \qquad (16.8)$$

where

$$\eta = \tau_{\rm V}/\tau_T$$
.

In order to solve these equations one temporal and six spatial boundary conditions are required, which are specific to a given situation. In time-dependent problems a condition on *T* at some given time must be specified. Three of the spatial boundary conditions are that the radiances and temperature must be finite everywhere, or if the medium is not infinitely thick, then values at the lower boundary must be specified. Two more result from the fact that at the upper boundary there cannot be any downward-going sources of visual or thermal radiance (the incident irradiance *J* is included as a source term in the visual equation and is not a boundary condition). The remaining boundary condition is on *T* and comes from the requirement that the flux of heat across the upper boundary can only be carried by thermal radiation and none by conduction. However, the conducted heat flux *k*∂*T /*∂*z* must be continuous across any horizontal plane, including the upper surface of the medium. Since *k* = 0 above the surface but not below it, this requires

$$\frac{\partial T}{\partial z}(0,t) = 0. \tag{16.9}$$

### 16.2.2 Equations for a uniform medium of isotropically scattering particles in the two-stream approximation

16.2.2.1 Equations

In this section we will employ these equations to media of isotropic scatterers with properties independent of depth using the two-stream approximation. The solution for aniosotropically scattering particles has been published in Hapke (1996a). (However, anyone who consults that paper should be cautioned that it contains a large number of typographical errors which the author was not able to correct because of an editorial mixup.) Since the particles scatter equally in all directions,  $p_V(z, \Omega', \Omega) = p_T(z, \Omega', \Omega) = 1$ . In a uniform medium all parameters in the equations are independent of z. Then the equations become

$$-\cos\vartheta \frac{\partial I_{V}(\tau_{V}, \Omega, t)}{\partial \tau_{V}} = -I_{V}(\tau_{V}, \Omega, t)$$

$$+ \frac{w_{V}}{4\pi} \int_{4\pi} I_{V}(\tau_{V}, \Omega, t) d\Omega$$

$$+JF(t) \frac{w_{V}}{4\pi} \exp\left[-\frac{\tau_{V}}{\mu_{0}(t)}\right], \qquad (16.10)$$

$$-\cos\vartheta \frac{\partial I_{T}(\tau_{T}, \Omega, t)}{\partial \tau_{T}} = -I_{T}(\tau_{T}, \Omega, t)$$

$$+ \frac{w_{T}}{4\pi} \int_{4\pi} I_{T}(\tau_{T}, \Omega, t) d\Omega + \frac{\gamma_{T}^{2}}{\pi} V(T), \qquad (16.11)$$

$$\rho C \frac{\partial T(\tau_{T}, t)}{\partial t} = kE_{T}^{2} \frac{\partial^{2} T}{\partial \tau_{T}^{2}}$$

$$+E_{T}\gamma_{T}^{2} \int_{4\pi} I_{T}(\tau_{T}, \Omega, t) d\Omega - 4E_{T}\gamma_{T}^{2} V(T)$$

$$+E_{V}\gamma_{V}^{2} JF(t) \exp\left[-\frac{\eta \tau_{T}}{\mu_{0}(t)}\right]$$

$$+E_{V}\gamma_{V}^{2} \int_{4\pi} I_{V}(\tau_{T}, \Omega, t) d\Omega. \qquad (16.12)$$

In the two-stream approximation (see Chapters 7 and 8) the radiances in the equations are replaced by their averages over the upward-going and downward-going hemispheres. Let  $I_{1V}$  and  $I_{2V}$  be the average visual radiances going

respectively in the upward and downward directions, and let *I*1*T* and *I*2*T* be similar thermal radiances,

$$\begin{split} I_{1V}(\tau_{V},t) &= \frac{1}{2\pi} \int_{\text{upper hemisphere}} I_{V}(\tau_{V},\Omega,t) d\Omega, I_{2V}(\tau_{V},t) \\ I_{2V}(\tau_{V},t) &= \frac{1}{2\pi} \int_{\text{lower hemisphere}} I_{V}(\tau_{V},\Omega,t) d\Omega, \\ I_{1T}(\tau_{V},t) &= \frac{1}{2\pi} \int_{\text{upper hemisphere}} I_{T}(\tau_{T},\Omega,t) d\Omega, I_{2T}(\tau_{T},t) \\ I_{2T}(\tau_{T},t) &= \frac{1}{2\pi} \int_{\text{lower hemisphere}} I_{T}(\tau_{T},\Omega,t) d\Omega. \end{split}$$

Then the radiances averaged over all directions are

$$\begin{split} \varphi_V(z,t) &= (I_{1V} + I_{2V})/2 = \frac{1}{4\pi} \int_{4\pi} I_V(z,\Omega,t) d\Omega, \\ \varphi_T(z,t) &= (I_{1T} + I_{2T})/2 = \frac{1}{4\pi} \int_{4\pi} I_T(z,\Omega,t) d\Omega, \end{split}$$

and the average hemispherical radiance differences are

$$\Delta \varphi_V = (I_{1V} - I_{2V})/2,$$
  
$$\Delta \varphi_T = (I_{1T} - I_{2T})/2.$$

After making these substitutions and combining the resulting expressions (see Chapter 8 for details), the equations for the visual radiance become

$$\frac{1}{4} \frac{\partial^2 \varphi_V(\tau_V, t)}{\partial \tau_V^2} = \gamma_V^2 \varphi_V(\tau_V, t) - JF(t) \frac{w_V}{4\pi} \exp\left[-\frac{\tau_V}{\mu_0(t)}\right], \quad (16.13a)$$

$$\Delta\varphi_V(\tau_V, t) = \frac{1}{2} \frac{\partial\varphi_V(\tau_V, t)}{\partial\tau_V},$$
(16.13b)

with the condition at the surface that *I*2*V (*0*,t)* = 0, which requires

$$\Delta\varphi_V(0,t) = \varphi_V(0,t) = \frac{1}{2} \frac{\partial\varphi_V}{\partial\tau_V}(0,t), \qquad (16.13c)$$

and the equations for the thermal radiance are

$$\frac{1}{4\gamma_T^2} \frac{\partial^2 \varphi_T(\tau_T, t)}{\partial \tau_T^2} = \varphi_T(\tau_V, t) - \frac{1}{\pi} V(T), \tag{16.14a}$$

$$\Delta \varphi_T(\tau_T, t) = \frac{1}{2} \frac{\partial \varphi_T(\tau_T, t)}{\partial \tau_T},$$
 (16.14b)

with the condition at the surface that  $I_{2T}(0, t) = 0$ , so that

$$\Delta\varphi_V(0,t) = \varphi_V(0,t) = \frac{1}{2} \frac{\partial\varphi_V}{\partial\tau_V}(0,t). \tag{16.14c}$$

The heat equation becomes

$$\rho C \frac{\partial T(\tau_T, t)}{\partial t} = kE_T^2 \frac{\partial^2 T(\tau_T, t)}{\partial \tau_T^2} + 4\pi E_T \gamma_T^2 \left\{ \varphi_T(\tau_T, t) - \frac{1}{\pi} V(T) \right\}$$

$$+ E_V \gamma_V^2 \left\{ JF(t) \exp\left[ -\frac{\eta \tau_T}{\mu_0(t)} \right] + 4\pi \varphi_V(\tau_T t) \right\},$$
(16.15a)

where  $\eta = \tau_V/\tau_T = E_V/E_T$ . An alternative form of the heat equation may be obtained by substituting equations (16.14a) into (16.15a), and after dividing by  $kE_T^2$ , gives

$$\frac{\rho C}{kE_T^2} \frac{\partial T(\tau_T, t)}{\partial t} = \frac{\partial^2 T(\tau_T, t)}{\partial \tau_T^2} + \pi q \frac{\partial^2 \varphi_T(\tau_T, t)}{\partial \tau_T^2} + \eta \gamma_V^2 q \{J_V F(t) \exp[-\eta \tau_T / \mu_0(t)] + 4\pi \varphi_V(\tau_T, t)\}, \quad (16.15b)$$

where

$$q = 1/kE_T, \tag{16.15c}$$

with the condition at the surface for either form of the equation,

$$\frac{\partial T}{\partial \tau_T}(0,t) = 0. \tag{16.15d}$$

It must be emphasized that all of these surface boundary conditions apply only to situations where there is no atmosphere and the surface sees cold space. If the medium is at the bottom of an atmosphere then at the surface the heat flux conducted through the medium must be continuous with the flux conducted through the air above the surface. Also, the downward-going radiances  $I_{2V}$  and  $I_{2T}$  at the surface must be equal to the visual and IR radiances scattered and radiated downward onto the surface by the atmosphere.

A further check on the validity of any solution is that deep in the interior the thermal radiance must be in thermodynamic equilibrium with the particle temperature. This requires

$$\varphi_T(\tau_T \gg 1, t) = \frac{1}{\pi} V(T).$$
 (16.16)

### 16.2.2.2 The boundary-layer approximation

Because the equations for T and  $\varphi_T$  are nonlinear, exact solutions are difficult to obtain except numerically by computer, which is often inconvenient. A useful,

approximate relation can be derived by realizing that because the temperature gradient is zero at the surface there is a small region near the surface in which the temperature is almost constant. Within this boundary layer equation (16.14a) is approximately

$$\frac{1}{4\gamma_T^2} \frac{\partial^2 \varphi_T(\tau_T, t)}{\partial \tau_T^2} = \varphi_T(\tau_V, t) - \frac{1}{\pi} V(T_S),$$

where  $T_S(t) = T(0, t)$  is the surface temperature. The solution to this equation that also satisfies the boundary conditions on  $\varphi_T$  is

$$\varphi_T(\tau_v, t) = \frac{V(T_S)}{\pi} - \frac{1}{1 + \nu_T} \frac{V(T_S)}{\pi} \exp(-2\gamma_T \tau_T).$$
 (16.17)

At the surface this solution becomes

$$\varphi_S = \frac{\gamma_T}{1 + \gamma_T} \frac{V(T_S)}{\pi} = \frac{\gamma_T}{1 + \gamma_T} \frac{\sigma_0}{\pi} T_S^4,$$
 (16.18)

where  $\varphi_S(t) = \varphi(0, t)$ . Equation(16.18) provides an alternative boundary condition at the surface.

Furthermore, the requirement that  $\varphi_T \to V(T)/\pi$  as  $\tau_T$  increases away from the surface suggests that a good approximate solution for  $\varphi_T$  can be obtained by replacing  $V(T_S)$  by V(T) in the first term of equation (16.17),

$$\varphi_{T}(\tau_{v}, t) \approx \frac{V(T)}{\pi} - \frac{1}{1 + \gamma_{T}} \frac{V(T_{S})}{\pi} \exp(-2\gamma_{T}\tau_{T})$$

$$= \frac{\sigma_{0}}{\pi} T^{4}(\tau_{T}, t) - \frac{1}{1 + \gamma_{T}} \frac{\sigma_{0}}{\pi} T_{S}^{4} \exp(-2\gamma_{T}\tau_{T}). \tag{16.19}$$

Equation(16.19) is the boundary-layer approximation for  $\varphi_T$ . It is exact for both large and small  $\tau_T$ . Comparisons with exact computer solutions of the radiative and heat equations and solutions using the boundary-layer approximation will be given below. It will be seen that in all cases the solutions differ by only a few percent.

### 16.2.2.3 The equations in reduced form

Frequently it is useful to put the equations in nondimensional form in such as way as to reduce the number of parameters to a minimum. Let  $t_R$  be an interval of time that characterizes the system of interest, and  $T_R$  be a temperature that is characteristic of the system. Define

$$\varphi_V^* = \varphi_V/J,$$

$$\varphi_T^* = \pi \varphi_T/\sigma_0 T_R^4,$$

$$T^* = T/T_R$$

$$t^* = t/t_R.$$

Then equations (16.13)–(16.15) become

$$\frac{1}{4} \frac{\partial^2 \varphi_V^*(\tau_V, t^*)}{\partial \tau_V^2} = \gamma_V^2 \varphi_V^*(\tau_V, t^*) - F(t^*) \frac{w_V}{4\pi} \exp\left[-\frac{\tau_V}{\mu_0(t^*)}\right], \quad (16.20a)$$

$$\varphi_V^*(0, t^*) = \frac{1}{2} \frac{\partial \varphi_V^*}{\partial \tau_V}(0, t^*), \tag{16.20b}$$

$$\frac{1}{4\gamma_T^2} \frac{\partial^2 \varphi_T^*(\tau_T, t^*)}{\partial \tau_T^2} = \varphi_T^*(\tau_V, t^*) - T^{*4}, \tag{16.21a}$$

$$\varphi_V^*(0, t^*) = \frac{1}{2} \frac{\partial \varphi_V^*}{\partial \tau_V}(0, t^*), \tag{16.21b}$$

$$\frac{t_D}{t_R} \frac{\partial T^*(\tau_T, t^*)}{\partial t^*} = \frac{\partial^2 T^*(\tau_T, t^*)}{\partial \tau_T^2} + q_T \frac{\partial^2 \varphi_T^*(\tau_T, t^*)}{\partial \tau_T^2}$$
(16.22a)

$$+F(t^*)q_V\left\{\exp\left[-\eta\tau_T/\mu_0(t^*)\right]+4\pi\varphi_V^*(\tau_T,t^*)\right\},$$

$$\frac{\partial T}{\partial \tau_T}(0, t^*) = 0, \tag{16.22b}$$

where

$$t_D = \rho C / k E_T^2 \tag{16.23a}$$

$$q_T = \sigma_0 T_R^3 / k E_T, \tag{16.23b}$$

$$q_V = J\eta \gamma_v^2 / kE_T T_R, \tag{16.23c}$$

$$\eta = E_V / E_T. \tag{16.23d}$$

## 16.3 Some time-independent applications of the equations 16.3.1 An optically thick layer heated from below

In this section we will address the problem of a particulate medium of thickness  $Z \gg 1/E_T$  heated from below by a plate at constant temperature  $T_P$  and radiating into cold space from the top surface. This might represent the situation in a laboratory measurement of emissivity where the surface of the medium sees only cold surfaces close to absolute zero.

For this problem all quantities are independent of t and the visual radiance is negligible, so F(t) = 1, and  $\partial T/dt = J_V = \varphi_V = 0$ . Then equation (16.15b) becomes

$$\frac{d^2T(\tau_T)}{d\tau_T^2} + \pi q \frac{d^2\varphi_T(\tau_T)}{d\tau_T^2} = 0.$$
 (16.24)

Integrating from 0 to  $\tau_T$  gives

$$\frac{dT(\tau_T)}{d\tau_T} - \frac{dT(0)}{d\tau_T} + \pi q \frac{d\varphi_T(\tau_T)}{d\tau_T} - \pi q \frac{d\varphi_T(0)}{d\tau_T} = 0.$$

Applying boundary conditions (16.14c) and (16.15c) this is

$$\frac{dT(\tau_T)}{d\tau_T} + \pi q \frac{d\varphi_T(\tau_T)}{d\tau_T} = 2\pi q \varphi_S. \tag{16.25}$$

Integrating again we obtain

$$T(\tau_T) + \pi q \varphi_T(\tau_T) = T_S + \pi q \varphi_S + 2\pi q \varphi_S \tau_T. \tag{16.26}$$

This equation shows that the quantity  $(T + \pi q \varphi_T)$  is linearly proportional to  $\tau_T$ . At the bottom of the layer  $T = T_P$ ,  $\varphi_T = \varphi_P$ , and  $\tau_T = \tau_P = E_T Z$ , and equation (16.26) is

$$T_P + \pi q \varphi_P = T_S + \pi q \varphi_S + 2\pi q \varphi_S \tau_P. \tag{16.27}$$

Since the layer is optically thick, the radiation is in thermodynamic equilibrium with the temperature of the grains at the plate; hence  $\varphi_P = V(T_P)/\pi$ . Inserting this, together with equation (16.18), into equation (16.27) gives

$$T_P + q\sigma_0 T_P^4 = T_S + q \frac{\gamma_T}{1 + \gamma_T} \sigma_0 T_S^4 (1 + 2\tau_P),$$
 (16.28)

where  $T_P$  is the known plate temperature. Equation (16.28) is a transcendental equation for  $T_S$  that can be rapidly solved by iteration. Once  $T_S$  is obtained it can be inserted into equation (16.18) to get  $\varphi_S$ .

Inserting equation (16.19) into (16.26), we obtain

$$T(\tau_T) + q \left[ \sigma_0 T^4(\tau_T) - \frac{1}{1 + \gamma_T} \sigma_0 T_S^4 \exp(-2\gamma_T \tau_T) \right]$$
  
=  $T_S + q \frac{\gamma_T}{1 + \gamma_T} \sigma_0 T_S^4(1 + 2\tau_T),$  (16.29)

which can be solved by iteration. The values for  $T(\tau_T)$  are then inserted into equation (16.19) to give the solution for  $\varphi_T(\tau_T)$ . This completes the solution of the problem using the boundary layer approximation. An example of the temperature and thermal radiance calculated from equations (16.19) and (16.29) is given in Figure 16.1. For comparison, the figure also shows the exact numerical solution. The temperature shown is relative to that of the heating plate  $T_P$ . The IR radiance is relative to the thermal equilibrium radiance at the plate  $\sigma_0 T_P^4/\pi$ .

<!-- IMAGE: _page_11_Figure_2.jpeg -->

Figure 16.1 Reduced temperature and thermal radiance as a function of thermal optical depth in a layer of powder in a vacuum lying on a hot plate and radiating into a cold environment from its upper surface. The heater plate is located at an optical depth of 10. Other parameters are  $w_T = 0.36$  and q = 0.26. Solid line is the numerical solution; dashed line is the approximate solution using the boundary-layer approximation. (Reproduced from Hapke [1996], copyright 1996 by the American Geophysical Union.)

### 16.3.2 Radiative conductivity

The power radiated from the upper surface of the slab is

$$P_{rad} = \int_0^{\pi/2} I_{1T}(0) 2\pi \cos e \sin e de = \pi I_{1T}(0) = 2\pi \varphi_S.$$

Since there are no sources or sinks of energy in the slab the heat flux  $2\pi\phi_S$  must be constant through the slab. From equations (16.19) and (16.25)

$$P_{rad} = 2\pi \varphi_{S} = kE_{T} \frac{dT(z)}{d\tau_{T}} + \pi \frac{d\varphi_{T}(z)}{d\tau_{T}} = k \frac{dT(z)}{dz} + \frac{\pi}{E_{T}} \frac{d\varphi_{T}(z)}{dz}$$

$$= k \frac{dT(z)}{dz} + \frac{\pi}{E_{T}} \frac{d}{dz} \left[ \frac{V(T)}{\pi} - \frac{1}{1 + \gamma_{T}} \frac{V(T_{S})}{\pi} \exp(-2\gamma_{T} E_{T} z) \right]$$

$$= k \frac{dT(z)}{dz} + \frac{4}{E_{T}} \sigma_{0} T^{3}(z) \frac{dT(z)}{dz} + \frac{2\gamma_{T}}{1 + \gamma_{T}} \sigma_{0} T_{S}^{4} \exp(-2\gamma_{T} E_{T} z). \quad (16.30)$$

The first term on the right in equation (16.30) is the heat carried by ordinary conduction, where the coefficient of dT/dz is the solid-state conductivity k. The last two terms are the flux of energy carried by radiation. Far from the surface where the exponential is negligible the second term is the heat carried by radiation. Thus, the

coefficient of dT/dz in the second term may be defined as the radiative conductivity

$$k_{rad} = \frac{4}{E_T} \sigma_0 T^3(z). {(16.31)}$$

However, as the surface is approached within the boundary layer the first and second terms decrease while the third term increases until at the surface all of the heat flux is carried by the third term, where it is radiated away with an effective temperature  $T_S$  and hemispherical emissivity  $\varepsilon_h = 2\gamma_T(1 + \gamma_T)$ . Compare this expression for the emissivity with equations (15.24). Note that because of the boundary condition that dT/dz(0) = 0,  $P_{rad}$  is relatively insensitive to temperature gradients deeper under the surface.

### 16.3.3 Planetary regolith in equilibrium with sunlight

The second system to be considered is a semi-infinite medium of isotropically scattering particles illuminated at angle of incidence *i* by a constant source of visible light and radiating into a vacuum. This simulates the surface of a solar-system body tidally locked so the same side always faces the Sun. It also simulates conditions sometimes used in laboratory thermal measurements.

In the classical treatment of the steady-state problem all absorption and emission of radiation is assumed to take place at the surface and constitutes the boundary conditions. In that case the heat equation is simply  $d^2T/dz^2=0$ . The only solution to this equation that satisfies the boundary conditions is T(z)= constant. Then the visual light absorbed  $(1-A_h)J\mu_0$  must be equal to the IR radiated from the surface  $\varepsilon_h\sigma_0T^4$ , so that

$$T = [(1 - A_h) J \mu_0 / \varepsilon_h \sigma_0]^{1/4}$$
.

For a perfect black body,  $A_h = 0$  and  $\varepsilon_h = 1$ , so that at  $\mu_0 = 1$ ,  $T = T_{BB}$ , where  $T_{BB}$  is the *black-body radiative equilibrium temperature* 

$$T_{BB} = (J_V/\sigma_0)^{1/4}$$
. (16.32)

Although no real object is a perfect black body,  $T_{BB}$  is a useful quantity with which to compare actual temperatures on bodies of the solar system. In this section we will derive more realistic expressions for the temperature and radiation within the medium, using the two-stream and boundary-layer approximations.

Equation (16.13a) for the directionally averaged visual radiance is independent of the thermal radiative and heat equations and can be solved separately. The solution with F(t) = 1 that satisfies the condition that the radiance is finite everywhere is given by equations (8.39), (8.42), and (8.43). Inserting these solutions into equation

(16.15b) gives

$$\frac{d^{2}T(\tau_{T})}{d\tau_{T}^{2}} + \pi q \frac{d^{2}\phi_{T}}{d\tau_{T}^{2}} = -\eta q \gamma_{\nu}^{2} \left[ A \exp(-\eta \tau_{T}/\mu_{0}) + B \exp(-2\gamma_{V} \eta \tau_{T}) \right], \tag{16.33a}$$

where

$$A = J \frac{(1 - 4\mu_0^2)}{1 - 4\gamma_V^2 \mu_0^2},\tag{16.33b}$$

$$B = J \frac{2\mu_0(1 - \gamma_V)(1 + 2\mu_0)}{1 - 4\gamma_V^2 \mu_0^2},$$
 (16.33c)

and  $q = 1/kE_T$ .

Integrating equation (16.33a) from 0 to  $\tau_T$  and applying the boundary conditions gives

$$\begin{split} &\frac{dT(\tau_T)}{d\tau_T} + \pi q \left[ \frac{d\varphi_T(\tau_T)}{d\tau_T} - 2\varphi_S \right] \\ &= \gamma_V^2 q \left\{ A\mu_0 [\exp(-\eta \tau_T/\mu_0) - 1] + \frac{B}{2\gamma_V} [\exp(-2\gamma_V \eta \tau_T) - 1] \right\} \end{split}$$

where  $\varphi_S = \varphi_T(0)$ . Integrating again, we obtain

$$T(\tau_T) - T_S + \pi q \left[ \varphi_T(\tau_T) - \varphi_S - 2\varphi_S \tau_T \right]$$

$$= -\gamma_V^2 q \left( A\mu_0 \left\{ \frac{\mu_0}{\eta} \left[ \exp(-\eta \tau_T / \mu_0) - 1 \right] + \tau_T \right\} \right)$$

$$+ \frac{B}{2\gamma_V} \left\{ \frac{1}{2\eta \gamma_V} \left[ \exp(-2\gamma_V \eta \tau_T) - 1 \right] + \tau_T \right\} \right), \tag{16.34}$$

where  $T_S = T(0)$ . Now,  $T(\tau_T)$  must remain finite as  $\tau_T \to \infty$ . The only way this can be true is if the sum of the coefficients of  $\tau_T$  vanishes. Thus,

$$2\varphi_S = \gamma_V^2 \left( A\mu_0 + B/2\gamma_V \right) / \pi.$$

After substituting for A and B this becomes

$$\varphi_S = J \frac{\gamma_V \mu_0}{2\pi} \frac{1 + 2\mu_0}{1 + 2\gamma_V \mu_0},\tag{16.35}$$

which becomes the boundary condition on  $\varphi_T$ . Then equation (16.34) is

$$T(\tau_T) - T_S + \pi q \left[ \varphi_T(\tau_T) - \varphi_S \right]$$

$$= \frac{q}{\eta} \left\{ A \gamma_V^2 \mu_0^2 [1 - \exp(-\eta \tau_T / \mu_0)] + \frac{B}{4} [1 - \exp(-2\gamma_V \eta \tau_T)] \right\}. \quad (16.36)$$

Substituting the boundary-layer approximation, equation (16.19), and putting  $\tau_T = E_T|z|$ , we obtain

$$T(z) - T_S + \frac{1}{kE_T} \left[ \sigma_0 T^4(z) - \frac{1}{1 + \gamma_T} \sigma_0 T_S^4 \exp(-2\gamma_T E_T |z|) - \pi \phi_S \right]$$

$$= \frac{1}{kE_V} \left\{ A \gamma_V^2 \mu_0^2 [1 - \exp(-E_V |z|/\mu_0)] + \frac{B}{4} [1 - \exp(-2\gamma_V E_V |z|)] \right\},$$
(16.37)

where, from equations (16.18) and (16.30),

$$T_S = \left(\frac{1 + \gamma_T}{\gamma_T} \varphi_S\right)^{1/4} = \left[J \frac{\mu_0 (1 + \gamma_V)}{2\sigma_0} \frac{1 + 2\mu_0}{1 + 2\gamma_V \mu_0}\right]^{1/4}.$$
 (16.38)

T(z) can rapidly be found from equation (16.37) by iteration, and  $\varphi_T(z)$  from the boundary-layer approximation,

$$\varphi_T(z) = \frac{\sigma_0}{\pi} T^4(z) - \frac{1}{1 + \nu_V} \frac{\sigma_0}{\pi} T_S^4 \exp(-2\gamma_T E_T |z|). \tag{16.39}$$

This completes the solution for the distribution of temperature and radiances in the medium.

Figures 16.2–16.5 show the temperature and thermal radiance as a function of depth for several values of the parameters in these equations. For comparison, the exact numerical solutions are also shown. Since the particles are assumed to be large compared to the IR wavelength, the extinction lengths should not vary strongly with wavelength. Hence, for these figures it was assumed that  $E_V = E_T$ , so that  $\eta = 1$  and  $\tau_T = \tau_V$ . The low value of the visual single-scattering albedo of  $w_V = 0.36$  might be representative of a relatively low-albedo body, such as the Moon or an asteroid. The high value of  $w_V = 0.91$  might be representative of somewhat dirty ice on the surface of a rocky-icy satellite, while  $w_V = 0.9996$ is representative of clean, fresh snow. In the thermal IR  $w_T = 0.36$  is probably representative of most materials. A value of  $w_T = 0.91$  probably is unrealistically high because most materials of interest for planetary remote sensing have restrahlen bands at IR wavelengths. However, it is included to show the effect of a high IR albedo, such as that of an alkali halide. The thermal radiances shown are relative to  $J/\pi$ , which is the IR radiance from the surface of a nonconducting black body illuminated by visual irradiance J. The temperatures are relative to the black-body temperature  $(\pi J/\sigma_0)^{1/4}$  of the surface of the body.

In all cases, as the optical depth increases  $\varphi_T$  rises rapidly from a value of  $\varphi_T = \varphi_S$  at the surface and then levels off to either a constant value or to a more gentle rate of increase. The rapid rise is a direct result of leakage of thermal radiation from the surface. Thermodynamic equilibrium is approached when  $\tau_T > \sim 3$ .

<!-- IMAGE: _page_15_Figure_2.jpeg -->

Figure 16.2 Reduced temperature and thermal radiance as a function of thermal optical depth in a regolith in vacuum in equilibrium with sunlight, showing the effect of varying the angle of incidence i. Other parameters are  $w_V=0.36$ ,  $w_T=0.36$ , q=0.26. Solid line is the numerical solution; dashed line is the approximate solution using the boundary-layer approximation. (Reproduced from Hapke [1996], copyright 1996 by the American Geophysical Union.)

<!-- IMAGE: _page_15_Figure_4.jpeg -->

Figure 16.3 Reduced temperature and thermal radiance as a function of thermal optical depth in a regolith in vacuum in equilibrium with sunlight, showing the effect of varying the visual single-scattering albedo  $w_V$ . Other parameters are  $w_T = 0.36$ , q = 0.26, i = 0. Solid line is the numerical solution; dashed line is the approximate solution using the boundary-layer approximation. (Reproduced from Hapke [1996], copyright 1996 by the American Geophysical Union.)

<!-- IMAGE: _page_16_Figure_2.jpeg -->

Figure 16.4 Reduced temperature and thermal radiance as a function of thermal optical depth in a regolith in vacuum in equilibrium with sunlight, showing the effect of varying the thermal single-scattering albedo  $w_T$ . Other parameters are  $w_V = 0.36$ , q = 0.26, i = 0. Solid line is the numerical solution; dashed line is the approximate solution using the boundary-layer approximation. (Reproduced from Hapke [1996], copyright 1996 by the American Geophysical Union.)

<!-- IMAGE: _page_16_Figure_4.jpeg -->

Figure 16.5 Reduced temperature and thermal radiance as a function of thermal optical depth in a regolith in vacuum in equilibrium with sunlight, showing the effect of varying the parameter  $q=1/kE_T$ . Other parameters are  $w_V=0.36$ ,  $w_T=0.36$ , i=0. Solid line is the numerical solution; dashed line is the approximate solution using the boundary-layer approximation. (Reproduced from Hapke [1996], copyright 1996 by the American Geophysical Union.)

The behavior of T is more complex. The slope of T is zero at the surface, as required by the boundary condition, but as the optical depth increases T may exhibit a positive or negative slope, depending on the value of  $\gamma_T$  compared with  $\gamma_V$  and  $\mu_0$ . If these quantities are comparable T has a positive slope. However, the slope of T may be small or even negative if  $\gamma_T$  is small. Heating by unscattered visible irradiance occurs over an optical depth  $\sim 1/\mu_0$ , and by multiply scattered visible radiance over a distance  $\sim 1/\gamma_V$ , but the IR flux is radiated from the surface from optical depths  $\sim 1/\gamma_T$ . If  $1/\gamma_T > 1/\gamma_V$  or  $1/\mu_0$  then heat must be conducted from the surface to supply power to the deeper IR radiative sink. This requires a negative temperature gradient. It should also be emphasized that the widths of the gradients in actual depth z, rather than optical depth  $\tau_T$ , will depend on particle size and filling factor.

### 16.3.4 The solid-state greenhouse effect

An atmospheric greenhouse effect can occur on a planet whose atmosphere is transparent to visible light but opaque to thermal radiation. The energy of visible sunlight is absorbed at the ground level but radiated back into space as thermal radiation from the upper layers of the atmosphere. This requires a temperature gradient to transport heat from the surface to the radiating layer. On Venus this effect produces a surface temperature that is nearly triple the black-body temperature. Brown and Matson (1987) and Matson and Brown (1989) have pointed out that an analogous solid-state greenhouse effect could occur in a planetary regolith. Visible sunlight is deposited over a depth  $\sim 1/E_V \sqrt{1-w_V}$ , but thermally radiated from a depth  $\sim 1/E_T \sqrt{1-w_T}$ . If the regolith is weakly absorbing in the visible and strongly absorbing in the IR so that  $w_V \sim 1$  but  $w_T \ll 1$  this could cause a considerable increase in temperature from the surface to the interior.

The increase in temperature from the surface to the deep interior in a regolith irradiated by sunlight can be calculated from equation (16.37) by letting  $z \to \infty$ ,

$$T(\infty) = T_S + \frac{1}{kE_T} \left[ \pi \varphi_S - \sigma_0 T^4(\infty) \right] + \frac{1}{kE_V} \left[ A \gamma_V^2 \mu_0^2 + \frac{B}{4} \right].$$

After substituting for A, B, and  $\varphi_S$  from equations (16.33) and (16.35) this equation can be considerably simplified. The final result is

$$T(\infty) = T_S - \frac{\sigma_0}{kE_T} T^4(\infty) + \frac{J}{2kE_T} \mu_0 (1 + 2\mu_0), \tag{16.40}$$

where  $T_S$  is given by equation (16.38).

The surprising result is that equation (16.40) is independent of both  $w_V$  and  $w_T$ . The reason is that although a small absorption coefficient allows the visible radiance to be deposited deep in the regolith, it also causes a high visual albedo so

| Location          | $R_e(\mathrm{AU})$ | $kE_T({\rm W} {\rm m}^{-2} {\rm K}^{-1})$ | $T_S(K)$ | $T(\infty)(K)$ | $\Delta T_{Gr}(\mathbf{K})$ |
|-------------------|--------------------|-------------------------------------------|----------|----------------|-----------------------------|
| Moon              | 1                  | 10                                        | 397      | 422            | 25                          |
| Jovian satellites | 5                  | 1                                         | 176      | 188            | 12                          |
|                   | 5                  | 10                                        | 176      | 180            | 4                           |
|                   | 5                  | 100                                       | 176      | 178            | 2                           |

Table 16.1. The solid-state greenhouse effect on a nonrotating body

that less sunlight is absorbed by the medium. The two effects exactly cancel each other when the particles are isotropic scatterers so that only a relatively small rise in temperature occurs.

Let us estimate the greenhouse effect for a few locations in the solar system. The incident irradiance  $J = S_{\odot}/R_{\odot}^2$ , where  $S_{\odot} = 1360 \text{ W m}^{-2}$  is the irradiance of sunlight at the earth and  $R_{\odot}$  is the distance of the body from the Sun in astronomical units. Assuming that the particles are equant and larger than the wavelength,  $Q_E =$ 1, the filling factor is  $\phi = \pi ND^3/6$ , and the extinction coefficient is  $E_T = E_V =$  $N\sigma Q_E = (6\phi/\pi D^3)(\pi D^{2-}/4)Q_E = 3\phi/2D$ . Thus  $kE_T = 3k\phi/2D$ . The solidstate thermal conductivity is the bulk conductivity of the medium and not just the conductivity of the material of which the particles are made. It includes the fact that the particles are in good thermal contact with each other in only a few small places on their surfaces. Hence the bulk thermal conductivity is primarily determined by the sizes of the contact areas and is relatively insensitive to the composition of the material. Fountain and West (1970) measured the radiative and solid-state thermal conductivity of lunar soil in the laboratory and found  $k \approx 0.001 \,\mathrm{W m^{-1} K^{-1}}$ . Since the atmosphereless, icy bodies of the solar system have regoliths that, like the Moon's, are generated by meteoritic impacts, Matson and Brown (1989) argued that this value if k is probably also representative of the icy bodies. For lunar soil,  $\phi \sim 0.30$  (Carrier et al., 1973) and  $D \sim 50 \mu m$  (McKay et al., 1974), so that  $kE_T \sim 10 \text{ W m}^{-2} \text{K}^{-1}$ .

The time-independent greenhouse rise in temperature  $\Delta T_{Gr} = T(\infty) - T_S$  is calculated for  $\mu_0 = 1$  in Table 16.1 for bodies at the location of the Moon and the Jovian satellites for several values of  $kE_T$ . It is seen to be only a few 10's of degrees. A somewhat larger greenhouse effect can occur if the particles in the medium scatter anisotropically (Hapke, 1996b). If the particles are forward-scattering in the visual, but backscattering in the IR, and if the bodies are allowed to rotate, temperature rises as large as 40 K are possible in the regoliths of the Jovian icy satellites.

A solid-state greenhouse effect is intrinsically different from an atmospheric greenhouse effect. In the latter the optical depth at which visual energy is deposited is essentially independent of the bolometric albedo, whereas in the former the two

are tightly coupled. In addition, radiation can contribute to the thermal conductivity even at the low temperatures of the Jovian satellites and reduce the temperature differences within the medium.

### 16.3.5 Physical meaning of the parameters in the reduced equations

The quantity  $\rho C/k$  that appears in equations (16.23) is known as the *thermal diffusivity*. The related quantity  $t_D = \rho C/kE_T^2$  has the units of time and is called the *thermal diffusion time*. The physical meaning of the diffusion time may be seen by writing it in the form

$$t_D = \frac{\rho C \Delta T l_{eT}}{k \frac{\Delta T}{l_{eT}}}$$

where  $\Delta T$  is a small rise in temperature and  $l_{eT}=1/E_T$ , the extinction length for thermal radiation Now,  $\rho C \Delta T l_{eT}$  is the amount of heat necessary to increase the temperature of a layer of thickness  $l_{eT}$  by  $\Delta T$ , and  $k\Delta T/l_{eT}$  is the flux of heat conducted through the layer. Thus,  $t_D$  is a measure of the time required to change the temperature distribution of a system by solid-state conduction when some parameter the system is changed. For typical soils in a vacuum the thermal diffusion time is of the order of seconds.

The diffusion time may also be written

$$t_D = \frac{k\rho C}{k^2 E_T^2} = (q \, \Gamma)^2$$

where  $q = 1/kE_T$  and

$$\Gamma = \sqrt{k\rho C} \tag{16.41}$$

is the *thermal inertia*. If the thermal inertia is high, relatively large amounts of heat are required to change the temperature of the medium appreciably, and heat is efficiently conducted between the surface and the interior of the medium, so that only small temperature fluctuations result from changing J. Conversely, a small value of the thermal inertia means that changing J causes large temperature fluctuations.

From equation (16.23b) the parameter  $q_T$  is

$$q_T = \frac{\sigma_0 T_R^3}{k E_T} = \frac{1}{4} \frac{k_{rad}}{k}.$$

Thus  $q_T$  is a measure of the flux of heat carried by thermal radiation relative to that carried by conduction.

Assuming  $E_V \approx E_T$  in equation (16.23c) the parameter  $q_V = J(1-w_V)/kE_TT_R$ . If we take  $T_R = T_{BB} = (J/\sigma_0)^{1/4}$  this becomes

$$q_V = \frac{\sigma_0 T_{BB}^3 (1 - w_V)}{k E_T} = \frac{1}{4} \frac{k_{rad}}{k} (1 - w_V).$$

Now,  $(1-w_V)$  is the fraction of J absorbed per unit volume. Hence,  $q_V$  is a measure of the amount of absorbed visible light carried away by thermal radiation relative to conduction.

## 16.4 Time-dependent radiative and conductive models

Thus far, only problems that are constant in time have been considered because they allow analytic solutions. However, in order to realistically model the thermal regime in a planetary regolith, time-dependent models must be considered. Unfortunately this renders the problem analytically intractable and solutions must be obtained numerically.

One of the early efforts to do this was the classical paper of Wesselink (1948). He assumed a constant thermal conductivity and that the visual and thermal radiation interacted with the medium only at the surface. Then the heat equation is simply

$$\rho C \frac{\partial T(z,t)}{\partial t} = k \frac{\partial^2 T(z,t)}{\partial z^2},$$

with the boundary condition that the conductive heat flux under the surface must be equal to the thermal and visual radiative fluxes above the surface,

$$JF(t)\mu_0(t) = \varepsilon_h \sigma_0 T^4(0,t) + k \frac{\partial T(z,t)}{\partial z},$$

where F(t) is a binary function equal to 1 during the day and 0 at night. To reduce these equations to dimensionless form, let  $T\#=T/T_R$ , where  $T_R=(J_V/\varepsilon_h\sigma_0)^{1/4}$ , t#=t/P, where P is the Moon's period of rotation, and  $z\#=z/z_R$ , where  $z_R=(kP/\rho C)^{1/2}$ . Making these substitutions, the differential equation becomes

$$\frac{\partial T^{\#}(z^{\#}, t^{\#})}{\partial t^{\#}} = \frac{\partial^{2} T^{\#}(z^{\#}, t^{\#})}{\partial z^{\#2}},$$

and the boundary condition is

$$F(t^{\#})\mu_{0}(t^{\#}) = T^{\#^{4}} - \frac{\Gamma}{\varepsilon_{h}\sigma_{0}T_{R}^{3}\sqrt{P}} \frac{\partial T^{\#}(0, t^{\#})}{\partial z^{\#}}.$$

Now, the values of the quantities  $\sigma_0$ ,  $T_R$ , and P are known, and to a good approximation  $\varepsilon_h \approx 1$ , so  $\Gamma$  is the only unknown. By comparing solutions of these equations to measured data  $\Gamma$  can be found. The best value of the thermal inertia found by

<!-- IMAGE: _page_21_Figure_2.jpeg -->

Figure 16.6 Brightness temperature of the lunar surface versus time for an area on the equator. Line is the model with  $\Gamma = 43 \text{ J m}^{-2} \text{ K}^{-1} \text{ s}^{-1/2}$ ,  $kE_T = 18.4 \text{ J s}^{-1} \text{ m}^{-2} \text{ s}^{-1}$ . Dots are observations of Shorthill (1972). (Reproduced from Hale and Hapke [2002], copyright 2002 with permission of Elsevier.)

<!-- IMAGE: _page_21_Figure_4.jpeg -->

Figure 16.7 Calculated temperature versus thermal optical depth in the lunar regolith for an area on the lunar equator for the same model parameters as in Figure 16.6. The two curves show the temperatures at noon and just before dawn. (Reproduced from Hale and Hapke [2002], copyright 2002 with permission of Elsevier.)

Wesselink for the Moon was surprisingly small,  $43 \,\mathrm{Jm^{-2}K^{-1}s^{-1/2}}$ , which implied, well before the *Apollo* missions, that the regolith was an exceptionally good thermal insulator, consistent with fine powder in vacuum.

The more realistic time-dependent equations (16.13)–(16.15) for a regolith of isotropically scattering particles can be put into reduced form by letting  $T_R = T_{BB}$ , where  $T_{BB} = (J/\sigma_0)^{1/4}$  is the black-body temperature,  $t_R = P$ , the period of revolution, and F(t) is the binary function. Then the reduced equations take the form

$$\frac{1}{4} \frac{\partial^{2} \varphi_{V}^{*}(\tau_{V}, t^{*})}{\partial \tau_{V}^{2}} = \gamma_{V}^{2} \varphi_{V}^{*}(\tau_{V}, t^{*}) - F(t^{*}) \frac{w_{V}}{4\pi} \exp\left[-\frac{\tau_{V}}{\mu_{0}(t^{*})}\right],$$

$$\varphi_{V}^{*}(0, t^{*}) = \frac{1}{2} \frac{\partial \varphi_{V}^{*}}{\partial \tau_{V}}(0, t^{*}),$$

$$\frac{1}{4\gamma_{T}^{2}} \frac{\partial^{2} \varphi_{T}^{*}(\tau_{T}, t^{*})}{\partial \tau_{T}^{2}} = \varphi_{T}^{*}(\tau_{V}, t^{*}) - T^{*4},$$

$$\varphi_{T}^{*}(0, t^{*}) = \frac{1}{2} \frac{\partial \varphi_{T}^{*}}{\partial \tau_{V}}(0, t^{*}),$$

$$\frac{t_{D}}{P} \frac{\partial T^{*}(\tau_{T}, t^{*})}{\partial t^{*}} = \frac{\partial^{2} T^{*}(\tau_{T}, t^{*})}{\partial \tau_{T}^{2}} + q_{T} \frac{\partial^{2} \varphi_{T}^{*}(\tau_{T}, t^{*})}{\partial \tau_{T}^{2}}$$

$$+q_{V} F(t^{*}) \gamma_{V}^{2} \left\{ \exp\left[-\frac{\tau_{T}}{\mu_{0}(t^{*})}\right] + 4\pi \varphi_{V}^{*}(\tau_{T}, t^{*}) \right\},$$

$$\frac{\partial T^{*}}{\partial \tau_{T}}(0, t^{*}) = 0.$$

As with the steady-state case, the visual equations can be solved independently, and,  $\gamma_V$  can be estimated from the optical properties of the Moon. The IR reflectance of the Moon is known to be small, so that  $\gamma_T$  is not very different from 1.00. Thus there are two unknown parameters,  $(kE_T)$  and  $\Gamma$ , which can be found by fitting solutions of the heat equation to time-varying temperature measurements of the lunar surface.

These equations were solved numerically for conditions appropriate to the Moon and Mercury by Hale and Hapke (2002). Figure 16.6 shows the best-fit theoretical solutions to thermal measurements of an area on the lunar equator. The values found by these authors were  $\Gamma = 43\,\mathrm{Jm^{-2}\,K^{-1}\,s^{-1/2}}$ , which is the same value obtained by Wesselink, and  $kE_T = 18.4\,\mathrm{J\,s^{-1}\,m^{-2}\,K^{-1}}$ . Figure 16.7 shows the calculated distribution of temperature with depth corresponding to these values at noon and just before dawn. Note that the diurnal temperature fluctuations are confined to a layer a few centimeters thick.