from paraview.simple import *
test_tec = TecplotReader(FileNames=['/Users/yimingzhang/Downloads/IRM_SantaFe_2019/Example1-MERRILL_meshing/iron_30nm_mult.tec'])

# Apply Calculator for M
calculator_M = Calculator(Input=test_tec, Function='Mx*iHat + My*jHat + Mz*kHat', ResultArrayName='M')
calculator_M.UpdatePipeline()

# Apply Gradient for Vorticity
gradient = Gradient(Input=calculator_M, ComputeVorticity=True, VorticityArrayName='V')
gradient.UpdatePipeline()

# Apply Calculator for H
calculator_H = Calculator(Input=gradient)
calculator_H.Function = 'dot(M,V)'
calculator_H.ResultArrayName = 'H'
calculator_H.UpdatePipeline()

# Apply Glyph
glyph = Glyph(Input=calculator_H, GlyphType="Arrow", ScaleArray=False)
glyph.OrientationArray = ['POINTS', 'M']
# glyph.ScaleFactor = 1.0
glyph.UpdatePipeline()

# Show the result
Show(glyph)
Render()