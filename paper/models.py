from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # ユーザー情報
    pass


class Paper(models.Model):
    # 論文情報
    title = models.TextField()
    filename = models.CharField(max_length=100)
    bibliographic_information = models.TextField()


class Underline(models.Model):
    # 下線情報
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    color = models.CharField(max_length=100)


class Score(models.Model):
    # 評価
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return '点数は' + str(self.score)


class Block(models.Model):
    # ブロック情報
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    subject = models.TextField()
    conclusion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Block_Score(models.Model):
    # ブロックの評価
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    score_id = models.ForeignKey(Score, on_delete=models.CASCADE)


class Memo(models.Model):
    # メモ情報
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Memo_Score(models.Model):
    # メモの評価
    memo_id = models.ForeignKey(Memo, on_delete=models.CASCADE)
    score_id = models.ForeignKey(Score, on_delete=models.CASCADE)


class Comment(models.Model):
    # コメント
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'commentは' + self.comment


class Comment_Score(models.Model):
    # コメントの評価
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    score_id = models.ForeignKey(Score, on_delete=models.CASCADE)


class Relationship(models.Model):
    # 親子関係
    parent_id = models.ForeignKey(
        Comment, related_name="parent_comment", on_delete=models.CASCADE)
    child_id = models.ForeignKey(
        Comment, related_name="child_comment", on_delete=models.CASCADE)
    hierarchy = models.IntegerField()


class Paper_Comment(models.Model):
    # ペーパーコメント
    paper_id = models.ForeignKey(Paper, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Block_Comment(models.Model):
    # ブロックコメント
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Memo_Comment(models.Model):
    # メモコメント
    memo_id = models.ForeignKey(Memo, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
