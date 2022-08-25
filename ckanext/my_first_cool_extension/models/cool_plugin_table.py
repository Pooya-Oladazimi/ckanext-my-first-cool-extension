# encoding: utf-8

import datetime
from sqlalchemy import Column, Table, ForeignKey, orm
from sqlalchemy import types as _types
from ckan.model import meta, Package, domain_object


__all__ = [u"CoolPluginTable", u"cool_plugin_table"]

cool_plugin_table = Table(
    u"cool_plugin_table",
    meta.metadata,
    Column(u"id", _types.Integer, primary_key=True, nullable=False),
    Column(u"random_number", _types.Integer,  nullable=False),
    Column(u"name", _types.UnicodeText, nullable=False),
    Column(u"dataset", _types.UnicodeText, ForeignKey(u"package.name"), nullable=False),
    Column(u"created_at", _types.DateTime, default=datetime.datetime.utcnow, nullable=False),
)


class CoolPluginTable(domain_object.DomainObject):
    def __init__(self, random_number=None, name=None, dataset_name=None, created_at=None):
        self.random_number = random_number
        self.name = name        
        self.create_at = created_at
        self.dataset = dataset_name
        

    
    @classmethod
    def get_by_package(cls, name, autoflush=True):
        if not name:
            return None

        exists = meta.Session.query(cls).filter(cls.dataset==name).first() is not None
        if not exists:
            return False
        query = meta.Session.query(cls).filter(cls.dataset==name)
        query = query.autoflush(autoflush)
        record = query.all()
        return record


meta.mapper(
    CoolPluginTable,
    cool_plugin_table,
    properties={
        u"package": orm.relation(
            Package, backref=orm.backref(u"cool_plugin_table", cascade=u"all, delete, delete-orphan")
        )
    },
)







