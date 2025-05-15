from ..config import db
from datetime import datetime

# Define KnowledgeDecision class for use in the knowledge base manager
class KnowledgeDecision(db.Model):
    __bind_key__ = 'knowledge'
    __tablename__ = 'knowledge_decision'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    decision_type = db.Column(db.String(50))
    input_facts = db.Column(db.Text)
    applied_rules = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    confidence_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = {'extend_existing': True}
