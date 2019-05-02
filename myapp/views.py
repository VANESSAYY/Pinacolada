from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    #공백 기준 나누기
    word_dictionary = {}
    #빈 사전형 객체
  
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, 'result.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})