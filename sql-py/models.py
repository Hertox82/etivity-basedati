# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, String, Text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Categoria(Base):
    __tablename__ = 'Categoria'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCategoria = Column(INTEGER(10), primary_key=True)
    NomeCategoria = Column(String(191))
    DescrizioneCategoria = Column(Text)


class Città(Base):
    __tablename__ = 'Città'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCittà = Column(INTEGER(10), primary_key=True)
    NomeCittà = Column(String(191), nullable=False)


class Cliente(Base):
    __tablename__ = 'Cliente'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCliente = Column(INTEGER(10), primary_key=True)
    email = Column(String(191), nullable=False, unique=True)
    password = Column(String(191), nullable=False)


class DatiAnagrafici(Base):
    __tablename__ = 'DatiAnagrafici'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCliente = Column(ForeignKey('Cliente.IDCliente', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    nome = Column(String(191))
    cognome = Column(String(191))
    indirizzo = Column(String(191))
    telefono1 = Column(String(191))
    telefono2 = Column(String(191))
    IDCittà = Column(ForeignKey('Città.IDCittà', ondelete='SET NULL'), index=True)

    Città = relationship('Città', uselist=False)
    Cliente = relationship('Cliente', uselist=False)
    

class Coupon(Base):
    __tablename__ = 'Coupon'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCoupon = Column(INTEGER(10), primary_key=True)
    Sconto = Column(TINYINT(1))
    CodiceCoupon = Column(String(30))


class Magazzino(Base):
    __tablename__ = 'Magazzino'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDMagazzino = Column(INTEGER(10), primary_key=True)


class MetodoPagamento(Base):
    __tablename__ = 'MetodoPagamento'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDMetodoPagamento = Column(INTEGER(10), primary_key=True)
    NomeMetodoPagamento = Column(String(191))


class MetodoSpedizione(Base):
    __tablename__ = 'MetodoSpedizione'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDMetodoSpedizione = Column(INTEGER(10), primary_key=True)
    NomeMetodoSpedizione = Column(String(191))
    SpeseSpedizione = Column(Float(7))


class Provincia(Base):
    __tablename__ = 'Provincia'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDProvincia = Column(INTEGER(10), primary_key=True)
    Provincia = Column(String(2), nullable=False)


class StatusOrdine(Base):
    __tablename__ = 'StatusOrdine'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDStatusOrdine = Column(INTEGER(10), primary_key=True)
    statusOrdine = Column(String(40))


class Vetrina(Base):
    __tablename__ = 'Vetrina'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDVetrina = Column(INTEGER(10), primary_key=True)
    NomeVetrina = Column(String(191))


class CAP(Base):
    __tablename__ = 'CAP'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDCap = Column(INTEGER(10), primary_key=True)
    CAP = Column(String(5), nullable=False)
    IDCittà = Column(ForeignKey('Città.IDCittà', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    IDProvincia = Column(ForeignKey('Provincia.IDProvincia', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    Città = relationship('Città')
    Provincia = relationship('Provincia')


class Prodotto(Base):
    __tablename__ = 'Prodotto'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDProdotto = Column(INTEGER(10), primary_key=True)
    NomeProdotto = Column(String(191), index=True)
    Forma = Column(String(50))
    Prezzo = Column(Float(7))
    PercorsoImmagine = Column(String(191))
    DescrizioneBreveProdotto = Column(String(255))
    DescrizioneDettagliataProdotto = Column(Text)
    IDCategoria = Column(ForeignKey('Categoria.IDCategoria', ondelete='CASCADE', onupdate='CASCADE'), index=True)

    Categoria = relationship('Categoria', uselist=False)


class RubricaIndirizzi(Base):
    __tablename__ = 'RubricaIndirizzi'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDIndirizzo = Column(INTEGER(10), primary_key=True)
    IDCliente = Column(ForeignKey('Cliente.IDCliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    nominativo = Column(String(191))
    nome = Column(String(191))
    cognome = Column(String(191))
    indirizzo = Column(String(191))
    IDCittà = Column(ForeignKey('Città.IDCittà', ondelete='SET NULL'), index=True)

    Città = relationship('Città')
    Cliente = relationship('Cliente')


class Sconto(Base):
    __tablename__ = 'Sconto'
    __table_args__ = (
        Index('IDCliente', 'IDCliente', 'IDCoupon', unique=True),
        {"mysql_engine": "InnoDB"}
    )

    IDSconto = Column(INTEGER(10), primary_key=True)
    IDCliente = Column(ForeignKey('Cliente.IDCliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    IDCoupon = Column(ForeignKey('Coupon.IDCoupon', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    Cliente = relationship('Cliente')
    Coupon = relationship('Coupon')


class Evidenza(Base):
    __tablename__ = 'Evidenza'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDProdotto = Column(ForeignKey('Prodotto.IDProdotto', ondelete='CASCADE'), primary_key=True, nullable=False)
    IDVetrina = Column(ForeignKey('Vetrina.IDVetrina', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    testoInEvidenza = Column(Text)

    Prodotto = relationship('Prodotto')
    Vetrina = relationship('Vetrina')


class Locazione(Base):
    __tablename__ = 'Locazione'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDProdotto = Column(ForeignKey('Prodotto.IDProdotto', ondelete='CASCADE'), primary_key=True, nullable=False)
    IDMagazzino = Column(ForeignKey('Magazzino.IDMagazzino', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    Disponibilità = Column(INTEGER(10))

    Magazzino = relationship('Magazzino')
    Prodotto = relationship('Prodotto')


class Ordine(Base):
    __tablename__ = 'Ordine'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDOrdine = Column(INTEGER(10), primary_key=True)
    dataInserimento = Column(DateTime)
    Status = Column(ForeignKey('StatusOrdine.IDStatusOrdine', ondelete='SET NULL'), index=True)
    IDCliente = Column(ForeignKey('Cliente.IDCliente', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    IDSconto = Column(ForeignKey('Sconto.IDSconto', ondelete='SET NULL'), index=True)

    Cliente = relationship('Cliente')
    Sconto = relationship('Sconto')
    StatusOrdine = relationship('StatusOrdine')


class Valutazione(Base):
    __tablename__ = 'Valutazione'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDProdotto = Column(ForeignKey('Prodotto.IDProdotto', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    IDCliente = Column(ForeignKey('Cliente.IDCliente', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, index=True)
    DataCommento = Column(DateTime)
    Commento = Column(Text)
    Voto = Column(TINYINT(1))

    Cliente = relationship('Cliente')
    Prodotto = relationship('Prodotto')


class Composizione(Base):
    __tablename__ = 'Composizione'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDOrdine = Column(ForeignKey('Ordine.IDOrdine', ondelete='CASCADE'), primary_key=True, nullable=False)
    IDProdotto = Column(ForeignKey('Prodotto.IDProdotto', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    quantità = Column(INTEGER(10))

    Ordine = relationship('Ordine')
    Prodotto = relationship('Prodotto')


class Pagamento(Base):
    __tablename__ = 'Pagamento'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDPagamento = Column(INTEGER(10), primary_key=True)
    ImportoPagamento = Column(Float(8))
    DataPagamento = Column(DateTime)
    IDMetodoPagamento = Column(ForeignKey('MetodoPagamento.IDMetodoPagamento', ondelete='SET NULL'), index=True)
    IDOrdine = Column(ForeignKey('Ordine.IDOrdine', ondelete='CASCADE'), nullable=False, index=True)

    MetodoPagamento = relationship('MetodoPagamento')
    Ordine = relationship('Ordine')


class Spedizione(Base):
    __tablename__ = 'Spedizione'
    __table_args__ = {"mysql_engine": "InnoDB"}
    IDSpedizione = Column(INTEGER(10), primary_key=True)
    DataSpedizione = Column(DateTime)
    IDTipoSpedizione = Column(ForeignKey('MetodoSpedizione.IDMetodoSpedizione', ondelete='SET NULL'), index=True)
    IDOrdine = Column(ForeignKey('Ordine.IDOrdine', ondelete='CASCADE'), index=True)

    Ordine = relationship('Ordine')
    MetodoSpedizione = relationship('MetodoSpedizione')
