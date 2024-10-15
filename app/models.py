# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Biology(Model):
    views = IntegerField()
    concept = StringField()
    related_keywords = StringField()
    archive = BooleanField()
    confused = BooleanField()
    confused_percentage = FloatField()
    discussion = StringField()

    

    def json_response(self):
        
        return {
            'id': self.id,
            'concept': self.concept,
            'views': self.views,
            'related keywords': self.related_keywords,
            'archive': self.archive,
            'confused' : self.confused,
            'discussion' : self.discussion
        }

    def increase_view(self):
        self.views += 1
        self.save()
    
    def change_archive(self):
        self.archive = True
        self.save()

    # def calculate_confused_percentage(self):
    #     self.confused_percentage = (self.confused)/(self.views)
    #     self.save()
    
    # def confused_percentage_json_response(self):
    #     return {
    #         'id': self.id,
    #         'concept': self.concept,
    #         'confused percentage': self.confused_percentage
    #     }