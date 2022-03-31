from functools import reduce
from django import forms
from project.models import Language

class Projectform(forms.Form):
    # 제목
    title = forms.CharField(
        error_messages={
            "required": '타이틀을 입력해주세요',
        },
        max_length=50, label='타이틀'
    )

    # 개요
    summary = forms.CharField(max_length=100,
        error_messages={
            'required': '내용을 입력해주세요',
        },
        label='개요')

    # 내용
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요',
        },
        widget=forms.Textarea, label='내용'
    )

    # 시작일
    startdate = forms.DateTimeField(label='시작일')

    # 공개 여부
    private = forms.BooleanField(required=False,initial=False,label='비공개')

    # 썸네일
    thumbnail = forms.ImageField(label='썸네일')

    # 언어
    LANGUAGE_OPTIONS = reduce(lambda result, lang: result.append((lang.id, lang.language)) or result,Language.objects.all(), [])

    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LANGUAGE_OPTIONS, label='언어 선택')

