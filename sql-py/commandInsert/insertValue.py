from sqlalchemy.orm import Session
from models import Cliente,Città,Provincia,CAP,DatiAnagrafici,RubricaIndirizzi,Categoria,Prodotto,\
    Valutazione,Coupon,Sconto,StatusOrdine,Ordine,Composizione,MetodoPagamento,Pagamento,MetodoSpedizione,\
    Spedizione,Magazzino,Locazione,Vetrina,Evidenza
import hashlib

class Insert:
    def __init__(self, session: Session):
        self.session=session

    def insert(self):
        print("Inserendo i clienti...")
        #Inserisci i Clienti
        cliente1 = Cliente(email="prova@gmail.com",password=hashlib.sha1(b"ciao").hexdigest())
        cliente2 = Cliente(email="prova2@gmail.com",password=hashlib.sha1(b"prova").hexdigest())
        cliente3 = Cliente(email="prova3@gmail.com",password=hashlib.sha1(b"prova3").hexdigest())

        self.session.add_all([cliente1,cliente2,cliente3])
        self.session.commit()

        print("Inserendo le città...")
        # Inserisco le città
        città1 = Città(NomeCittà="Roma")
        città2 = Città(NomeCittà="Milano")
        città3 = Città(NomeCittà="Torino")
        città4 = Città(NomeCittà="Napoli")
        città5 = Città(NomeCittà="Bologna")

        self.session.add_all([città1,città2,città3,città4,città5])
        self.session.commit()
        print("Inserendo le provincie...")
        #Inserisco le Provincie
        provincia1 = Provincia(Provincia="RM")
        provincia2 = Provincia(Provincia="MI")
        provincia3 = Provincia(Provincia="TO")
        provincia4 = Provincia(Provincia="NA")
        provincia5 = Provincia(Provincia="BO")

        self.session.add_all([provincia1,provincia2,provincia3,provincia4,provincia5])
        self.session.commit()
        print("Inserendo i CAP...")
        #Inserisco i CAP
        cap1= CAP(CAP="00100",Città=città1, Provincia=provincia1)
        cap2= CAP(CAP="00165",Città=città1, Provincia=provincia1)
        cap3= CAP(CAP="20019",Città=città2, Provincia=provincia2)
        cap4= CAP(CAP="20021",Città=città2, Provincia=provincia2)
        cap5= CAP(CAP="10024",Città=città3, Provincia=provincia3)
        cap6= CAP(CAP="10094",Città=città3, Provincia=provincia3)
        cap7= CAP(CAP="80016",Città=città4, Provincia=provincia4)
        cap8= CAP(CAP="80100",Città=città4, Provincia=provincia4)
        cap9= CAP(CAP="40100",Città=città5, Provincia=provincia5)
        cap10= CAP(CAP="40121",Città=città5, Provincia=provincia5)

        self.session.add_all([cap1,cap2,cap3,cap4,cap5,cap6,cap7,cap8,cap9,cap10])
        self.session.commit()
        print("Inserendo i dati anagrafici...")
        #Inserisco i dati anagrafici
        queryClient = self.session.query(Cliente).all()
        clientenew1 = queryClient[0]
        clientenew2 = queryClient[1]
        clientenew3 = queryClient[2]
        datiana1 = DatiAnagrafici(nome="Mario", cognome="Rossi", indirizzo="Viale del muro torto,13", telefono1="+393333243209", telefono2=None,Cliente=clientenew1, Città=città1)
        datiana2 = DatiAnagrafici(nome="Giuseppe", cognome="Verdi", indirizzo="Viale Monza,33", telefono1="024329034", telefono2=None,Cliente=clientenew2, Città=città2)
        datiana3 = DatiAnagrafici(nome="Franco", cognome="Franchini", indirizzo="Viale Milano", telefono1="0812312441", telefono2=None,Cliente=clientenew3, Città=città4)

        self.session.add_all([datiana1, datiana2, datiana3])
        self.session.commit()
        print("Inserendo la rubrica indirizzi...")
        # Inserisco la rubrica indirizzi
        rubricaindirizzi1 = RubricaIndirizzi(Cliente=clientenew1, nominativo=None,nome="Mario",cognome="Rossi",indirizzo="Via torto,13",Città=città1)
        rubricaindirizzi2 = RubricaIndirizzi(Cliente=clientenew2, nominativo=None,nome="Giuseppe",cognome="Verdi",indirizzo="Viale Monza, 33",Città=città2)
        rubricaindirizzi3 = RubricaIndirizzi(Cliente=clientenew3, nominativo="Portiere",nome="Angelo",cognome="Sidorni",indirizzo="Viale Marino,3",Città=città4)

        self.session.add_all([rubricaindirizzi1, rubricaindirizzi2, rubricaindirizzi3])
        self.session.commit()
        print("Inserendo le categorie prodotto...")
        #Inserisco le Categorie prodotto
        descrizioneCat1 = "La vitamina C, o acido ascorbico, appartiene al gruppo delle vitamine cosiddette idrosolubili, quelle cioè che non possono essere accumulate nell\'organismo, ma devono essere regolarmente assunte attraverso l\'alimentazione."
        descrizioneCat2 = "Per vitamina D si intende un gruppo di pro-ormoni liposolubili costituito da 5 diverse vitamine: vitamina D1, D2, D3, D4 e D5. Le due più importanti forme in cui la vitamina D si può trovare sono la vitamina D2 (ergocalciferolo) e la vitamina D3 (colecalciferolo), entrambe dall\'attività biologica molto simile."
        categoria1 = Categoria(NomeCategoria="Vitamine C",DescrizioneCategoria=descrizioneCat1)
        categoria2 = Categoria(NomeCategoria="Vitamine D",DescrizioneCategoria=descrizioneCat2)

        self.session.add_all([categoria1, categoria2])
        self.session.commit()

        # Inserisco i Prodotti
        print("Inserendo i prodotti...")
        prodotto1 = Prodotto(
            NomeProdotto="Altrient C",
            Forma="Bustine 10ml",
            Prezzo=45.90,
            PercorsoImmagine="/img/altrient-c.jpg",
            DescrizioneBreveProdotto="Altrient C Liposomal è un integratore alimentare ad alta potenza che è stato formulato secondo standard farmaceutici, con una tecnologia progettata per rompere",
            DescrizioneDettagliataProdotto="""Altrient C offre la perfetta soluzione, grazie al suo metodo di somministrazione liposomiale scientificamente dimostrato. Questa potente forma di trasporto incapsula le sostanze nutritive in una microscopica bolla fosfolipidica capace di portarle direttamente nelle cellule in pochi minuti, proteggendole dagli elementi distruttivi dell\'apparato digerente.\n
        Altrient C è stato testato clinicamente e contribuisce a migliorare i livelli di elasticità, idratazione e collagene della pelle del 61% in 3 mesi.\n
        La vitamina C aiuta anche a proteggere le cellule dallo stress ossidativo e a ridurre la stanchezza e l\'affaticamento, oltre a contribuire alla naturale sintesi del collagene per la salute di ossa, cartilagini, gengive, pelle e denti. Un integratore perfetto quando ci si sente giù di tono, poiché la vitamina C sostiene la normale funzione del sistema immunitario.""",
            Categoria=categoria1
            )

        prodotto2 = Prodotto(
            NomeProdotto="Vitamina D3 5000UI",
            Forma="tavolette 90",
            Prezzo=27.30,
            PercorsoImmagine="/img/vitaminad3.jpg",
            DescrizioneBreveProdotto="adatto ai vegetariani. Le compresse di vitamina D3 5000 sono una forma specifica e altamente biodisponibile di vitamina D.",
            DescrizioneDettagliataProdotto="""Nature\'s Plus VITAMIN D3 5000 IU Complemento alimentare a base di colecalciferolo. 
            Non contiene glutine, lievito, frumento, mais, soia o latte. 
            Ingredienti per 1 capsula Vitamina D3 (colecalciferolo) 125 µg Altri ingredienti: olio di cartamo; gelatina; glicerina; acqua purificata.""",
            Categoria=categoria2
            )

        self.session.add_all([prodotto1, prodotto2])
        self.session.commit()

        # Inserisco le valutazioni
        print("Inserendo le valutazioni...")
        valutazione1 = Valutazione(Prodotto=prodotto1, Cliente=clientenew1,DataCommento="2023-03-11 18:00:00",Commento="Mi sono trovato molto bene con il prodotto in questione",Voto=8)
        valutazione2 = Valutazione(Prodotto=prodotto2, Cliente=clientenew1,DataCommento="2023-01-01 17:00:00",Commento="Prezzo forse troppo alto, in giro si trova a di meno",Voto=5)

        self.session.add_all([valutazione1, valutazione2])
        self.session.commit()
        #Inserisco i coupon
        print("Inserendo i coupon...")
        coupon1 = Coupon(Sconto=20,CodiceCoupon="MERRYCHRISTMAS")
        coupon2 = Coupon(Sconto=30,CodiceCoupon="MIDSEASONSALE")
        self.session.add_all([coupon1, coupon2])
        self.session.commit()
        #Inserisco gli Sconti
        print("Inserendo gli sconti...")
        sconto1 = Sconto(Cliente=clientenew1,Coupon=coupon1)
        sconto2 = Sconto(Cliente=clientenew1,Coupon=coupon2)
        sconto3 = Sconto(Cliente=clientenew2,Coupon=coupon2)
        self.session.add_all([sconto1, sconto2, sconto3])
        self.session.commit()        
        # Inserisco gli Status dell'ordine
        print("Inserendo gli StatusOrdine...")
        status1 = StatusOrdine(statusOrdine="Creato")
        status2 = StatusOrdine(statusOrdine="In Attesa di Bonifico")
        status3 = StatusOrdine(statusOrdine="Pagato")
        status4 = StatusOrdine(statusOrdine="Spedito")
        status5 = StatusOrdine(statusOrdine="Annullato")
        status6 = StatusOrdine(statusOrdine="Contabilizzato")
        self.session.add_all([status1, status2, status3, status4, status5, status6])
        self.session.commit()
        # Inserisco gli ordini
        print("Inserendo gli ordini...")
        ordine1 = Ordine(dataInserimento="2022-12-28 12:00:00",StatusOrdine=status6,Cliente=clientenew1,Sconto=None)
        ordine2 = Ordine(dataInserimento="2023-03-10 15:00:00",StatusOrdine=status1,Cliente=clientenew1,Sconto=None)
        self.session.add_all([ordine1, ordine2])
        self.session.commit()
        # Inserisco la composizione degli ordini
        print("Inserendo la composizione degli ordini")
        composizione1 = Composizione(Ordine=ordine1,Prodotto=prodotto2,quantità=4)
        composizione2 = Composizione(Ordine=ordine2,Prodotto=prodotto1,quantità=3)
        composizione3 = Composizione(Ordine=ordine2,Prodotto=prodotto2,quantità=1)
        self.session.add_all([composizione1, composizione2, composizione3])
        self.session.commit()
        # Inserisco il metodo di pagamento
        print("Inserendo i metodi di pagamento...")
        metodo1 = MetodoPagamento(NomeMetodoPagamento="Bonifico Anticipato")
        metodo2 = MetodoPagamento(NomeMetodoPagamento="Carta di Credito")
        metodo3 = MetodoPagamento(NomeMetodoPagamento="PayPal")
        self.session.add_all([metodo1, metodo2, metodo3])
        self.session.commit()
        # Inserisco il pagamento
        print("Inserendo i pagamenti...")
        pagamento1 = Pagamento(ImportoPagamento=192.60,DataPagamento="2022-12-28 14:00:00",MetodoPagamento=metodo3,Ordine=ordine1)
        self.session.add(pagamento1)
        self.session.commit()
        # Inserisco il metodo di spedizione
        print("Inserendo i metodi di spedizione")
        metodo1 = MetodoSpedizione(NomeMetodoSpedizione="Corriere Standard",SpeseSpedizione=9.00)
        metodo2 = MetodoSpedizione(NomeMetodoSpedizione="Corriere Espresso",SpeseSpedizione=14.00)
        self.session.add_all([metodo1, metodo2])
        self.session.commit()
        # Inserisco la Spedizione
        print("Inserendo le spedizioni")
        spedizione1 = Spedizione(DataSpedizione="2022-12-29 13:00:00",MetodoSpedizione=metodo1,Ordine=ordine1)
        self.session.add(spedizione1)
        self.session.commit()
        # Inserisco il Magazzino
        print("Inserendo i magazzini...")
        magazzino1 = Magazzino()
        self.session.add(magazzino1)
        self.session.commit()
        # Inserisco le disponibilità
        print("Inserendo le disponibilità...")
        loca1 = Locazione(Prodotto=prodotto1,Magazzino=magazzino1,Disponibilità=50)
        loca2 = Locazione(Prodotto=prodotto2,Magazzino=magazzino1,Disponibilità=30)
        self.session.add_all([loca1, loca2])
        self.session.commit()
        # Inserisco le vetrine
        print("Inserendo le vetrine...")
        vetrina1 = Vetrina(NomeVetrina="HOMEPAGE")
        self.session.add(vetrina1)
        self.session.commit()
        #Inserisco i prodotti in evidenza
        print("Inserendo i prodotti in vetrina...")
        evidenza1 = Evidenza(Prodotto=prodotto1,Vetrina=vetrina1,testoInEvidenza="Arrivato questo nuovo prodotto non perdetelo!")
        self.session.add(evidenza1)
        self.session.commit()
