import tellurium as te

# convert to eliminate rate rules
model = te.loadAntimonyModel(te.sbmlToAntimony('huang-ferrell-96.xml'))
model.conservedMoietyAnalysis = True
print(model.steadyStateNamedArray())

# the output variable is PP_K (which represents doubly phosphorylated MAPK)

# parameter 2: r1b_k2 (original: MAPKKK activation.k1)
fig1a_local = model.getuCC('K_PP_norm', 'r1b_k2')
print('Figure 1A: local value = {}'.format(fig1a_local))

# parameter 5: r8a_a8 (original: binding MAPK—Pase and P-MAPK.k1)
fig1b_local = model.getCC('PP_K', 'r8a_a8')
print('Figure 1B: local value = {}'.format(fig1b_local))

# parameter 7: r10a_a10 (original: binding MAPK—Pase and PP—MAPK.k1)
fig1c_local = model.getCC('PP_K', 'r10a_a10')
print('Figure 1C: local value = {}'.format(fig1c_local))
