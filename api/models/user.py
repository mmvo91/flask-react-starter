from api.extensions import sql


class User(sql.Model):
    __tablename__ = 'user'
    __table_args__ = {"schema": "app"}

    id = sql.Column(sql.Integer, primary_key=True)
    username = sql.Column(sql.String, unique=True)
    email = sql.Column(sql.String)
    password = sql.Column(sql.String)
    active = sql.Column(sql.Boolean, default=False)
    last_login = sql.Column(sql.DateTime)
    ModifiedDate = sql.Column(sql.DateTime, default=sql.func.now(), onupdate=sql.func.now())
    ModifiedBy = sql.Column(sql.String, default="sqlAlchemy")
    CreatedDate = sql.Column(sql.DateTime, default=sql.func.now())
    CreatedBy = sql.Column(sql.String, default="sqlAlchemy")
