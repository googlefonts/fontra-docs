import os

baseFolder    = os.path.dirname(os.getcwd())
iconsFolder   = os.path.join(baseFolder, 'images', 'icons') 
iconsFontPath = '/Users/gferreira/hipertipo/tools/fontra/icons/fontra-icons.ufo'

f = OpenFont(iconsFontPath, showInterface=False)

skipGlyphs = ['_geartooth']

for glyphName in f.glyphOrder:
    if not len(f[glyphName]) or glyphName in skipGlyphs:
        continue
    newDrawing()
    print(glyphName)
    newPage(1000, 1000)
    translate(0, 200)
    drawGlyph(f[glyphName])
    iconPath = os.path.join(iconsFolder, f'{glyphName}.svg')
    saveImage(iconPath)

