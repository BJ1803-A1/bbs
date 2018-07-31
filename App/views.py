from django.shortcuts import render, redirect
from django.urls import reverse

from  App.models import Card



def index(request):
    cards = Card.objects.all()
    data = {
        "cards" : cards
    }
    return render(request,'main_index.html', context=data)



def create_card(request):
    print('a1111111111111')
    if request.method == 'POST':
        print('222222222222222')
        card_title = request.POST.get('card_title')
        card_content = request.POST.get('card_content')
        card = Card.objects.create(card_title=card_title, card_content=card_content)
        card.save()
        print('保存成功')
        return  redirect(reverse('bbs:index'))

    else :

        return render(request, 'create_card.html',)


def card_content(request,id):
    # card_id = request.GET.get(id)
    title = Card.objects.filter(id=id)[0].card_title
    content = Card.objects.filter(id=id)[0].card_content
    time = Card.objects.filter(id=id)[0].card_create_time
    data ={
        'card_title' : title,
        'card_content' : content,
        'card_time' : time
    }
    return render(request, 'card_content.html', context=data)