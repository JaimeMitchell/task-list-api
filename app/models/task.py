from app import db


class Task(db.Model):#A model is a table in postgres
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    @classmethod
    def from_dict(cls, data_dict): #given a response body, which is a json, it makes it an instance of a class
        
        return cls(title=data_dict["title"], # brackets are called "sub" 
                   description=data_dict["description"])

    def to_dict(self):
        return dict(
            id=self.task_id,
            title=self.title,
            description=self.description,
            is_complete=bool(self.completed_at))
# stuff on the left is what the user sees and the stuff on the right is the class being instantiated by the database query
