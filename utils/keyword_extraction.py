import spacy
import re
import pytextrank
from keybert import KeyBERT
from cleaning import preprocess_text, load_stopwords
import yake

jd_text = """
 We are looking for an experienced Software Developer to join our client's fast-growing technology company. The ideal candidate will have a strong background in creating web applications with Python and using AWS tools. You will be responsible for building and maintaining the backend and frontend of our applications and systems.
Responsibilities:

    Design and develop API's using Redshift
    Build and maintain scalable, high-performance systems
    Collaborate with cross-functional teams to design and launch new features
    Debug and optimize applications to ensure they are running smoothly
    Write clean, maintainable, and efficient code
    Stay up-to-date with new technologies and methodologies

Requirements:

    Strong experience with web development, with Python
    Experience on AWS cloud and using AWS tools is a PLUS
    Excellent problem-solving and analytical skills
    Comfortable working in a fast-paced, high-pressure environment
    Excellent communication skills, both written and verbal
    No ego, and comfortable working in a team-oriented environment

"""
tt_jd_text = """
Software Engineer Intern - TikTok Growth - 2025 Summer (BS/MS)
San Jose
Intern
R&D
Undergraduate/Master Intern- 2025 Start
Job ID: A109683
Responsibilities
TikTok is the leading destination for short-form mobile video. At TikTok, our mission is to inspire creativity and bring joy. TikTok's global headquarters are in Los Angeles and Singapore, and its offices include New York, London, Dublin, Paris, Berlin, Dubai, Jakarta, Seoul, and Tokyo. 

Why Join Us
Creation is the core of TikTok's purpose. Our platform is built to help imaginations thrive. This is doubly true of the teams that make TikTok possible. 
Together, we inspire creativity and bring joy - a mission we all believe in and aim towards achieving every day. 
To us, every challenge, no matter how difficult, is an opportunity; to learn, to innovate, and to grow as one team. Status quo? Never. Courage? Always. 
At TikTok, we create together and grow together. That's how we drive impact - for ourselves, our company, and the communities we serve. 
Join us.

Millions of users install TikTok every day. At the User Growth engineering team, we deliver business impact by optimizing the new users' experience since they install the app, and help users of various backgrounds and intentions to find their "Aha!" moment on the platform. Our engineering team drives high-visibility end to end impact by touching various parts of the product, including onboarding experience, video playback experience, Algorithm of For You Feed. 

We are looking for talented individuals to join us for an internship in 2025. Internships at TikTok aim to offer students industry exposure and hands-on experience. Turn your ambitions into reality as your inspiration brings infinite opportunities at TikTok.

Internships at TikTok aim to provide students with hands-on experience in developing fundamental skills and exploring potential career paths. A vibrant blend of social events and enriching development workshops will be available for you to explore. Here, you will utilize your knowledge in real-world scenarios while laying a strong foundation for personal and professional growth. This Internship Program runs for 12 weeks beginning in May/June 2025. Successful candidates must be able to commit to one of the following summer internship start dates below: 
Monday, May 12
Monday, May 19
Tuesday May 27 (Memorial Day May 26)
Monday, June 9
Monday, June 23

We will prioritize candidates who are able to commit to these start dates. Please state your availability clearly in your resume (Start date, End date).

Candidates can apply to a maximum of two positions and will be considered for jobs in the order you apply. The application limit is applicable to TikTok and its affiliates' jobs globally. Applications will be reviewed on a rolling basis - we encourage you to apply early.

Online Assessment
Candidates who pass resume evaluation will be invited to participate in TikTok's technical online assessment in HackerRank.

Responsibilities:
• Build new features that touch hundreds of millions of people around the world.
• Solve unique, large-scale, highly complex technical problems.
• Participate in technical discussions related to team's product and engineering work.
Qualifications
Minimum Qualifications
- Currently pursuing an Undergraduate/Graduate/Master in Software Development, Computer Science, Computer Engineering or a related technical discipline
- Able to commit to working for 12 weeks during Summer 2025;
- computer science, statistics, or other relevant, machine-learning-heavy majors.
- Experience with Python, Java, Golang, C#, or C++.
- Experience in either mobile development or backend development
- Must obtain work authorization in country of employment at the time of hire, and maintain ongoing work authorization during employment.


Preferred Qualifications 
- Graduating December 2025 onwards with the intent to return to degree program after the completion of the internship.
- Passionate about TikTok, augmented reality, as well as creating the most fun, original and creative ideas and experiences.
- Demonstrated software engineering experience from previous internship, work experience, coding competitions, or publications.
- High levels of creativity and quick problem-solving capabilities

TikTok is committed to creating an inclusive space where employees are valued for their skills, experiences, and unique perspectives. Our platform connects people from across the globe and so does our workplace. At TikTok, our mission is to inspire creativity and bring joy. To achieve that goal, we are committed to celebrating our diverse voices and to creating an environment that reflects the many communities we reach. We are passionate about this and hope you are too.

TikTok is committed to providing reasonable accommodations in our recruitment processes for candidates with disabilities, pregnancy, sincerely held religious beliefs or other reasons protected by applicable laws. If you need assistance or a reasonable accommodation, please reach out to us at https://shorturl.at/cdpT2
Job Information
【For Pay Transparency】Compensation Description Intern (hourly)

The hourly rate range for this position in the selected city is $45- $60. We cover 100% premium coverage for Full-Time intern medical insurance after 90 days from the date of hire. Medical coverage only, no dental or vision coverage.​

Our time off and leave plans are: Paid holidays and paid sick leave. The sick leave entitlement is based on the time you join.​

We also provide mental and emotional health benefits through our Employee Assistance Program and provide reimbursements for your mobile phone expense. The Company reserves the right to modify or change these benefits programs at any time, with or without notice.​

"""

op_jd_text = """
As our Quantitative Trading Intern, you’ll spend your summer in the heart of Optiver’s dynamic trading floor in Amsterdam. Under the guidance and support of industry experts, you’ll collaborate on complex problems that have real-world impact on the financial markets.

From derivative theory training to hands-on trading experience, you’ll have deepened your understanding of the quantitative trading industry by the end of the 8-week internship. Plus, if you’ve excelled over the summer, you could receive an offer to return as a Graduate Quantitative Trader in our Singapore Office. 

What you’ll do

Requiring quick thinking, a critical mindset and bold action, our internship is as close as you can get to real trading experience. Led by our in-house education team that consists of ex-traders and engineers, the comprehensive training program offers you the opportunity to:

    Deep dive into trading fundamentals, from theoretical concepts to financial markets, strategies and cutting-edge technology.
    Apply your knowledge in a simulated trading environment, honing your skills with hands-on practice.
    Learn directly from an experienced trader, gaining exposure to various trading desks and experience the financial markets first-hand.
    Push your limits and accelerate your growth in a fascinating and high-performing environment.

Read Sean’s story as he shares his experience in the internship program.

What you’ll get

You’ll join a culture of collaboration and excellence, where you’ll be surrounded by curious thinkers and creative problem solvers. Driven by a passion for continuous improvement, you’ll thrive in a supportive, high-performing environment alongside talented colleagues, working collectively to tackle the toughest problems in the financial markets.

In addition, you’ll receive:

    A highly competitive remuneration package
    Optiver-covered flights and accommodations for the duration of the internship
    Training, mentoring and personal development opportunities
    Daily breakfast and lunch
    Regular social events
    Opportunity to receive a return offer as a Graduate Quantitative Trader in our Singapore Office

Who you are

    Penultimate or pre-penultimate university student, with a graduation date of December 2025 to June 2027
    Lateral thinker, with a passion for quantitative problems and working in collaborative, dynamic environments
    Holds superior quantitative and logical reasoning skills
    Interested in strategic games and/or competitive activities
    Experienced in programming or scripting in Python a plus
    May have an interest in trading or financial markets
    We encourage Singapore nationals to apply

Diversity statement

As an intentionally flat organisation, we believe that great ideas and impact can come from everyone. We are passionate about empowering individuals and creating diverse teams that thrive. Every person at Optiver should feel included, valued and respected, because we believe our best work is done together.

Our commitment to diversity and inclusion is hardwired through every stage of our hiring process. We encourage applications from candidates from any and all backgrounds, and we welcome requests for reasonable adjustments during the process to ensure that you can best demonstrate your abilities.
"""

course_info = """
Bioelectronics This is the second course in the series covering bioelectrical phenomena and systems. In this course the focus is electronics for biomedical applications, and the objective is to discuss electrical systems pertaining to the human body.
"""

def yake_extract_keywords(text, max_keywords=10):
    # Define YAKE keyword extractor
    processed_text = preprocess_text(text)
    kw_extractor = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, top=max_keywords, features=None)
    
    # Extract keywords
    keywords = kw_extractor.extract_keywords(processed_text)
    
    return [keyword for keyword, score in keywords]


def bert_extract_keywords(text, model="all-MiniLM-L6-v2", top_n=10, ngram_range=(1,1)):
    # Define KeyBERT keyword extractor
    kw_extractor = KeyBERT(model=model)
    
    # Extract keywords
    keywords = kw_extractor.extract_keywords(text, keyphrase_ngram_range=ngram_range, stop_words=load_stopwords(), top_n=top_n)
    
    return keywords

def spacy_extract_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('textrank')
    doc = nlp(text)
    keywords = [(p.text, p.rank) for p in doc._.phrases]
    return keywords

# Extract keywords using YAKE
yake_keywords = yake_extract_keywords(course_info, max_keywords=10)
print("YAKE Keywords:", yake_keywords)
bert_keywords = bert_extract_keywords(course_info, top_n=10)
print("KeyBERT Keywords:", bert_keywords)
spacy_keywords = spacy_extract_keywords(course_info)
print("Spacy Keywords:", spacy_keywords)