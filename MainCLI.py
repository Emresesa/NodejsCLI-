
from __future__ import print_function
import sys
import os
import ExtractorCli

wrongcom="Please enter a proper command, for help enter 'piton e14000 -h'"


#Sadece Script'in adi yazildiginda script taniminin yazilmasi
if len(sys.argv) is 3 and sys.argv[1]=="piton" and sys.argv[2]=="e14000":

    print ("piton e14000 is CLI for installing and handling Nodejs packages")
#fonsiyonlarin tanimi
elif len(sys.argv) is 4 and sys.argv[1]=="piton" and sys.argv[2]=="e14000":

    #sistemden username i alir
    user= ExtractorCli.nuser
    #!!!Dosyalarin cikartilacagi path !!!!
    DPath="/home/%s/Belgeler/aaa"%user
#install fonksiyonu
    def ins():
        if sys.argv[3]=='-i':
            os.system("wget https://github.com/nodejs/node/archive/master.zip")
            os.system("unzip *.zip")
            os.system("cd node-master && sudo python2 ./configure && make && sudo make install")
            UPath = ExtractorCli.usbway
            dirp= ExtractorCli.dirpaths(UPath)
            ExtractorCli.extractor(dirp)
            print("It's installed")
        return
#nodejs paketlerinin guncellenmesi icin update fonksiyonu
    def upt():
        if sys.argv[3]=='-u':
            os.system("sudo npm cache clean -f && sudo npm install -g n && sudo n stable")

            print("It's Updated")
        return
#script in komutlarini gostermek icin help fonksiyonu
    def hlp():
        if sys.argv[3]=='-h':
            helper=["-i : for installing nodejs packages",
                    "-u : for updating nodejs packages",
                    "-r : for removing nodejs packages",
                    "-h : to see this info again"]
            print(*helper,sep='\n')
        return
#zip dosyalarini ve nodejs paketlerini remove eden fonksiyon
    def rmv():
        if sys.argv[3]=='-r':
            os.system("cd node-master && sudo make uninstall")
            os.system("rm -rf node-master && rm *.zip")
            os.system("rm %s/*"%DPath)
            print("Removed")
        return
#fonksiyonlari switch eden fonksiyon
    def switcher(third_arg):
        optlist={'-u':upt(),'-h':hlp(),'-r':rmv(),'-i':ins()}
        return optlist.get(third_arg,wrongcom)

#komutlari calistiran if
    if sys.argv[1]=="piton" and sys.argv[2]=="e14000":
            if switcher(sys.argv[3]) is not None:
                print (switcher(sys.argv[3]))

else :
    print(wrongcom)
#yanlis komut verildiginde parse edilen yazi
