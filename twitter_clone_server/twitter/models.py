from django.db import models
# import uuid

# Create your models here.
class Tweet(models.Model):
  # id = models.UUIDField(primary_key=True, verbose_name='ID', default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
  content = models.CharField(verbose_name='ツイート', max_length=100, null=True, blank=True)

  class Meta:
    verbose_name_plural = 'Tweet'
  
  def __str__(self):
    return str(self.content)

class Like(models.Model):
  tweet = models.ForeignKey(Tweet, verbose_name='ツイート', on_delete=models.PROTECT)
  created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

  class Meta:
    verbose_name_plural = 'Like'
  
  def __str__(self):
    return str(self.id)