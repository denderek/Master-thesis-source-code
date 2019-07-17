define e = Character("Eva", color="ffcccc")
#define participant_name = ("[participant_name]")
image grass_pitch:
     "grassfield#1.jpg"
     size(1300,800) 
     
image Eva_default:  
    "Eva_default#15.png"
    #size(1590,869)
    xalign -0.5
    yalign 0.4
    
image Eva_blinking:
    "Eva_blinking#19.png" 
    #size(1590,869)
    xalign -0.5
    yalign 0.4
    
image Eva_arm_fold:
    "Eva_armfold#2.png"
    xalign -0.5
    yalign 0.4
    
    
image Eva_animation:
    "Eva_default"
    3.9
    "Eva_blinking"
    0.3
    "Eva_default"
    4.6
    "Eva_blinking"
    0.2
    "Eva_arm_fold"
    3.5
    "Eva_blinking"
    0.2
    "Eva_default"
    4.7
    "Eva_blinking"
    0.2
    "Eva_default"
    3.7
    "Eva_arm_fold"
    2.3
    "Eva_blinking"
    0.2
    "Eva_default"
    3.2
    "Eva_blinking"
    0.2
    "Eva_arm_fold"
    1.9
    "Eva_blinking"
    0.2
    "Eva_default"
    3.7
    "Eva_blinking"
    0.2
    repeat
    
label start:

    scene grass_pitch
    show Eva_animation:
        
    #define audio.eerste_zin = "hallo_van.mp4"
    play sound "Audio scherm 1 Eva.mp3"#fadeout 1 
    
    e "Welkom, mijn naam is Eva en ik ga u helpen bij het aanmaken van een DigiD.
    Druk op Enter of de linker muisknop om naar het volgende scherm te gaan."
    stop sound
    
    play sound "Audio scherm 2.mp3"
    #queue sound "Druk op enter.mp3"
    e "Het aanmaken van een DigiD kan soms lastig zijn. Het is belangrijk dat u voor elke vraag de tijd neemt en dat u de vraag goed leest. Druk op Enter."
    stop sound
    
    play sound "Audio scherm 3.mp3"
    #queue sound "Druk op enter.mp3"
    e "Voor het aanvragen van een DigiD is het belangrijk dat we wat persoonlijke gegevens weten. De volgende vragen zullen hierop gericht zijn. Druk op Enter."
    stop sound
    
    play sound "Audio scherm 4.mp3"
    #queue sound "Druk daarna op Enter.mp3"
    $ participant_name_input = renpy.input("Wat is uw voornaam? (Typ in). Druk daarna op Enter.")
    $ participant_name = participant_name_input.strip()
    stop sound 
    
    play sound "Audio scherm 5.mp3"
    e "Uw burgerservicenummer wordt ook wel aangeduid als persoonsnummer of BSN en bestaat uit 9 cijfers. Dit kunt u vinden op uw Nederlandse paspoort, rijbewijs, identiteitskaart of zorgpas. Druk op Enter." 
    stop sound
    
    #python: 
        
    play sound "Audio scherm 7.mp3"
    python: 
        participant_BSN_input = renpy.input("Vul hier uw burgerservicenummer in? (9 cijfers). Druk daarna op Enter.")
        participant_BSN = participant_BSN_input.strip()
    stop sound
    
    play sound "Audio scherm 6.mp3"
    python: 
        participant_birthdate_input = renpy.input("Wat is uw geboortedatum? (DD-MM-JJJJ). Druk daarna op Enter.")
        participant_birthdate = participant_birthdate_input.strip()
    stop sound
        
    play sound "Audio scherm 8.mp3"
    python: 
        participant_zipcode_input = renpy.input("Wat is uw postcode? (4 cijfers + 2 letters). Druk daarna op Enter.")
        participant_zipcode = participant_zipcode_input.strip()
    stop sound
    
    play sound "Audio scherm 9.mp3"
    python:    
        participant_housenumber_input = renpy.input("Wat is uw huisnummer + eventuele toevoeging? Druk op Enter om verder te gaan.")
        participant_housenumber = participant_housenumber_input.strip()
    stop sound
    
    play sound "Audio scherm 10.mp3"   
    python:    
        e("Heel goed " + participant_name + ". Laten we even controleren of uw gegevens kloppen. Druk op Enter.")
    stop sound         
    
    play sound "Audio scherm 11.mp3"   
    python:
        e ("Heeft u alles goed ingevuld? " + participant_BSN + ", " + participant_birthdate + ",  " + participant_zipcode + ", " + participant_housenumber + ". Druk op Enter.")
    stop sound   
    
    play sound "Audio scherm 12.mp3"
    e"We zijn nu aangekomen bij het maken van inloggegevens. Onthoudt deze gegevens goed, hiermee kunt u inloggen bij DigiD. Druk op Enter."
    stop sound
    
    play sound "Audio scherm 13.mp3"
    python:
        participant_gebruikersnaam_input = renpy.input("Vul een gebruikersnaam in. (6-32 letters, geen spaties). Druk daarna op Enter.")
        participant_gebruikersnaam = participant_gebruikersnaam_input.strip()
    stop sound

    play sound "Audio scherm 14.mp3"
    python:
        participant_ww_input = renpy.input("Vul hier uw wachtwoord in. (8-32 letters, 1 kleine letter, 1 hoofdletter, 1 cijfer en een 1 leesteken (!@#$%...)). Druk daarna op Enter.")
        participant_ww = participant_ww_input.strip()
    stop sound
    
    play sound "Audio scherm 15.mp3"
    python:
        e("Heel goed " + participant_name +". Nogmaals, onthoudt deze gegevens goed. Hiermee kunt u voortaan inloggen. Druk op Enter.")
    stop sound
    
    play sound "Audio scherm 16.mp3"
    e"We zijn bij de laatste twee vragen aangekomen. Daarna heeft u een DigiD aangevraagd. Druk op Enter."
    stop sound
    
    play sound "Audio scherm 17.mp3"
    $ participant_telefoonnummer = renpy.input("Vul hier uw telefoonnummer in? Druk daarna op Enter.")
    stop sound
    
    play sound "Audio scherm 18.mp3"
    $ participant_email = renpy.input("Wat is uw e-mailadres? (als u dit niet heeft, klik dan op Enter)")
    stop sound
    
    play sound "Audio scherm 19.mp3"
    $ e("Goed gedaan "+ participant_name + "! U heeft uw DigiD succesvol aangevraagd.")
    stop sound
    
    
    #menu:
    #        e"Bent u getrouwd?"
    #        "ja":
    #            e"Heel goed. Op naar de volgende vraag"
    #        "nee":
    #           e"Heel goed. Op naar de volgende vraag"
              
    #python: 
       # url = "https://vunet.login.vu.nl/Pages/default.aspx"
 
        #e ("De volgende link brengt je naar een vragenlijst over het gebruik van Eva. Uw feedback zal gebruikt worden om Eva te verbeteren. Graag naar eerlijkheid invullen "  "{a=" + url + "}Klik hier voor de vragenlijst.{/a}")
    
    # This ends the game.
    return
