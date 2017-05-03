import zipfile
import os

#Klasorlerin pathlerini cikaran fonksiyon
def dirpaths(way):
    dirpaths=[]
    for(dirpath,dirnames,filenames) in os.walk(way):
        dirpaths.append(dirpath)
    return dirpaths
#Klasorlerdeki dosyalari kopyalayan fonksiyon
def extractor(patharr):
    for y,x in enumerate(patharr):
        filearr=os.listdir(dirP[y])
        for i,x in enumerate(filearr):
            if filearr[i].endswith('.zip'):
                filename=dirP[y]+"/"+filearr[i]
                zip_ref = zipfile.ZipFile(filename, 'r')
                zip_ref.extractall(destway)
                zip_ref.close()
#sistemden username'i almak

nuser=os.path.expanduser('~')
nuser=os.path.split(nuser)[-1]

#destination ve start pathleri
usbway="/run/media/%s"%(nuser)
#kopyalanacak klasorun check edilmesi yoksa acilmasi
destway= "/home/%s/Belgeler/USBfiles"%nuser

#path in cikartilmasi

#zipleri extract eden fonsiyonun cagirilmasi
