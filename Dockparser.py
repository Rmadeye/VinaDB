# Data required: filename, date, ligandname, Estimated Free Energy of Binding, Number of non-hydrogen atoms in ligand, RMSD TABLE
import re
import pandas as pd
from pathlib import Path

#r"MODEL (\d+)\s+REMARK VINA RESULT:\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)")
#sys.path.append('/home/rafmad/Dokowania_Róża_Luty/Vinaparser')

#logfile='/home/rafmad/Dokowania_Róża_Luty/Wyniki/hypo.pdbqt'

def parse(logfile):
#    print(logfile)
    #Patterns for parsing vina txt files
    patternM=re.compile(r"MODEL")
    patternV=re.compile(r"REMARK VINA RESULT")
    PatternVDS=re.compile(r"viewdock state:")
    #Tables for data storage
    names=[]
    energy_values = []
    rmsddist=[]
    rmsd=[]
    status=[]

    with open(logfile,'rt') as in_file:
        for line in in_file:
            if patternV.search(line) !=None:
                data=re.findall(r"\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)",line)
                data=data[0]
                energy_values.append(float(data[0]))
                rmsd.append(float(data[1]))
                rmsddist.append(float(data[2]))
            if PatternVDS.search(line) != None:
                VDS=re.findall(r"[DPV]",line)
                status.append(VDS)
    #DataFrameCreation
    energy_values=pd.DataFrame(energy_values)
    rmsddist=pd.DataFrame(rmsddist)
    rmsd=pd.DataFrame(rmsd)
    logfile=Path(logfile).name
    status=pd.DataFrame(status)
    names.append(logfile)
    names=pd.DataFrame(names)
    #MainDF
    maindf=pd.concat([names,energy_values,rmsd,rmsddist, status], axis=1)
    maindf.fillna(method='ffill', inplace=True)
    maindf.columns=['Filename','Energy_value','RMSDdist','RMSDBestMode','Status']
    indexNames=maindf[maindf['Status']=='D'].index
    maindf.drop(indexNames, inplace=True)
    print(maindf)
    return(maindf)