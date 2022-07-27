import pytube
from pytube import YouTube
from downloads import download_high_res, download_low_res, download_audio
import os
import time
import sys


if __name__ == '__main__':

    def banner():
        print('')
        print('██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ')
        print('╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗')
        print(' ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝')
        print('  ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗')
        print('   ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║')
        print('   ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝')
    
    def home():
        print('')
        print('1. Download Video')
        print('2. Download Audio')
        print('3. Safepath festlegen')
        print('4. brings you back to this menu at everytime')
        print('')
    
    def video():
        print('')
        video_url = input('Link einfügen : ')
        print('')
        return video_url
    
    def res(): 
        print('') 
        video_res = input('Resolution wählen (H)igh (L)ow: ')
        print('')
        return video_res

    def path():
        print('')
        path = input("Pfad auswählen oder s fuer standard : ")
        print('')
        return path

    def mainmenu():
        mainmenu_input = input("Drücke 3 um zum Hauptmenü zurück zu kehren.")
        if mainmenu_input == '3':
            main()
        
    def animate(done):
        while done == 'false':
            sys.stdout.write('\rDownloading |')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading /')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading -')
            time.sleep(0.1)
            sys.stdout.write('\rDownloading \\')
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    def set_path():
        
        print('')
        standardpath = input('Pfad auswählen : ')
        if standardpath == '4':
            main()
        else:
            with open('path.txt', 'r+') as f:
                f.truncate()
            with open('path.txt', 'a+') as f:
                f.write(standardpath)
            print('Path set')
            main()

        
        
    def read_path():
        with open('path.txt') as f:
            lines = f.read()
        return lines


        
# Program ?S?tart

    def main():
        banner()
        home()
    
        eingeben = input()
        if eingeben==None:
            main()
        
        elif eingeben=='1':
            video_link = video()
            if video_link == '4':
                main()
            if video_link is not None:
                resolution = res()
                if resolution == '4':
                    main()
                if resolution == 'H' or resolution == 'h':
                    print("Hohe Qualität")
                    safepath = path()
                    if safepath =='4':
                        main()
                    if safepath =='s' or safepath=='S':
                        stanpath = read_path()
                        download_high_res(video_link, stanpath)
                        print('Download complete')
                        print('')
                        main()
                    else: 
                        download_high_res(video_link, safepath)
                        print('Download complete')
                        print('')
                        main()

                elif resolution == 'L' or resolution == 'l':
                    print("Niedrige Qualität")
                    safepath = path()
                    if safepath =='4':
                        main()
                    if safepath =='s' or safepath=='S':
                        stanpath = read_path()
                        download_low_res(video_link, stanpath)
                        print('Download complete')
                        print('')
                        main()
                    else:   
                        download_low_res(video_link, safepath)
                        print('Download complete')
                        print('')
                        main()
        elif eingeben=='2':
            video_link = video()
            if video_link == '4':
                main()
            if video_link is not None:
                safepath = path()
                if safepath == '4':
                    main()
                if safepath =='s' or safepath=='S':
                        stanpath = read_path()
                        download_audio(video_link, stanpath)
                        print('Download complete')
                        print('')
                        main()
                else:   
                    download_audio(video_link, safepath)
                    print('Download complete')
                    print('')
                    main()
                  
        elif eingeben=='3':
            set_path()
           
        elif eingeben=='4':
            main()


    main()