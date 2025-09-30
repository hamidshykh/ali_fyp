import spacy
from rake_nltk import Rake
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pdfminer import high_level
import docx2txt
import re

#from .tools import toWordCloud
from .models import Candidate
from .models import Job
import threading
import os
debug = False
nlp = spacy.load("en_core_web_sm")


def toLower(s):
    return s.lower()


def parse_through_spacy(text, asList=False):
    doc = nlp(text)
    to_list = [ent.text for ent in doc.ents]
    to_list = list(map(toLower, to_list))
    if debug:
        print(to_list)
    return to_list if asList else " ".join(to_list)


def parse_through_rake(text, asList=False):
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    keyword_extracted = list(map(toLower, keyword_extracted))
    if debug:
        print(keyword_extracted)
    return keyword_extracted if asList else " ".join(keyword_extracted)


def resume_to_text(path):
    if path.endswith('.pdf'):
        return high_level.extract_text(path)
    elif path.endswith('.docx'):
        return docx2txt.process(path)
    else:
        return ""


def clean_text(text):
    regex = re.compile('[^a-zA-Z]')
    return ' '.join(regex.sub(' ', text).split())


def calculate_simi(resume, description):
    text = [resume, description]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    if debug:
        print("\nSimilarity Scores:")
        print(cosine_similarity(count_matrix))
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2)  # round to two decimal
    if debug:
        print("Your resume matches about " + str(matchPercentage) + "% of the job description.")
    return matchPercentage


def calculate_simi_by_cross(resume_text, des):
    aa = [words for segments in parse_through_spacy(resume_text, True) for words in segments.split()]
    bb = [words for segments in parse_through_spacy(des, True) for words in segments.split()]

    total_score = len(bb)
    obtained = 0
    for word in aa:
        if word in bb:
            obtained = obtained + 1

    cc = [words for segments in parse_through_rake(resume_text, True) for words in segments.split()]
    dd = [words for segments in parse_through_rake(des, True) for words in segments.split()]

    total_score2 = len(dd)
    obtained2 = 0
    for word in cc:
        if word in dd:
            obtained2 = obtained2 + 1

    per1 = (obtained / total_score) * 100
    per2 = (obtained2 / total_score2) * 100
    return (per1 + per2) / 2


class JobApplicationsProfiler(threading.Thread):
    def __init__(self, candidate):
        super().__init__()
        self.candidate = candidate

    def createJobProfile(self):
        resumePath = self.candidate.resumePath
        des = self.candidate.appliedFor.description
        resume_text = clean_text(resume_to_text(resumePath.path))
        des = clean_text(des)

        resume_data_by_spacy = parse_through_spacy(resume_text)
        des_data_by_spacy = parse_through_spacy(des)
        resume_data_by_rake = parse_through_rake(resume_text)
        des_data_by_rake = parse_through_rake(des)

        score1 = calculate_simi(resume_data_by_spacy, des_data_by_spacy)
        score2 = calculate_simi(resume_data_by_rake, des_data_by_rake)

        final_score_cosine = (score1 + score2) / 2
        final_score_cross = calculate_simi_by_cross(resume_text, des)
        final_score = (final_score_cosine + final_score_cross) / 2
        if debug:
            print(round(final_score, 2))

        #wcPath = r"system\templates\des_wc\{}.png".format(self.candidate.id)
        #data = "{} {}".format(resume_data_by_spacy, des_data_by_rake)  # change
        #toWordCloud(data, wcPath)
        #self.candidate.wcPath = wcPath
        return final_score

    def save_as_job_application(self, score):
        self.candidate.resumeMatched = round(score, 2)
        self.candidate.save()
        return

    def run(self):
        score = self.createJobProfile()
        self.save_as_job_application(score)
        return
