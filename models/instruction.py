from extensions import db

instruction_list = []

def get_last_id():
    if instruction_list:
        last_instruction = instruction_list[-1]
    else:
        return 1
    return last_instruction.id + 1

class Instructions(db.Model):
    __tablename__ = 'instruction'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    steps = db.Column(db.String(1000))
    tools = db.Column(db.String(400))
    cost = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))