from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.question_text)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('question-detail', args=[str(self.id)])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
