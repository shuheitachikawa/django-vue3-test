from django.db import models

# Create your models here.
class Twitter(models.Model):
  created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
  content = models.CharField(verbose_name='ツイート', max_length=100, null=True, blank=True)

  class Meta:
    verbose_name_plural = 'Twitter'
  
  def __str__(self):
    return self.content