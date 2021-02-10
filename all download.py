from colorama import Back, Fore, Style, deinit
import pytube
import os
import sys
import wget
import time
import sys
os.system("cls")

def pytube_1():
	print(f"{Fore.WHITE}Veillez choisir une option: ex: 1-3")
	print("")
	print(f"{Fore.RED}1) Telechargez une video.")
	print(f"{Fore.YELLOW}2)Telechargez une liste de video.")
	print(f"{Fore.GREEN}3)Telechargez plusieur video à partir d'une fichier text.")
	option = int(input("==> "))
	if option == 1:
		try:
		    os.system("cls")
		    url_1 = input("Ton url: ")
		    os.system("cls")
		    print(f"{Style.RESET_ALL}Veillez patientez le telechargement à demaré...")
		    youtube = pytube.YouTube(url_1)
		    video = youtube.streams.first()
		    video.download()
		    print(f"sauvegarder: {os.getcwd()}")
		except:
		    print(f"{Fore.RED}error Veillez recommencé")    
		finally:
			pass



	if option == 2:
	    os.system("cls")
	    urln = int(input("le nombre de url: "))
	    liste = [input("url: ") for ch in range(urln)]
	    os.system("cls")
	    for urll in liste:
	    	
	    	youtube = pytube.YouTube(urll)
	    	video = youtube.streams.first()
	    	video.download()
	    	
	    	print("un nouveau vient de terminer")
	    print(f"sauvegarder: {os.getcwd()}")


	    


	if option == 3:
		os.system("cls")
		file = input("le directory du fichier texte: ")
		os.system("cls")
		try:
			with open(file, 'r') as test:
				for i in test:
					try:
					    youtube = pytube.YouTube(i)
					    video = youtube.streams.first()
					    video.download()
					    print("un nouveau vient de terminer")
					    print(f"sauvegarder: {os.getcwd()}")
					except:
						print(f"{Fore.RED}echec du telechargement")
		except FileNotFoundError:
			print("veillez choisir un fichier")
			sys.exit("bye")

def wget_1():
	url = input("Ton url: ")
	os.system("cls")
	print("Le telechargement à demaré...")
	#url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
	save = f"sauvegarder: {os.getcwd()}"
	wget.download(url)
	print(f"\n {save}")




while 1:
	os.system("cls")

	print(f"""##########################################################################################################################
		     #   Paypal: cheikhoudieng032@gmail.com                         #
		     #   Coinbase: cheikhoudieng032@gmail.com                       #
		     #   Bitcoin: 3PzoUhhHdHsDrbZW4RrGurpCME67Ear5v9                #
		     #   Ethereum: 0xA184436C064F41c97442e89c6061E9475eF60528       #
		     ################################################################

		""")   
	print(f"""                                        AllDownload




    {Fore.GREEN}1) {Fore.RED}Youtube down"
    {Fore.GREEN}2) {Fore.RED}File down {Style.RESET_ALL}""")
	try:
	    allin = int(input("==> "))
	    if allin == 1:
	    	os.system("cls")
	    	pytube_1()
	    if allin == 2:
	    	os.system("cls")
	    	wget_1()
	    else:
	    	print("veillez choisir 1-2 ")
	    	time.sleep(1)
	    	continue
	except (ValueError):
		print("veillez choisir 1-2")
		time.sleep(1)
		continue
	except  KeyboardInterrupt:
		print("bye")
		break
	except EOFError:
		print("pour quitez tapez 'Control + C'")
		time.sleep(1)
		