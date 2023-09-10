import os

baseFolder = os.path.dirname(os.getcwd())
iconsFolder = os.path.join(baseFolder, 'images', 'icons') 

f = CurrentFont()

for glyphName in f.selectedGlyphNames:    
    newDrawing()
    newPage(1000, 1000)
    translate(0, 200)
    drawGlyph(f[glyphName])
    iconPath = os.path.join(iconsFolder, f'{glyphName}.svg')
    saveImage(iconPath)

