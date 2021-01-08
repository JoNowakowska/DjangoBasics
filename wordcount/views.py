from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    full_text = request.GET['fulltext']
    full_text_list = full_text.split()
    no_of_words = len(full_text_list)

    count_words_dict = {}

    for word in full_text_list:
        if word in count_words_dict:
            count_words_dict[word] += 1
        else:
            count_words_dict[word] = 1

    sorted_word_count = {
        word: counted
        for word, counted
        in sorted(
            count_words_dict.items(),
            key=lambda x: x[1],
            reverse=True
        )
    }

    return render(
                  request,
                  'count.html',
                  {
                      'full_text': full_text,
                      'no_of_words': no_of_words,
                      'sorted_word_count': sorted_word_count.items(),
                  }
    )


def about(request):
    return render(request, 'about.html')