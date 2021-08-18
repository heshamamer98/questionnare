from django.db import models

# first table
class questionnaire(models.Model):
    submit_num = models.CharField(max_length=100)
    counter= models.IntegerField()

# second table
class questions(models.Model):
    # q1-q8
    name = models.CharField(max_length=100)
    yes = models.IntegerField()
    no = models.IntegerField()
    
    # q9
    husband = models.IntegerField()
    parents = models.IntegerField()
    others = models.IntegerField()
    one = models.IntegerField()
    
    # q10
    father = models.IntegerField()

    # q11
    physical = models.IntegerField()
    psychologically = models.IntegerField()
    both = models.IntegerField()
    violated = models.IntegerField()
    
    # q12
    answer1 = models.IntegerField()
    answer2 = models.IntegerField()
    answer3 = models.IntegerField()
    answer4 = models.IntegerField()
    
    # q13
    city = models.IntegerField()
    countryside = models.IntegerField()

    # q14
    single = models.IntegerField()
    married = models.IntegerField()
    divorced = models.IntegerField()
    widow = models.IntegerField()

    # q15
    illiterate = models.IntegerField()
    read = models.IntegerField()
    middle = models.IntegerField()
    high = models.IntegerField()

    # q16
    educated = models.IntegerField()
    uneducated = models.IntegerField()

    # q17
    zerotothree = models.IntegerField()
    threetofive = models.IntegerField()
    fivetoseven = models.IntegerField()
    morethan = models.IntegerField()

    # q18
    physicalviolence = models.IntegerField()
    psychologicalviolence = models.IntegerField()
    verbalviolence = models.IntegerField()
    otherviolence = models.IntegerField()



    def __str__(self):
        return self.name