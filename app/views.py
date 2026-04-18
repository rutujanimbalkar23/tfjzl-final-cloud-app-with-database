from django.shortcuts import render, redirect
from .models import Question, Choice, Submission


# -----------------------------
# Submit Exam View
# -----------------------------
def submit_exam(request):
    if request.method == "POST":
        score = 0

        # Loop through all questions
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(str(question.id))

            if selected_choice_id:
                try:
                    choice = Choice.objects.get(id=selected_choice_id)

                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        # Save submission result
        Submission.objects.create(score=score)

        # Redirect to result page
        return redirect('show_exam_result', score=score)

    # GET request → show exam page
    questions = Question.objects.all()
    return render(request, 'exam.html', {'questions': questions})


# -----------------------------
# Show Exam Result View
# -----------------------------
def show_exam_result(request, score):
    total_questions = Question.objects.count()

    return render(request, 'result.html', {
        'score': score,
        'total': total_questions
    })