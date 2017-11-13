@echo off
goto loading



:loading
title gameMain
echo Initializing Assets . . .
echo Setting Blocks . . .
echo Getting Client Data . . .
echo Connecting to Local Servers . . .
echo Starting Program . . .
pause
goto gameInitialize



:gameInitialize
echo Welcome to THE TALE OF THE NIGHT WIZARD!
echo.
echo Copyright (C) 2017 by Ryan Kwong
echo.
echo All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, write to the publisher, addressed !Attention: Permissions Coordinator at the address below.
echo.
echo ThePotatoPlace Inc.
echo 1233 Main Street
echo San Francisco, CA 94909
echo http://thepotatoplace.ml
echo.
echo.
echo.
echo.
pause
goto instructions



:instructions
cls
echo Please note this is a preview. The game is not complete and may have a few glitches now and then. By continuing, you are entering our BETA testing. If you have any questions contact bebostunner234@gmail.com
echo.
echo.
echo.
echo.
echo FUNCTIONS
echo.
echo GUIDE accesses the guide(start)
echo MAP accesses the map(after Wizard Duel)
echo INVETORY accesses your inventory(after Wizard Duel)
echo.
echo.
echo.
echo.
echo Please Note:
echo 1. Please type in all CAPS
echo 2. The GUIDE is currently unavailable
echo.
echo  Now... What is your name?
echo.
set /p name=
echo.
echo 
cls
SET progress=0
goto gameStart



:gameStart
color 00
SET progress=1
echo You arrive at the village of Aerilon where you hope to make a living. However, the village seems troubled and empty. Determined to fit into your new life you decide to go to see the VILLAGE HEAD, but first you need to go to the DEPOT to get supplies.
echo Do you goto the DEPOT or to the HALL?
set /p resultscene1=
if %resultscene1% equ HOME goto home
if %resultscene1% equ DEPOT goto depot
if %resultscene1% equ HALL goto hall
if %resultscene1% equ GUIDE goto guide



:home
cls
echo As you enter the cramped shed that's supposed to be your home you remember the GUIDE your fried gave you. [type in GUIDE if you need to use the guide]. Satisfied that everything is in order, you leave the house to search the village.
echo Do you go to the DEPOT, or the HALL?
set /p resultscene2 =
if %resultscene2% equ DEPOT goto depot
if %resultscene2% equ HALL goto hall
if %resultscene2% equ GUIDE goto guide
:guide
cls
echo ERROR 395
echo Please close this app. 
set /p error=



:depot
cls
echo The depot is currently empty. However, you see a NOTE on the desk.
echo Will you read the NOTE or go HOME?
set /p resultscene2=
if %resultscene2% equ NOTE goto note
if %resultscene2% nqu NOTE goto depot
if %resultscene2% equ HOME goto home



:note
cls
echo The note reads "at village meeting. will be back at 8:00"
echo Will you go to the HALL?
set /p resultscene2=
if %resultscene2% equ HALL goto hall



:hall
cls
echo You enter the hall to see angry men shouting at each other. They quiet as soon as they see you. "Have you any news?", they ask with beseeching eyes.
echo What do you say?
echo YES
echo NO
echo WHATS HAPPENING
set /p resultscene2=
if %resultscene2% equ YES goto yesq1
if %resultscene2% equ NO goto noq1
if %resultscene2% equ WHATS HAPPENING goto explanation



:yesq1
echo.
echo Excited, they all rush over to you asking for details. Caught, you have to admit that you don't have any information to share. They all sit down looking defeated.
echo What do you say?
echo Type 'a' to ask "what's hapening?"
echo Type 'b' to say "Sorry?"
set /p resultscene3=
if %resultscene3% equ A goto explanation
if %resultscene3% equ B goto explanation 



:noq1
echo Disappointed they, sit down looking defeated.
echo What do you say?
echo Type 'a' to say "What happened?"
set /p resultscene3=
if %resultscene3% equ A goto explanation



:explanation
echo One man looks nevously around. "There was a man named Andrew Smith. He used to be a carpenter for our village. However, 2 weeks ago, he died mysteriously. 4 days later, another woman, Ava Sanchez, also died from the same mysterious circumstances. We think that there is a wizard that is cursing this village. Could you help?".
echo Type 'YES' to say 'yes'
echo Type 'NO' to say 'no'
set /p resultscene4=
if %resultscene4% equ YES goto achievment
if %resultscene4% equ NO goto explanation



:achievment
echo The men smile in relief. "Thank you!", they cry shaking your hand. Then one man asks, "Where do you think the wizard is?"
echo What do you suggest?
echo Type 'CAVE' to say 'Cave'
echo Type 'IDK' to say 'I don't know'
set /p resultscene4=
if %resultscene4% equ CAVE goto caveassent
if %resultscene4% equ IDK goto caveassent



:caveassent
cls
echo **5 HOURS LATER**
echo The cave gives off the feeling of being haunted. Shivering, you trudge on. Soon, you find yourself confronted with 3 tunnels. There is a plaque that reads "Beyond one of the tunnels lies the Great Wizard. If you must meet him, know that 2 of the tunnels leads to a pain far worse than death. The other leads to a tunnel.
echo Below there is another plaque. This one reads "Three men sit at a table. Two will need to be sacraficed. One man says that he refuses to be abandoned. He is quickly killed. Another man says that he has done no wrong. He is also killed. The last one survives and creates the correct tunnel"
echo Which tunnel?
echo Type 'R' to go right
echo Type 'M' to go through the middle
echo Type 'L' to go left
set /p resultscene5=
if %resultscene5% equ R goto death
if %resultscene5% equ M goto passage
if %resultscene5% equ L goto death



:death
cls
echo YOU DIED
set /p death=



:passage
cls
echo At the end of the hallway lies a door. Through it you can here a muttering sound. Listening closer, you make out some sort of incantion. Then, you hear a male voice say, "Beware the door!" Besides the door is a BATTLEAXE and a TORCH
echo What do you do?
echo Type 'OPEN' to open the door
echo Type 'B' to pick up the Battleaxe
echo Type 'T' to pick up the Torch
set /p item=
if %item% equ OPEN goto explosion
if %item% equ B goto explosion
if %item% equ T goto open



:open
cls 
echo The torch burns through the door. A few minutes later, all that is left is ashes. There standing before you is the WIZARD, and he looks mad.
pause
echo The Wizard looks at you for the longest time. Then he raises his hand. In his hand, you can see a WAND . . .
echo.
echo.
echo.
echo TO BE CONTINUED
set /p end=
