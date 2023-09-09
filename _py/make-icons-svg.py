f = CurrentFont()
for glyphName in f.selectedGlyphNames:    
    newPage(1000, 1000)
    translate(0, 200)
    drawGlyph(f[glyphName])
    

