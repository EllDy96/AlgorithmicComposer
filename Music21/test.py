import os
import glob 
print(glob.glob("C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/*.abc"))
'''
os.path.normcase(path)
Normalize the case of a pathname. On Windows, convert all characters in the pathname to lowercase, and also convert forward slashes to backward slashes. 
On other operating systems, return the path unchanged. Raise a TypeError if the type of path is not str or bytes (directly or indirectly through the os.PathLike interface).
'''
#print(os.listdir("C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned"))
#print(os.path.join('/bull'))
#print(os.path.realpath('ashover.abc'))
originalPatch="C:/Users/david/Documents/Il mio mondo/Corsi Università/Tesi Triennale/nottingham-dataset-master/ABC_cleaned"
#for d in os.listdir(originalPatch):



for x in os.listdir(originalPatch):
    file_path= os.path.abspath(x)
    print(file_path)



