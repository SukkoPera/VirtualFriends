#!/usr/bin/env python
# -*- coding: utf-8 -*-

channels = [
	"#alessandria",
	"#casale",
	"#u2",
	"#u2ita"
]

triggers = {
	"ciao|salve": [
		"Ciaoooo!",
		"Welcome to $channel!",
		"Ave tibi quoque",
		"Hellozzzz!",
		"Yooooooo!",
		"ecco da dove arrivava la puzza...",
		"non vedevo l'ora di vederti...",
		"se arrivi tu me ne vado io",
		"mancavi solo tu",
		"ueeeee, guarda com'è tardi!!!",
		"la madre degli imbecilli è sempre incinta, eh?",
		"DA QUANTO TEMPOOOOOO!!!!",
		"Noooo... sei *già* qua!? Uff...",
		"Addio quiete...",
		"no, dico: ma proprio QUA dovevi entrare?",
		"È arrivato *lui*...",
		"Ma guarda un po' chi c'è!",
		"NOOOOOOOOOOOOOO, non è possibile!!! Ma sei proprio TU?!?!?",
		"Non hai niente di meglio da fare che chattare? :)",
		"si stava così bene senza di te...",
		"è proprio vero che le disgrazie non arrivano mai da sole...",
		"ecco, ora che è arrivato lui siamo proprio a posto",
		"sì vabbe'... e poi basta!? non manca nessun altro idiota!?",
		"Arriva il più figo...",
		"alèèèè, uno stupido in più!",
		"eccal'lì...",
		"la ciliegina sulla torta...",
		"\"certi giorni incominciano male e continuano sempre peggio\"",
		"noooooo, solo questo ci mancava...",
		"ehhhhhhhh...",
		"Non pensi che sia ora di andartene?",
		"eh, figuriamoci se adesso non arrivava lui",
		"Menomale che ci sei tu...",
		"uà che gnokka!!",
		"tira almeno su la cerniera prima di entrare",
		"è buona educazione togliersi il cappello quando si entra da qualche parte",
		"Ti stavamo aspettando!",
		"Wow, chi si vede!!",
		"ahhhhh! volevo ben dire che avresti fatto qualcosa di più furbo che chattare...",
		"Ciao, benvenuto su $channel! Premi ALT-F4 per diventare operatore, o scrivi \"/list *\" per avere la lista delle ragazze del canale.",
		"uno come te starebbe meglio sul canale #0",
		"Ciao!!!",
		"Benvenuto su $chan, o gentile chattatore. Per la salute del canale sarai IMMEDIATAMENTE sottoposto ad un'esame rettale. Ti preghiamo gentilmente di collaborare, grazie."
	],
	"violator|space|cane": [
		"ehhh? mi hai chiamato???",
		"cosa c'entro io adesso!?!?",
		"senti chi parla...",
		"whaaat!?!?",
		"parla italiano please!!",
		"uhm... vediamo un po'...",
		"sì??",
		"mah, dipende dall'umidità, non si sa mai...",
		"franco!!!",
		"sgracchiu",
		"marta!?",
		"mmmh...",
		"pronti!",
		"agli ordini!",
		"cosa fai stasera?",
		"io bevo solo birra, superalcoolici e acqua *NATURALE*",
		"ma tu fai palestra?",
		"supermaaaaaaaaan!",
		"il messaggio è: conservare bottiglie vuote",
		"la vuotezza è solitudine",
		"la solitudine è pulizia",
		"la pulizia è divinità",
		"è un mondo diFicile!",
		"tonino carotone, il mio idoloooo!!",
		"oh, skuuuuuuuuuusa!",
		"taci, stolto",
		"oggi mi sono svegliato male",
		"non proferire verbo...",
		"wow!",
		"uh?",
		"come no",
		"per carità",
		"ma sì, e poi,!?",
		"una fetta di kulo no eh???",
		"a me mi piace la frutta ma però la mela mi fa skifo mentre invece adoro la pera",
		"così mi arrapi...",
		"ADDIO MONDO CRUDELE!",
		"mai pensato al suicidio eh?",
		"ma perché devono sempre capitare tutte a me?",
		"ahhh, la tauromachia",
		"eh sì già!",
		"oddio...",
		"ma va??",
		"ihihihihih",
		"ma perché io e te dobbiamo condividere lo stesso pianeta?",
		":)",
		":(",
		"...",
		"mah...",
		"non rompere",
		"no comment",
		"chi ha sbagliato, pagliuca?",
		"rigore è quando arbitro fischia",
		"io non c'ero, e se c'ero dormivo",
		"io??? guarda che ti sbagli!",
		"cielo, cielo, cielo... salvami tu",
		"when I feel heavy-metal...",
		"ciccio di nonna papera",
		"schumacher al rogo",
		"se lo dici tu...",
		"DEATH TO FRANCE!",
		"io sono la gomma, tu la colla...",
		"sto tremando, sto tremando!",
		"combatti come un contadino!",
		"chissà perché!!",
		"questi sono i momenti in cui mi accordo che c'è troppa gente su questa terra",
		"ma quante ne sai?",
		"l'acqua a casa tua non c'è, eh?",
		"troppa gIente su sto canale per i mii gusti",
		"cosa vuoi, botte? ti aspetto fuori!!",
		"giochiamo a scala 40?",
		"oh, mio Dio... HANNO UCCISO KENNY!!! BRUTTI BASTARDI!!!",
		"'zo vuoi?",
		"la gente scappa quanto mi vede arrivare...",
		"be'?",
		"perché esisti?",
		"spegni il computer e vai a dormire",
		"Ke palleeeee!",
		"Ehi... Atti insensati di violenza gratuita sono il *MIO* forte!",
		"Io ODIO gli idioti...",
		"a volte penso che se non ci fossi io questo mondo andrebbe proprio a rotoli",
		"eh sapessi...",
		"ma sei proprio _così_ allergico all'acqua???",
		"su che pianeta eri quando Dio distribuì l'intelligenza sulla Terra?",
		#~ "uhm... $nick is $uhost...",
		"non nominare il mio nome invano",
		"scappa finché sei in tempo",
		"senti maaaaaaaaaaaaaaaaa... tu suoni?",
		"non ci sono più le mezze stagioni...",
		"<G>",
		"Vinci un deretano se sputi piu lontano!",
		"Pisello corto, sparati un colpo!",
		"presente!",
		"sono qua",
		"sono sordo",
		"non so leggere",
		"per te sono SEMPRE disponibile, baby!",
		"io non credo proprio",
		"io no parlare tua lingua, no",
		"kec... cellai 'na milletta?",
		"sì certo",
		"quando vuoi",
		"sono qui apposta",
		"ma anche no",
		"l'essenziale è invisibile agli occhi",
		"ma alla fine chi è kaiser soze?",
		"non l'ho capita",
		"sempre meglio un cetriolo oggi che una vasca di pere domani",
		"ti è mai capitato di vergognarti guardandoti nello specchio?",
		"che voglia di fare un falò...",
		"antani",
		"*BUUUUURP*",
		"perché quando parli sembra che rutti?",
		"ammazzati",
		"contaci!",
		"hasta la vista, baby!"
	],
	"[^@]sukko": [
		"il mio capo!!",
		"il mio idoloooooooooooooooooooo",
		"l'onnipotente...",
		"okkio! siete SEMPRE sotto il mio sguardo!!!",
		"uhm... credevi di farla franca, eh?! sukko ti vede SEMPRE!",
		"shtai attenzione...",
		"i'm watching you...",
		"1° Comandamento: non pronunciare *QUEL nome* invano..."
	],
	"depeche": [
		"ci stai a fare una celebrazione nera stasera? ;)",
		"The grabbing hands grab all they can, all for themselves after all...",
		"could you please tell me the meaning of love?",
		"I know that five years is a long time and that times change, but I think in the end you will find people are basically the same",
		"Most of the time love's not enough, in itself",
		"Tora! Tora! Tora!",
		"I take pictures, photographic pictures",
		"Enjoy the silence",
		"Now I'm clean!",
		"The sweetest perfection, to call myself",
		"I hope you'll never let me down again!",
		"Let's play master and servant!",
		"People are people",
		"Everything counts in large amounts...",
		"You can run but you cannot hide",
		"Don't say you want me, don't say you need me, don't say you love me, it's understood",
		"I can't understand what makes a man hate another man, help me understand!",
		"Get the balance right (or left!?)",
		"Try walking in my shoes",
		"Nobody knows me as well as you do"
	],
	"bot": [
		"bot!? si mangia??",
		"naah, io preferisco i cct",
		"bott*na che non sei altro!!!",
		"noooo, bastaaaaa! non voglio averne a che fare con quella roba!!!",
		"eeeeeh? vuoi BOTte??",
		"sìsì, certo... una BOTte di vino. rosso o bianco? nero!?!?!?",
		"bramaputra...",
		"ma che BOTtiglie d'egitto..."
	],
	"sesso|ragazz[ae]|qualche.*ragazza": [
		"BALLERINA specialista nella lap dance, cerca uomo per attrezzo di lavoro.",
		"BELLA ragazza, disposta a tutto, cerca ragazzo per trascorrere momenti intensi.",
		"BELLISSIMA trans, fisico mozzafiato, cerca amico super per...",
		"DOPO un'estate calda, ma deludente, mi appresto a trascorrere un inverno freddo. Cerco te, uomo caldo, per riscaldare il mio corpo.",
		"RAGAZZA molto carina, scoperta la mia vera natura, cerca amica come lei, per relazione sincere e duratura.",
		"AMO girare nuda per casa... solo se qualcuno mi può guardare.",
		"COPPIA particolare con eccentriche fantasie cerca maschietto per giochi a tre.",
		"BIONDA naturale, cerca uomo distinto, per relazione esplosiva.",
		"AFFETTUOSA passerottina cerca un nido molto caldo dove trascorrere l'inverno.",
		"AMORE DELUSO dalla vita? La soluzione? La mia gonna senza mutandine.",
		"AMANTE travolgente, curve mozzafiato, cerca carroziere per il suo collaudo.",
		"AGNESE, autoritaria, cerca sottomessi per coinvolgenti giochi crudeli.",
		"ECCEZIONALMENTE donna, conoscerebbe partners generosi, per stimolanti esperienze.",
		"EURORAGAZZA cerca ragazzo speciale, per una relazione speciale.",
		"INSAZIABILE collezionista di uomini, cerca volontari da inserire nei suoi numerosi trofei.",
		"L'AMORE è una specie di chimica, ma il sesso è sicuramente una specie di fisica.",
		"PADRONI di casa. Anna, la dolcissima cameriera, è veramente sola.",
		"RAGAZZA particolare, cerca ragazzo particolare, per una relazione particolare, dai momenti particolari.",
		"SMARRITI un paio di slip neri, zona centro. Lauta ricompensa a chi mi aiuta a ritrovarli.",
		"LIBERA e selvaggia pantera aspetta cacciatore che la catturi con lo sguardo.",
		"AGGRESSIVA ma allo stesso tempo adorabile, cerca uomo incapace di saziarsi delle sue irrefrenabili fantasie.",
		"RICCA ragazza ospita per fine settimana in propria villa trentenne bello e gentiluomo per ore liete.",
		"SMARRITO reggiseno in zona centro. Lauta ricompensa a chi me lo ritrova.",
		"ASCOLTAMI in silenzio. Ti parlerò... Toccherai il cielo con un dito.",
		"COME EVA nel Paradiso terrestre, ho voglia di peccare... Vuoi essere il mio Adamo?",
		"LUNGO il Po: camminare, parlare, ridere, baciarsi, poi... casa mia...",
		"MODELLA di carattere selvaggio dedica serate piacevoli.",
		"PADRONA molto riservata cerca schiavi per momenti piacevoli.",
		"RAGAZZA carina, molto dolce e simpatica, cerca urgentemente gattone per amicizia sincera e duratura.",
		"BELLA gallinella cerca lupo per incontro da brivido.",
		"AFFIATATISSIME 30enni, amanti del divertimento, conoscerebbero uomini da svezzare.",
		"CERCASI abile ceramista per costruire un bel paio di corna al marito.",
		"DONNA meridionale, particolarmente coinvolgente, conoscerebbe uomo bisognoso di calore.",
		"DUE sono le cose che mi piacciono della vita: gli uomini e la libertà. Però sarebbe bello perdere la libertà per un uomo come te.",
		"SE vuoi un'amica, sono qui. Se vuoi una donna, sono qui. Se vuoi un'amante, sono qui. Se vuoi... e basta, sono qui.",
		"SEI INTERESSATO al mio conto in banca, alla mia bellezza, o ad una cena a lume di candela?",
		"A. A. A. fidanzato cercasi urgentemente, per essere strapazzata di coccole.",
		"BISEX spregiudicata e senza inibizioni ricerca nuove coivolgenti situazioni.",
		"CAPRICCIOSA gattina dai lunghi artigli ricerca \"padroncino\" per sensuali effusioni.",
		"COSA si può fare con le labbra? Impazzire! Chi vuole giocare insieme a me?",
		"DELUSA da tanti uomini che parlano d'amore e pensano ad altro, ho deciso di cambiare. Ti offro una bella serata e... me stessa.",
		"DIAVOLETTA sexy e simpatica, cerca angioletto da condurre sulle vie del peccato.",
		"HO una bocca provocante e sensuale. Vorrei mordere dolcemente qualsiasi parte di te!",
		"SEI UN bravo domatore? Hai voglia di domarmi? Allora che aspetti? Fai attenzione... Io mordo.",
		"SEXY ed intraprendente, affascinata dalla trasgressione, cerco un uomo con cui realizzare i miei desideri più nascosti.",
		"SONO una ragazza dal fisico mozzafiato, intrigante e sensuale, che sarà tua quando vuoi. Svegliati, sono qui!",
		"BASTA accontentarsi di donne insignificanti: ci sono io, indimenticabile.",
		"DONNA SOLA, annoiata, cerca avventure riservate con uomini trasgressivi.",
		"INTRIGANTE, misteriosa, sensuale... esaudisce ogni voglia più intima.",
		"SEGRETARIA, fisico perfetto, cerca titolare da sottomettere alle proprie passioni.",
		"STUPENDA, formosa, molto calda... cerca compagnia notturna.",
		"AMO essere corteggiata, ma alla fine cedo alle tentazioni.",
		"PROSSIMA alle nozze, vorrei dare l'addio al nubilato in compagnia di un uomo mozzafiato. Ora o mai più. Virginia.",
		"GABY: novità spagnola, mora chiara, 5a misura. Chiamami, voglio giocare con te!"
	],
	"alessandria": [
		"per ogni porkata che dici ti stacchero un capello!",
		"no, figurati. tutti di cagliari qua.",
		"tua stessa città? no no, per carità...",
		"no, di benevento",
		"no, spiacente. prova su #piacenza",
		"fortunatamente no"
	],
	"brutto|cattivo|pessimo|schifo": [
		"ma è la parte migliore!"
	],
	"dilegua": [
		"svapora...svapora...uhm...sul dizionario non c'è"
	],
	"bastard": [
		"chiederò a mia madre..."
	]
}
