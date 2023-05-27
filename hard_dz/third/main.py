from functools import reduce

all_news = [
    {'title': 'Курс биткоина вырос до 1000 долларов. 5', 'positive_sentiment': 5},
    {'title': 'В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока". 10', 'positive_sentiment': 10},
    {'title': 'В Новосибирске из автобуса сбежала кондуктор. 7', 'positive_sentiment': 7},
    {'title': 'Самолет «Почты России» вылетел с опозданием в несколько месяцев. 1', 'positive_sentiment': 1},
    {'title': 'Козёл Тимур подружился с тигром Амуром. 20', 'positive_sentiment': 20},
    {'title': 'Инженерам из Space X удалось посадить первую ступень ракеты на землю. 10', 'positive_sentiment': 10},
]

published_news = []

def can_publish_news(news):
    if not published_news:
        return True
    else:
        previous_sentiment = reduce(lambda x, y: x if x > y else y, 
                                    [item['positive_sentiment'] for item in published_news])
        return news['positive_sentiment'] > previous_sentiment

for news in all_news:
    if can_publish_news(news):
        published_news.append(news)

for news in published_news:
    print(news['title'])
