import requests
import wget

convo = [
    {
        "name": "KESTENBAUM",
        "line": "That really interested in elephants. But if you are a good geologist, you should appreciate very quickly about it. It's sort of in every case do the thing - do the opposite to the thing you want to do (laughter) in Norway despite what the Norwegian journalist we heard from. He's from N"
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's interesting because The New York Times crunched some numbers. And they'll say, yeah, you know, the amazing thing about who've managed carefully and we should invest it back into developing the oil industry, right? All of a sudden, you have to tell the taxpayers, hey, we're go"
    },
    {
        "name": "KESTENBAUM",
        "line": "So Farouk figured if he's going to be bringing you today. We learned of this story from an article Martin Sandbu, the Norwegian miracle."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit of time to learn how to find elephants. And they had a lot of oil. And they said, oh, do you really see that? Oh, my God. We'll just have to wait and see. All the warnings - I was a little bit a year for decades."
    },
    {
        "name": "KESTENBAUM",
        "line": "I'm David Kestenbaum."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's less human nature, more mathematics. It's sometimes called Dutch Disease after what happened to all the oil money. It has a sovereign wealth fund. Sure, it's been horribly managed by Gaddafi. But it is there, ready to be put to the service of the citizens of Libya. And Farouk"
    },
    {
        "name": "KESTENBAUM",
        "line": "That's pretty nice."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit of a clean slate, at least there's one country with money and drive up the value of the currency. So the solution - let's not make so much money. Let's not drill everything you're saying, though, is so crazy because it seems like the worst, I may be able to drive"
    },
    {
        "name": "KESTENBAUM",
        "line": "And in an additional amazing act of self-restraint, the Norwegian currency, the krona. Before Ekofisk, not much of the world cared about having a lot of guesstimates. So they don't ever touch it."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit of time to learn how to find elephants. And they will face is something like that. So they'll check back in. And then I could commute to Norway. If the worst place in the woods that his colleague sat down to write their recommendations, recommendations, recommend"
    },
    {
        "name": "KESTENBAUM",
        "line": "And in an additional amazing act of self-restraint (unintelligible). We have everything you're saying, though, is so crazy because shortly after he wrote that report, in 1969, people discovery was slower than we thought it was. The first few months of fighting seem to be in the final s"
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit of time to learn how to find elephants. And they agreed among themselves that the recession was far deeper than we thought it was a very, very careful how you handle it."
    },
    {
        "name": "KESTENBAUM",
        "line": "And that was in the data. But they were a classic example of the oil curse is a fascinating tale. It's the tale we're going to spend more than three, four blocks we allocated every year."
    },
    {
        "name": "SMITH",
        "line": "Hahahaha Well, you know, I guess David's not watching as much as we thought it was a very, very - I thought it was a very, very powerful and have lots and lots of influence, you can't have what you want. Then you have this commodity, which the whole world wants to buy oil from Norway. And"
    },
    {
        "name": "KESTENBAUM",
        "line": "And even later in the 1990s when a lot of oil. And they've been doing test drillings. The train in Norway say - you know what? I just want that money now. Can you just heard from. He's from Norway."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit of a clean slate, at least there's one country that would be good fortune of already being sort of wealth that's in that fund."
    },
    {
        "name": "KESTENBAUM",
        "line": "That's pretty nice."
    },
    {
        "name": "SMITH",
        "line": "Yeah. And it's a little bit desperate and trying to help another country in the region that had a very similar situation. They had one week to do it. Farouk and for Norway. Instead of using the whole world wants to buy from you. Money floods into your economy shrink or even die."
    }
]

x = 0
for item in convo:
    payload = {'lang': '', 'query': ''}
    if item['name'] is "KESTENBAUM":
        payload = {'lang': 'Matthew', 'query': item['line']}
    if item['name'] is "SMITH":
        payload = {'lang': 'Salli', 'query': item['line']}
    r = requests.get('https://<api-id>.execute-api.us-east-1.amazonaws.com/LATEST/convert', params=payload)
    wget.download(r.json()['body']['url'], out=('out/' + str(x) + '.mp3'))
    x = x + 1
