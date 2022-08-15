from models import Score
import uuid

def get_scores_txn(session):
    query = session.query(Score)
    return query.all()

def add_score_txn(session, playername, points):
    score = Score(
        id=str(
            uuid.uuid4()),
        playername=playername,
        points=points
    )
    session.add(score)
