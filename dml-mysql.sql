INSERT INTO Cliente(email, password) VALUES('prova@gmail.com',SHA1('ciao')),('prova2@gmail.com',SHA1('prova')),
('prova3@gmail.com',SHA1('prova3'));

INSERT INTO Città(NomeCittà) VALUES('Roma'),('Milano'),('Torino'),('Napoli'),('Bologna');

INSERT INTO Provincia(Provincia) VALUES ('RM'),('MI'),('TO'),
('NA'),('BO');

INSERT INTO CAP(CAP, IDCittà, IDProvincia) VALUES('00100',1,1),('00165',1,1),('20019',2,2),('20021',2,2),('10024',3,3),('10094',3,3),('80016',4,4),('80100',4,4),('40100',5,5),('40121',5,5);

INSERT INTO DatiAnagrafici(IDCliente, nome, cognome, indirizzo, telefono1, telefono2, IDCittà) VALUES(1, 'Mario','Rossi','Viale del muro torto,13','+393333243209',NULL, 1),(2,'Giuseppe','Verdi','Viale Monza,33','024329034',NULL, 2),(3,'Franco','Franchini','Viale Milano','0812312441',NULL,
4);

INSERT INTO RubricaIndirizzi(IDCliente, nominativo, nome, cognome, indirizzo,IDCittà) VALUES(1,NULL,'Mario','Rossi','Via torto,13',1),(2,NULL,'Giuseppe','Verdi','Viale Monza, 33',2),(3,'Portiere','Angelo','Sidorni','Viale Marino,3',4);

INSERT INTO Categoria(NomeCategoria,DescrizioneCategoria) VALUES ('Vitamine C','La vitamina C, o acido ascorbico, appartiene al gruppo delle vitamine cosiddette idrosolubili, quelle cioè che non possono essere accumulate nell\'organismo, ma devono essere regolarmente assunte attraverso l\'alimentazione.'), ('Vitamine D','Per vitamina D si intende un gruppo di pro-ormoni liposolubili costituito da 5 diverse vitamine: vitamina D1, D2, D3, D4 e D5. Le due più importanti forme in cui la vitamina D si può trovare sono la vitamina D2 (ergocalciferolo) e la vitamina D3 (colecalciferolo), entrambe dall\'attività biologica molto simile.');

INSERT INTO Prodotto(NomeProdotto,Forma,Prezzo,PercorsoImmagine,DescrizioneBreveProdotto,DescrizioneDettagliataProdotto,IDCategoria) 
VALUES ('Altrient C','Bustine 10ml',45.90,'/img/altrient-c.jpg','Altrient C Liposomal è un integratore alimentare ad alta potenza che è stato formulato secondo standard farmaceutici, con una tecnologia progettata per rompere',
'Altrient C offre la perfetta soluzione, grazie al suo metodo di somministrazione liposomiale scientificamente dimostrato. Questa potente forma di trasporto incapsula le sostanze nutritive in una microscopica bolla fosfolipidica capace di portarle direttamente nelle cellule in pochi minuti, proteggendole dagli elementi distruttivi dell\'apparato digerente.\n
Altrient C è stato testato clinicamente e contribuisce a migliorare i livelli di elasticità, idratazione e collagene della pelle del 61% in 3 mesi.\n
La vitamina C aiuta anche a proteggere le cellule dallo stress ossidativo e a ridurre la stanchezza e l\'affaticamento, oltre a contribuire alla naturale sintesi del collagene per la salute di ossa, cartilagini, gengive, pelle e denti. Un integratore perfetto quando ci si sente giù di tono, poiché la vitamina C sostiene la normale funzione del sistema immunitario.',1),
('Vitamina D3 5000UI','tavolette 90',27.30,'/img/vitaminad3.jpg',
'adatto ai vegetariani. Le compresse di vitamina D3 5000 sono una forma specifica e altamente biodisponibile di vitamina D.',
'Nature\'s Plus VITAMIN D3 5000 IU Complemento alimentare a base di colecalciferolo. Non contiene glutine, lievito, frumento, mais, soia o latte. Ingredienti per 1 capsula Vitamina D3 (colecalciferolo) 125 µg Altri ingredienti: olio di cartamo; gelatina; glicerina; acqua purificata.',
2);

INSERT INTO Valutazione (IDProdotto, IDCliente, DataCommento, Commento, Voto) 
VALUES(1,1,'2023-03-11 18:00:00','Mi sono trovato molto bene con il prodotto in questione',8),
(2,1,'2023-01-01 17:00:00','Prezzo forse troppo alto, in giro si trova a di meno',5);

INSERT INTO Coupon(Sconto, CodiceCoupon) VALUES (20,'MERRYCHRISTMAS'),(30,'MIDSEASONSALE');
INSERT INTO Sconto(IDCliente, IDCoupon) VALUES(1,1),(1,2),(2,2);
INSERT INTO StatusOrdine(statusOrdine) VALUES ('Creato'),('In Attesa di Bonifico'),('Pagato'),('Spedito'),('Annullato'),('Contabilizzato');

INSERT INTO Ordine(dataInserimento,`Status`,IDCliente, IDSconto) VALUES ('2022-12-28 12:00:00',6,1,NULL), ('2023-03-10 15:00:00',1,1,NULL);

INSERT INTO Composizione(IDOrdine,IDProdotto,quantità) VALUES (1,1,4),(2,1,3),(2,2,1);
INSERT INTO MetodoPagamento(NomeMetodoPagamento) VALUES('Bonifico Anticipato'),('Carta di Credito'),('PayPal');
INSERT INTO Pagamento(ImportoPagamento, DataPagamento, IDMetodoPagamento,IDOrdine) VALUES (192.60, '2022-12-28 14:00:00',3,1);
INSERT INTO MetodoSpedizione(NomeMetodoSpedizione, SpeseSpedizione) VALUES ('Corriere Standard',9.00),('Corriere Espresso',14.00);

INSERT INTO Spedizione(DataSpedizione, IDTipoSpedizione, IDOrdine) VALUES ('2022-12-29 13:00:00',1,1);

INSERT INTO Magazzino(IDMagazzino) VALUES (1);
INSERT INTO Locazione(IDProdotto, IDMagazzino, Disponibilità) VALUES (1,1,50), (2,1,30);

INSERT INTO Vetrina(NomeVetrina) VALUES ('HOMEPAGE');

INSERT INTO Evidenza(IDProdotto, IDVetrina, testoInEvidenza) VALUES(1,1,'Arrivato questo nuovo prodotto non perdetelo!');