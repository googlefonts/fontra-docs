import os, glob, shutil

# update these to match your system
fontraFolder = '/Users/gferreira/hipertipo/tools/fontra'
fontraDocsIconsFolder = '/Users/gferreira/hipertipo/tools/fontra-docs/images/icons'

iconsFolder  = os.path.join(fontraFolder, 'src/fontra/client/images')
tablerFolder = os.path.join(fontraFolder, 'src/fontra/client/tabler-icons')

assert os.path.exists(iconsFolder)
assert os.path.exists(tablerFolder)

iconsFontra = glob.glob(f'{iconsFolder}/*.svg')
iconsTabler = glob.glob(f'{tablerFolder}/*.svg')

iconsAll = iconsFontra + iconsTabler

for svgPath in iconsAll:
    dstPath = os.path.join(fontraDocsIconsFolder, os.path.split(svgPath)[-1])
    shutil.copyfile(svgPath, dstPath)
