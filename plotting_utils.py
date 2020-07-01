import xarray as xr
import matplotlib as mpl 
import matplotlib.path as mpath
from matplotlib import pyplot as plt 
import cartopy.crs as ccrs
import cartopy.feature as cfeature
mpl.rcParams['font.size'] = 12

def plot_NH_differences(case_array1, case_array2, times, variable_list):
    
    grid = xr.open_dataset('/glade/work/vcooper/grid_ref/sithick_SImon_CESM2_piControl_r1i1p1f1_gn_110001-120012.nc')
    
    case_array1.TLAT[:]=grid.lat
    case_array1.TLON[:]=grid.lon
    case_array2.TLAT[:]=grid.lat
    case_array2.TLON[:]=grid.lon
    
    for var in variable_list:
        fig = plt.figure(figsize=(18,8))
        ax1 = plt.subplot(2,3,1,projection=ccrs.NorthPolarStereo())
        ax1.coastlines()
        ax1.set_extent([-180, 180, 55, 90], ccrs.PlateCarree())
        case_array1[var][times[0]*12-1,:,:].plot.pcolormesh('TLON', 'TLAT', ax=ax1, transform=ccrs.PlateCarree())
        
        ax2 = plt.subplot(2,3,2,projection=ccrs.NorthPolarStereo())
        ax2.coastlines()
        ax2.set_extent([-180, 180, 55, 90], crs=ccrs.PlateCarree())
        case_array2[var][times[1]*12-1,:,:].plot.pcolormesh('TLON', 'TLAT', ax=ax2, transform=ccrs.PlateCarree())

        ax3 = plt.subplot(2,3,3,projection=ccrs.NorthPolarStereo())
        ax3.coastlines()
        ax3.set_extent([-180, 180, 55, 90], crs=ccrs.PlateCarree())
        diff = case_array2[var][times[1]*12-1,:,:] - case_array1[var][times[0]*12-1,:,:]

        diff.plot.pcolormesh('TLON', 'TLAT', ax=ax3, transform=ccrs.PlateCarree(), cmap = 'RdBu_r')
        ax3.set_title('$\Delta$'+var)
        
        plt.show()
        plt.tight_layout()
        

def plot_SH_differences(case_array1, case_array2, times, variable_list):
    
    grid = xr.open_dataset('/glade/work/vcooper/grid_ref/sithick_SImon_CESM2_piControl_r1i1p1f1_gn_110001-120012.nc')
    
    case_array1.TLAT[:]=grid.lat
    case_array1.TLON[:]=grid.lon
    case_array2.TLAT[:]=grid.lat
    case_array2.TLON[:]=grid.lon
    
    for var in variable_list:
        fig = plt.figure(figsize=(18,8))
        ax1 = plt.subplot(2,3,1,projection=ccrs.SouthPolarStereo())
        ax1.coastlines()
        ax1.set_extent([-180, 180, -90, -55], ccrs.PlateCarree())
        case_array1[var][(times[0]*12-1),:,:].where(case_array1.TLAT < -30).plot.pcolormesh('TLON', 'TLAT', ax=ax1, transform=ccrs.PlateCarree())
        
        ax2 = plt.subplot(2,3,2,projection=ccrs.SouthPolarStereo())
        ax2.coastlines()
        ax2.set_extent([-180, 180, -90, -55], crs=ccrs.PlateCarree())
        case_array2[var][(times[1]*12-1),:,:].where(case_array2.TLAT < -30).plot.pcolormesh('TLON', 'TLAT', ax=ax2, transform=ccrs.PlateCarree())

        ax3 = plt.subplot(2,3,3,projection=ccrs.SouthPolarStereo())
        ax3.coastlines()
        ax3.set_extent([-180, 180, -90, -55], crs=ccrs.PlateCarree())
        diff = case_array2[var][(times[1]*12-1),:,:].where(case_array1.TLAT < -30) - case_array1[var][(times[0]*12-1),:,:].where(case_array1.TLAT < -30)

        diff.plot.pcolormesh('TLON', 'TLAT', ax=ax3, transform=ccrs.PlateCarree(), cmap = 'RdBu_r')
        ax3.set_title('$\Delta$'+var)
        
        plt.show()
        plt.tight_layout()