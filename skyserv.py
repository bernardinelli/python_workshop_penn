import skimage
def getImStamp(ra,dec,width=300,height=300):
    url="http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?ra="+str(ra)
    url+="&dec="+str(dec)+"&width="+str(width)
    url+="&height="+str(height)
    img=skimage.io.imread(url)
    return img
