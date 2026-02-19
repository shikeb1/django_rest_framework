from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()

    def __str__(self):
        return self.blog_title


class Comments(models.Model):  # 🔥 C capital karo
    blog = models.ForeignKey(
        'Blog',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text