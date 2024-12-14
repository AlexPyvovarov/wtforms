from sqlmodel import SQLModel, Field, Session, create_engine


class Config:
    ENGINE = create_engine("sqlite:///reviews.db")
    SESSION = Session(bind=ENGINE)

    @classmethod
    def restart_db(cls):
        SQLModel.metadata.drop_all(bind=cls.ENGINE)
        SQLModel.metadata.create_all(bind=cls.ENGINE)
    
    @classmethod
    def migrate(cls):
        books = [Reviews(rating=x+1, text=f"text{x+1}") for x in range(5)]
        cls.SESSION.add_all(books)
        cls.SESSION.commit()


class AutoID(SQLModel, table=False):
    id: int | None = Field(default=None, primary_key=True)

class Reviews(AutoID, table=True):
    rating: int = Field(nullable=False)
    text: str = Field(nullable=False)
