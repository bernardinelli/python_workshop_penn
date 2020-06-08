from astropy.cosmology import FlatwCDM

def distance(z,om=0.3,w=-1):
    #this function takes a redshift and two parameters (om,w)
    cosmo = FlatwCDM(Om0=om, w0=w)
    return cosmom.distmod(z)
