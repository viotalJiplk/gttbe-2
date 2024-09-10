from testUtils import requestExpect

schools = [
    {
        "schoolId": 1,
        "name": "1. IT Gymnázium, s.r.o."
    }, {
        "schoolId": 2,
        "name": "1. kladenská soukromá střední škola a základní škola 1. KŠPA, s.r.o."
    }, {
        "schoolId": 3,
        "name": "1. Scio Střední škola, s.r.o."
    }, {
        "schoolId": 4,
        "name": "1. Slovanské gymnázium a jazyková škola s právem státní jazykové zkoušky"
    }, {
        "schoolId": 5,
        "name": "ACADEMIA MERCURII soukromá střední škola, s. r. o."
    }, {
        "schoolId": 6,
        "name": "AKADEMIA Gymnázium, Základní škola a Mateřská škola, s. r. o."
    }, {
        "schoolId": 7,
        "name": "Akademické gymnázium a Jazyková škola s právem státní jazykové zkoušky, školy hlavního města Prahy"
    }, {
        "schoolId": 8,
        "name": "Akademie řemesel Praha - Střední škola technická"
    }, {
        "schoolId": 9,
        "name": "Akademie SOUVIN, střední škola"
    }, {
        "schoolId": 10,
        "name": "Akademie VŠEM - střední škola, s.r.o."
    }, {
        "schoolId": 11,
        "name": "Albrechtova střední škola Český Těšín, příspěvková organizace"
    }, {
        "schoolId": 12,
        "name": "Anglo - německá obchodní akademie a.s."
    }, {
        "schoolId": 13,
        "name": "Arcibiskupské gymnázium"
    }, {
        "schoolId": 14,
        "name": "ART ECON - Střední škola a vyšší odborná škola Praha, s.r.o."
    }, {
        "schoolId": 15,
        "name": "Bankovní akademie - Gymnázium a Střední odborná škola, a.s."
    }, {
        "schoolId": 16,
        "name": "BEZPEČNOSTNĚ PRÁVNÍ AKADEMIE BRNO, S.R.O."
    }, {
        "schoolId": 17,
        "name": "Biskupské gymnázium Brno a mateřská škola"
    }, {
        "schoolId": 18,
        "name": "Biskupské gymnázium J. N. Neumanna, církevní základní škola a základní umělecká škola České Budějovice"
    }, {
        "schoolId": 19,
        "name": "Biskupské gymnázium, církevní základní škola, mateřská škola a základní umělecká škola Hradec Králov"
    }, {
        "schoolId": 20,
        "name": "Boleslavská soukromá střední škola a základní škola, s.r.o."
    }, {
        "schoolId": 21,
        "name": "Česká zahradnická akademie Mělník - střední škola a vyšší odborná škola, příspěvková organizace"
    }, {
        "schoolId": 22,
        "name": "České reálné gymnázium s.r.o."
    }, {
        "schoolId": 23,
        "name": "Česko-anglické gymnázium s.r.o."
    }, {
        "schoolId": 24,
        "name": "Českoslovanská akademie obchodní Dr. Edvarda Beneše, střední odborná škola, Praha 2, Resslova 8"
    }, {
        "schoolId": 25,
        "name": "Českoslovanská akademie obchodní, střední odborná škola, Praha 2, Resslova 5"
    }, {
        "schoolId": 26,
        "name": "Církevní gymnázium v Kutné Hoře"
    }, {
        "schoolId": 27,
        "name": "Církevní střední škola Jana Boska"
    }, {
        "schoolId": 28,
        "name": "Církevní střední zdravotnická škola Jana Pavla II."
    }, {
        "schoolId": 29,
        "name": "Církevní střední zdravotnická škola s. r. o."
    }, {
        "schoolId": 30,
        "name": "Creative Hill College, Zlín"
    }, {
        "schoolId": 31,
        "name": "Cyrilometodějské gymnázium a střední odborná škola pedagogická Brno"
    }, {
        "schoolId": 32,
        "name": "Dětský domov, Mateřská škola, Základní škola a Praktická škola, Písek, Šobrova 111"
    }, {
        "schoolId": 33,
        "name": "Dětský domov, Praktická škola, Základní škola a Mateřská škola Nymburk, příspěvková organizace"
    }, {
        "schoolId": 34,
        "name": "Dívčí katolická střední škola"
    }, {
        "schoolId": 35,
        "name": "Doctrina - Podještědské gymnázium, s.r.o."
    }, {
        "schoolId": 36,
        "name": "DRAPA SPORT - středisko praktického vyučování s.r.o."
    }, {
        "schoolId": 37,
        "name": "Dvořákovo gymnázium Kralupy nad Vltavou, příspěvková organizace"
    }, {
        "schoolId": 38,
        "name": "Dvouletá katolická střední škola a mateřská škola"
    }, {
        "schoolId": 39,
        "name": "EDUCAnet - gymnázium, střední odborná škola a základní škola Praha, s.r.o."
    }, {
        "schoolId": 40,
        "name": "EDUCAnet - střední škola a základní škola České Budějovice, s.r.o."
    }, {
        "schoolId": 41,
        "name": "EKO Gymnázium a Střední odborná škola Multimediálních studií"
    }, {
        "schoolId": 42,
        "name": "EKO GYMNÁZIUM BRNO o. p. s."
    }, {
        "schoolId": 43,
        "name": "Ekonomické lyceum a Obchodní akademie SOVA, o.p.s."
    }, {
        "schoolId": 44,
        "name": "Euroškola Česká Lípa střední odborná škola s.r.o."
    }, {
        "schoolId": 45,
        "name": "Euroškola Praha střední odborná škola s.r.o."
    }, {
        "schoolId": 46,
        "name": "Euroškola Strakonice střední odborná škola s.r.o."
    }, {
        "schoolId": 47,
        "name": "Evangelická akademie - Vyšší odborná škola sociální práce a střední odborná škola"
    }, {
        "schoolId": 48,
        "name": "G.A.P.education, střední škola s.r.o."
    }, {
        "schoolId": 49,
        "name": "Gymnázium a Hudební škola hlavního města Prahy, základní umělecká škola"
    }, {
        "schoolId": 50,
        "name": "Gymnázium a Jazyková škola s právem státní jazykové zkoušky Břeclav, příspěvková organizace"
    }, {
        "schoolId": 51,
        "name": "Gymnázium a obchodní akademie Bučovice, příspěvková organizace"
    }, {
        "schoolId": 52,
        "name": "Gymnázium a obchodní akademie Mariánské Lázně, příspěvková organizace"
    }, {
        "schoolId": 53,
        "name": "Gymnázium a obchodní akademie Mariánské Lázně, příspěvková organizace"
    }, {
        "schoolId": 54,
        "name": "Gymnázium a Střední odborná škola ekonomická, Sedlčany, Nádražní 90"
    }, {
        "schoolId": 55,
        "name": "Gymnázium a střední odborná škola Mikulov, příspěvková organizace"
    }, {
        "schoolId": 56,
        "name": "Gymnázium a Střední odborná škola pedagogická, Čáslav, Masarykova 248"
    }, {
        "schoolId": 57,
        "name": "Gymnázium a Střední odborná škola pedagogická, Liberec, Jeronýmova 425/27, příspěvková organizace"
    }, {
        "schoolId": 58,
        "name": "Gymnázium a Střední odborná škola pedagogická, Nová Paka, Kumburská 740"
    }, {
        "schoolId": 59,
        "name": "Gymnázium a Střední odborná škola pedagogická, Nová Paka, Kumburská 740"
    }, {
        "schoolId": 60,
        "name": "Gymnázium a Střední odborná škola zdravotnická a ekonomická Vyškov, příspěvková organizace"
    }, {
        "schoolId": 61,
        "name": "Gymnázium a ZUŠ, Riegrova 17, Šlapanice"
    }, {
        "schoolId": 62,
        "name": "Gymnázium ALTIS s.r.o."
    }, {
        "schoolId": 63,
        "name": "Gymnázium ARTION"
    }, {
        "schoolId": 64,
        "name": "Gymnázium Aš, příspěvková organizace"
    }, {
        "schoolId": 65,
        "name": "Gymnázium Aš, příspěvková organizace"
    }, {
        "schoolId": 66,
        "name": "Gymnázium Blansko, příspěvková organizace"
    }, {
        "schoolId": 67,
        "name": "Gymnázium Bohumila Hrabala v Nymburce, příspěvková organizace"
    }, {
        "schoolId": 68,
        "name": "Gymnázium Boskovice, příspěvková organizace"
    }, {
        "schoolId": 69,
        "name": "Gymnázium Boženy Němcové, Hradec Králové, Pospíšilova tř. 324"
    }, {
        "schoolId": 70,
        "name": "Gymnázium bratří Čapků a První české soukromé střední odborné učiliště s.r.o."
    }, {
        "schoolId": 71,
        "name": "Gymnázium Brno, Elgartova, příspěvková organizace"
    }, {
        "schoolId": 72,
        "name": "Gymnázium Brno, Křenová, příspěvková organizace"
    }, {
        "schoolId": 73,
        "name": "Gymnázium Brno, Slovanské náměstí, příspěvková organizace"
    }, {
        "schoolId": 74,
        "name": "Gymnázium Brno, třída Kapitána Jaroše, příspěvková organizace"
    }, {
        "schoolId": 75,
        "name": "Gymnázium Brno, Vídeňská, příspěvková organizace"
    }, {
        "schoolId": 76,
        "name": "Gymnázium Brno-Bystrc, příspěvková organizace"
    }, {
        "schoolId": 77,
        "name": "Gymnázium Čakovice, Praha 9, nám. 25. března 100"
    }, {
        "schoolId": 78,
        "name": "Gymnázium Cheb, příspěvková organizace"
    }, {
        "schoolId": 79,
        "name": "Gymnázium Cheb, příspěvková organizace"
    }, {
        "schoolId": 80,
        "name": "Gymnázium Christiana Dopplera"
    }, {
        "schoolId": 81,
        "name": "Gymnázium Dr. Antona Randy, Jablonec nad Nisou, příspěvková organizace"
    }, {
        "schoolId": 82,
        "name": "Gymnázium Dr. Josefa Pekaře, Mladá Boleslav, Palackého 211"
    }, {
        "schoolId": 83,
        "name": "Gymnázium Dr. Karla Polesného Znojmo, příspěvková organizace"
    }, {
        "schoolId": 84,
        "name": "Gymnázium Duhovka s.r.o."
    }, {
        "schoolId": 85,
        "name": "Gymnázium Elišky Krásnohorské, Praha 4 - Michle, Ohradní 55"
    }, {
        "schoolId": 86,
        "name": "Gymnázium F. X. Šaldy, Liberec 11, Partyzánská 530, příspěvková organizace"
    }, {
        "schoolId": 87,
        "name": "Gymnázium Františka Palackého, Neratovice, Masarykova 450"
    }, {
        "schoolId": 88,
        "name": "Gymnázium Globe, s. r. o."
    }, {
        "schoolId": 89,
        "name": "Gymnázium Hostivice, příspěvková organizace"
    }, {
        "schoolId": 90,
        "name": "Gymnázium Ivana Olbrachta, Semily, Nad Špejcharem 574, příspěvková organizace"
    }, {
        "schoolId": 91,
        "name": "Gymnázium J. A. Komenského, Nové Strašecí, Komenského nám. 209"
    }, {
        "schoolId": 92,
        "name": "Gymnázium J. G. Mendela a jeho zař. a ZUŠ, Mendlovo nám. č. p. 1, č. o. 3/4, Brno"
    }, {
        "schoolId": 93,
        "name": "Gymnázium J. K. Tyla, Hradec Králové, Tylovo nábř. 682"
    }, {
        "schoolId": 94,
        "name": "Gymnázium J. S. Machara, Brandýs nad Labem - Stará Boleslav, Královická 668"
    }, {
        "schoolId": 95,
        "name": "Gymnázium J. Seiferta o.p.s."
    }, {
        "schoolId": 96,
        "name": "Gymnázium J. V. Jirsíka, České Budějovice, Fráni Šrámka 23"
    }, {
        "schoolId": 97,
        "name": "Gymnázium Jana Blahoslava, Lány 2, Ivančice"
    }, {
        "schoolId": 98,
        "name": "Gymnázium Jana Keplera, Praha 6, Parléřova 2"
    }, {
        "schoolId": 99,
        "name": "Gymnázium Jana Nerudy, škola hlavního města Prahy, Praha 1, Hellichova 3"
    }, {
        "schoolId": 100,
        "name": "GYMNÁZIUM JANA PALACHA PRAHA 1, s.r.o."
    }, {
        "schoolId": 101,
        "name": "Gymnázium Jana Palacha, Mělník, Pod Vrchem 3421"
    }, {
        "schoolId": 102,
        "name": "Gymnázium Jaroslava Heyrovského, Praha 5, Mezi Školami 2475"
    }, {
        "schoolId": 103,
        "name": "Gymnázium Jaroslava Žáka, Jaroměř"
    }, {
        "schoolId": 104,
        "name": "Gymnázium Jiřího Gutha-Jarkovského, Praha 1, Truhlářská 22"
    }, {
        "schoolId": 105,
        "name": "Gymnázium Jiřího Ortena, Kutná Hora, Jaselská 932"
    }, {
        "schoolId": 106,
        "name": "Gymnázium Jiřího z Poděbrad, Poděbrady, Studentská 166"
    }, {
        "schoolId": 107,
        "name": "Gymnázium Joachima Barranda, Beroun, Talichova 824"
    }, {
        "schoolId": 108,
        "name": "Gymnázium Josefa Kainara, Hlučín"
    }, {
        "schoolId": 109,
        "name": "Gymnázium Kadaň"
    }, {
        "schoolId": 110,
        "name": "Gymnázium Karla Čapka, Dobříš, Školní 1530"
    }, {
        "schoolId": 111,
        "name": "Gymnázium Karla Sladkovského, Praha 3, Sladkovského náměstí 8"
    }, {
        "schoolId": 112,
        "name": "Gymnázium Karviná, příspěvková organizace Karviná-Nové Město, Mírová 1442"
    }, {
        "schoolId": 113,
        "name": "Gymnázium Matyáše Lercha, Brno, Žižkova 55, příspěvková organizace"
    }, {
        "schoolId": 114,
        "name": "Gymnázium mezinárodních a veřejných vztahů Praha s.r.o."
    }, {
        "schoolId": 115,
        "name": "Gymnázium Mikuláše Koperníka, Bílovec"
    }, {
        "schoolId": 116,
        "name": "Gymnázium Milady Horákové"
    }, {
        "schoolId": 117,
        "name": "Gymnázium Mnichovo Hradiště, příspěvková organizace"
    }, {
        "schoolId": 118,
        "name": "Gymnázium Mojmírovo náměstí s. r. o."
    }, {
        "schoolId": 119,
        "name": "Gymnázium Moravský Krumlov, příspěvková organizace"
    }, {
        "schoolId": 120,
        "name": "Gymnázium Opatov, Praha 4, Konstantinova 1500"
    }, {
        "schoolId": 121,
        "name": "Gymnázium Ostrov, příspěvková organizace"
    }, {
        "schoolId": 122,
        "name": "Gymnázium Ostrov, příspěvková organizace"
    }, {
        "schoolId": 123,
        "name": "Gymnázium Oty Pavla, Praha 5, Loučanská 520"
    }, {
        "schoolId": 124,
        "name": "Gymnázium P. Křížkovského s uměleckou profilací, s. r. o."
    }, {
        "schoolId": 125,
        "name": "Gymnázium Paměti národa, s.r.o."
    }, {
        "schoolId": 126,
        "name": "Gymnázium Pierra de Coubertina, Tábor, Náměstí Františka Křižíka 860"
    }, {
        "schoolId": 127,
        "name": "Gymnázium Přírodní škola, o.p.s."
    }, {
        "schoolId": 128,
        "name": "Gymnázium pro zrakově postižené a Střední odborná škola pro zrakově postižené, Praha 5, Radlická 115"
    }, {
        "schoolId": 129,
        "name": "Gymnázium prof. Jana Patočky, Praha 1, Jindřišská 36"
    }, {
        "schoolId": 130,
        "name": "Gymnázium Rájec-Jestřebí, o. p. s."
    }, {
        "schoolId": 131,
        "name": "Gymnázium Říčany, příspěvková organizace"
    }, {
        "schoolId": 132,
        "name": "Gymnázium Sokolov a Krajské vzdělávací centrum, příspěvková organizace"
    }, {
        "schoolId": 133,
        "name": "Gymnázium Sokolov a Krajské vzdělávací centrum, příspěvková organizace"
    }, {
        "schoolId": 134,
        "name": "Gymnázium Strakonice"
    }, {
        "schoolId": 135,
        "name": "Gymnázium T. G. Masaryka Hustopeče, příspěvková organizace"
    }, {
        "schoolId": 136,
        "name": "Gymnázium T. G. Masaryka, U Školy 39, Zastávka"
    }, {
        "schoolId": 137,
        "name": "Gymnázium Thomase Manna, z. ú."
    }, {
        "schoolId": 138,
        "name": "Gymnázium Tišnov, příspěvková organizace"
    }, {
        "schoolId": 139,
        "name": "Gymnázium Václava Beneše Třebízského, Slaný, Smetanovo nám. 1310"
    }, {
        "schoolId": 140,
        "name": "Gymnázium Václava Hraběte, Hořovice, Jiráskova 617"
    }, {
        "schoolId": 141,
        "name": "Gymnázium Velké Meziříčí"
    }, {
        "schoolId": 142,
        "name": "Gymnázium Vítězslava Nováka, Jindřichův Hradec, Husova 333"
    }, {
        "schoolId": 143,
        "name": "Gymnázium Vojtecha Mihálika Sereď"
    }, {
        "schoolId": 144,
        "name": "Gymnázium Žamberk"
    }, {
        "schoolId": 145,
        "name": "Gymnázium Zikmunda Wintra Rakovník, příspěvková organizace"
    }, {
        "schoolId": 146,
        "name": "Gymnázium, Benešov, Husova 470"
    }, {
        "schoolId": 147,
        "name": "Gymnázium, Broumov, Hradební 218"
    }, {
        "schoolId": 148,
        "name": "Gymnázium, Čelákovice, J. A. Komenského 414"
    }, {
        "schoolId": 149,
        "name": "Gymnázium, Česká Lípa, Žitavská 2969, příspěvková organizace"
    }, {
        "schoolId": 150,
        "name": "Gymnázium, České Budějovice, Česká 64"
    }, {
        "schoolId": 151,
        "name": "Gymnázium, České Budějovice, Jírovcova 8"
    }, {
        "schoolId": 152,
        "name": "Gymnázium, Český Brod, Vítězná 616"
    }, {
        "schoolId": 153,
        "name": "Gymnázium, Český Krumlov, Chvalšinská 112"
    }, {
        "schoolId": 154,
        "name": "Gymnázium, Dačice, Boženy Němcové 213"
    }, {
        "schoolId": 155,
        "name": "Gymnázium, Dobruška, Pulická 779"
    }, {
        "schoolId": 156,
        "name": "Gymnázium, Frýdlant, Mládeže 884, příspěvková organizace"
    }, {
        "schoolId": 157,
        "name": "Gymnázium, Jablonec nad Nisou, U Balvanu 16, příspěvková organizace"
    }, {
        "schoolId": 158,
        "name": "Gymnázium, Kladno, nám.Edvarda Beneše 1573"
    }, {
        "schoolId": 159,
        "name": "Gymnázium, Kolín III, Žižkova 162"
    }, {
        "schoolId": 160,
        "name": "Gymnázium, Milevsko, Masarykova 183"
    }, {
        "schoolId": 161,
        "name": "Gymnázium, Mimoň, Letná 263, příspěvková organizace"
    }, {
        "schoolId": 162,
        "name": "Gymnázium, Mladá Boleslav, Palackého 191/1"
    }, {
        "schoolId": 163,
        "name": "Gymnázium, Obchodní akademie a Jazyková škola s právem státní jazykové zkoušky Hodonín, příspěvková"
    }, {
        "schoolId": 164,
        "name": "Gymnázium, Písek, Komenského 89"
    }, {
        "schoolId": 165,
        "name": "Gymnázium, Prachatice, Zlatá stezka 137"
    }, {
        "schoolId": 166,
        "name": "Gymnázium, Praha 10, Omská 1300"
    }, {
        "schoolId": 167,
        "name": "Gymnázium, Praha 10, Přípotoční 1337"
    }, {
        "schoolId": 168,
        "name": "Gymnázium, Praha 10, Voděradská 2"
    }, {
        "schoolId": 169,
        "name": "Gymnázium, Praha 2, Botičská 1"
    }, {
        "schoolId": 170,
        "name": "Gymnázium, Praha 4, Budějovická 680"
    }, {
        "schoolId": 171,
        "name": "Gymnázium, Praha 4, Na Vítězné pláni 1160"
    }, {
        "schoolId": 172,
        "name": "Gymnázium, Praha 4, Písnická 760"
    }, {
        "schoolId": 173,
        "name": "Gymnázium, Praha 4, Postupická 3150"
    }, {
        "schoolId": 174,
        "name": "Gymnázium, Praha 5, Na Zatlance 11"
    }, {
        "schoolId": 175,
        "name": "Gymnázium, Praha 5, Nad Kavalírkou 1"
    }, {
        "schoolId": 176,
        "name": "Gymnázium, Praha 6, Arabská 14"
    }, {
        "schoolId": 177,
        "name": "Gymnázium, Praha 8, Ústavní 400"
    }, {
        "schoolId": 178,
        "name": "Gymnázium, Praha 9, Českolipská 373"
    }, {
        "schoolId": 179,
        "name": "Gymnázium, Praha 9, Chodovická 2250"
    }, {
        "schoolId": 180,
        "name": "Gymnázium, Praha 9, Litoměřická 726"
    }, {
        "schoolId": 181,
        "name": "Gymnázium, Praha 9, Špitálská 2"
    }, {
        "schoolId": 182,
        "name": "Gymnázium, Soběslav, Dr. Edvarda Beneše 449/II"
    }, {
        "schoolId": 183,
        "name": "Gymnázium, Strakonice, Máchova 174"
    }, {
        "schoolId": 184,
        "name": "Gymnázium, Střední odborná škola a Střední zdravotnická škola, Jilemnice, příspěvková organizace"
    }, {
        "schoolId": 185,
        "name": "Gymnázium, Střední odborná škola a Vyšší odborná škola, Nový Bydžov"
    }, {
        "schoolId": 186,
        "name": "Gymnázium, Střední odborná škola, Základní škola a Mateřská škola pro sluchově postižené, Praha 2, Ječná 27"
    }, {
        "schoolId": 187,
        "name": "Gymnázium, Střední pedagogická škola, Obchodní akademie a Jazyková škola s právem státní jazykové zk"
    }, {
        "schoolId": 188,
        "name": "Gymnázium, Sušice, Fr. Procházky 324"
    }, {
        "schoolId": 189,
        "name": "Gymnázium, Tanvald, příspěvková organizace"
    }, {
        "schoolId": 190,
        "name": "Gymnázium, Terezy Novákové 2, Brno - Řečkovice"
    }, {
        "schoolId": 191,
        "name": "Gymnázium, Třeboň, Na Sadech 308"
    }, {
        "schoolId": 192,
        "name": "Gymnázium, Trhové Sviny, Školní 995"
    }, {
        "schoolId": 193,
        "name": "Gymnázium, Turnov, Jana Palacha 804, příspěvková organizace"
    }, {
        "schoolId": 194,
        "name": "Gymnázium, Týn nad Vltavou, Havlíčkova 13"
    }, {
        "schoolId": 195,
        "name": "Gymnázium, Tyršova 400, Židlochovice"
    }, {
        "schoolId": 196,
        "name": "Gymnázium, Velké Pavlovice, Pod Školou 10, příspěvková organizace"
    }, {
        "schoolId": 197,
        "name": "Gymnázium, Vlašim, Tylova 271"
    }, {
        "schoolId": 198,
        "name": "Heřmánek Praha, základní škola a gymnázium"
    }, {
        "schoolId": 199,
        "name": "Hořické gymnázium"
    }, {
        "schoolId": 200,
        "name": "Hotelová škola a Gymnázium Radlická"
    }, {
        "schoolId": 201,
        "name": "Hotelová škola Hradec Králové, s. r. o."
    }, {
        "schoolId": 202,
        "name": "Hotelová škola Mariánské Lázně, příspěvková organizace"
    }, {
        "schoolId": 203,
        "name": "Hotelová škola Mariánské Lázně, příspěvková organizace"
    }, {
        "schoolId": 204,
        "name": "Hotelová škola Mariánské Lázně, příspěvková organizace"
    }, {
        "schoolId": 205,
        "name": "Hotelová škola Poděbrady, příspěvková organizace"
    }, {
        "schoolId": 206,
        "name": "Hotelová škola s. r. o."
    }, {
        "schoolId": 207,
        "name": "Hotelová škola, Obchodní akademie a Střední průmyslová škola, Teplice, Benešovo náměstí 1, příspěvková organizace"
    }, {
        "schoolId": 208,
        "name": "Hotelová škola, Praha 10, Vršovická 43"
    }, {
        "schoolId": 209,
        "name": "Hudební gymnázium České Budějovice s.r.o."
    }, {
        "schoolId": 210,
        "name": "I. Německé zemské gymnasium, ZŠ a MŠ, o.p.s., Mendlovo nám. 1/ 3,4, Brno"
    }, {
        "schoolId": 211,
        "name": "Integrovaná střední škola Cheb, příspěvková organizace"
    }, {
        "schoolId": 212,
        "name": "Integrovaná střední škola Cheb, příspěvková organizace"
    }, {
        "schoolId": 213,
        "name": "Integrovaná střední škola Hodonín, příspěvková organizace"
    }, {
        "schoolId": 214,
        "name": "Integrovaná střední škola hotelového provozu, obchodu a služeb, Příbram, Gen. R. Tesaříka 114"
    }, {
        "schoolId": 215,
        "name": "Integrovaná střední škola Rakovník, příspěvková organizace"
    }, {
        "schoolId": 216,
        "name": "Integrovaná střední škola Slavkov u Brna, příspěvková organizace"
    }, {
        "schoolId": 217,
        "name": "Integrovaná střední škola technická a ekonomická Sokolov, příspěvková organizace"
    }, {
        "schoolId": 218,
        "name": "Integrovaná střední škola technická a ekonomická Sokolov, příspěvková organizace"
    }, {
        "schoolId": 219,
        "name": "Integrovaná střední škola technická Mělník, příspěvková organizace"
    }, {
        "schoolId": 220,
        "name": "Integrovaná střední škola technická, Benešov, Černoleská 1997"
    }, {
        "schoolId": 221,
        "name": "Integrovaná střední škola, , Sokolnice 496"
    }, {
        "schoolId": 222,
        "name": "Integrovaná střední škola, Mladá Boleslav, Na Karmeli 206"
    }, {
        "schoolId": 223,
        "name": "Integrovaná střední škola, Vysoké nad Jizerou, Dr. Farského 300, příspěvková organizace"
    }, {
        "schoolId": 224,
        "name": "ISŠ - COP, Olomoucká 61, Brno"
    }, {
        "schoolId": 225,
        "name": "ISŠ automobilní, Křižíkova 15, Brno"
    }, {
        "schoolId": 226,
        "name": "Jazykové gymnázium Pavla Tigrida"
    }, {
        "schoolId": 227,
        "name": "Jedličkův ústav a Mateřská škola a Základní škola a Střední škola"
    }, {
        "schoolId": 228,
        "name": "JEZDECKÁ AKADEMIE - střední odborná škola Mariánské Lázně s.r.o."
    }, {
        "schoolId": 229,
        "name": "JEZDECKÁ AKADEMIE – střední odborná škola Mariánské Lázně s. r. o."
    }, {
        "schoolId": 230,
        "name": "Jiráskovo gymnázium, Náchod, Řezníčkova 451"
    }, {
        "schoolId": 231,
        "name": "K-TV-středisko praktického vyučování, s.r.o."
    }, {
        "schoolId": 232,
        "name": "Karlínské gymnázium, Praha 8, Pernerova 25"
    }, {
        "schoolId": 233,
        "name": "Klasické gymnázium Modřany a základní škola, s.r.o."
    }, {
        "schoolId": 234,
        "name": "Klvaňovo gymnázium a střední zdravotnická škola Kyjov, příspěvková organizace"
    }, {
        "schoolId": 235,
        "name": "Konzervatoř a střední škola Jana Deyla, příspěvková organizace"
    }, {
        "schoolId": 236,
        "name": "Konzervatoř a Vyšší odborná škola Jaroslava Ježka"
    }, {
        "schoolId": 237,
        "name": "Konzervatoř Brno, příspěvková organizace"
    }, {
        "schoolId": 238,
        "name": "Konzervatoř Duncan centre, Praha 4, Branická 41"
    }, {
        "schoolId": 239,
        "name": "Konzervatoř, České Budějovice, Kanovnická 22"
    }, {
        "schoolId": 240,
        "name": "Křesťanská střední škola, základní škola a mateřská škola Elijáš, Praha 4 - Michle"
    }, {
        "schoolId": 241,
        "name": "Křesťanské gymnázium"
    }, {
        "schoolId": 242,
        "name": "Labská střední odborná škola a Střední odborné učiliště Pardubice, s. r. o"
    }, {
        "schoolId": 243,
        "name": "Lauderova mateřská škola, základní škola a gymnázium při Židovské obci v Praze"
    }, {
        "schoolId": 244,
        "name": "Lékařské a přírodovědné GYMNÁZIUM PRIGO PRAHA, s.r.o."
    }, {
        "schoolId": 245,
        "name": "Lepařovo gymnázium, Jičín, Jiráskova 30"
    }, {
        "schoolId": 246,
        "name": "Malostranské gymnázium, Praha 1, Josefská 7"
    }, {
        "schoolId": 247,
        "name": "Manažerská akademie, soukromá střední škola"
    }, {
        "schoolId": 248,
        "name": "Masarykova obchodní akademie, Jičín, 17. listopadu 220"
    }, {
        "schoolId": 249,
        "name": "Masarykova obchodní akademie, Rakovník, Pražská 1222"
    }, {
        "schoolId": 250,
        "name": "Masarykova střední škola chemická, Praha 1, Křemencova 12"
    }, {
        "schoolId": 251,
        "name": "Masarykova střední škola Letovice, příspěvková organizace"
    }, {
        "schoolId": 252,
        "name": "Masarykovo klasické gymnázium, s.r.o."
    }, {
        "schoolId": 253,
        "name": "Mateřská škola speciální, Základní škola a Praktická škola Diakonie ČCE Čáslav"
    }, {
        "schoolId": 254,
        "name": "Mateřská škola, základní škola a gymnázium sv. Augustina"
    }, {
        "schoolId": 255,
        "name": "Mateřská škola, základní škola a praktická škola Boskovice, příspěvková organizace"
    }, {
        "schoolId": 256,
        "name": "Mateřská škola, Základní škola a Praktická škola při centru ARPIDA, o.p.s."
    }, {
        "schoolId": 257,
        "name": "Mateřská škola, základní škola a praktická škola Znojmo, příspěvková organizace"
    }, {
        "schoolId": 258,
        "name": "Mateřská škola, Základní škola a Praktická škola, České Budějovice, Štítného 3"
    }, {
        "schoolId": 259,
        "name": "Mateřská škola, Základní škola a Praktická škola, Jindřichův Hradec, Jarošovská 1125/II"
    }, {
        "schoolId": 260,
        "name": "Mateřská škola, Základní škola a Praktická škola, Strakonice, Plánkova 430"
    }, {
        "schoolId": 261,
        "name": "Mateřská škola, Základní škola a Praktická škola, Trhové Sviny, Nové Město 228"
    }, {
        "schoolId": 262,
        "name": "Mateřská škola, základní škola a střední škola Daneta, s. r. o."
    }, {
        "schoolId": 263,
        "name": "Mateřská škola, základní škola a střední škola Gellnerka Brno, příspěvková organizace"
    }, {
        "schoolId": 264,
        "name": "Mateřská škola, základní škola a střední škola pro sluchově postižené, České Budějovice, Riegrova 1"
    }, {
        "schoolId": 265,
        "name": "Mateřská škola, základní škola a střední škola Vyškov, příspěvková organizace"
    }, {
        "schoolId": 266,
        "name": "Mateřská škola, základní škola speciální a praktická škola Diakonie ČCE Rolnička Soběslav"
    }, {
        "schoolId": 267,
        "name": "Mendelova Střední Škola It a Veřejnosprávní, Nový Jičín"
    }, {
        "schoolId": 268,
        "name": "Mensa gymnázium, o.p.s."
    }, {
        "schoolId": 269,
        "name": "Městská střední odborná škola, Klobouky u Brna, nám. Míru 6, příspěvková organizace"
    }, {
        "schoolId": 270,
        "name": "Městské víceleté gymnázium Klobouky u Brna, příspěvková organizace"
    }, {
        "schoolId": 271,
        "name": "Metropolitní gymnázium"
    }, {
        "schoolId": 272,
        "name": "Metropolitní odborná umělecká střední škola Praha 4 s.r.o."
    }, {
        "schoolId": 273,
        "name": "Mezinárodní Konzervatoř Praha - International conservatory Prague, s.r.o."
    }, {
        "schoolId": 274,
        "name": "MICHAEL - Střední škola a Vyšší odborná škola reklamní a umělecké tvorby, s.r.o."
    }, {
        "schoolId": 275,
        "name": "Moravské gymnázium Brno s. r. o."
    }, {
        "schoolId": 276,
        "name": "Naše lyceum - střední škola s.r.o."
    }, {
        "schoolId": 277,
        "name": "Obchodní akademie a Jazyková škola s právem státní jazykové zkoušky Mladá Boleslav, příspěvková organizace"
    }, {
        "schoolId": 278,
        "name": "Obchodní akademie a Jazyková škola s právem státní jazykové zkoušky, Liberec, Šamánkova 500/8, příspěvková organizace"
    }, {
        "schoolId": 279,
        "name": "Obchodní akademie a Jazyková škola s právem státní jazykové zkoušky, Písek, Čelakovského 200"
    }, {
        "schoolId": 280,
        "name": "Obchodní akademie a Střední odborná škola logistická, Opava"
    }, {
        "schoolId": 281,
        "name": "Obchodní akademie a Střední odborné učiliště Veselí nad Moravou, příspěvková organizace"
    }, {
        "schoolId": 282,
        "name": "Obchodní akademie a Střední zdravotnická škola Blansko, příspěvková organizace"
    }, {
        "schoolId": 283,
        "name": "Obchodní akademie a vyšší odborná škola Brno, Kotlářská, příspěvková organizace"
    }, {
        "schoolId": 284,
        "name": "Obchodní akademie a Vyšší odborná škola sociální, Ostrava-Mariánské Hory, příspěvková organizace"
    }, {
        "schoolId": 285,
        "name": "Obchodní akademie a Vyšší odborná škola, Příbram I, Na Příkopech 104"
    }, {
        "schoolId": 286,
        "name": "Obchodní akademie Bubeneč"
    }, {
        "schoolId": 287,
        "name": "Obchodní akademie Dr. Edvarda Beneše, Slaný, Smetanovo nám. 1200"
    }, {
        "schoolId": 288,
        "name": "Obchodní akademie Dušní"
    }, {
        "schoolId": 289,
        "name": "Obchodní akademie ELDO, o. p. s."
    }, {
        "schoolId": 290,
        "name": "Obchodní akademie Holešovice"
    }, {
        "schoolId": 291,
        "name": "Obchodní akademie Hovorčovická"
    }, {
        "schoolId": 292,
        "name": "Obchodní Akademie Kroměříž"
    }, {
        "schoolId": 293,
        "name": "Obchodní akademie Neveklov"
    }, {
        "schoolId": 294,
        "name": "Obchodní akademie Praha, s.r.o."
    }, {
        "schoolId": 295,
        "name": "Obchodní akademie T. G. Masaryka a Jazyková škola s právem státní jazykové zkoušky, Jindřichův Hradec, Husova 156"
    }, {
        "schoolId": 296,
        "name": "Obchodní akademie Vinohradská"
    }, {
        "schoolId": 297,
        "name": "Obchodní akademie, Česká Lípa, náměstí Osvobození 422, příspěvková organizace"
    }, {
        "schoolId": 298,
        "name": "Obchodní akademie, České Budějovice, Husova 1"
    }, {
        "schoolId": 299,
        "name": "Obchodní akademie, Hotelová škola a Střední odborná škola, Turnov, Zborovská 519, příspěvková organizace"
    }, {
        "schoolId": 300,
        "name": "Obchodní akademie, Kolín IV, Kutnohorská 41"
    }, {
        "schoolId": 301,
        "name": "Obchodní akademie, Lysá nad Labem, Komenského 1534"
    }, {
        "schoolId": 302,
        "name": "Obchodní akademie, Praha 10, Heroldovy sady 1"
    }, {
        "schoolId": 303,
        "name": "Obchodní akademie, Praha 3, Kubelíkova 37"
    }, {
        "schoolId": 304,
        "name": "Obchodní akademie, ŠKOLA 2000, s.r.o."
    }, {
        "schoolId": 305,
        "name": "Obchodní akademie, Střední odborná škola a Jazyková škola s právem státní jazykové zkoušky, Hradec K"
    }, {
        "schoolId": 306,
        "name": "Obchodní akademie, Střední odborná škola a Střední odborné učiliště, Třeboň, Vrchlického 567"
    }, {
        "schoolId": 307,
        "name": "Obchodní akademie, Střední pedagogická škola a Jazyková škola s právem státní jazykové zkoušky, Beroun, U Stadionu 486"
    }, {
        "schoolId": 308,
        "name": "Obchodní akademie, Střední pedagogická škola, Vyšší odborná škola cestovního ruchu a Jazyková škola"
    }, {
        "schoolId": 309,
        "name": "Obchodní akademie, Tábor, Jiráskova 1615"
    }, {
        "schoolId": 310,
        "name": "Obchodní akademie, Vlašim, V Sadě 1565"
    }, {
        "schoolId": 311,
        "name": "Obchodní akademie, Vyšší odborná škola a Jazyková škola s právem státní jazykové zkoušky Uherské Hradiště"
    }, {
        "schoolId": 312,
        "name": "Obchodní akademie, vyšší odborná škola cestovního ruchu a jazyková škola s právem státní jazykové zk"
    }, {
        "schoolId": 313,
        "name": "Obchodní akademie, vyšší odborná škola cestovního ruchu a jazyková škola s právem státní jazykové zkoušky Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 314,
        "name": "Odborná střední škola podnikání a mediální tvorby Kolín s.r.o."
    }, {
        "schoolId": 315,
        "name": "Odborné učiliště a praktická škola Brno, příspěvková organizace"
    }, {
        "schoolId": 316,
        "name": "Odborné učiliště pro žáky s více vadami, s.r.o."
    }, {
        "schoolId": 317,
        "name": "Odborné učiliště Vyšehrad"
    }, {
        "schoolId": 318,
        "name": "Odborné učiliště, Cvrčovice 131, Pohořelice"
    }, {
        "schoolId": 319,
        "name": "Odborné učiliště, Praktická škola, Základní škola a Mateřská škola Příbram IV, příspěvková organizace"
    }, {
        "schoolId": 320,
        "name": "Praktická škola a Základní škola Lysá nad Labem, příspěvková organizace"
    }, {
        "schoolId": 321,
        "name": "Praktická škola, Základní škola a Mateřská škola Josefa Zemana, Náchod"
    }, {
        "schoolId": 322,
        "name": "Pražská konzervatoř, Praha 1, Na Rejdišti 1"
    }, {
        "schoolId": 323,
        "name": "Pražská taneční konzervatoř a střední odborná škola, s.r.o."
    }, {
        "schoolId": 324,
        "name": "Pražské humanitní gymnázium, školská právnická osoba"
    }, {
        "schoolId": 325,
        "name": "PROINTEPO – Střední škola, Základní škola a Mateřská škola s. r. o."
    }, {
        "schoolId": 326,
        "name": "První české gymnázium v Karlových Varech, příspěvková organizace"
    }, {
        "schoolId": 327,
        "name": "První české gymnázium v Karlových Varech, příspěvková organizace"
    }, {
        "schoolId": 328,
        "name": "První soukromá hotelová škola, spol. s r.o."
    }, {
        "schoolId": 329,
        "name": "První soukromé jazykové gymnázium Hradec Králové spol. s r. o."
    }, {
        "schoolId": 330,
        "name": "Purkyňovo gymnázium, Strážnice, Masarykova 379, příspěvková organizace"
    }, {
        "schoolId": 331,
        "name": "ScioŠkola Brno – střední škola, s. r. o."
    }, {
        "schoolId": 332,
        "name": "ŠKODA AUTO a.s., Střední odborné učiliště strojírenské, odštěpný závod"
    }, {
        "schoolId": 333,
        "name": "Škola Jaroslava Ježka, Mateřská škola, základní škola, praktická škola a základní umělecká škola pro zrakově postižené, Praha 1, Loretánská 19 a 17"
    }, {
        "schoolId": 334,
        "name": "Škola Kavčí hory - Mateřská škola, Základní škola a Střední odborná škola služeb, Praha 4, K Sídlišti 840"
    }, {
        "schoolId": 335,
        "name": "Škola mezinárodních a veřejných vztahů Praha, Střední odborná škola, Gymnázium, s.r.o."
    }, {
        "schoolId": 336,
        "name": "Škola Můj Projekt Mánesova - gymnázium, základní škola a mateřská škola s.r.o."
    }, {
        "schoolId": 337,
        "name": "Škola Můj Projekt Mánesova – gymnázium, základní škola a mateřská škola s. r. o."
    }, {
        "schoolId": 338,
        "name": "Smíchovská střední průmyslová škola a gymnázium"
    }, {
        "schoolId": 339,
        "name": "SOŠ a SOU Hustopeče"
    }, {
        "schoolId": 340,
        "name": "SOŠ a SOU stavební, Pražská 38b, Brno - Bosonohy"
    }, {
        "schoolId": 341,
        "name": "SOŠ a SOU strojírenské a elektrotech., Trnkova 113, Brno - Líšeň"
    }, {
        "schoolId": 342,
        "name": "SOŠ zahradnická a SOU, Masarykova 198, Rajhrad"
    }, {
        "schoolId": 343,
        "name": "Soukromá mateřská škola, základní škola a střední škola Slunce, o.p.s."
    }, {
        "schoolId": 344,
        "name": "Soukromá obchodní akademie Opava s. r. o."
    }, {
        "schoolId": 345,
        "name": "Soukromá obchodní akademie Podnikatel, spol. s r. o."
    }, {
        "schoolId": 346,
        "name": "Soukromá obchodní akademie Podnikatel, spol. s r.o."
    }, {
        "schoolId": 347,
        "name": "Soukromá obchodní akademie Sokolov, s. r. o."
    }, {
        "schoolId": 348,
        "name": "Soukromá obchodní akademie Sokolov, s.r.o."
    }, {
        "schoolId": 349,
        "name": "Soukromá podřipská střední odborná škola a střední odborné učiliště"
    }, {
        "schoolId": 350,
        "name": "Soukromá střední odborná škola a Soukromé střední odborné učiliště BEAN, s.r.o."
    }, {
        "schoolId": 351,
        "name": "Soukromá střední odborná škola manažerská a zdravotnická s. r. o."
    }, {
        "schoolId": 352,
        "name": "Soukromá střední odborná škola START, s.r.o."
    }, {
        "schoolId": 353,
        "name": "Soukromá střední průmyslová škola Břeclav, spol. s r. o. CULTUS"
    }, {
        "schoolId": 354,
        "name": "Soukromá střední škola a základní škola 1. KŠPA Praha s.r.o."
    }, {
        "schoolId": 355,
        "name": "Soukromá střední škola DANAÉ, s.r.o."
    }, {
        "schoolId": 356,
        "name": "Soukromá střední škola gastronomie s.r.o."
    }, {
        "schoolId": 357,
        "name": "Soukromá střední škola podnikatelská – ALTMAN, s. r. o."
    }, {
        "schoolId": 358,
        "name": "Soukromá střední škola výpočetní techniky s.r.o."
    }, {
        "schoolId": 359,
        "name": "SOUKROMÁ STŘEDNÍ UMĚLECKÁ ŠKOLA DESIGNU, s.r.o."
    }, {
        "schoolId": 360,
        "name": "Soukromá střední zdravotnická škola Mělník, o.p.s."
    }, {
        "schoolId": 361,
        "name": "Soukromá výtvarná střední škola s.r.o."
    }, {
        "schoolId": 362,
        "name": "Soukromé gymnázium ARCUS PRAHA 9, s.r.o."
    }, {
        "schoolId": 363,
        "name": "Soukromé osmileté gymnázium DINO-HIGH SCHOOL s.r.o."
    }, {
        "schoolId": 364,
        "name": "Soukromé střední odborné učiliště ATHOZ, spol. s r.o."
    }, {
        "schoolId": 365,
        "name": "Sportovní gymnázium Ludvíka Daňka, Brno, Botanická 70, příspěvková organizace"
    }, {
        "schoolId": 366,
        "name": "Sportovní gymnázium, Kladno, Plzeňská 3103"
    }, {
        "schoolId": 367,
        "name": "SPŠ a VOŠ technická, Sokolská 1, Brno"
    }, {
        "schoolId": 368,
        "name": "SPŠ, SOŠ a SOU, Hradec Králové, Hradební"
    }, {
        "schoolId": 369,
        "name": "SPV - středisko praktického vyučování, s.r.o."
    }, {
        "schoolId": 370,
        "name": "Středisko praktického vyučování - CENTRUM 3000 s.r.o."
    }, {
        "schoolId": 371,
        "name": "Středisko praktického vyučování Asociace starožitníků, s.r.o."
    }, {
        "schoolId": 372,
        "name": "Středisko praktického vyučování Golden Prague Hotel managed by Fairmont s.r.o."
    }, {
        "schoolId": 373,
        "name": "Středisko praktického vyučování GRANDHOTEL PUPP o.p.s."
    }, {
        "schoolId": 374,
        "name": "Středisko praktického vyučování NAKLADATELSTVÍ PRIMUS s.r.o."
    }, {
        "schoolId": 375,
        "name": "Středisko praktického vyučování truhlářů Ledenice spol. s r.o."
    }, {
        "schoolId": 376,
        "name": "Středisko praktického vyučování Vinohrady, s.r.o."
    }, {
        "schoolId": 377,
        "name": "STŘEDISKO PRAKTICKÉHO VYUČOVÁNÍ ZLATNICKÉ A RYTECKÉ, s.r.o."
    }, {
        "schoolId": 378,
        "name": "Středisko praktického vyučování, Praha 5, Seydlerova 2451"
    }, {
        "schoolId": 379,
        "name": "Střední hotelová škola, Vyšší odborná škola a Jazyková škola s právem státní jazykové zkoušky s.r.o."
    }, {
        "schoolId": 380,
        "name": "Střední lesnická škola a Střední odborné učiliště, Křivoklát, Písky 181"
    }, {
        "schoolId": 381,
        "name": "Střední lesnická škola Žlutice, příspěvková organizace"
    }, {
        "schoolId": 382,
        "name": "Střední lesnická škola Žlutice, příspěvková organizace"
    }, {
        "schoolId": 383,
        "name": "Střední odborná škola - Centrum odborné přípravy a Gymnázium"
    }, {
        "schoolId": 384,
        "name": "Střední odborná škola a Gymnázium Staré Město"
    }, {
        "schoolId": 385,
        "name": "Střední odborná škola a Střední odborné učiliště dopravní Čáslav, příspěvková organizace"
    }, {
        "schoolId": 386,
        "name": "Střední odborná škola a střední odborné učiliště HEUREKA s.r.o."
    }, {
        "schoolId": 387,
        "name": "Střední odborná škola a střední odborné učiliště Hustopeče, příspěvková organizace"
    }, {
        "schoolId": 388,
        "name": "Střední odborná škola a Střední odborné učiliště Jílové u Prahy, příspěvková organizace"
    }, {
        "schoolId": 389,
        "name": "Střední odborná škola a Střední odborné učiliště Kuřim"
    }, {
        "schoolId": 390,
        "name": "Střední odborná škola a Střední odborné učiliště řemesel, Kutná Hora, Čáslavská 202"
    }, {
        "schoolId": 391,
        "name": "Střední odborná škola a Střední odborné učiliště Vyškov, příspěvková organizace"
    }, {
        "schoolId": 392,
        "name": "Střední odborná škola a Střední odborné učiliště, Beroun - Hlinky, Okružní 1404"
    }, {
        "schoolId": 393,
        "name": "Střední odborná škola a Střední odborné učiliště, Dubno"
    }, {
        "schoolId": 394,
        "name": "Střední odborná škola a Střední odborné učiliště, Hněvkovice 865"
    }, {
        "schoolId": 395,
        "name": "Střední odborná škola a Střední odborné učiliště, Horky nad Jizerou 35"
    }, {
        "schoolId": 396,
        "name": "Střední odborná škola a Střední odborné učiliště, Hořovice, Palackého náměstí 100"
    }, {
        "schoolId": 397,
        "name": "Střední odborná škola a Střední odborné učiliště, Hradec Králové, Vocelova 1338"
    }, {
        "schoolId": 398,
        "name": "Střední odborná škola a Střední odborné učiliště, Jindřichův Hradec, Jáchymova 478"
    }, {
        "schoolId": 399,
        "name": "Střední odborná škola a Střední odborné učiliště, Kaplice, Pohorská 86"
    }, {
        "schoolId": 400,
        "name": "Střední odborná škola a Střední odborné učiliště, Kladno, Dubská"
    }, {
        "schoolId": 401,
        "name": "Střední odborná škola a Střední odborné učiliště, Kladno, náměstí Edvarda Beneše 2353"
    }, {
        "schoolId": 402,
        "name": "Střední odborná škola a Střední odborné učiliště, Městec Králové, T. G. Masaryka 4"
    }, {
        "schoolId": 403,
        "name": "Střední odborná škola a Střední odborné učiliště, Milevsko, Čs. armády 777"
    }, {
        "schoolId": 404,
        "name": "Střední odborná škola a Střední odborné učiliště, Mladá Boleslav, Jičínská 762"
    }, {
        "schoolId": 405,
        "name": "Střední odborná škola a Střední odborné učiliště, Neratovice, Školní 664"
    }, {
        "schoolId": 406,
        "name": "Střední odborná škola a Střední odborné učiliště, Nymburk, V Kolonii 1804"
    }, {
        "schoolId": 407,
        "name": "Střední odborná škola a Střední odborné učiliště, Písek, Komenského 86"
    }, {
        "schoolId": 408,
        "name": "Střední odborná škola a Střední odborné učiliště, Praha - Čakovice"
    }, {
        "schoolId": 409,
        "name": "Střední odborná škola a Střední odborné učiliště, Vlašim, Zámek 1"
    }, {
        "schoolId": 410,
        "name": "Střední odborná škola a Střední zdravotnická škola Benešov, příspěvková organizace"
    }, {
        "schoolId": 411,
        "name": "Střední odborná škola Čelákovice s.r.o."
    }, {
        "schoolId": 412,
        "name": "Střední odborná škola civilního letectví, Praha - Ruzyně"
    }, {
        "schoolId": 413,
        "name": "Střední odborná škola EDUCAnet Brno, o. p. s."
    }, {
        "schoolId": 414,
        "name": "Střední odborná škola ekologická a potravinářská, Veselí nad Lužnicí, Blatské sídliště 600/I"
    }, {
        "schoolId": 415,
        "name": "Střední odborná škola elektrotechnická, Centrum odborné přípravy, Hluboká nad Vltavou, Zvolenovská 537"
    }, {
        "schoolId": 416,
        "name": "Střední odborná škola FORTIKA, Tišnovská 15, Lomnice u Tišnova"
    }, {
        "schoolId": 417,
        "name": "Střední odborná škola informatiky a spojů a Střední odborné učiliště, Kolín, Jaselská 826"
    }, {
        "schoolId": 418,
        "name": "Střední odborná škola Jarov"
    }, {
        "schoolId": 419,
        "name": "Střední odborná škola Karlovy Vary, s. r. o."
    }, {
        "schoolId": 420,
        "name": "Střední odborná škola Karlovy Vary, s.r.o."
    }, {
        "schoolId": 421,
        "name": "Střední odborná škola logistických služeb"
    }, {
        "schoolId": 422,
        "name": "Střední odborná škola managementu a práva, s. r. o."
    }, {
        "schoolId": 423,
        "name": "Střední odborná škola managementu a práva, s.r.o."
    }, {
        "schoolId": 424,
        "name": "Střední odborná škola MORAVA o. p. s."
    }, {
        "schoolId": 425,
        "name": "Střední odborná škola multimediální a propagační tvorby, s.r.o."
    }, {
        "schoolId": 426,
        "name": "Střední odborná škola Nové Město na Moravě"
    }, {
        "schoolId": 427,
        "name": "Střední odborná škola obchodní s.r.o."
    }, {
        "schoolId": 428,
        "name": "Střední odborná škola podnikání a obchodu, spol. s r.o., Prostějov"
    }, {
        "schoolId": 429,
        "name": "Střední odborná škola podnikatelská PROFIT, spol. s r.o."
    }, {
        "schoolId": 430,
        "name": "Střední odborná škola pro administrativu Evropské unie, Praha 9, Lipí 1911"
    }, {
        "schoolId": 431,
        "name": "Střední odborná škola sociální a zdravotnická – Evangelická akademie"
    }, {
        "schoolId": 432,
        "name": "Střední odborná škola sociální svaté Zdislavy"
    }, {
        "schoolId": 433,
        "name": "Střední odborná škola stavební a Střední odborné učiliště stavební, Kolín II, Pražská 112"
    }, {
        "schoolId": 434,
        "name": "Střední odborná škola stavební Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 435,
        "name": "Střední odborná škola stavební Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 436,
        "name": "Střední odborná škola stravování Říčany s.r.o."
    }, {
        "schoolId": 437,
        "name": "Střední odborná škola strojní a elektrotechnická, Velešín, U Hřiště 527"
    }, {
        "schoolId": 438,
        "name": "Střední odborná škola uměleckořemeslná s.r.o."
    }, {
        "schoolId": 439,
        "name": "Střední odborná škola veterinární, Hradec Králové-Kukleny, Pražská 68"
    }, {
        "schoolId": 440,
        "name": "Střední odborná škola veterinární, mechanizační a zahradnická a Jazyková škola s právem státní jazykové zkoušky, České Budějovice, Rudolfovská 92"
    }, {
        "schoolId": 441,
        "name": "Střední odborná škola zdravotnická a Střední odborné učiliště, Český Krumlov, Tavírna 342"
    }, {
        "schoolId": 442,
        "name": "Střední odborná škola Znojmo, Dvořákova, příspěvková organizace"
    }, {
        "schoolId": 443,
        "name": "Střední odborná škola, Blatná, V Jezárkách 745"
    }, {
        "schoolId": 444,
        "name": "Střední odborná škola, Frýdek-Místek, příspěvková organizace"
    }, {
        "schoolId": 445,
        "name": "Střední odborná škola, Liberec, Jablonecká 999, příspěvková organizace"
    }, {
        "schoolId": 446,
        "name": "Střední odborná škola, Praha 5, Drtinova 3/498"
    }, {
        "schoolId": 447,
        "name": "Střední odborné učiliště"
    }, {
        "schoolId": 448,
        "name": "Střední odborné učiliště a Praktická škola Kladno - Vrapice, příspěvková organizace"
    }, {
        "schoolId": 449,
        "name": "Střední odborné učiliště a Střední odborná škola SČMSD, Znojmo, s. r. o."
    }, {
        "schoolId": 450,
        "name": "Střední odborné učiliště gastronomie"
    }, {
        "schoolId": 451,
        "name": "Střední odborné učiliště kadeřnické, Praha 8, Karlínské náměstí 8/225"
    }, {
        "schoolId": 452,
        "name": "Střední odborné učiliště Kyjov, příspěvková organizace od 1. 1. 2022 Střední škola polytechnická Ky"
    }, {
        "schoolId": 453,
        "name": "Střední odborné učiliště Slaný, příspěvková organizace"
    }, {
        "schoolId": 454,
        "name": "Střední odborné učiliště služeb Vodňany, Zeyerovy sady 43/II"
    }, {
        "schoolId": 455,
        "name": "Střední odborné učiliště společného stravování, Poděbrady, Dr. Beneše 413/II"
    }, {
        "schoolId": 456,
        "name": "Střední odborné učiliště stavební, Benešov, Jana Nohy 1302"
    }, {
        "schoolId": 457,
        "name": "Střední odborné učiliště STRAVON spol. s r.o."
    }, {
        "schoolId": 458,
        "name": "Střední odborné učiliště tradičních řemesel a Vyšší odborná škola, spol. s r. o."
    }, {
        "schoolId": 459,
        "name": "Střední odborné učiliště zemědělské a služeb, Dačice, nám. Republiky 86"
    }, {
        "schoolId": 460,
        "name": "Střední odborné učiliště, Blatná, U Sladovny 671"
    }, {
        "schoolId": 461,
        "name": "Střední odborné učiliště, Čáslav, Žižkovo nám. 75"
    }, {
        "schoolId": 462,
        "name": "Střední odborné učiliště, Hluboš 178"
    }, {
        "schoolId": 463,
        "name": "Střední odborné učiliště, Hubálov 17"
    }, {
        "schoolId": 464,
        "name": "Střední odborné učiliště, Liběchov, Boží Voda 230"
    }, {
        "schoolId": 465,
        "name": "Střední odborné učiliště, Lišov, tř. 5. května 3"
    }, {
        "schoolId": 466,
        "name": "Střední odborné učiliště, Nové Strašecí, Sportovní 1135"
    }, {
        "schoolId": 467,
        "name": "Střední odborné učiliště, Praha - Radotín"
    }, {
        "schoolId": 468,
        "name": "Střední odborné učiliště, Praha 4, Ohradní 57"
    }, {
        "schoolId": 469,
        "name": "Střední odborné učiliště, Sedlčany, Petra Bezruče 364"
    }, {
        "schoolId": 470,
        "name": "Střední pedagogická škola Boskovice, příspěvková organizace"
    }, {
        "schoolId": 471,
        "name": "Střední pedagogická škola Futurum, s.r.o."
    }, {
        "schoolId": 472,
        "name": "Střední pedagogická škola, gymnázium a vyšší odborná škola Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 473,
        "name": "Střední pedagogická škola, gymnázium a vyšší odborná škola Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 474,
        "name": "Střední průmyslová škola a Gymnázium Na Třebešíně"
    }, {
        "schoolId": 475,
        "name": "Střední průmyslová škola a Střední odborné učiliště Pelhřimov"
    }, {
        "schoolId": 476,
        "name": "Střední průmyslová škola a Vyšší odborná škola Chomutov"
    }, {
        "schoolId": 477,
        "name": "Střední průmyslová škola a Vyšší odborná škola, Kladno, Jana Palacha 1840"
    }, {
        "schoolId": 478,
        "name": "Střední průmyslová škola a Vyšší odborná škola, Písek, Karla Čapka 402"
    }, {
        "schoolId": 479,
        "name": "Střední průmyslová škola a Vyšší odborná škola, Příbram II, Hrabákova 271"
    }, {
        "schoolId": 480,
        "name": "Střední průmyslová škola chemická Brno, Vranovská, příspěvková organizace"
    }, {
        "schoolId": 481,
        "name": "Střední průmyslová škola dopravní, a.s."
    }, {
        "schoolId": 482,
        "name": "Střední průmyslová škola Edvarda Beneše a obchodní akademie Břeclav, příspěvková organizace"
    }, {
        "schoolId": 483,
        "name": "Střední průmyslová škola elektrotechnická Havířov"
    }, {
        "schoolId": 484,
        "name": "Střední průmyslová škola elektrotechnická, Praha 10, V Úžlabině 320"
    }, {
        "schoolId": 485,
        "name": "Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30"
    }, {
        "schoolId": 486,
        "name": "Střední průmyslová škola elektrotechniky a informačních technologií, Dobruška, Čs. odboje 670"
    }, {
        "schoolId": 487,
        "name": "Střední průmyslová škola Emila Kolbena Rakovník, příspěvková organizace"
    }, {
        "schoolId": 488,
        "name": "Střední průmyslová škola Hranice"
    }, {
        "schoolId": 489,
        "name": "Střední průmyslová škola Jedovnice, příspěvková organizace"
    }, {
        "schoolId": 490,
        "name": "Střední průmyslová škola na Proseku"
    }, {
        "schoolId": 491,
        "name": "Střední průmyslová škola Ostrov, příspěvková organizace"
    }, {
        "schoolId": 492,
        "name": "Střední průmyslová škola Ostrov, příspěvková organizace"
    }, {
        "schoolId": 493,
        "name": "Střední průmyslová škola Otty Wichterleho, příspěvková organizace"
    }, {
        "schoolId": 494,
        "name": "Střední průmyslová škola sdělovací techniky, Praha 1, Panská 3"
    }, {
        "schoolId": 495,
        "name": "Střední průmyslová škola stavební a Obchodní akademie arch. Jana Letzela, Náchod, příspěvková organi"
    }, {
        "schoolId": 496,
        "name": "Střední průmyslová škola stavební a Obchodní akademie, Kladno, Cyrila Boudy 2954"
    }, {
        "schoolId": 497,
        "name": "Střední průmyslová škola stavební Brno, příspěvková organizace"
    }, {
        "schoolId": 498,
        "name": "Střední průmyslová škola stavební Josefa Gočára, Praha 4, Družstevní ochoz 3"
    }, {
        "schoolId": 499,
        "name": "Střední průmyslová škola stavební, České Budějovice, Resslova 2"
    }, {
        "schoolId": 500,
        "name": "Střední průmyslová škola stavební, Hradec Králové, Pospíšilova tř. 787"
    }, {
        "schoolId": 501,
        "name": "Střední průmyslová škola stavební, Liberec 1, Sokolovské náměstí 14, příspěvková organizace"
    }, {
        "schoolId": 502,
        "name": "Střední průmyslová škola stavební, Mělník, Českobratrská 386"
    }, {
        "schoolId": 503,
        "name": "Střední průmyslová škola stavební, Plzeň, Chodské nám. 2"
    }, {
        "schoolId": 504,
        "name": "Střední průmyslová škola strojírenská a Jazyková škola s právem státní jazykové zkoušky, Kolín IV, Heverova 191"
    }, {
        "schoolId": 505,
        "name": "Střední průmyslová škola strojní a elektrotechnická a Vyšší odborná škola, Liberec 1, Masarykova 3, příspěvková organizace"
    }, {
        "schoolId": 506,
        "name": "Střední průmyslová škola strojní a elektrotechnická, České Budějovice, Dukelská 13"
    }, {
        "schoolId": 507,
        "name": "Střední průmyslová škola strojní a stavební, Tábor, Komenského 1670"
    }, {
        "schoolId": 508,
        "name": "Střední průmyslová škola strojnická, škola hlavního města Prahy, Praha 1, Betlémská 4/287"
    }, {
        "schoolId": 509,
        "name": "Střední průmyslová škola technická, Jablonec nad Nisou, Belgická 4852, příspěvková organizace"
    }, {
        "schoolId": 510,
        "name": "Střední průmyslová škola textilní, Liberec, Tyršova 1, příspěvková organizace"
    }, {
        "schoolId": 511,
        "name": "Střední průmyslová škola zeměměřická a Geografické gymnázium Praha"
    }, {
        "schoolId": 512,
        "name": "Střední průmyslová škola Zlín"
    }, {
        "schoolId": 513,
        "name": "Střední průmyslová škola, Česká Lípa, Havlíčkova 426, příspěvková organizace"
    }, {
        "schoolId": 514,
        "name": "Střední průmyslová škola, Mladá Boleslav, Havlíčkova 456"
    }, {
        "schoolId": 515,
        "name": "Střední průmyslová škola, Obchodní akademie a Jazyková škola s právem státní jazykové zkoušky, Frýdek Místek"
    }, {
        "schoolId": 516,
        "name": "Střední průmyslová škola, Odborná škola a Základní škola, Nové Město nad Metují"
    }, {
        "schoolId": 517,
        "name": "Střední průmyslová škola, Ostrava - Vítkovice, příspěvková organizace"
    }, {
        "schoolId": 518,
        "name": "Střední průmyslová škola, Střední odborná škola a Střední odborné učiliště, Hradec Králové"
    }, {
        "schoolId": 519,
        "name": "Střední průmyslová škola, Vlašim, Komenského 41"
    }, {
        "schoolId": 520,
        "name": "Střední rybářská škola a Vyšší odborná škola vodního hospodářství a ekologie, Vodňany, Zátiší 480"
    }, {
        "schoolId": 521,
        "name": "Střední škola - Waldorfské lyceum"
    }, {
        "schoolId": 522,
        "name": "Střední škola a Jazyková škola s právem státní jazykové zkoušky, Volyně, Lidická 135"
    }, {
        "schoolId": 523,
        "name": "Střední škola a Mateřská škola Aloyse Klara"
    }, {
        "schoolId": 524,
        "name": "Střední škola a Mateřská škola, Liberec, Na Bojišti 15, příspěvková organizace"
    }, {
        "schoolId": 525,
        "name": "Střední škola a vyšší odborná škola aplikované kybernetiky s. r. o."
    }, {
        "schoolId": 526,
        "name": "Střední škola a Vyšší odborná škola cestovního ruchu, České Budějovice, Senovážné náměstí 12"
    }, {
        "schoolId": 527,
        "name": "Střední škola a vyšší odborná škola umělecká a řemeslná"
    }, {
        "schoolId": 528,
        "name": "Střední škola a Základní škola Beroun, příspěvková organizace"
    }, {
        "schoolId": 529,
        "name": "Střední škola a Základní škola Jesenice, příspěvková organizace"
    }, {
        "schoolId": 530,
        "name": "Střední škola a Základní škola Tišnov, nám. Míru 22, Tišnov"
    }, {
        "schoolId": 531,
        "name": "Střední škola a Základní škola, Vimperk, Nerudova 267"
    }, {
        "schoolId": 532,
        "name": "Střední škola André Citroëna Boskovice, příspěvková organizace"
    }, {
        "schoolId": 533,
        "name": "Střední škola ARCUS, s.r.o."
    }, {
        "schoolId": 534,
        "name": "Střední škola automobilní a informatiky"
    }, {
        "schoolId": 535,
        "name": "Střední škola automobilní Kyjov, příspěvková organizace"
    }, {
        "schoolId": 536,
        "name": "Střední škola Brno, Charbulova, příspěvková organizace"
    }, {
        "schoolId": 537,
        "name": "Střední škola cestovního ruchu a gastronomie, s. r. o."
    }, {
        "schoolId": 538,
        "name": "Střední škola designu a řemesel Kladno, příspěvková organizace"
    }, {
        "schoolId": 539,
        "name": "Střední škola designu a umění, knižní kultury a ekonomiky Náhorní"
    }, {
        "schoolId": 540,
        "name": "Střední škola designu interiéru Kateřinky - Liberec, s.r.o."
    }, {
        "schoolId": 541,
        "name": "Střední škola designu Lysá nad Labem, příspěvková organizace"
    }, {
        "schoolId": 542,
        "name": "Střední škola dopravy, obchodu a služeb Moravský Krumlov, příspěvková organizace"
    }, {
        "schoolId": 543,
        "name": "Střední škola dostihového sportu a jezdectví"
    }, {
        "schoolId": 544,
        "name": "Střední škola Educhem, a.s., Meziboří"
    }, {
        "schoolId": 545,
        "name": "Střední škola ekonomická se sportovním zaměřením, s.r.o."
    }, {
        "schoolId": 546,
        "name": "Střední škola elektrotechnická, Lipník nad Bečvou"
    }, {
        "schoolId": 547,
        "name": "Střední škola elektrotechnická, Lipník nad Bečvou, Tyršova 781"
    }, {
        "schoolId": 548,
        "name": "Střední škola elektrotechniky a strojírenství"
    }, {
        "schoolId": 549,
        "name": "Střední škola Euroinstitut"
    }, {
        "schoolId": 550,
        "name": "Střední škola Euroinstitut v Karlovarském kraji"
    }, {
        "schoolId": 551,
        "name": "Střední škola Euroinstitut v Praze"
    }, {
        "schoolId": 552,
        "name": "Střední škola F. D. Roosevelta pro TP, Křižíkova 11/1694, Brno"
    }, {
        "schoolId": 553,
        "name": "Střední škola gastronomická a hotelová s.r.o."
    }, {
        "schoolId": 554,
        "name": "Střední škola gastronomie a hotelnictví Mladá Boleslav, s.r.o."
    }, {
        "schoolId": 555,
        "name": "Střední škola gastronomie a služeb, Liberec, Dvorská 447/29, příspěvková organizace"
    }, {
        "schoolId": 556,
        "name": "Střední škola gastronomie, hotelnictví a lesnictví Bzenec, příspěvková organizace"
    }, {
        "schoolId": 557,
        "name": "Střední škola Gemini Brno, příspěvková organizace"
    }, {
        "schoolId": 558,
        "name": "Střední škola grafická Brno, příspěvková organizace"
    }, {
        "schoolId": 559,
        "name": "Střední škola hospodářská a lesnická, Frýdlant, Bělíkova 1387, příspěvková organizace"
    }, {
        "schoolId": 560,
        "name": "Střední škola hotelnictví a gastronomie International, s.r.o."
    }, {
        "schoolId": 561,
        "name": "Střední škola hotelnictví a gastronomie SČMSD Praha, s.r.o."
    }, {
        "schoolId": 562,
        "name": "Střední škola inf. tech. a soc. péče, Purkyňova 97, Brno"
    }, {
        "schoolId": 563,
        "name": "Střední škola informatiky a právních studií, z.ú."
    }, {
        "schoolId": 564,
        "name": "Střední škola informatiky elektrotechniky a řemesel Rožnov pod Radhoštěm"
    }, {
        "schoolId": 565,
        "name": "Střední škola informatiky, poštovnictví a finančnictví Brno, příspěvková organizace"
    }, {
        "schoolId": 566,
        "name": "Střední škola Jana Blahoslava"
    }, {
        "schoolId": 567,
        "name": "Střední škola Jeronýmova České Budějovice, s.r.o."
    }, {
        "schoolId": 568,
        "name": "Střední škola Kateřinky - Liberec, s.r.o."
    }, {
        "schoolId": 569,
        "name": "Střední škola Klíč s.r.o."
    }, {
        "schoolId": 570,
        "name": "Střední škola KNIH, o. p. s."
    }, {
        "schoolId": 571,
        "name": "Střední škola knižní kultury s.r.o."
    }, {
        "schoolId": 572,
        "name": "Střední škola kosmetiky a hotelnictví BEAN, s.r.o."
    }, {
        "schoolId": 573,
        "name": "Střední škola letecké a výpočetní techniky, Odolena Voda, U Letiště 370"
    }, {
        "schoolId": 574,
        "name": "Střední škola logistická Dalovice, příspěvková organizace"
    }, {
        "schoolId": 575,
        "name": "Střední škola logistická Dalovice, příspěvková organizace"
    }, {
        "schoolId": 576,
        "name": "Střední škola logistiky a chemie, Olomouc, U Hradiska 29"
    }, {
        "schoolId": 577,
        "name": "Střední škola managementu a grafiky"
    }, {
        "schoolId": 578,
        "name": "Střední škola managementu a služeb s.r.o."
    }, {
        "schoolId": 579,
        "name": "Střední škola mediální grafiky a tisku, s.r.o."
    }, {
        "schoolId": 580,
        "name": "Střední škola obchodní"
    }, {
        "schoolId": 581,
        "name": "Střední škola obchodní, České Budějovice, Husova 9"
    }, {
        "schoolId": 582,
        "name": "Střední škola obchodní, Kolín IV, Havlíčkova 42"
    }, {
        "schoolId": 583,
        "name": "Střední škola obchodu, služeb a řemesel a Jazyková škola s právem státní jazykové zkoušky, Tábor, Bydlinského 2474"
    }, {
        "schoolId": 584,
        "name": "Střední škola oděvního designu Kateřinky - Liberec, s.r.o."
    }, {
        "schoolId": 585,
        "name": "Střední škola pedagogická a sociálně právní a střední zdravotnická škola Jana Blahoslava"
    }, {
        "schoolId": 586,
        "name": "Střední škola podnikání a gastronomie"
    }, {
        "schoolId": 587,
        "name": "Střední škola Podnikatelská akademie, s.r.o."
    }, {
        "schoolId": 588,
        "name": "Střední škola podnikatelská HERMÉS MB s.r.o."
    }, {
        "schoolId": 589,
        "name": "Střední škola polytechnická Brno, Jílová, příspěvková organizace"
    }, {
        "schoolId": 590,
        "name": "Střední škola polytechnická, České Budějovice, Nerudova 59"
    }, {
        "schoolId": 591,
        "name": "Střední škola právní - Právní akademie, s.r.o."
    }, {
        "schoolId": 592,
        "name": "Střední škola profesní přípravy, Hradec Králové"
    }, {
        "schoolId": 593,
        "name": "Střední škola průmyslová a umělecká Hodonín, příspěvková organizace"
    }, {
        "schoolId": 594,
        "name": "Střední škola řemesel a služeb, Jablonec nad Nisou, Smetanova 66, příspěvková organizace"
    }, {
        "schoolId": 595,
        "name": "Střední škola řemesel a Základní škola, Hořice"
    }, {
        "schoolId": 596,
        "name": "Střední škola řemesel Kunice, příspěvková organizace"
    }, {
        "schoolId": 597,
        "name": "Střední škola řemeslná a Základní škola, Soběslav, Wilsonova 405"
    }, {
        "schoolId": 598,
        "name": "Střední škola řemeslná, Jaroměř, Studničkova 260"
    }, {
        "schoolId": 599,
        "name": "Střední škola rybářská a vodohospodářská Jakuba Krčína, Třeboň, Táboritská 688"
    }, {
        "schoolId": 600,
        "name": "Střední škola Sion High School, Hradec Králové"
    }, {
        "schoolId": 601,
        "name": "Střední škola služeb a řemesel, Stochov, J. Šípka 187"
    }, {
        "schoolId": 602,
        "name": "Střední škola služeb, obchodu a gastronomie"
    }, {
        "schoolId": 603,
        "name": "Střední škola Spektrum Mladá Boleslav, s.r.o."
    }, {
        "schoolId": 604,
        "name": "Střední škola spojů a informatiky, Tábor, Bydlinského 2474"
    }, {
        "schoolId": 605,
        "name": "Střední škola stravování a služeb Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 606,
        "name": "Střední škola stravování a služeb Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 607,
        "name": "Střední škola Strážnice, příspěvková organizace"
    }, {
        "schoolId": 608,
        "name": "Střední škola strojírenská a elektrotechnická"
    }, {
        "schoolId": 609,
        "name": "Střední škola strojní, stavební a dopravní, Liberec II, Truhlářská 360/3, příspěvková organizace"
    }, {
        "schoolId": 610,
        "name": "Střední škola technická a dopravní Gustava Habrmana Česká Třebová"
    }, {
        "schoolId": 611,
        "name": "Střední škola technická a dopravní Ostrava-Vítkovice"
    }, {
        "schoolId": 612,
        "name": "Střední škola technická a gastronomická Blansko, příspěvková organizace"
    }, {
        "schoolId": 613,
        "name": "Střední škola technická a obchodní, Dačice, Strojírenská 304"
    }, {
        "schoolId": 614,
        "name": "Střední škola technická a řemeslná, Nový Bydžov, Dr. M. Tyrše 112"
    }, {
        "schoolId": 615,
        "name": "Střední škola technická Znojmo, příspěvková organizace"
    }, {
        "schoolId": 616,
        "name": "Střední škola technických oborů. Lidická 600/1a 736 01 Havířov"
    }, {
        "schoolId": 617,
        "name": "Střední škola tradičních řemesel HERMÉS MB s.r.o."
    }, {
        "schoolId": 618,
        "name": "Střední škola uměleckomanažerská, s. r. o."
    }, {
        "schoolId": 619,
        "name": "Střední škola umění a designu a Vyšší odborná škola Brno, příspěvková organizace"
    }, {
        "schoolId": 620,
        "name": "Střední škola VIZE"
    }, {
        "schoolId": 621,
        "name": "Střední škola vizuální tvorby, s. r. o."
    }, {
        "schoolId": 622,
        "name": "Střední škola zahradnická, Kopidlno, náměstí Hilmarovo 1"
    }, {
        "schoolId": 623,
        "name": "Střední škola živnostenská a ZŠ, Planá"
    }, {
        "schoolId": 624,
        "name": "Střední škola živnostenská Sokolov, příspěvková organizace"
    }, {
        "schoolId": 625,
        "name": "Střední škola živnostenská Sokolov, příspěvková organizace"
    }, {
        "schoolId": 626,
        "name": "Střední škola – Podorlické vzdělávací centrum, Dobruška"
    }, {
        "schoolId": 627,
        "name": "Střední škola, České Velenice, Revoluční 220"
    }, {
        "schoolId": 628,
        "name": "Střední škola, Lomnice nad Popelkou, Antala Staška 213, příspěvková organizace"
    }, {
        "schoolId": 629,
        "name": "Střední škola, Rokycany, Jeřabinová 96/III"
    }, {
        "schoolId": 630,
        "name": "Střední škola, Semily, příspěvková organizace"
    }, {
        "schoolId": 631,
        "name": "Střední škola, Trhové Sviny, Školní 709"
    }, {
        "schoolId": 632,
        "name": "Střední škola, základní škola a mateřská škola da Vinci"
    }, {
        "schoolId": 633,
        "name": "Střední škola, základní škola a mateřská škola Kraslice, příspěvková organizace"
    }, {
        "schoolId": 634,
        "name": "Střední škola, základní škola a mateřská škola Kraslice, příspěvková organizace"
    }, {
        "schoolId": 635,
        "name": "Střední škola, základní škola a mateřská škola pro sluchově postižené, Praha 5, Holečkova 4"
    }, {
        "schoolId": 636,
        "name": "Střední škola, Základní škola a Mateřská škola pro sluchově postižené, Praha 5, Výmolova 169"
    }, {
        "schoolId": 637,
        "name": "Střední škola, Základní škola a Mateřská škola Rakovník, příspěvková organizace"
    }, {
        "schoolId": 638,
        "name": "Střední škola, Základní škola a Mateřská škola, Praha 10, Chotouňská 476"
    }, {
        "schoolId": 639,
        "name": "Střední škola, Základní škola, Mateřská škola, Dětský domov a Speciálně pedagogické centrum Mladá Boleslav, příspěvková organizace"
    }, {
        "schoolId": 640,
        "name": "Střední umělecká škola v Liberci s.r.o."
    }, {
        "schoolId": 641,
        "name": "Střední uměleckoprůmyslová škola a Vyšší odborná škola, Jablonec nad Nisou, Horní náměstí 1, příspěvková organizace"
    }, {
        "schoolId": 642,
        "name": "Střední uměleckoprůmyslová škola a Vyšší odborná škola, Turnov, Skálova 373, příspěvková organizace"
    }, {
        "schoolId": 643,
        "name": "Střední uměleckoprůmyslová škola hudebních nástrojů a nábytku, Hradec Králové, 17. listopadu 1202"
    }, {
        "schoolId": 644,
        "name": "Střední uměleckoprůmyslová škola keramická a sklářská Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 645,
        "name": "Střední uměleckoprůmyslová škola keramická a sklářská Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 646,
        "name": "Střední uměleckoprůmyslová škola sklářská, Kamenický Šenov, Havlíčkova 57, příspěvková organizace"
    }, {
        "schoolId": 647,
        "name": "Střední uměleckoprůmyslová škola sklářská, Železný Brod"
    }, {
        "schoolId": 648,
        "name": "Střední uměleckoprůmyslová škola sklářská, Železný Brod, Smetanovo zátiší 470, příspěvková organizace"
    }, {
        "schoolId": 649,
        "name": "Střední uměleckoprůmyslová škola sochařská a kamenická, Hořice, příspěvková organizace"
    }, {
        "schoolId": 650,
        "name": "Střední uměleckoprůmyslová škola sv. Anežky České, Český Krumlov, Tavírna 109"
    }, {
        "schoolId": 651,
        "name": "Střední uměleckoprůmyslová škola, Bechyně, Písecká 203"
    }, {
        "schoolId": 652,
        "name": "Střední vinařská škola Valtice, příspěvková organizace"
    }, {
        "schoolId": 653,
        "name": "Střední zahradnická škola a Střední odborné učiliště s.r.o."
    }, {
        "schoolId": 654,
        "name": "Střední zdravotnická škola"
    }, {
        "schoolId": 655,
        "name": "Střední zdravotnická škola a Střední odborná škola, Česká Lípa, příspěvková organizace"
    }, {
        "schoolId": 656,
        "name": "Střední zdravotnická škola a vyšší odborná škola Cheb, příspěvková organizace"
    }, {
        "schoolId": 657,
        "name": "Střední zdravotnická škola a vyšší odborná škola Cheb, příspěvková organizace"
    }, {
        "schoolId": 658,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická Brno, Merhautova, příspěvková organiza"
    }, {
        "schoolId": 659,
        "name": "Střední zdravotnická škola a vyšší odborná škola zdravotnická Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 660,
        "name": "Střední zdravotnická škola a vyšší odborná škola zdravotnická Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 661,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická Znojmo, příspěvková organizace"
    }, {
        "schoolId": 662,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, České Budějovice, Husova 3"
    }, {
        "schoolId": 663,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Kladno, Havířská 1141"
    }, {
        "schoolId": 664,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Kolín, Karoliny Světlé 135"
    }, {
        "schoolId": 665,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Liberec, Kostelní 9, příspěvková organizace"
    }, {
        "schoolId": 666,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Mladá Boleslav, B. Němcové 482"
    }, {
        "schoolId": 667,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Nymburk, Soudní 20"
    }, {
        "schoolId": 668,
        "name": "Střední zdravotnická škola a Vyšší odborná škola zdravotnická, Příbram I, Jiráskovy sady 113"
    }, {
        "schoolId": 669,
        "name": "Střední zdravotnická škola Brno, Jaselská, příspěvková organizace"
    }, {
        "schoolId": 670,
        "name": "Střední zdravotnická škola Evangelické akademie"
    }, {
        "schoolId": 671,
        "name": "Střední zdravotnická škola, Beroun, Mládeže 1102"
    }, {
        "schoolId": 672,
        "name": "Střední zdravotnická škola, Hranice, Nová 1820"
    }, {
        "schoolId": 673,
        "name": "Střední zdravotnická škola, Jindřichův Hradec, Klášterská 77/II"
    }, {
        "schoolId": 674,
        "name": "Střední zdravotnická škola, Písek, Národní svobody 420"
    }, {
        "schoolId": 675,
        "name": "Střední zdravotnická škola, Tábor, Mostecká 1912"
    }, {
        "schoolId": 676,
        "name": "Střední zdravotnická škola, Turnov, 28. října 1390, příspěvková organizace"
    }, {
        "schoolId": 677,
        "name": "Střední zemědělská škola a Střední odborná škola Poděbrady, příspěvková organizace"
    }, {
        "schoolId": 678,
        "name": "Střední zemědělská škola, Brandýs nad Labem - Stará Boleslav, Zápská 302"
    }, {
        "schoolId": 679,
        "name": "Střední zemědělská škola, Čáslav, Sadová 1234"
    }, {
        "schoolId": 680,
        "name": "Střední zemědělská škola, Písek, Čelakovského 200"
    }, {
        "schoolId": 681,
        "name": "Střední zemědělská škola, Rakovník, Pražská 1222"
    }, {
        "schoolId": 682,
        "name": "Svobodná chebská škola, základní škola a gymnázium s. r. o."
    }, {
        "schoolId": 683,
        "name": "Svobodná chebská škola, základní škola a gymnázium s.r.o."
    }, {
        "schoolId": 684,
        "name": "Táborské soukromé gymnázium a Základní škola, s.r.o."
    }, {
        "schoolId": 685,
        "name": "Taneční centrum Praha - konzervatoř, z. ú."
    }, {
        "schoolId": 686,
        "name": "Taneční konzervatoř Brno, příspěvková organizace"
    }, {
        "schoolId": 687,
        "name": "Taneční konzervatoř hlavního města Prahy, Praha 1, Křížovnická 7"
    }, {
        "schoolId": 688,
        "name": "TRIVIS - Střední škola veřejnoprávní a Vyšší odborná škola prevence kriminality a krizového řízení Praha, s.r.o."
    }, {
        "schoolId": 689,
        "name": "TRIVIS - Střední škola veřejnoprávní Karlovy Vary, s.r.o."
    }, {
        "schoolId": 690,
        "name": "TRIVIS - Střední škola veřejnoprávní Vodňany, s.r.o."
    }, {
        "schoolId": 691,
        "name": "TRIVIS – Střední škola veřejnoprávní Brno, s. r. o."
    }, {
        "schoolId": 692,
        "name": "TRIVIS – Střední škola veřejnoprávní Karlovy Vary, s. r. o."
    }, {
        "schoolId": 693,
        "name": "TRIVIS – Střední škola veřejnoprávní Třebechovice pod Orebem, s. r. o."
    }, {
        "schoolId": 694,
        "name": "TRIVIS – Střední škola veterinární Emila Holuba Brno, s. r. o."
    }, {
        "schoolId": 695,
        "name": "Trojské gymnázium s.r.o."
    }, {
        "schoolId": 696,
        "name": "U2B ¦ multimediální střední škola"
    }, {
        "schoolId": 697,
        "name": "VAKANTIS střední škola a vyšší odborná škola s.r.o."
    }, {
        "schoolId": 698,
        "name": "Veřejnosprávní akademie a střední škola, s. r. o."
    }, {
        "schoolId": 699,
        "name": "Vojenská střední škola a Vyšší odborná škola Ministerstva obrany v Moravské Třebové pracoviště Soko"
    }, {
        "schoolId": 700,
        "name": "VOŠ a SPŠE Plzeň"
    }, {
        "schoolId": 701,
        "name": "Všeobecné a sportovní gymnázium, Vimperk, Pivovarská 69"
    }, {
        "schoolId": 702,
        "name": "Výchovný ústav a střední škola, Olešnice na Moravě, Trpínská 317"
    }, {
        "schoolId": 703,
        "name": "Výchovný ústav, dětský domov se školou, středisko výchovné péče, střední škola a základní škola, Mor"
    }, {
        "schoolId": 704,
        "name": "Výchovný ústav, středisko výchovné péče a střední škola Jindřichův Hradec"
    }, {
        "schoolId": 705,
        "name": "Výchovný ústav, středisko výchovné péče Klíčov a střední škola"
    }, {
        "schoolId": 706,
        "name": "Výchovný ústav, střední škola a školní jídelna Višňové, Zámek 1"
    }, {
        "schoolId": 707,
        "name": "Výchovný ústav, střední škola a školní jídelna, Obořiště 1"
    }, {
        "schoolId": 708,
        "name": "Vyšší odborná škola a Střední odborná škola, Březnice, Rožmitálská 340"
    }, {
        "schoolId": 709,
        "name": "Vyšší odborná škola a Střední průmyslová škola dopravní, Praha 1, Masná 18"
    }, {
        "schoolId": 710,
        "name": "Vyšší odborná škola a Střední průmyslová škola elektrotechnická Františka Křižíka, Praha 1, Na Příkopě 16"
    }, {
        "schoolId": 711,
        "name": "Vyšší odborná škola a Střední průmyslová škola, Jičín, Pod Koželuhy 100"
    }, {
        "schoolId": 712,
        "name": "Vyšší odborná škola a Střední průmyslová škola, Volyně, Resslova 440"
    }, {
        "schoolId": 713,
        "name": "Vyšší odborná škola a střední škola Boskovice, příspěvková organizace"
    }, {
        "schoolId": 714,
        "name": "Vyšší odborná škola a Střední škola, s.r.o."
    }, {
        "schoolId": 715,
        "name": "Vyšší odborná škola a Střední umělecká škola Václava Hollara, Praha 3, Hollarovo náměstí 2"
    }, {
        "schoolId": 716,
        "name": "Vyšší odborná škola a Střední zemědělská škola, Benešov, Mendelova 131"
    }, {
        "schoolId": 717,
        "name": "Vyšší odborná škola a Střední zemědělská škola, Tábor, Náměstí T. G. Masaryka 788"
    }, {
        "schoolId": 718,
        "name": "Vyšší odborná škola ekonomických studií, Gymnázium, Střední průmyslová škola potravinářských technologií a Střední odborná škola přírodovědná a veterinární, Praha 2, Podskalská 10"
    }, {
        "schoolId": 719,
        "name": "Vyšší odborná škola grafická a Střední průmyslová škola grafická, Praha 1, Hellichova 22"
    }, {
        "schoolId": 720,
        "name": "Vyšší odborná škola informačních studií a Střední škola elektrotechniky, multimédií a informatiky"
    }, {
        "schoolId": 721,
        "name": "Vyšší odborná škola lesnická a Střední lesnická škola Bedřicha Schwarzenberga, Písek, Lesnická 55"
    }, {
        "schoolId": 722,
        "name": "Vyšší odborná škola mezinárodního obchodu a Obchodní akademie, Jablonec nad Nisou, Horní náměstí 15, příspěvková organizace"
    }, {
        "schoolId": 723,
        "name": "Vyšší odborná škola oděvního návrhářství a Střední průmyslová škola oděvní, Praha 7, Jablonského 3"
    }, {
        "schoolId": 724,
        "name": "Vyšší odborná škola pedagogická a sociální, Střední odborná škola pedagogická a Gymnázium, Praha 6, Evropská 33"
    }, {
        "schoolId": 725,
        "name": "Vyšší odborná škola sklářská a Střední škola v Novém Boru"
    }, {
        "schoolId": 726,
        "name": "Vyšší odborná škola sklářská a Střední škola, Nový Bor, Wolkerova 316, příspěvková organizace"
    }, {
        "schoolId": 727,
        "name": "Vyšší odborná škola sociální a Střední pedagogická škola, Prachatice, Zahradní 249"
    }, {
        "schoolId": 728,
        "name": "Vyšší odborná škola stavební a Střední průmyslová škola stavební, Praha 1, Dušní 17"
    }, {
        "schoolId": 729,
        "name": "Vyšší odborná škola textilních řemesel a Střední umělecká škola textilních řemesel, Praha 1, U Půjčovny 9"
    }, {
        "schoolId": 730,
        "name": "Vyšší odborná škola uměleckoprůmyslová a Střední uměleckoprůmyslová škola, Praha 3, Žižkovo náměstí 1"
    }, {
        "schoolId": 731,
        "name": "Vyšší odborná škola zdravotnická a Střední zdravotnická škola, Hradec Králové, Komenského 234"
    }, {
        "schoolId": 732,
        "name": "Vyšší odborná škola zdravotnická a Střední zdravotnická škola, Praha 1, Alšovo nábřeží 6"
    }, {
        "schoolId": 733,
        "name": "Vyšší odborná škola zdravotnická a Střední zdravotnická škola, Praha 4, 5. května 51"
    }, {
        "schoolId": 734,
        "name": "Vyšší odborná škola, Střední průmyslová škola a Jazyková škola s právem státní jazykové zkoušky, Kutná Hora, Masarykova 197"
    }, {
        "schoolId": 735,
        "name": "Vyšší odborná škola, Střední průmyslová škola a Obchodní akademie, Čáslav, Přemysla Otakara II. 938"
    }, {
        "schoolId": 736,
        "name": "Vyšší odborná škola, Střední průmyslová škola a Střední odborná škola řemesel a služeb, Strakonice, Zvolenská 934"
    }, {
        "schoolId": 737,
        "name": "Vyšší odborná škola, Střední průmyslová škola automobilní a technická, České Budějovice, Skuherského 3"
    }, {
        "schoolId": 738,
        "name": "Vyšší odborná škola, Střední škola, Centrum odborné přípravy, Sezimovo Ústí, Budějovická 421"
    }, {
        "schoolId": 739,
        "name": "Vyšší odborná škola, střední škola, jazyková škola s právem státní jazykové zkoušky, základní škola a mateřská škola MILLS, s.r.o."
    }, {
        "schoolId": 740,
        "name": "Vyšší odborná škola, Střední škola, Základní škola a Mateřská škola, Hradec Králové, Štefánikova 549"
    }, {
        "schoolId": 741,
        "name": "Vyšší policejní škola a Střední policejní škola Ministerstva vnitra v Praze"
    }, {
        "schoolId": 742,
        "name": "Vyšší policejní škola a Střední policejní škola Ministerstva vnitra v Praze pracoviště Sokolov"
    }, {
        "schoolId": 743,
        "name": "Waldorfská škola České Budějovice – mateřská škola, základní škola a střední škola o.p.s."
    }, {
        "schoolId": 744,
        "name": "Waldorfská škola Příbram - mateřská škola, základní škola a střední škola"
    }, {
        "schoolId": 745,
        "name": "Waldorfská základní škola a střední škola Semily, příspěvková organizace"
    }, {
        "schoolId": 746,
        "name": "Základní a mateřská škola Dolní kounice"
    }, {
        "schoolId": 747,
        "name": "Základní škola a gymnázium Ježek bez klece"
    }, {
        "schoolId": 748,
        "name": "Základní škola a Gymnázium Leonardo da Vinci Academy"
    }, {
        "schoolId": 749,
        "name": "Základní škola a gymnázium Navis"
    }, {
        "schoolId": 750,
        "name": "Základní škola a Gymnázium Vodňany"
    }, {
        "schoolId": 751,
        "name": "Základní škola a mateřská škola Těšany, okres Brno-venkov, příspěvková organizace"
    }, {
        "schoolId": 752,
        "name": "Základní škola a Praktická škola Benešov, Hodějovského 1654"
    }, {
        "schoolId": 753,
        "name": "Základní škola a praktická škola Brno, Vídeňská, příspěvková organizace"
    }, {
        "schoolId": 754,
        "name": "Základní škola a praktická škola Hodonín, náměstí B. Martinů, příspěvková organizace"
    }, {
        "schoolId": 755,
        "name": "Základní škola a praktická škola Hustopeče, příspěvková organizace"
    }, {
        "schoolId": 756,
        "name": "Základní škola a Praktická škola Kutná Hora, příspěvková organizace"
    }, {
        "schoolId": 757,
        "name": "Základní škola a Praktická škola Neratovice, příspěvková organizace"
    }, {
        "schoolId": 758,
        "name": "Základní škola a praktická škola Veselí nad Moravou, příspěvková organizace"
    }, {
        "schoolId": 759,
        "name": "Základní škola a Praktická škola, Broumov"
    }, {
        "schoolId": 760,
        "name": "Základní škola a Praktická škola, Český Brod, Žitomířská 1359"
    }, {
        "schoolId": 761,
        "name": "Základní škola a Praktická škola, Jičín"
    }, {
        "schoolId": 762,
        "name": "Základní škola a Praktická škola, Kostelec nad Černými lesy, K Jatkám 748"
    }, {
        "schoolId": 763,
        "name": "Základní škola a praktická škola, Slavkov u Brna, příspěvková organizace"
    }, {
        "schoolId": 764,
        "name": "Základní škola a střední škola Aš, příspěvková organizace"
    }, {
        "schoolId": 765,
        "name": "Základní škola a střední škola Aš, příspěvková organizace"
    }, {
        "schoolId": 766,
        "name": "Základní škola a Střední škola Donum Felix s.r.o."
    }, {
        "schoolId": 767,
        "name": "Základní škola a Střední škola JEDNA RADOST Pňov-Předhradí"
    }, {
        "schoolId": 768,
        "name": "Základní škola a Střední škola Karla Herforta, Praha 1, Josefská 4"
    }, {
        "schoolId": 769,
        "name": "Základní škola a střední škola Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 770,
        "name": "Základní škola a střední škola Karlovy Vary, příspěvková organizace"
    }, {
        "schoolId": 771,
        "name": "Základní škola a střední škola waldorfská"
    }, {
        "schoolId": 772,
        "name": "Základní škola a Střední škola, Praha 10, Vachkova 941"
    }, {
        "schoolId": 773,
        "name": "Základní škola a Střední škola, Praha 2, Vinohradská 54"
    }, {
        "schoolId": 774,
        "name": "Základní škola a Střední škola, Praha 4, Kupeckého 576"
    }, {
        "schoolId": 775,
        "name": "Základní Škola Dubí 2, Tovární 110, Okres Teplice"
    }, {
        "schoolId": 776,
        "name": "Základní škola Mukařov, příspěvková organizace"
    }, {
        "schoolId": 777,
        "name": "Základní škola speciální a Praktická škola, Praha 6, Rooseveltova 8"
    }, {
        "schoolId": 778,
        "name": "Základní škola T. G. Masaryka v Praze 12"
    }, {
        "schoolId": 779,
        "name": "Základní škola, Mateřská škola a Praktická škola Kolín, příspěvková organizace"
    }, {
        "schoolId": 780,
        "name": "Základní škola, Praktická škola a Mateřská škola, Česká Lípa, Moskevská 679, příspěvková organizace"
    }, {
        "schoolId": 781,
        "name": "Zemědělská akademie a Gymnázium Hořice – střední škola a vyšší odborná škola, příspěvková organizace"
    }, {
        "schoolId": 782,
        "name": "Zlatnické středisko praktického vyučování Solunka, spol. s r.o."
    }, {
        "schoolId": 783,
        "name": "ZŠ Elanor Sušice"
    }
]


class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.get("/backend/school/listAll/", 200, [], schools)

    def __del__(self):
        pass
