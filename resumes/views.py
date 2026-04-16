from utils.parser import extract_text_from_pdf
from utils.skills import extract_skills
from utils.scoring import calculate_ats_score
from utils.matching import calculate_similarity

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import render
from .models import Resume
from .serializers import ResumeSerializer


# ---------------- API VIEW ---------------- #
class UploadResumeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        return Response({"message": "Upload your resume using POST"})

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            resume = serializer.save()

            # Extract text
            text = extract_text_from_pdf(resume.file.path)
            resume.extracted_text = text
            resume.save()

            # Extract skills
            skills = extract_skills(text)

            # ATS Score
            score, missing = calculate_ats_score(skills)

            # Job Description
            job_desc = request.data.get("job_description", "")

            similarity = None
            if job_desc:
                similarity = calculate_similarity(text, job_desc)

            return Response({
                "message": "Resume analyzed successfully",
                "skills": skills,
                "score": score,
                "missing_skills": missing,
                "match_percentage": similarity,
                "text_preview": text[:200]
            })

        return Response(serializer.errors)


# ---------------- UI VIEW ---------------- #
def home(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        job_desc = request.POST.get('job_description', '')

        if file:
            resume = Resume.objects.create(file=file)

            # Extract text
            text = extract_text_from_pdf(resume.file.path)

            # Extract skills
            skills = extract_skills(text)

            # ATS score
            score, missing = calculate_ats_score(skills)

            # Job matching
            similarity = None
            if job_desc:
                similarity = calculate_similarity(text, job_desc)

            result = {
                "skills": skills,
                "score": score,
                "missing_skills": missing,
                "match_percentage": similarity
            }

            return render(request, 'index.html', {"result": result})

    return render(request, 'index.html')