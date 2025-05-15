from .kb_models import db, KnowledgeDecision

class KnowledgeBaseManager:
    def record_decision(self, user_id, decision_type, input_facts, applied_rules, conclusion, confidence_score):
        decision = KnowledgeDecision(
            user_id=user_id,
            decision_type=decision_type,
            input_facts=str(input_facts),
            applied_rules=str(applied_rules),
            conclusion=conclusion,
            confidence_score=confidence_score
        )
        db.session.add(decision)
        db.session.commit() 