from sqlalchemy import inspect
from datetime import datetime

from .. import db  # from __init__.py


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(50), db.ForeignKey('account.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    details = db.Column(db.JSON, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
