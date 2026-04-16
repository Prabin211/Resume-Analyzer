from utils.parser import extract_text_from_pdf
from utils.skills import extract_skills
from utils.scoring import calculate_ats_score
from utils.matching import calculate_similarity

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import ResumeSerializer


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

            #Job Description
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