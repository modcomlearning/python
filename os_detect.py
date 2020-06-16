import platform 
plt = platform.system()

if plt == "Windows":
    print("Your system is Windows")
    # do x y z
elif plt == "Linux":
    print("Your system is Linux")
    # do x y z
elif plt == "Darwin":
    print("Your system is MacOS")
    # do x y z
else:
    print("Unidentified system")