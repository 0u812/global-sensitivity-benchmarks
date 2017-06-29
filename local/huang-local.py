import tellurium as te

# convert to eliminate rate rules
model = te.loadAntimonyModel(te.sbmlToAntimony('huang-ferrell-96.xml'))
model.conservedMoietyAnalysis = True
print(model.steadyStateNamedArray())

# the output variable is PP_K (which stands for double phosphorylated MAPK)

# parameter 2: r1b_k2
