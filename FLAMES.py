try :
    import subprocess
    from flames import flames

except ModuleNotFoundError:
     subprocess.call("pip3 install flames", shell=True)

subprocess.call("color 0a ", shell=True)

print("""
                             (     (                *          (     
                             )\ )  )\ )    (      (  `         )\ )  
                            (()/( (()/(    )\     )\))(   (   (()/(  
                             /(_)) /(_))((((_)(  ((_)()\  )\   /(_)) 
                            (_))_|(_))   )\ _ )\ (_()((_)((_) (_))         
                            | |_  | |    (_)_\(_)|  \/  || __|/ __|           CODED BY  : SWAGKARNA
                            | __| | |__   / _ \  | |\/| || _| \__ \           GITHUB    : github.com/swagkarna   
                            |_|   |____| /_/ \_\ |_|  |_||___||___/           My Crush  : YOHANI          

                            A powerful python tool for predicting your future with your crush
""")

yourname = str(input("Enter your Name : "))
crushname = str(input("Enter yor Crush Name : "))
bsdk  = flames(yourname, crushname)
bsdk.result()
bsdk.info()
