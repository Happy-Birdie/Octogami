#EQUATIONS FROM PAPER

import math

# eqt 1: θ_c cone half-angle
def eqt1_theta_c(r1, r2, h1):
    return math.atan((r1 - r2) / h1)

# eqt 2: μ strip center-angle
def eqt2_mu(theta_c):
    return 2 * math.pi * math.sin(theta_c)

# eqt 3: r₀ curvature radius
def eqt3_R0(r0, theta_c):
    return r0 / math.sin(theta_c)

# eqt 4: θ₁ unit segment angle
def eqt4_theta1(mu):
    return 1 / mu

# eqt 5: a₀ segment length
def eqt5_A0(R0, theta1):
    return math.sqrt((2) * (R0 * R0) * math.sqrt(1 - math.cos(theta1)))

# eqt 6: b₀ segment width
def eqt6_b0(A0, lr0):
    return A0 / (1 + lr0)

# eqt 7: a₀ segment width from a₀ and b₀
def eqt7_a0(A0, b0):
    return A0 - b0

# eqt 8: Φ₀ internal angle
def eqt8_phi0(theta1, alpha0):
    return 0.5 * (math.pi - theta1) - alpha0

# eqt 9: β₀ bending angle
def eqt9_beta0(theta1, phi0):
    return (0.5 * math.pi - theta1) - phi0

# eqt 10: γ₀ intermediate angle
def eqt10_gamma0(alpha0, theta1, theta2):
    return alpha0 + theta1 - theta2

# eqt 11: δ₀ offset angle
def eqt11_delta0(beta0, theta2):
    return beta0 - theta2

# eqt 12: closure closure condition
def eqt12_closure(alpha, beta0, mu, m):
    return 2 * m * (alpha - beta0) + mu

#eqt 13: φᵢ (phi_i)
def eq13_phi_i(phi_0, i, theta_2):
    return phi_0 + i * theta_2

#eqt 14: αᵢ (alpha_i)
def eq14_alpha_i(i, m, mu, theta_2, phi_0):
    return 0.5 * (math.pi - mu / m) - i * theta_2 - phi_0

#eqt 15: βᵢ (beta_i)
def eq15_beta_i(i, m, theta_2, phi_0):
    return (math.pi / 2 - math.pi / m) - i * theta_2 - phi_0

#eqt 16: γᵢ (gamma_i)
def eq16_gamma_i(i, m, mu, theta_2, phi_0): ##CHECK LATER
    return 0.5 * (math.pi + mu / m) - (i + 1) * theta_2 - phi_0

#eqt 17: δᵢ (delta_i)
def eq17_delta_i(i, m, theta_2, phi_0):
    return (math.pi / 2 - math.pi / m) - (i + 1) * theta_2 - phi_0

#eqt 18: rᵢ (radius ratio)
def eq18_r_i(phi_i, theta_2): #R_i1, R_i
    return math.sin(phi_i) / math.sin(phi_i + theta_2)

#eqt 19: Aᵢ₊₁ (scaled polygon area)
def eq19_A_i1(r_i, A_i):
    return r_i * A_i

#eqt 20: cᵢ (distance between polygon centers)
def eq20_c_i(A_i, r_i, alpha_i, gamma_i):
    numerator = A_i * (1 - r_i**2)
    denominator = 2 * (math.cos(alpha_i) - r_i * math.cos(gamma_i))
    return numerator / denominator

#eqt 21: dᵢ (fold line length)
def eq21_d_i(b_i, theta_2, r_i, a_i, c_i, alpha_i, gamma_i, delta_i, beta_i):
    numerator = (
        b_i * math.cos(theta_2) * (r_i - math.cos(theta_2)) +
        a_i * (r_i * math.cos(theta_2) - 1) +
        c_i * (math.cos(alpha_i) - math.cos(gamma_i) * math.cos(theta_2))
    )
    denominator = math.cos(beta_i) - math.cos(delta_i) * math.cos(theta_2)
    return numerator / denominator

#eqt 22: aᵢ₊₁ (fold projection length)
def eq22_a_i1(b_i, theta_2, r_i, a_i, c_i, delta_i, beta_i, alpha_i, gamma_i):
    numerator = (
        b_i * math.cos(theta_2) * (r_i * math.cos(delta_i) - math.cos(beta_i)) +
        a_i * (r_i * math.cos(theta_2) * math.cos(delta_i) - math.cos(delta_i)) +
        c_i * (math.cos(alpha_i) * math.cos(theta_2) - math.cos(gamma_i) * math.cos(beta_i))
    )
    denominator = math.cos(theta_2) * math.cos(delta_i) - math.cos(beta_i)
    return numerator / denominator

#eqt 23: bᵢ₊₁ (fold side length)
def eq23_b_i1(A_i1, a_i1):
    return A_i1 - a_i1

#eqt 24: lᵣᵢ₊₁ (length ratio of folds)
def eq24_lri1(a_i1, b_i1):
    return a_i1 / b_i1

#eqt 25a: R_cᵢ (circumradius of fold polygon i)
def eq25a_Rc_i(A_i, lr_i, beta_i, m):
    numerator = A_i**2 * (1 + lr_i**2 - 2 * lr_i * math.cos(math.pi - 2 * beta_i))
    denominator = 2 * (1 + lr_i)**2 * (1 - math.cos(2 * math.pi / m))
    return math.sqrt(numerator / denominator)

#eqt 25b: R_cᵢ₊₁ (circumradius of fold polygon i+1)
def eq25b_Rc_i1(A_i1, lr_i1, delta_i, m):
    numerator = A_i1**2 * (1 + lr_i1**2 - 2 * lr_i1 * math.cos(math.pi - 2 * delta_i))
    denominator = 2 * (1 + lr_i1)**2 * (1 - math.cos(2 * math.pi / m))
    return math.sqrt(numerator / denominator)

#eqt 26: θᵢ (angle between folded polygons)
def eq26_theta_i(Rc_i, Rc_i1, c_i):
    numerator = Rc_i**2 + Rc_i1**2 - c_i**2
    denominator = 2 * Rc_i * Rc_i1
    return math.acos(numerator / denominator)

def calculate_fold_angle(i, m, mu, theta_2, phi_0):
    #eqt 13-18: φᵢ, rᵢ, αᵢ, βᵢ, γᵢ, δᵢ
    ##eqt 13: φᵢ (phi_i)
    phi_i = eq13_phi_i(phi_0, i, theta_2)
    r_i = eq18_r_i(phi_i, theta_2)
    #fold angles
    alpha_i = eq14_alpha_i(i, m, mu, theta_2, phi_0)
    beta_i = eq15_beta_i(i, m, theta_2, phi_0)
    gamma_i = eq16_gamma_i(i, m, mu, theta_2, phi_0)
    delta_i = eq17_delta_i(i, m, theta_2, phi_0)
    return phi_i, r_i, alpha_i, beta_i, gamma_i, delta_i

def calculate_fold_length(i, r_i, A_i, b_i, a_i, theta_2, alpha_i, gamma_i, delta_i, beta_i):
    #eqt 19: Aᵢ₊₁
    A_i = eq19_A_i1(r_i, A_i)

    #eqt 20, 21: cᵢ & dᵢ
    c_i = eq20_c_i(A_i, r_i, alpha_i, gamma_i)
    d_i = eq21_d_i(b_i, theta_2, r_i, a_i, c_i, alpha_i, gamma_i, delta_i, beta_i)
    #eqt 22, 23: aᵢ₊₁ & bᵢ₊₁
    a_i = eq22_a_i1(b_i, theta_2, r_i, a_i, c_i, delta_i, beta_i, alpha_i, gamma_i)
    b_i = eq23_b_i1(A_i, a_i) #A_i1, a_i1
    return A_i, b_i, a_i, c_i, d_i

def calculate_pts(a_i, b_i, c_i, d_i, alpha_i, beta_i, gamma_i, delta_i):
    '''
    0,0 --> 

    \__\ 
    /__/
    '''