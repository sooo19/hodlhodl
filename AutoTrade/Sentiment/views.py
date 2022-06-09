from django.shortcuts import redirect, render
from Sentiment.models import Sentiment, Comments, WordcloudTable
from django.forms.models import model_to_dict
from django.core import serializers
import json

# Create your views here.
def sentiment_result(request):
    
    # sentiment 예측 모델 변경으로 인한 table의 값이 None이기에 아래는 주석처리하고 예제코드로 진행한다.

    # sentiment = Sentiment.objects.first()
    # print(sentiment)
    # res_data = model_to_dict(sentiment)
    # print(res_data)
    
    # # datetime 객체 string으로 변환
    # res_data['crawling_date'] = res_data['crawling_date'].strftime("%Y %b %d")
    # print(res_data['crawling_date'])
    # res_data=json.dumps(res_data)

    # 따라서, 예제코드로 작성해서 test를 진행한다.
    # sentiment = Sentiment
    # sentiment(crawling_date = "2022-05-25", n_count = 30, p_count = 50, e_count = 60, k_val = 0.478, com_count = 140).save()

    # sentiment = sentiment.objects.first()
    # res_data = model_to_dict(sentiment)
    # print(res_data)
    # res_data['crawling_date'] = res_data['crawling_date'].strftime("%Y %b %d")
    # res_data = json.dumps(res_data)
    
    # 각 단어의 언급량을 weight로 설정하여 워드 클라우딩을 진행한다.

    wordcloud = WordcloudTable.objects.filter(crawling_date = '2021-12-29')
    print(wordcloud)
    
    res_data2=serializers.serialize("json",wordcloud)


    return render(request,"AI_result/sentiment.html",{ 'res_data2' : res_data2})
