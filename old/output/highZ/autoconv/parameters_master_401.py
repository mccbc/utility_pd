#===============================================
#RESOLUTION KEYWORDS
#===============================================
oref = 0 #over refine factor - should typically be set to 0
n_ref = 32 #when n_particles > n_ref, octree refines further
zoom_box_len = 100 #kpc; so the box will be +/- zoom_box_len from the center
bbox_lim = 1.e5 #kpc - this is the initial bounding box of the grid (+/- bbox_lim)
               #This *must* encompass all of the particles in the
               #simulation. 

#===============================================
#PARALLELIZATION
#===============================================

n_processes = 16 #number of pool processes to run
n_MPI_processes = 1 #number oF MPI processes to run

#===============================================
#RT INFORMATION
#===============================================
n_photons_initial = 1.e5
n_photons_imaging = 1.e5
n_photons_raytracing_sources = 1.e5
n_photons_raytracing_dust = 1.e5

FORCE_RANDOM_SEED = False
seed = -12345 #has to be an int, and negative.

#===============================================
#DUST INFORMATION 
#===============================================
dustdir = '/home/cmcclellan1010/hyperion-dust-0.1.0/dust_files/' #location of your dust files
dustfile = 'd03_3.1_6.0_A.hdf5'
PAH = True
dust_grid_type = 'dtm' #needs to be in ['dtm','rr','manual']
dusttometals_ratio = 0.4
enforce_energy_range = False #False is the default;  ensures energy conservation

SUBLIMATION = False #do we automatically kill dust grains above the
                    #sublimation temperature; right now is set to fast
                    #mode
SUBLIMATION_TEMPERATURE = 1600. #K -- meaningliess if SUBLIMATION == False

#===============================================
#HYDRO CODE UNITS
#===============================================
unit_mass = 1.e10 #msun
unit_length = 1. #kpc
unit_age = 1. #Gyr
unit_velocity = 1.e5 #cm/s

#===============================================
#STELLAR SEDS INFO
#===============================================
FORCE_BINNING = True #force SED binning
COSMOFLAG = True  #is this a cosmological simulation?

imf_type = 2 #FSPS imf types; 0 = salpeter, 1 = chabrier; 2 = kroupa; 3 and 4 (vandokkum/dave) not currently supported
pagb = 0 #weight given to post agb stars# 1 is the default
add_neb_emission = False #add nebular line emission from Cloudy Lookup tables (dev. by Nell Byler)
gas_logu = -2 #gas ionization parameter for HII regions; only relevant
              #if add_neb_emission = True default = -2
FORCE_gas_logz = False #if set, then we force the gas_logz of HII
                       #regions to be gas_logz (next parameter); else, it is taken to be the star particles metallicity.  default is False
gas_logz = 0 #units of log(Z/Z_sun); metallicity of the HII region
             #metallicity; only relevant if add_neb_emission = True;
             #default is 0

add_agb_dust_model=False #add circumstellar AGB dust model (100%); Villaume, Conroy & Jonson 2015

CF_on = False #if set to true, then we enable the Charlot & Fall birthcloud models 
birth_cloud_clearing_age = 0.01 #Gyr - stars with age <
                                #birth_cloud_clearing_age have
                                #charlot&fall birthclouds meaningless
                                #of CF_on  == False

Z_init = 0 #force a metallicity increase in the newstar particles.
           #This is useful for idealized galaxies.  The units for this
           #are absolute (so enter 0.02 for solar).  Setting to 0
           #means you use the stellar metallicities as they come in
           #the simulation (more likely appropriate for cosmological
           #runs)

#Idealized Galaxy SED Parameters
disk_stars_age = 8 #Gyr ;meaningless if COSMOFLAG = True; note, if this is <= 7, then these will live in birth clouds
bulge_stars_age = 8 #Gyr ; meaningless if COSMOFLAG = True; note, if this is <= 7, then these will live in birth clouds
disk_stars_metals = 19 #in fsps metallicity units
bulge_stars_metals = 19 #in fsps metallicity units



#bins for binning the stellar ages and metallicities for SED
#assignments in cases of many (where many ==
#>N_METALLICITY_BINS*N_STELLAR_AGE_BINS) stars; this is necessary for
#reduction of memory load; see manual for details.

N_STELLAR_AGE_BINS = 100


metallicity_legend= "/home/cmcclellan1010/fsps/ISOCHRONES/Padova/Padova2007/zlegend.dat"



#===============================================
#IMAGES AND SED
#===============================================

NTHETA = 1
NPHI = 1
SED = True

SED_MONOCHROMATIC = False
FIX_SED_MONOCHROMATIC_WAVELENGTHS = False #if set, then we only use
                                         #nlam wavelengths in the
                                         #range between min_lam and
                                         #max_lam
SED_MONOCHROMATIC_min_lam = 0.3 #micron
SED_MONOCHROMATIC_max_lam = 0.4 #micron
SED_MONOCHROMATIC_nlam = 100 




IMAGING = True
# filter_file = '/home/cmcclellan1010/powderday/pdfilters.dat'
filter_file = '/home/cmcclellan1010/powderday/STIS_clear_8.dat'
npix_x = 512
npix_y = 512

#experimental and under development - not advised for use
IMAGING_TRANSMISSION_FILTER = True
filter_list = ['filters/STIS_clear_8.filter']
TRANSMISSION_FILTER_REDSHIFT = 3.1

#===============================================
#GRID INFORMATION  
#===============================================

#center cell position #currently deprecated, though will be used for zooming later
MANUAL_CENTERING = True


#===============================================
#OTHER INFORMATION
#===============================================

solar = 0.013

#===============================================
#DEBUGGING
#===============================================

SOURCES_IN_CENTER = False
STELLAR_SED_WRITE = True
SKIP_RT = False #skip radiative transfer (i.e. just read in the grids and maybe write some diagnostics)
SUPER_SIMPLE_SED = False #just generate 1 oct of 100 pc on a side,
                         #centered on [0,0,0].  sources are added at
                         #random positions.
SKIP_GRID_READIN = False

CONSTANT_DUST_GRID = False #if set, then we don't create a dust grid by
                          #smoothing, but rather just make it the same
                          #size as the octree with a constant value of
                          #4e-20
                          
N_MASS_BINS = 1 #this is really just a place holder that exists in
                #some loops to be able to insert some code downstream
                #for spatially varying IMFs.  right now for speed best
                #to set to 1 as it doesn't actually do anything.

FORCE_STELLAR_AGES = False
FORCE_STELLAR_AGES_VALUE = 0.05# Gyr

FORCE_STELLAR_METALLICITIES = False
FORCE_STELLAR_METALLICITIES_VALUE = 0.012 #absolute values (so 0.013 ~ solar)
