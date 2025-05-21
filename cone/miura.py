#ALGORITHM
#Algorithm 1 (Conical origami design: Four-fold line pattern).

import miurafunct

#Design variables: m; a0; lr0 and h2;
#Number of segments:n
m, n = 1, 1 # m = # -->, n == # ^^
alpha_0, lr0, theta_2 = 0.523598776, 8, 0.174532925 #30, 10 degrees
r1, r2, h1 = 100, 20, 50
cur_y = 0

#Calculate r₀; μ; θ₁
theta_c = miurafunct.eqt1_theta_c(r1, r2, h1) #just there
mu = miurafunct.eqt2_mu(theta_c)
R0 = miurafunct.eqt3_R0(r1, theta_c)
theta_1 = miurafunct.eqt4_theta1(mu)

#Calculate the following A₀; b₀; a₀; Φ₀
'''Ensure: The fold angles and fold lengths of the 
Unit cell of ith segment %Unit cell dimensions'''
A_i = miurafunct.eqt5_A0(R0, theta_1) #A_0
b_i = miurafunct.eqt6_b0(A_i, lr0) #b_0
a_i = miurafunct.eqt7_a0(A_i, b_i) #a_i
phi_0 = miurafunct.eqt8_phi0(theta_1, alpha_0)

#iterate
for i in range(n): #from 0-(n-1)
    #eqt 13-18: φᵢ, rᵢ, αᵢ, βᵢ, γᵢ, δᵢ
    phi_i, r_i, alpha_i, beta_i, gamma_i, delta_i = miurafunct.calculate_fold_angle(i, m, mu, theta_2, phi_0)
    #19-23: Aᵢ₊₁, cᵢ, dᵢ, aᵢ, bᵢ
    A_i, b_i, a_i, c_i, d_i = miurafunct.calculate_fold_length(i, r_i, A_i, b_i, a_i, theta_2, alpha_i, gamma_i, delta_i, beta_i)
    
    print(f"i: {i}, phi_i: {phi_i}, r_i: {r_i}, alpha_i: {alpha_i}, beta_i: {beta_i}, gamma_i: {gamma_i}, delta_i: {delta_i}")
    print(f"A_i: {A_i}, b_i: {b_i}, a_i: {a_i}, c_i: {c_i}, d_i: {d_i}")
