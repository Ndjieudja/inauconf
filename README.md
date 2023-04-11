
                                                                                                                        22.01.22
                                                                
pip install inauconf

Author: NDJIEU'DJA Gabriel
Develloper en Python 3.5
Version: 1.1


REsumer:
    Inauconf est une application de criptage de donner de type string sur la base utf8. L'application a pour finiter plusieur utiliter:
        - cripter les mot de passe 
        - cripter les documents de type string 
        - lecture de document cripter par la memem application
        - dans le volet de mote de passe des eventuealiter d'insertion de ses dernier directimeent dans la base de donner. pour cel volet en 
    exeption en date d'aujourd'hui on ne parlera que la base de donnne Postgres dans sa verion 13.


Presentation:

>>from inauconf import shuffle

* le modeule Shuffle.py :
    ce dernier contient essenetiellement l'agorithme de chiffrement et de dechiffrement. Il contient la classe 
        - EncripAll() 
    donc les deux fonction principale comme mentionnner plus haut sont les chiffrement 
            * cript(target)
                target ici designe la cibre a cript cela part etre tout type de docuement en format string
            * uncript(target)
                target ici designe toujours la cible de dechiffre dans ce cas exeptionnellement la cible dois
                etre un document chiffrer par la meme application 


* le module INC_REader.py:
    celui ci contient l'utilitaire de gestion graphique qui quant a lui est designe par l'applicaiton standar de lecture de documemnt 
    chiffre ou decriffre par l Inauconf qui possedera l'extension "*.inc"
    en effet l GUI est cree sur la base de l'utilitarie tkinter syste de gestion graphique.

* le module main:
    Mian designe le programme principale de l'applicaition qui reunira tout les differents citer et possible en une seule execution

* sgbd:
    comme le nom le dis c'est ce module qui gere le systeme de gestion de base de donne pour le compte du volet de sauvegarde 
    des mot de passe chiffrer et la lecture de ces dernier dans le cadre d'une eventuel ouverture de seession ou tout objet blocquer par inauconf ayant une cles sauvegarder dans la base de donner 
    par defaut la db_name est Inauconf

* global vavrious, shema.sql sont des fichier contenant le neccessaire au bon fonctionnnement de l'appliaiton dans ses different volets.

                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        Inauconf.inc
                                                                                                        dev/ Gabrielhack
                                                                                                        /media/anonymous/NG 40/Backup/logo.png
                                                                                                        tel: +237 672 87 30 02
                                                                                                        github: github/Ndjieudja
                                                                                                        web: gabrielhack.pythonanywhere.com/start


