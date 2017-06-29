import tellurium as te

# convert to eliminate rate rules
model = te.loadAntimonyModel(te.sbmlToAntimony('huang-ferrell-96.xml'))
model.conservedMoietyAnalysis = True
print(model.steadyStateNamedArray())
