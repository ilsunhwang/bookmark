from django.db import models

# 데이터베이스에 어떤 자료를 어떻게 저장할것이냐 결정
# 각 모델에 관련된 기능들을 만드는 부분
# O.R.M


class Bookmark(models.Model):
    # 필드들을 써줌
    # 필드 이름 = 필드 종류
    # 필드 종류의 목적
    # 1. 데이터베이스 어떤식으로 데이터 저장할 것이냐,
    # 2. 사용자의 입력을 받을 때 어떤 form 태그를 보여줄 것이냐
    # 2-1. 입력폼의 제한사항, 유효성 검사
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return "사이트명 : " + self.site_name

    def get_absolute_url(self):
        pass
