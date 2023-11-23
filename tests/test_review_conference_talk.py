"""Test cases for the review_conference_talk"""
"""
This test checks for text after '=========='
if it exists it will fail so that the text will
be removed or pass if it has already been removed
"""
# flake8: noqa

import re
from typing import Any

from models.load_conf import clean_text


mark_text = """
<a name="p2"></a>Brethren, it’s a marvelous privilege to be with you this evening. I’ve appreciated so much the messages that we have heard.

<a name="p3"></a>Someone who was a little more poetic than theological said, “Memory is the one Garden of Eden out of which one need never be cast.” Good memories are real blessings. Tonight I would like to share a few memories that have made a real difference in my life.

<a name="p4"></a>When I was a young man about the age of some of you deacons here, my dad was bishop of the ward in our little farming town of Banida in southeastern Idaho. I remember the first time he brought me with him to Salt Lake City to attend a general priesthood meeting. In those years, Dad always seemed to me to be really old. As I recognize now, he must have been around thirty-eight years of age. I was happy to be with him.

<a name="p5"></a>I remember we sat in the balcony there on the north side. Before the meeting started, Dad pointed out which one of the Brethren on the stand was President Heber J. Grant and which were his Counselors. I saw the Twelve Apostles and the other Brethren. And that night, a warm feeling of love and respect for the leaders of the Church came over me and has continued to grow to this day.

<a name="p6"></a>That night, I decided I wanted to do everything I could to support my dad as bishop. I didn’t want to do anything that would embarrass or disappoint him. To this day, I am grateful for those feelings that came to me that night.

<a name="p7"></a>None of us knows how long we are going to live. In the Book of Mormon, Alma asked the question, “Can ye look up to God at that day with a pure heart and clean hands?” ([Alma 5:19](https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/5.19?lang=eng#p19).) I remember when the need to have “clean hands and a pure heart” ([Ps. 24:4](https://www.churchofjesuschrist.org/study/scriptures/ot/ps/24.4?lang=eng#p4)) became very meaningful to me.

<a name="p8"></a>It was just after my friend David Carlson and I had graduated from Preston High School. We were happy with the fact that it was the same school that Presidents Ezra Taft Benson and Harold B. Lee had attended when they were growing up. Even though they had changed the name from the Oneida Stake Academy to Preston High School, we still had some of our classes in the same building.

<a name="p9"></a>We thought that 1946 was the “golden year” of athletics at Preston High. That year our teams won the district championship in every sport, and in basketball our team won the state championship—and that was in the days when the small high schools played against the big ones.

<a name="p10"></a>David was a good friend to me and, I think, to everybody in the school. He was a fine student. He worked hard and received excellent grades. He achieved in Scouting and seminary and was a well-coordinated athlete. David was a member of the basketball team, and his playing was one of the reasons our team won the state championship.

<a name="p11"></a>Soon after high school graduation, David went to the hospital for what everyone thought was a routine operation, but there were some complications. Infection set in, and the next thing we heard was that he had died. We could not believe it. At age eighteen, David had died. What a shock! I still remember how painful it was to lose a good friend.

<a name="p12"></a>His funeral was held in the stake center. Everyone seemed to come. It was like a crowded stake conference with standing room only.

<a name="p13"></a>Bishop Eberhard included a statement in his remarks that made a powerful impression on me. He pointed over to the sacrament table and said, “When David knelt to bless the sacrament, I knew that he knelt there with ‘clean hands and a pure heart.’ I never had to worry about what he had been doing the Saturday night before.”

<a name="p14"></a>I thought that was one of the finest compliments he could have paid to my friend, and I wanted to live in such a way that my bishop would not have to worry about what I had been doing the night before. I’m sure that all of us could benefit from making a similar decision.

<a name="p15"></a>Another memory taught me more about the value and importance of fulfilling a mission.

<a name="p16"></a>A few years ago, while serving as president of the Missionary Training Center in Provo, Utah, I had a delightful visit with one of the missionaries who came into my office. He was obviously older than the average young elder. He was about twenty-five years of age. He told me of his conversion.

<a name="p17"></a>When he was sixteen, he was baptized into the Church in Europe along with his mother. His father did not object to his wife’s and son’s joining the Church, even though he was not interested. He was a banker and wanted his son to prepare himself for a profession in the same area.

<a name="p18"></a>The young man loved studying the scriptures, but occasionally had some difficulty when his father would interrupt him when he was studying his seminary course and say, “Don’t waste your time studying those things. Study your regular school courses so that you can be accepted at the university.”

<a name="p19"></a>The elder said, “One night later on, when I was about eighteen, I had a dream. I dreamed that I had been called on a mission to Japan. I felt so good about it. I really wanted to go. The next day, when I told my parents about my dream, my dad strongly objected. He said, “Oh, no! Don’t waste two years of your life on a mission. You need to get on with your university studies.”

<a name="p20"></a>Since he was too young to leave for a mission at that time anyway, he did go on with his university studies. He chose to come to Brigham Young University. He majored in finance and banking for his undergraduate degree and stayed to complete a master’s degree in business administration.

<a name="p21"></a>He was hired by an international banking firm in Germany and was doing very well as a promising junior executive, but the idea of filling a mission would not leave his mind, and so he went to visit with his bishop and stake president. When he told his stake president of the vivid dream he had years before about going on a mission to Japan, his stake president chuckled and said, “Well, I don’t think you will be going to Japan. Missionaries from here generally are called to some other country on the continent, and a few go over to the British Isles.”

<a name="p22"></a>When he received his call and his father heard of it, he came and tried to change his son’s mind because he thought that a two-year interruption would be a disaster for his son’s professional career. One of the bank executives came down from Frankfurt and tried to discourage him from leaving, saying something like, “My boy, do you know how much this will cost you in salary and opportunity loss? You ought to sit down and figure it out.”

<a name="p23"></a>The elder said that he did that, and he had determined that the mission would cost him a very large amount of money—more than 150,000 dollars. Then tears came to his eyes, and he said, “But President, if it were to cost several times that amount, I would still be here, because I know that serving a mission is what the Lord wants me to do.”

<a name="p24"></a>That elder was one of the few I remember who left the Missionary Training Center speaking what Japanese he had learned with a German accent. He was called to Japan. He served a successful mission, and I am confident that when he finished he found many international businesses that would like to hire a junior executive who can speak English, German, and Japanese—the major languages of the economic free world. Even if he didn’t earn an extra cent, he still knew that he had done what the Lord wanted him to do.

<a name="p25"></a>Through the Prophet Joseph Smith, the Lord revealed the scripture which we have already heard from Elder Banks this evening—“that the thing which will be of the most worth unto you will be to declare repentance unto this people, that you may bring souls unto me.” ([D&C 15:6](https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/15.6?lang=eng#p6); [D&C 16:6](https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/16.6?lang=eng#p6).)

<a name="p26"></a>Over the years we have been so impressed by the thousands of missionaries we have seen at the Missionary Training Center, at Ricks College, and elsewhere, who have demonstrated their willingness to serve their missions—and some of them, at great personal sacrifice.

<a name="p27"></a>Brethren, may it be that in our lives generally, and in our priesthood responsibilities specifically, we, like David, my good friend, will set the kind of example so that our bishops will not have to wonder or worry about what we have been doing the Saturday night before.

<a name="p28"></a>I am grateful for sons who still come with me to general priesthood sessions. You young brethren who are not with your fathers tonight, for whatever reason, can decide right now that when you are blessed with sons of your own, you will bring them to the general priesthood sessions wherever they may be broadcast.

<a name="p29"></a>As I look up into the balcony tonight, I see some of you young men who are seated with your fathers, and I remember—I remember that first time so long ago. Dad passed away four years ago, and especially at general priesthood session time I am reminded more forcefully of how much we miss him. May we strive never to do anything that would embarrass or disappoint our Father in Heaven or our parents, and it will help make more of our memories to be good ones, because good memories constitute the “one Garden of Eden out of which we need never be cast.”

<a name="p30"></a>Young brethren, we respect you. We have confidence that you will rise to the best that is in you, and we love you.

<a name="p31"></a>Our Heavenly Father lives. He also loves you and even knows you by name. Jesus is the Christ, and this is His church, led by the living prophets who are presiding at this general priesthood session. I share this testimony in the holy name of Jesus Christ, amen.

"""


def check_text(markdown_content: str) -> Any:
    # result check variable boolean
    result_check = []
    markdown_content = clean_text(markdown_content)

    # Search for the position of "abstract" (case insensitive)
    text_match = re.search(r'<a name="p(\d+)"><\/a>', markdown_content, re.IGNORECASE)

    if text_match:
        # Check content after the "text" text
        result_check.append("True")

    return result_check


def test_review_conference() -> None:
    """It returns a valid Document."""
    result = check_text(mark_text)

    assert len(result) == 0
    assert "True" not in result
