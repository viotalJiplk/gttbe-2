from testUtils import requestExpect
class Test:
    def __init__(self):
        pass

    def run(self):
        requestExpect.get("/backend/game/all/", 200, [], {
  "games": [
    {
      "gameId": 1,
      "name": "COUNTER_STRIKE",
      "registrationStart": "2024-01-29",
      "registrationEnd": "2025-02-21",
      "maxCaptains": 1,
      "maxMembers": 2,
      "maxReservists": 3,
      "minCaptains": 1,
      "minMembers": 1,
      "minReservists": 0,
      "gamePage": "test",
      "maxTeams": 0
    },
    {
      "gameId": 2,
      "name": "LOL",
      "registrationStart": "2023-10-17",
      "registrationEnd": "2023-11-13",
      "maxCaptains": 1,
      "maxMembers": 4,
      "maxReservists": 2,
      "minCaptains": 1,
      "minMembers": 4,
      "minReservists": 0,
      "gamePage": "# Pravidla\r\n\r\n## Týmy\r\n- Podle počtů týmů organizátoři vyhlásí formát zápasů, a to:\r\n\t- **Bo5** nebo **Bo3** nebo pouze **jeden zápas** (možnost knock out stagů)\r\n- Tým se sestává z **5 hráčů**, je možnost nahlášení náhradníků\r\n\t- Lidé, kteří nejsou přihlášeni jako součást týmu (náhradníci včetně) se nesmí zúčastnit \t\tturnaje\r\n- Každý tým musí vyhlásit svého **zástupce, kapitána**\r\n- Každý tým musí poskytnout svá **skutečná jména a in-game nicky** všech hráčů i náhradníků, které budou zveřejněna na startovní listině\r\n- Složení týmu se **nesmí změnit po datu** stanoveném organizátory z řad SPGT\r\n- Jméno týmu **nesmí být ofenzivní a urážlivé a nevhodné**. Právo o tomto rozhodovat si vyhrazují organizátoři\r\n\r\n## Hráč\r\n- Nahlášené jméno se od doby nahlášení až do vyhlášení výsledků nesmí změnit\r\n- Jméno nesmí být ofenzivní a urážlivé a nevhodné. Právo o tomto rozhodovat si vyhrazují organizátoři z řad SPGT\r\n\r\n## Hra\r\n- Champ select začíná, jakmile kapitáni obou týmů hlasovou nebo textovou formou potvrdí připravenost týmu\r\n- Hra se uskutečňuje na mapě **summoners rift**\r\n- Turnajový draft pick s 5ti bany (3+2)\r\n- Draft bude probíhat na stránkách: https://draftlol.dawe.gg (z důvodu že né všichni mají všechny champy)\r\n- Hráči jsou povinni se seřadit v normálním **LCS pořadí** (top, jungle, mid, bot, support)\r\n- Blue a Red strana je před bitvou náhodně vybrána a potom se střídá\r\n- Hra je ukončena vítězstvím jedné strany pokud\r\n\t- Je zničen nexus některého z týmů\r\n\t- Kapitulace jednoho z týmů (od 15. minuty)\r\n\t- Kapitán týmu vyhlásí kapitulaci týmu organizátorům (V jakýkoliv čas)\r\n- Pokud bude hra stagnovat (bude dlouho rovná) bude přerušena a vítěz bude vyhlášen organizátory na základě statistik\r\n- Po hře se výhra mezi organizátory diskutuje a proběhne rozhodnutí o uznání vítězství. Tým, který hru \"vyhraje\", nemusí být na základě porušení pravidel uznán za vítěze\r\n\t- Změnit rozhodnutí si organizátoři vyhrazují i jakýkoliv čas po zápasu\r\n- Hra se odehrává na **EUNE serveru**\r\n- **Exploitování** neboli využívání skrytých herních mechanik nebo bugů, které nejsou společností Riot Games ve hře úmyslně je **zakázané**\r\n- **Externí programy**, které nejsou v rozporu s Riot Games, např.: porofessor, blitz, mobalytics ad. jsou **povoleny**\r\n\r\n## Problémy\r\n- Pokud se vyskytne problém při loading screen a bude zapotřebí odehrát nový zápas je povinností obout týmů zvolit si naprosto **stejné championy** se stejnými schopnostmi a runami. Toto bude kontrolováno a jinak **trestáno** jako porušení pravidel\r\n- Pokud se vyskytne chyba v jakékoliv fázi před-hry (lobby až loading screen) může kapitán nahlásit organizátorům tuto chybu a organizátoři jsou povinni ji řešit například restartem hry\r\n- Je možnost se odvolat kvůli chybě hráče na změnu run. Pak je hra restartována. Tato výsada je **pouze jedna** na celý tým po dobu celého turnaje\r\n- Pokud se některý hráč ihned po startu hry nepřipojí hra bude pozastavena do doby, než se do hry připojí všech 10 hráčů.\r\n- Pokud se hráč nedostaví do lobby nebo do samotné hry ani po 10 minutách čekání bude **tým diskvalifikován**\r\n\t- Pokud je příčinnou faktor neovlivnitelný bude zváženo odsunutí zápasu\r\n- Hráč může pozastavit hru jen pokud:\r\n\t- Se nějaký hráč **neúmyslně odpojí**\r\n\t- Malfunkce hardwaru nebo samotné aplikace LoL\r\n\t- **Chyba vybavení** a prostředí (rozbitá židle, událost v domě, která nelze odložit)\r\n\t- **Zranění** nebo jiná kondice (například nutnost si dojít pro léky)\r\n- Pauza může být pouze **15 minut na tým** kvůli chybě daného hráče a 20 minut, pokud je to chyba hry nebo další.\r\n- Ostatní hráči nesmí zrušit pauzu\r\n- Pokud hra například crashne, můžou organizátoři vyhlásit vítěze na základě:\r\n\t- Rozdíl goldů mezi týmy **větší jak 33%**\r\n\t- Rozdíl mezi zničenými nebo stojícími turretami je **7 nebo více**\r\n\t- Rozdíl ve zničených nebo stojících inhibitorů je **2 a více**\r\n\t- Rozdíl mezi živými nebo mrtvými championy je **4 a více**\r\n\r\n## Komunikace\r\n- Hráči mají povinnost se dostavit na discord **10 minut před** turnajem do místnosti obecné, kde jim budou zděleny podrobnosti k zápasu\r\n- Komunikace probíhá mezi členy týmů **výhradně přes discord** , a to na serveru GT tournament v příslušných roomkách, kam budete přeřazeni\r\n- V in-game chatu, lobby chatu a champ select chatu je psát zprávy povoleno\r\n- Je zakázáno psát urážlivé, nevhodné i zprávy s úmyslem soupeře naštvat nebo vyhrožování\r\n\t- To se vztahuje i na zprávy „EZ“, „?“, „cy@“, atd.\r\n\r\n## Organizátoři\r\n- Vyhrazují si právo zasahovat do zápasu jako například nařídit pauzu.\r\n- Rozhodnout spor mezi hráči\r\n- Přerušit nebo ukončit hru\r\n- Diskvalifikovat tým na základě porušení pravidel nebo obecných pravidel chování\r\n- Rozhodovat o výsledku zápasu\r\n",
      "maxTeams": 0
    },
    {
      "gameId": 3,
      "name": "MINECRAFT",
      "registrationStart": "2023-10-17",
      "registrationEnd": "2023-11-13",
      "maxCaptains": 1,
      "maxMembers": 3,
      "maxReservists": 2,
      "minCaptains": 1,
      "minMembers": 3,
      "minReservists": 0,
      "gamePage": "# Pravidla\r\n\r\n1. **Zakazuje se:**\r\n\r\n\t1. Používat jakékoli hacky, cheaty, mody (krom specificky povolených), resourcepacky co by dávaly výhody ve hře (např. Xray) – (máme anticheat!)\r\n\t\t1. Specificky povolené módy jsou: Sodium, Lithium, Iris, and Starlight.\r\n\t\t\t1. Pokud používáte OptiFine je nutno **vypnout fast math**.\r\n\t\t1. Jiné optimalizační módy je možné použít po domluvě s admin teamem.\r\n\t1. Používat jakákoli makra nebo modifikace myši které dávají nefér výhodu ve hře. (např. autoclicker)\r\n\t\tDále je zakázáno:\r\n\t\t\t- Přemapovávat si více tlačítel na útok.\r\n\t\t\t- Dvojklikání\r\n\t\t\t- Klikat rychleji než 20 cps.\r\n\t1. Sledovat stream a tím neférově získávat informace o ostatních týmech\r\n\t1. Zneužívat exploity ve hře, pokud nějaké znáte (duplikace itemů a podobně) **Hrajte fair-play a bavte se!**\r\n\r\n2. Pro chat na serveru platí stejná pravidla jako na discordu.\r\n\r\n2. **Průběh hry:**\r\n\r\n\t1. Turnaj bude probíhat na **verzi Minecraftu 1.20.2 s PVP 1.8**\r\n\t1. Pro připojení musíte používat **originální Launcher** hry (warez hráči s i se nemohou zúčastnit)\r\n\t1. Turnaj vyhrává tým, který zvítězí ve finální hře\r\n\t1. Konkrétní bracket bude uveřejněn na Discordu, bude se odvíjet od počtu nahlášených týmů apod. Organizátoři si vyhrazují právo jej kdykoliv změnit!\r\n\t1. Každý tým sestává ze **čtyř hráčů** +- náhradníci, jeden z hráčů má status kapitána týmu\r\n\t1. Před zápasem se bude vybírat mapa, kapitán týmu vždy napíše do příslušného kanálu na Discordu hlas za svůj tým, na výběr bude ze 3-5 map, jejichž podoba bude v předstihu uveřejněna na Discordu\r\n\t1. Organizátoři si vyhrazují právo na změnu pravidel kdykoliv během turnaje\r\n\t1. Dále si organizátoři vyhrazují právo na vyloučení jakéhokoliv týmu bez udání důvodu (buďte v pohodě a my budeme taky)\r\n",
      "maxTeams": 0
    },
    {
      "gameId": 4,
      "name": "ROCKET_LEAGUE",
      "registrationStart": "2023-10-17",
      "registrationEnd": "2023-11-13",
      "maxCaptains": 1,
      "maxMembers": 1,
      "maxReservists": 0,
      "minCaptains": 1,
      "minMembers": 1,
      "minReservists": 0,
      "gamePage": "## **Pravidla turnaje**\r\n\r\n **1 Technické problémy**\r\n - Tým je zodpovědný za technický stav svého zařízení. Zápas nemůže být přeložen z důvodu technických problémů, zápas se musí odehrát.\r\n - Každý tým má nárok na 10 min pauzu k vyřešení svých technických problémů. Pokud se během tohoto časového úseku problémy nevyřeší je tým nucen odehrát zápas s hráči, kteří jsou schopni hrát, nebo zápas ukončit ve prospěch soupeře.\r\n\r\n **2 Obecná pravidla**\r\n - Týmy budou hrát všichni proti všem.\r\n - Zápasy se odehrávají hned po skončení předchozího zápasu.\r\n - Nezapomeňte, že právě vy můžete být streamováni, proto byste měli poslouchat pokyny na twitchi.\r\n - Jakýkoliv admin má právo sledovat zápas. ▪ Spectatovat mohou pouze admini.\r\n - Je zakázáno mít nevhodné názvy týmu, nicky hráčů a nadávat si v zápase.\r\n -  Admin může trestat vyřazením týmu z turnaje, v nejhorším případě může být hráč zabanován.\r\n - Tým, který se kvalifikuje do finále, musí finále odehrát ve stejném složení hráčů, se kterýma se kvalifikoval.\r\n - Ve skupinách rozhoduje nejprve vzájemný zápas, poté rozdíl skóre.\r\n - Po každém zápase kapitáni pošlou screen statistik zápasu.\r\n - Organizátor si vyhrazuje právo na změnu pravidel.\r\n\r\n**3 Nastavení hry**\r\n - Server: Evropa ▪ Mapy: DHF Stadium\r\n - Herní režim: Private Match\r\n - Sestava: 2v2\r\n - Formát: BO1-skupiny (BO3 – pavouk, BO5 - Finále)\r\n - Čas zápasu: 5 minut Match zakládají komentátoři a admini, typ Name+password.\r\n\r\n**4 Nedostavení se k zápasu**\r\n - Pokud se tým účastnící se turnaje nedostaví 15 minut po oficiálním času zahájení turnaje je diskvalifikován.\r\n\r\n**5 Protest**\r\n - Pokud zápas proběhl nekorektně, má tým 10 minut po skončení zápasu na podání protestu. Protest musí obsahovat média, která jasně prokáží porušení pravidel, která vedla k ovlivnění výsledků nebo zápasové série. Tým je zodpovědný za důkaz, který poskytne (např. screenshot).\r\n\r\n**6 Komunikace a podpora**\r\n - Veškerá komunikace s administrátorem probíhá na discordu v místnosti Rocket League a \"chat-k-turnaji,\" kde musíte být přítomni po celou dobu odehrávání turnaje.\r\n - Na tomto discordu se postují i informace ohledně turnaje.\r\n",
      "maxTeams": 0
    },
    {
      "gameId": 5,
      "name": "VALORANT",
      "registrationStart": "2023-10-17",
      "registrationEnd": "2023-11-13",
      "maxCaptains": 1,
      "maxMembers": 4,
      "maxReservists": 2,
      "minCaptains": 1,
      "minMembers": 4,
      "minReservists": 0,
      "gamePage": "# Pravidla\r\n\r\n## Formát zápasů\r\n- hraje se 5 vs 5 hráčů, minimální počet hráčů, ve kterém lze zápas dohrát jsou 4 (v jednom týmu)\r\n-  Pokud se soupeř nedostaví na zápas do 15 minut po jeho oficiálním začátku, bude zápas kontumován ve prospěch týmu, který se dostavil\r\n- hra končí ve chvíli, kdy jeden z týmů dovrší 13 vyhraných kol (nehraje se overtime)\r\n- každý tým má právo na 5 minut pauzy\r\n\r\n##  Výběr map\r\n- dostupné mapy k volbě (kompetetivní)\r\n- Ascent,Bind,Breeze,Haven,Lotus,Split,Sunset\r\n1.  Týmy se střídají v postupném banování map na stránce https://www.mapban.gg/cs/ban/valorant/competitive ,\r\n v sekci s 1 hvězdou (Do or die).\r\n2. Tým, který je na řadě si vybere mapu, kterou chce hrát.\r\n3. Druhý tým si vybere stranu na vybrané mapě.\r\n\r\n## Zákazy\r\n- zákaz všech externích programů, které nějak mění vlastnosti hry nebo poskytují výhodu nad soupeřem (cheaty), platí také pro tzv. \"low graphic mody\"\r\n- je zakázáno využívat bugů map, pokud se však hráč na pozici nedostane legální cestou (vysazení od spoluhráče)\r\n",
      "maxTeams": 0
    },
    {
      "gameId": 6,
      "name": "R6",
      "registrationStart": "2023-10-17",
      "registrationEnd": "2023-11-13",
      "maxCaptains": 1,
      "maxMembers": 4,
      "maxReservists": 2,
      "minCaptains": 1,
      "minMembers": 4,
      "minReservists": 0,
      "gamePage": "## Pravidla hry:\r\n\r\n\r\n\r\n***Formát hry:***\r\n\r\n-   Zápas se hraje formou 5 na 5 hráčů. Minimální počet hráčů v každém z týmů, který je nutný k zahájení zápasu, je 5.\r\n\r\n\r\n- Zápas se hraje jako ve formě Ranked módu :\r\n\r\n\r\n\r\n\r\n\r\n\t1. Kdo má první 4 body vyhrál, pokud je remíza, hraje se první overtime, pokud bude remíza znova, tak bude náhlá smrt.\r\n\r\n\t2. Preparation phase bude 45 sekund\r\n\r\n\t3. Action phase bude 3 minuty\r\n\r\n\t4. Defuse phase bude 45 vteřin\r\n\r\n\t5. Plant time a defuse time bude 7 vteřin\r\n\r\n\t6. Každý tým může zabanovat jednoho útočníka a jednoho obránce\r\n\r\n\r\n\r\n***Povinnosti hráčů:***\r\n\r\n-   Každý tým musí poskytnout skutečná jména, in game nicky a Ubisoft jména všech hráčů i náhradníků, jména a nicky budou zveřejněny na startovní listině.\r\n\r\n-   Hráči musí mít minimálně lvl 50\r\n\r\n-   Oficiální soupisky týmů vycházejí ze soupisky uvedené při registraci.\r\n\r\n-   Každý hráč je povinen mít při oficiálním zápase shodné Ubisoft jméno s hodnotou, kterou uvedl při přihlášení do turnaje.\r\n\r\n\r\n\r\n\r\n***Mapy:***\r\n\r\n-   Pickování a banování map bude probíhat na stránce [https://www.mapban.gg/en/ban/r6s/ranked](https://www.mapban.gg/en/ban/r6s/ranked)\r\n\r\n-   Týmy se budou střídat v banování map\r\n\r\n  ***Hratelné mapy:***\r\n\r\n\r\nOregon, Club house, Consulate, Bank, Kanal, Chalet, Kafe Dostoyevsky, Border, Skyscraper, Coastline, Theme park, Villa, Outback, Emerald plains, Stadium bravo, Nighthaven labs\r\n\r\n\r\n\r\n***Vyhodnocení zápasů:***\r\n\r\n-   Kapitáni týmů jsou povinni zaslat na konci hry screenshot výsledkové tabulky\r\n\r\n\r\n\r\n\r\n***Server hosting:***\r\n\r\n-   Hru vytváří kapitán útočícího týmu, po provedení banování map\r\n\r\n-   Kapitán vytvoří hru, podle zaslaného návodu\r\n\r\n-   Kapitán následně pozve členy svého týmu a kapitána protějšího týmu do hry\r\n\r\n-   Kapitán protějšího týmu následně pozve členy svého týmu\r\n\r\n-   Jakýkoliv úmyslný problém se začátkem hry může vést k diskvalifikaci\r\n\r\n-   Pokud nastane pádný technický problém před ukončením druhého kola po souhlasů adminů, musí oba týmy začínat hru novou.\r\n\r\n-   Jakýkoliv výpadek po tomto čase bude podle rozhodnutí admina\r\n\r\n\r\n\r\n\r\n***Zákazy:***\r\n\r\n-   Je zakázáno jakékoliv používání externích programů, které mění vlastnosti hry, anebo zvýhodňují hráče oproti ostatním.\r\n\r\n-   Smurfing a hosting je zakázán\r\n\r\n\r\n\r\n\r\n***Admini:***\r\n\r\n-   Admin má právo sledovat průběh zápasu ze spectator modu přímo na serveru, jak na discordu, tak ve hře.\r\n\r\n-   Admin může kontumačně vyřadit jakýkoliv tým, po konzultaci s admin týmem, pokud mu akce určitého týmu připadají nevhodné\r\n",
      "maxTeams": 0
    }
  ]
})

    def __del__(self):
        pass
