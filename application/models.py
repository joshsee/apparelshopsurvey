"""
models.py

App Engine datastore models

"""

from google.appengine.ext import db

"""
class ExampleModel(ndb.Model):
    "Example Model""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class AdNetwork(db.Model):
    "Newsletter Model""
    app_title = ndb.StringProperty(required=True)
    app_category = db.CategoryProperty(required=True)
    app_url = db.BlobProperty()
    app_name = db.StringProperty()
    ext = db.StringProperty()
    content_type = db.StringProperty()
    app_link = db.LinkProperty()
    new = db.BooleanProperty()
    exclusive = db.BooleanProperty()
"""


class Survey(db.Model):
    """Survey Model"""
    timestamp = db.DateTimeProperty(auto_now_add=True)
    sex = db.StringProperty(required=True, choices=set(["male", "female"]))
    age = db.IntegerProperty(required=True)


class Answer(db.Model):
    """Question Model"""
    survey = db.ReferenceProperty(Survey)
    question = db.IntegerProperty(required=True)
    sub_question = db.IntegerProperty(required=True)
    rating = db.RatingProperty(required=True)