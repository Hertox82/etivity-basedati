from sqlalchemy.orm import Session, aliased
from sqlalchemy.engine import Engine
from sqlalchemy import select, insert,update, text, delete
from models import Prodotto, Valutazione, DatiAnagrafici,Ordine,StatusOrdine, Cliente
from datetime import datetime

class Crud:
    def __init__(self, session: Session, engine: Engine):
        self.session=session
        self.engine=engine
    
    def create(self):
        # Creo un nuovo Commento
        # per creare un nuovo commento devo:
        # richiedere un Cliente
        client_select = select((Cliente.IDCliente)).join(DatiAnagrafici).where(DatiAnagrafici.nome == "Giuseppe").limit(1).scalar_subquery()
        product_select = select(Prodotto.IDProdotto).where(Prodotto.NomeProdotto == "Altrient C").limit(1).scalar_subquery()
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        insert_val = insert(Valutazione).\
            values({'Commento':"Questo prodotto è troppo costoso e non vale il rapporto qualità/prezzo","IDCliente":client_select,"IDProdotto":product_select,"DataCommento":formatted_date})
        print(insert_val.compile(compile_kwargs={'literal_binds': True}))
        # creare il commento
        with self.engine.connect() as conn:
            result = conn.execute(insert_val)
            

    def update(self):
        # Voglio aggiornare lo stato dell'ultimo ordine da creato a in attesa di bonifico
        # statusOrdine_select = select((StatusOrdine.IDStatusOrdine)).where(StatusOrdine.statusOrdine == 'In Attesa di Bonifico').limit(1).scalar_subquery()
        order_select = select((Ordine.IDOrdine)).order_by(Ordine.IDOrdine.desc()).limit(1)
        # # conn1 = self.engine.connect()
        # # result1 = conn1.execute(order_select)
        # # order_id = result1.first()[0];

        # update_order = update(Ordine).values(Status=statusOrdine_select).where(Ordine.IDOrdine == order_select)
        # print(update_order.compile(compile_kwargs={'literal_binds': True}))
        # with self.engine.connect() as conn:
        with self.engine.connect() as conn:
        #   conn.execute(update_order)
            conn.execute(text(""" 
                UPDATE `Ordine` SET `Status`= (SELECT `StatusOrdine`.`IDStatusOrdine` FROM `StatusOrdine`WHERE `StatusOrdine`.`statusOrdine` = 'In Attesa di Bonifico' LIMIT 1) WHERE `Ordine`.`IDOrdine` = (SELECT oal.`IDOrdine` FROM (SELECT * FROM `Ordine`) as oal ORDER BY oal.`IDOrdine` DESC LIMIT 1)
            """))
        
        print("Per verificare se l'update è andato a buon fine richiedo una SELECT")
        stmt = select((Ordine.IDOrdine,StatusOrdine.statusOrdine)).\
               join(StatusOrdine).\
               where(Ordine.IDOrdine == order_select.scalar_subquery())
        print(stmt.compile(compile_kwargs={'literal_binds': True}))
        with self.engine.connect() as conn2:
            result2 = conn2.execute(stmt)
            for row in result2:
                row_string=f"l'ordine n° {row.IDOrdine} ha il seguente status {row.statusOrdine}"
                print(row_string)

    def read(self):
        # voglio leggere i commenti dei prodotti
        stmt = select((Valutazione.Commento, Prodotto.NomeProdotto,DatiAnagrafici.nome, DatiAnagrafici.cognome)).\
            join(Prodotto).\
            join(DatiAnagrafici, DatiAnagrafici.IDCliente == Valutazione.IDCliente)
        print(stmt)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            for row in result:
                row_string=f"Il prodotto {row.NomeProdotto} ha avuto questa recensione: \"{row.Commento}\" da {row.nome} {row.cognome}"
                print(row_string)

        # voglio sapere il nome e cognome degli utenti che hanno fatto degli ordini
        secstmt = select((Ordine.IDOrdine,StatusOrdine.statusOrdine,DatiAnagrafici.nome,DatiAnagrafici.cognome)).\
                join(StatusOrdine).\
                join(DatiAnagrafici, DatiAnagrafici.IDCliente == Ordine.IDCliente)
        print(secstmt)
        with self.engine.connect() as conn2:
            result2 = conn2.execute(secstmt)
            for row in result2:
                row_string=f"l'ordine n° {row.IDOrdine} con status {row.statusOrdine} è stato realizzato da {row.nome} {row.cognome}"
                print(row_string)
    def delete(self):
        # voglio cancellare l'ultimo commento inserito
        last_comment=select(Valutazione).order_by(Valutazione.DataCommento.desc()).limit(1).subquery()
        lcomment = aliased(Valutazione, last_comment)
        delete_query = delete(Valutazione).\
            where(Valutazione.IDCliente == lcomment.IDCliente).\
            where(Valutazione.IDProdotto == lcomment.IDProdotto)
        print(delete_query.compile(compile_kwargs={'literal_binds': True}))
        with self.engine.connect() as conn:
            conn.execute(delete_query)
        
        stmt = select((Valutazione.Commento, Prodotto.NomeProdotto,DatiAnagrafici.nome, DatiAnagrafici.cognome)).\
            join(Prodotto).\
            join(DatiAnagrafici, DatiAnagrafici.IDCliente == Valutazione.IDCliente).order_by(Valutazione.DataCommento.desc())
        print(stmt)
        with self.engine.connect() as conn1:
            result = conn1.execute(stmt)
            for row in result:
                row_string=f"Il prodotto {row.NomeProdotto} ha avuto questa recensione: \"{row.Commento}\" da {row.nome} {row.cognome}"
                print(row_string)
