import random
import math

def greeting():                     #Create a greeting for the program.
    print("Welcome to Gundam Selector. \nLet's find a kit for you!")    #Print greeting.

def name():                         #Create a name for user.
    user = input("Hello, what's your name?\n").lower()                  #Asks user to their name, convert answer to lowercase only.
    if user in 'taew':              #If user name is Taew, print the following message.
        print("Hello wifey, you are beautiful as ever. <3")
    elif user in 'gem':             #If user name is Gem, print the following message.
        print("Hello Creator, hope you are well.")
    else:
        print("Hello " + user)      #If user name is none of the above, print the following message.

def disclaimer():                   #Disclaimer on prices and availibility.
    print("Before we get started, prices and availibility are pulled from the internet.\nPlease be aware as prices and availibility may have changed since my creation.\nAlso it's most likely cheaper on Gundam Planet.\nOkay! Let's go!")

gundam_with_pricing = {
                        'Rick DOM':45,                #Amazon
                        'DOM':38,                     #Amazon
                        'Gundam Virtue':110,          #Amazon
                        'Eclipse Gundam':64,          #Amazon
                        'Mobile Ginn':47,             #Amazon
                        'Wing Zero EW Ver. Ka':122,   #Amazon
                        'Gundam Kyrios':70,           #Amazon
                        'Fazz Ver. Ka':298,           #Amazon
                        'Gundam Barbatos':71,         #Amazon
                        'Gunner Zaku Warrior':80,     #Amazon
                        'Gundam NT-1 Ver. 2.0':66,    #Amazon
                        'Ex-S Gundam/S Gundam':209,   #Amazon
                        'Gundam Dynames':60,          #Amazon
                        'Gundam AGE II Magnum':102,   #Amazon
                        'Sinanju Stein':80,           #Amazon
                        '00 Qan[T] Full Saber':72,    #Amazo
                        'Jegan':47,                   #Amazon
                        'Gundam F91 Ver. 2.0':55,     #Amazon
                        'Plan303E Deep Striker':485,  #Amazon
                        'Unicorn Gundam 02 Banshee Ver. Ka':100,                      #Amazon
                        'GM Command':115,             #Amazon
                        'GM Sniper Custom':99,        #Amazon
                        'ZZ Gundam Ver. Ka':71,       #Amazon
                        'Justice Gundam':70,          #Amazon
                        'RX-78-2 Gundam(Gundam the Origin Ver.)(Special)':60,         #Amazon
                        'Providence Gundam':100,      #Amazon
                        'Providence Gundam (G.U.N.D.A.M Premium Edition)':156,        #Amazon
                        'Dramatic Combination [MG Freedum Gundam Ver 2.0 & Figure-rise Bust Kira Yamato)':154,    #Amazon
                        'GM Sniper II':60,            #Amazon
                        'Unicorn Gundam (Red / Green Twin Frame Edition) Titanium Finish':150,                    #Amazon
                        'High Mobility Type Zaku II `Psycho Zaku` Ver.Ka (Gundam Thunderbolt Ver.)':328,          #Amazon
                        'Full Armor Gundam Ver. Ka (Gundam Thunderbolt Ver.)':150,    #Amazon
                        'Freedom Gundam Ver. 2.0':73, #Amazon
                        'V2 Gundam Ver. Ka':'',          #Missing price
                        'RX-78-2 Gundam (GUNDAM THE ORIGIN Ver.)':64,                 #Amazon
                        'Gundam Amazing Red Warrior':120,                             #Amazon
                        'Gundam Fenice Rinascita':120,                                #Amazon
                        'Hyaku Shiki Ver 2.0':81,     #Amazon
                        'Gundam Double X':57,         #Amazon
                        'Gundam Exia Dark Matter':165,                                #Amazon
                        'Gundam Astray Blue Frame D':53,                              #Amazon
                        'Hi-Nu Gundam Ver. Ka':92,    #Amazon
                        'CONCEPT-X6-1-2 Turn X':195,  #eBay
                        'Universe Booster':210,       #eBay
                        'Build Gundam MK-II':85,      #Amazon
                        'Unicorn Gundam 03 Phenex':180,                               #Amazon
                        'Sengoku Astray Gundam':158,  #Amazon
                        'Gundam X-1':90,              #Amazon
                        'Build Strike Gundam Full Package':154,                       #Amazon
                        'Sazabi Ver. Ka':148,         #Amazon
                        'RX-93 Nu Gundam Ver. Ka Titanium Finish':253,                #Amazon
                        'Wing Gundam Proto Zero EW':73,                               #Amazon
                        'Strike Rouge + Ootori Equipment Ver. RM':110,                #Amazon
                        'RX-72-2 Gundam Ver 3.0':65,  #Amazon
                        'AMS-119 Geara Doga':63,      #Gundam Planet
                        'Gundam AGE-2 Double Bullet':116,                             #Amazon
                        'Aile Strike Gundam Ver. RM':65,                              #Amazon
                        'Jesta Cannon EW':141,        #Amazon
                        'Sinanju (OVA Ver.)':80,      #USA Gundam Store
                        'ReZEL Type C [Defenser-B Unit][GR]':264,                     #Amazon
                        'Sinanju Stein Ver. Ka':110,  #Amazon
                        'Tallgeese EW':59,            #Amazon
                        'RX-0 Unicorn Gundam 02 Banshee Titanium Finish Ver.':117,    #Amazon
                        'RX-92 Nu Gundam Ver. Ka':105,                                #Amazon
                        'Gundam AGE-II Dark Hound':60,                                #Amazon
                        'Aegis Gundam':38,
                        'Buster Gundam':48,
                        'Gundam AGE-II Normal':55,    #Amazon
                        'Blitz Gundam':48,            #Amazon
                        'Marasai':78,                 #Amazon
                        'Gundam AGE-I Sparrow':84,    #Amazon
                        'Unicorn Gundam 02 Banshee':96,                               #Amazon
                        'Gundam AGE-I Titus':106,     #Amazon
                        'Gundam AGE-I Normal':54,     #Amazon
                        'Duel Gundam Assault Shroud':51,                              #Amazon
                        'Gundam Heavyarms EW':55,     #Amazon
                        'Full Armor Unicorn Gundam Ver. Ka':132,                      #Amazon
                        'Gundam Sandrock EW':48,      #Amazon
                        '00 Gundam Seven Sword/G':60, #Amazon
                        'Delta Plus':62,              #Amazon
                        'Gundam Epyon EW':68,         #Amazon
                        '00 Raizer':60,               #Amazon
                        'Wing Gundam EW':122,         #Amazon
                        'Shenlong Gundam EW':49,      #Amazon
                        'Gundam Deathscythe Hell':50, #NewType
                        'ReZEL Commander Type':120,   #Amazon
                        '00 Qan[T]':49,               #Amazon
                        'ReZEL':60,                   #Amazon
                        'Gundam Deathscythe EW':60,   #Amazon
                        'The-O':151,                  #Amazon
                        'V-Dash Gundam Ver. Ka':123,  #Amazon
                        'Core Booster Ver. Ka':88,    #Amazon
                        'Full Armor Gundam':130,      #Amazon
                        'Musha Gundam Mk-II':159,     #Amazon
                        'Wing Gundam':57,             #Amazon
                        'Unicorn Gundam (OVA Ver.)':64,                               #Amazon
                        'RX-78-2 Gundam Ver. 2.0 Titanium Finish':133,                #Amazon
                        'Unicorn Gundam HD Color + MS Cage':121,                      #Amazon
                        'Sinanju Ver. Ka Titanium Finish':204,                        #Amazon
                        'Gundam Astray Red Frame Kai':70,                             #Amazon
                        'Gundam Exia Trans-AM Mode':123,                              #Amazon
                        'GN-X':58,                    #Amazon
                        'RX-78-2 Gundam Ver. 2.0':47, #Amazon
                        'Victory Gundam Ver. Ka':72,  #Amazon
                        'Qubeley Mk-II (Elpeo Ple Custom)':161,                       #Amazon
                        'Gundam Astray Blue Frame Second Revise':68,                  #Amazon
                        'Guntank':100,                #Amazon
                        'Gundam Exia Ignition Mode':134,                              #Amazon
                        'Gundam Exia':60,             #Amazon
                        'Zaku II White Orge':74,      #Amazon
                        'Gouf Ver. 2.0':55,           #Amazon
                        'Sword Impulse Gundam':60,    #Amazon
                        'Unicorn Gundam Ver. Ka Titanium Finish':157,                 #Amazon
                        'Shin Musha Gundam':171,      #Amazon
                        'Hyaku Shiki HD Color':123,   #Amazon
                        'GM Ver. 2.0':76,             #Amazon
                        'G Fighter':184,              #Amazon
                        'Zeta Gundam Ver. 2.0 HD Color':161,                          #Amazon
                        'Sinanju Ver. Ka':110,        #Amazon
                        'Zaku II Ver. 2.0 Shin Matsunaga Custom':117,                 #Amazon
                        'Gundam Mk-II Ver. 2.0 Titans Limited Ver.':110,              #Amazon
                        'Gundam Mk-II Ver. 2.0 A.E.U.G Limited Ver.':66,              #Amazon
                        'Infinite Justice Gundam':60, #Amazon
                        'Strike Freedom Gundam Extra Finish Ver.':125,                #Amazon
                        'Zaku II (Johnny Ridden Custom) Ver. 2.0':128,                #Amazon
                        'Zaku Cannon':175,            #Amazon
                        'Force Impulse Gundam':48,    #Amazon
                        'Gelgoog Ver 2.0':56,         #Amazon
                        'Launcher/Sword Strike Gundam':78,                            #Amazon
                        'Zaku II Ver 2.0':89,         #Amazon
                        'Zaku Minelayer':57,          #Gundam Planet
                        'RX-93 Nu Gundam Metallic Coating Ver.':156,                  #Amazon
                        'Strike E+IWSP Lukas O`Donnell Custom':150,                   #Amazon
                        'Zaku II (Black Tri-Stars) Ver. 2.0':96,                      #Amazon
                        'Unicorn Gundam Ver. Ka':105, #Amazon
                        'Sazabi Metallic Coating Ver.':185,                           #Amazon
                        'Destiny Gundam Extreme Blast Mode':90,                       #Amazon
                        'Destiny Gundam':60,          #Amazon
                        'Turn A Gundam':71,           #Amazon
                        'RX-78-2 Gundam Ver. O.Y.W 0079 Animation Color':49,          #Gundam Planet
                        'MS-06J Zaku II Ver. 2.0':89, #Amazon
                        'Strike Noir Gundam':70,      #Amazon
                        'Zeta Gundam 3 White Unicorn Color Ver.':247,                 #eBay
                        'Asian Regional Limited Edition Gundam RX-78-2':125,          #eBay
                        'Hi-V Gundam':92,             #Amazon
                        'Crossbone Gundam X-1 Full Cloth':90,                         #Amazon
                        'Strike Freedom Gundam Full Burst Mode':140,                  #Amazon
                        'Strike Freedom Gundam':103,  #Amazon
                        'GM Sniper':90,               #Amazon
                        'Gundam F91 (Harrison Madin Custom)':42,                      #Premium Bandai
                        'Strike Gundam + I.W.S.P':64, #Amazon
                        'Crossbone Gundam X-1 Ver. Ka':46,                            #Amazon
                        'Ball (Shark Mouth)':27,      #Amazon
                        'Gundam F91':55,              #Amazon
                        'YMS-15 Gyan':40,             #Amazon
                        'Gundam Mk-II (Titans) Ver. 2.0':55,                          #Amazon
                        'Nemo':70,                    #Amazon
                        'Zeta Gundam Ver 2.0':55,     #Amazon
                        'Gundam Mk-II (A.E.U.G) Ver. 2.0':70,                         #Amazon
                        'Freedom Gundam Extra Finish':84,                             #Amazon
                        'Hyaku Shiki + Ballute Pack':92,                              #Amazon
                        'Acguy':90,                   #Amazon
                        'Ball the 08 MS Ver.':77,     #Amazon
                        'Gelgoog (One Year War 0079 Ver.)':110,                       #Amazon
                        'Dom (One Year War 0079 Ver.)':108,                           #Amazon
                        'Gouf (One Year War 0079 Ver.)':75,                           #Amazon
                        'Zaku ll (One Year War 0079 Ver.)':76,                        #Amazon
                        'RX-78-2 Gundam (One Year War 0079 Ver.)':57,                 #eBay
                        'Rick Dias (Quattro Vegeena Custom)':177,                     #Amazon
                        'Mobile Pod Ball Ver. Ka':65,                                 #Amazon
                        'Wing Gundam Zero':82,        #Amazon
                        'Strike Rouge':88,            #Amazon
                        'Hi-Zack':60,                 #Amazon
                        'Freedom Gundam':72,          #Amazon
                        'Perfect Zeong':289,          #Amazon
                        'Rick Dias':45,               #Gundam Planet
                        'Wing Gundam Ver. Ka':41,     #Amazon
                        'Qubeley Mk-ll (Ple-Two Custom)':160,                         #Amazon
                        'Perfect Gundam':120,         #Amazon
                        'ZGok (Char Aznable Custom)':40,                              #Amazon
                        'Aile Strike Gundam':65,      #Amazon
                        'Gundam RX-78-5':84,          #Amazon
                        'Gundam RX-78-4':70,          #Amazon
                        'Gogg':65,                    #Amazon
                        'ZGok':55,                    #Amazon
                        'Hyper Mode God Gundam':82,   #Amazon
                        'Hyper Mode Master Gundam':93,                                #Amazon
                        'EX-S Gundam':100,            #Amazon
                        'Gelgoog (Anavel Gato Custom)':192,                           #Amazon
                        'Rick Dom (Char Custom)':130, #Amazon
                        'RX-78-2 Gundam Ver. Ka':64,  #Amazon
                        'GM Type C (Space Type)':80,  #Amazon
                        'S Gundam':112,               #Amazon
                        'Zaku II Type F2 (E.F.S.F)':97,                               #eBay
                        'Gundam Spiegel (Shadow Gundam)':82,                          #Amazon
                        'Gundam RX-78/C.A.':82,       #Amazon
                        'Zeong':100,                  #Amazon
                        'GM Type C (Earth Type)':39,  #Gundam Planet
                        'Shining Gundam':55,          #Amazon
                        'Zaku II Type F2 (Zeon)':82,  #Amazon
                        'Master Gundam':49,           #Amazon
                        'Zeta Plus C1':107,           #Amazon
                        'Gun Cannon':40,              #Amazon
                        'God Gundam':38,              #Amazon
                        'Zeta Plus':70,               #Amazon
                        'Qubeley':44,                 #Amazon
                        'Re-GZ':200,                  #Amazon
                        'Gundam GP03S':65,            #Amazon
                        'Hyaku Shiki':87,             #Amazon
                        'Gouf Custom':47,             #Amazon
                        'Kampfer Gundam':53,          #Amazon
                        'Nu Gundam':82,               #Amazon
                        'Gouf':55,                    #Amazon
                        'Zaku I (Ramba Ral Custom)':88,                               #Amazon
                        'Full Armor ZZ Gundam':110,   #Amazon
                        'Sazabi':148,                 #Amazon
                        'RX-78-2 Gundam Ver. 1.5':50, #Amazon
                        'RX-79(G) Gundam Ground Type':39,                             #Gundam Planet
                        'MS-06F/J Zaku II Coating Ver.':91,                           #Amazon
                        'Gundam RX-78 GP02A Coating Ver.':52,                         #Amazon
                        'ZZ Gundam':71,               #Amazon
                        'GM Quel':93,                 #Amazon
                        'GM Custom':89,               #Amazon
                        'Rick Dom (1999)':211,        #eBay
                        'Gundam GP01Fb Coating Ver.':43,                              #Amazon
                        'MS-06S Zaku II Coating Ver.':86,                             #Amazon
                        'Gundam RX-78 NT-1':72,       #Amazon
                        'MS-09 Dom':51,               #Gundam Planet 
                        'Zaku I (Black-Tri Stars)':33,                                #Gundam Planet
                        'MS-05B Zaku I':88,           #Amazon
                        'RGM-79 GM':76,               #Amazon
                        'Super Gundam':106,           #Amazon
                        'Gundam Mk-II (Titans)':45,   #Amazon
                        'Gundam Mk-II (A.E.U.G)':67,  #Amazon
                        'Zeta Gundam Coating Ver.':49,                                #Amazon
                        'RX-78-2 Gundam Coating Ver.':45,                             #Amazon
                        'Gundam RX-78 GP02A':65,      #Amazon
                        'Gundam GP01Fb':26,           #HobbyLink Japan
                        'MS-14A Gelgoog':153,         #Amazon
                        'Gundam GP01':52,             #Amazon
                        'Gelgoog Cannon (J. Ridden Custom)':37,                       #Gundam Planet
                        'Zaku II (Johnny Ridden Custom)':127,                         #Amazon
                        'Zaku II (Shin Matsunaga Custom)':117,                        #Amazon
                        'Gundam RX-78-3':66,          #Amazon
                        'MS-06F/J Zaku II':76,        #Amazon
                        'Gundam RX-78-2':62           #eBay
}

def filtered_under_thirty():
    {k:v for k,v in gundam_with_pricing.values() if v >=30 }
    print (filtered_under_thirty())

filtered_under_thirty()