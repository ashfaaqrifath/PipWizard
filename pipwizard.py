import os
import sys
import subprocess
import importlib
import pkgutil

if pkgutil.find_loader("colorama") is None:
    subprocess.check_call(["pip", "install", "colorama"])
    #installs colorama automatically
else:
    pass
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#clears terminal
os.system("cls")
print('''
 █▀▀█ ▀█▀ █▀▀█  █   █ ▀█▀  █▀▀▀█  █▀▀█  █▀▀█  █▀▀▄ 
 █▄▄█  █  █▄▄█  █ █ █  █   ▄▄▄▀▀  █▄▄█  █▄▄▀  █  █ 
 █    ▄█▄ █     █▄▀▄█ ▄█▄  █▄▄▄█  █  █  █  █  █▄▄▀ v1.5.1''')
print(Fore.YELLOW + "              PYTHON PACKAGE MANAGER")
print('''
 (1) Install package
 (2) Batch install from requirements file
 (3) Update package
 (4) Uninstall package
 (5) Batch uninstall from requirements file
 (6) Check package status
 (7) Display installed packages
 (8) Save requirements file
 (9) Exit''')


while True:
    print()
    option = input(Fore.CYAN + " Enter option: " + Style.RESET_ALL)
    if option == "1":
        print()
        install_pkg = input(Fore.CYAN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", install_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Installed {install_pkg} ")
            #input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            #input(" Press Enter to exit...")
        #break

    elif option == "2":
        print()
        print(Fore.YELLOW + " NOTE: Make sure requirements.txt is in this directory.")
        print(Fore.GREEN + " Batch installing packages...")

        with open("requirements.txt") as f:
            reqs = f.read().splitlines()
        for pkg in reqs:
            try:
                subprocess.check_call(["pip", "install", pkg])
                print(" " + Fore.BLACK + Back.GREEN + f" Installed {pkg} ")
                print()
            except subprocess.CalledProcessError:
                print(" " + Fore.BLACK  + Back.RED + " AN ERROR OCCURED ")
        #input(" Press Enter to exit...")
        #break

    elif option == "3":
        print()
        update_pkg = input(Fore.GREEN + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "install", "--upgrade", update_pkg])
            print(" " + Fore.BLACK + Back.GREEN + f" Updated {update_pkg} ")
            #input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            #input(" Press Enter to exit...")
        #break

    elif option == "4":
        print()
        uninstall_pkg = input(Fore.LIGHTRED_EX + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "uninstall", uninstall_pkg])
            print(" " + Fore.BLACK  + Back.RED + f" Uninstalled {uninstall_pkg} ")
            print()
            #input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            #input(" Press Enter to exit...")
        #break

    elif option == "5":
        print()
        print(Fore.YELLOW + " NOTE: Input package names in the requirements file." + Style.RESET_ALL)
        print(Fore.RED + " Batch uninstalling packages..." + Style.RESET_ALL)
        print()

        with open("requirements.txt") as f:
            reqs = f.read().splitlines()
        for pkg in reqs:
            try:
                subprocess.check_call(["pip", "uninstall", "-y", pkg])
                print(" " + Fore.BLACK + Back.RED + f" Uinstalled {pkg} ")
            except subprocess.CalledProcessError:
                print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")

    elif option == "6":
        print()
        verify_pkg = input(Fore.YELLOW + " Enter package name: " + Style.RESET_ALL)

        try:
            subprocess.check_call(["pip", "show", verify_pkg])
            print(" " + Fore.BLACK  + Back.GREEN + f" {verify_pkg} package exists ")
            #input(" Press Enter to exit...")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " PACKAGE NOT FOUND ")
            #input(" Press Enter to exit...")
        #break

    elif option == "7":
        print()
        print(Fore.GREEN + " Displaying all installed packages...")
        subprocess.check_call(["pip", "list"])

        # run pip list command and capture output
        output = subprocess.check_output(["pip", "list"])
        with open("packages.txt", "w") as f:
            f.write(output.decode("utf-8"))

    elif option == "8":
        print()
        print(Fore.YELLOW + " NOTE: Copy this tool to the project folder ")
        print(Fore.GREEN + " Saving project requirements to text file...")

        try:
            save = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
            with open('requirements.txt', 'wb') as f:
                f.write(save.stdout)
            print(" " + Fore.BLACK  + Back.GREEN + " PROJECT REQUIREMENTS SAVED ")
        except subprocess.CalledProcessError:
            print(" " + Fore.BLACK  + Back.RED + " AN ERROR OCCURED ")

    elif option == "help":
        print('''
 (1) Install package
 (2) Batch install from requirements file
 (3) Update package
 (4) Uninstall package
 (5) Batch uninstall from requirements file
 (6) Check package status
 (7) Display installed packages
 (8) Save requirements file
 (9) Exit''')

    elif option == "9":
        os._exit(0) #exits program
    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")



# Copyright © 2023 Ashfaaq Rifath - PipWizard v1.5.1
