from django.shortcuts import render, redirect
from .models import questions, questionnaire

def home(request):
    if request.method == 'POST':
        
        # q1
        if request.POST['q1'] == "yes":
            q1 = questions.objects.get(name='q1')
            q1.yes += 1
            q1.save()
        else:
            q1 = questions.objects.get(name='q1')
            q1.no += 1
            q1.save()

        # q2
        if request.POST['q2'] == "yes":
            q2 = questions.objects.get(name='q2')
            q2.yes += 1
            q2.save()
        else:
            q2 = questions.objects.get(name='q2')
            q2.no += 1
            q2.save()

        # q3
        if request.POST['q3'] == "yes":
            q3 = questions.objects.get(name='q3')
            q3.yes += 1
            q3.save()
        else:
            q3 = questions.objects.get(name='q3')
            q3.no += 1
            q3.save()

        # q4
        if request.POST['q4'] == "yes":
            q4 = questions.objects.get(name='q4')
            q4.yes += 1
            q4.save()
        else:
            q4 = questions.objects.get(name='q4')
            q4.no += 1
            q4.save()

        # q5
        if request.POST['q5'] == "yes":
            q5 = questions.objects.get(name='q5')
            q5.yes += 1
            q5.save()
        else:
            q5 = questions.objects.get(name='q5')
            q5.no += 1
            q5.save()

        # q6
        if request.POST['q6'] == "yes":
            q6 = questions.objects.get(name='q6')
            q6.yes += 1
            q6.save()
        else:
            q6 = questions.objects.get(name='q6')
            q6.no += 1
            q6.save()

        # q7
        if request.POST['q7'] == "yes":
            q7 = questions.objects.get(name='q7')
            q7.yes += 1
            q7.save()
        else:
            q7 = questions.objects.get(name='q7')
            q7.no += 1
            q7.save()

        # q8
        if request.POST['q8'] == "yes":
            q8 = questions.objects.get(name='q8')
            q8.yes += 1
            q8.save()
        else:
            q8 = questions.objects.get(name='q8')
            q8.no += 1
            q8.save()
        
        # # q9
        if request.POST['q9'] == "husband":
            q9 = questions.objects.get(name='q9')
            q9.husband += 1
            q9.save()
        elif request.POST['q9'] == "parents":
            q9 = questions.objects.get(name='q9')
            q9.parents += 1
            q9.save()
        elif request.POST['q9'] == "others":
            q9 = questions.objects.get(name='q9')
            q9.others += 1
            q9.save()
        else:
            q9 = questions.objects.get(name='q9')
            q9.one += 1
            q9.save()

        # q10
        if request.POST['q10'] == "father":
            q10 = questions.objects.get(name='q10')
            q10.father += 1
            q10.save()
        elif request.POST['q10'] == "husband":
            q10 = questions.objects.get(name='q10')
            q10.husband += 1
            q10.save()
        elif request.POST['q10'] == "others":
            q10 = questions.objects.get(name='q10')
            q10.others += 1
            q10.save()
        else:
            q10 = questions.objects.get(name='q10')
            q10.one += 1
            q10.save()

        # q11
        if request.POST['q11'] == "physical":
            q11 = questions.objects.get(name='q11')
            q11.physical += 1
            q11.save()
        elif request.POST['q11'] == "psychologically":
            q11 = questions.objects.get(name='q11')
            q11.psychologically += 1
            q11.save()
        elif request.POST['q11'] == "both":
            q11 = questions.objects.get(name='q11')
            q11.both += 1
            q11.save()
        else:
            q11 = questions.objects.get(name='q11')
            q11.violated += 1
            q11.save()

        # q12
        if request.POST['q12'] == "answer1":
            q12 = questions.objects.get(name='q12')
            q12.answer1 += 1
            q12.save()
        elif request.POST['q12'] == "answer2":
            q12 = questions.objects.get(name='q12')
            q12.answer2 += 1
            q12.save()
        elif request.POST['q12'] == "answer3":
            q12 = questions.objects.get(name='q12')
            q12.answer3 += 1
            q12.save()
        else:
            q12 = questions.objects.get(name='q12')
            q12.answer4 += 1
            q12.save()

        # q13
        if request.POST['q13'] == "city":
            q13 = questions.objects.get(name='q13')
            q13.city += 1
            q13.save()
        else:
            q13 = questions.objects.get(name='q13')
            q13.countryside += 1
            q13.save()

        # q14
        if request.POST['q14'] == "single":
            q14 = questions.objects.get(name='q14')
            q14.single += 1
            q14.save()
        elif request.POST['q14'] == "married":
            q14 = questions.objects.get(name='q14')
            q14.married += 1
            q14.save()
        elif request.POST['q14'] == "divorced":
            q14 = questions.objects.get(name='q14')
            q14.divorced += 1
            q14.save()
        else:
            q14 = questions.objects.get(name='q14')
            q14.widow += 1
            q14.save()

        # q15
        if request.POST['q15'] == "illiterate":
            q15 = questions.objects.get(name='q15')
            q15.illiterate += 1
            q15.save()
        elif request.POST['q15'] == "read":
            q15 = questions.objects.get(name='q15')
            q15.read += 1
            q15.save()
        elif request.POST['q15'] == "middle":
            q15 = questions.objects.get(name='q15')
            q15.middle += 1
            q15.save()
        else:
            q15 = questions.objects.get(name='q15')
            q15.high += 1
            q15.save()

        # q16
        if request.POST['q16'] == "educated":
            q16 = questions.objects.get(name='q16')
            q16.educated += 1
            q16.save()
        else:
            q16 = questions.objects.get(name='q16')
            q16.uneducated += 1
            q16.save()

        # q17
        if request.POST['q17'] == "zerotothree":
            q17 = questions.objects.get(name='q17')
            q17.zerotothree += 1
            q17.save()
        elif request.POST['q17'] == "threetofive":
            q17 = questions.objects.get(name='q17')
            q17.threetofive += 1
            q17.save()
        elif request.POST['q17'] == "fivetoseven":
            q17 = questions.objects.get(name='q17')
            q17.fivetoseven += 1
            q17.save()
        else:
            q17 = questions.objects.get(name='q17')
            q17.morethan += 1
            q17.save()

        # q18
        if request.POST['q18'] == "physicalviolence":
            q18 = questions.objects.get(name='q18')
            q18.physicalviolence += 1
            q18.save()
        elif request.POST['q18'] == "psychologicalviolence":
            q18 = questions.objects.get(name='q18')
            q18.psychologicalviolence += 1
            q18.save()
        elif request.POST['q18'] == "verbalviolence":
            q18 = questions.objects.get(name='q18')
            q18.verbalviolence += 1
            q18.save()
        else:
            q18 = questions.objects.get(name='q18')
            q18.otherviolence += 1
            q18.save()

        submited = questionnaire.objects.get(submit_num="first")
        submited.counter += 1
        submited.save()
        return redirect('blog-result')
    return render(request, 'blog/home.html')


def result(request):
    submited = questionnaire.objects.get(submit_num="first")
    if submited.counter == 0:
        submited.counter = 1
    # 4
    
    # q1
    q1 = questions.objects.get(name='q1')
    result1_yes = round( (q1.yes / submited.counter ) * 100, 1)
    result1_no = round( (q1.no / submited.counter ) * 100, 1)
    
    # q2
    q2 = questions.objects.get(name='q2')
    result2_yes = round( (q2.yes / submited.counter ) * 100, 1)
    result2_no = round( (q2.no / submited.counter ) * 100, 1)

    # q3
    q3 = questions.objects.get(name='q3')
    result3_yes = round( (q3.yes / submited.counter ) * 100, 1)
    result3_no = round( (q3.no / submited.counter ) * 100, 1)

    # q4
    q4 = questions.objects.get(name='q4')
    result4_yes = round( (q4.yes / submited.counter ) * 100, 1)
    result4_no = round( (q4.no / submited.counter ) * 100, 1)

    # q5
    q5 = questions.objects.get(name='q5')
    result5_yes = round( (q5.yes / submited.counter ) * 100, 1)
    result5_no = round( (q5.no / submited.counter ) * 100, 1)

    # q6
    q6 = questions.objects.get(name='q6')
    result6_yes = round( (q6.yes / submited.counter ) * 100, 1)
    result6_no = round( (q6.no / submited.counter ) * 100, 1)

    # q7
    q7 = questions.objects.get(name='q7')
    result7_yes = round( (q7.yes / submited.counter ) * 100, 1)
    result7_no = round( (q7.no / submited.counter ) * 100, 1)

    # q8
    q8 = questions.objects.get(name='q8')
    result8_yes = round( (q8.yes / submited.counter ) * 100, 1)
    result8_no = round( (q8.no / submited.counter ) * 100, 1)

    # q9
    q9 = questions.objects.get(name='q9')
    result9_husband = round( (q9.husband / submited.counter ) * 100, 1)
    result9_parents = round( (q9.parents / submited.counter ) * 100, 1)
    result9_others = round( (q9.others / submited.counter ) * 100, 1)
    result9_one = round( (q9.one / submited.counter ) * 100, 1)

    # q10
    q10 = questions.objects.get(name='q10')
    result10_father = round( (q10.father / submited.counter ) * 100, 1)
    result10_husband = round( (q10.husband / submited.counter ) * 100, 1)
    result10_others = round( (q10.others / submited.counter ) * 100, 1)
    result10_one = round( (q10.one / submited.counter ) * 100, 1)

    # q11
    q11 = questions.objects.get(name='q11')
    result11_physical = round( (q11.physical / submited.counter ) * 100, 1)
    result11_psychologically = round( (q11.psychologically / submited.counter ) * 100, 1)
    result11_both = round( (q11.both / submited.counter ) * 100, 1)
    result11_violated = round( (q11.violated / submited.counter ) * 100, 1)

    # q12
    q12 = questions.objects.get(name='q12')
    result12_answer1 = round( (q12.answer1 / submited.counter ) * 100, 1)
    result12_answer2 = round( (q12.answer2 / submited.counter ) * 100, 1)
    result12_answer3 = round( (q12.answer3 / submited.counter ) * 100, 1)
    result12_answer4 = round( (q12.answer4 / submited.counter ) * 100, 1)

    # q13
    q13 = questions.objects.get(name='q13')
    result13_city = round( (q13.city / submited.counter ) * 100, 1)
    result13_countryside = round( (q13.countryside / submited.counter ) * 100, 1)
    
    # q14
    q14 = questions.objects.get(name='q14')
    result14_single = round( (q14.single / submited.counter ) * 100, 1)
    result14_married = round( (q14.married / submited.counter ) * 100, 1)
    result14_divorced = round( (q14.divorced / submited.counter ) * 100, 1)
    result14_widow = round( (q14.widow / submited.counter ) * 100, 1)

    # q15
    q15 = questions.objects.get(name='q15')
    result15_illiterate = round( (q15.illiterate / submited.counter ) * 100, 1)
    result15_read = round( (q15.read / submited.counter ) * 100, 1)
    result15_middle = round( (q15.middle / submited.counter ) * 100, 1)
    result15_high = round( (q15.high / submited.counter ) * 100, 1)

    # q16
    q16 = questions.objects.get(name='q16')
    result16_educated = round( (q16.educated / submited.counter ) * 100, 1)
    result16_uneducated = round( (q16.uneducated / submited.counter ) * 100, 1)
    
    # q17
    q17 = questions.objects.get(name='q17')
    result17_zerotothree = round( (q17.zerotothree / submited.counter ) * 100,1)
    result17_threetofive = round( (q17.threetofive / submited.counter ) * 100,1)
    result17_fivetoseven = round( (q17.fivetoseven / submited.counter ) * 100,1)
    result17_morethan = round( (q17.morethan / submited.counter ) * 100,1)
    
    # q18
    q18 = questions.objects.get(name='q18')
    result18_physicalviolence = round( (q18.physicalviolence / submited.counter ) * 100, 1)
    result18_psychologicalviolence = round( (q18.psychologicalviolence / submited.counter ) * 100, 1)
    result18_verbalviolence = round( (q18.verbalviolence / submited.counter ) * 100, 1)
    result18_otherviolence = round( (q18.otherviolence / submited.counter ) * 100, 1)


    results = {
    'result1_yes': result1_yes,
    'result1_no': result1_no,

    'result2_yes': result2_yes,
    'result2_no': result2_no,
    
    'result3_yes': result3_yes,
    'result3_no': result3_no,

    'result4_yes': result4_yes,
    'result4_no': result4_no,

    'result5_yes': result5_yes,
    'result5_no': result5_no,

    'result6_yes': result6_yes,
    'result6_no': result6_no,

    'result7_yes': result7_yes,
    'result7_no': result7_no,

    'result8_yes': result8_yes,
    'result8_no': result8_no,

    'result9_husband': result9_husband,
    'result9_parents': result9_parents,
    'result9_others': result9_others,
    'result9_one': result9_one,

    'result10_father': result10_father,
    'result10_husband': result10_husband,
    'result10_others': result10_others,
    'result10_one': result10_one,

    'result11_physical': result11_physical,
    'result11_psychologically': result11_psychologically,
    'result11_both': result11_both,
    'result11_violated': result11_violated,

    'result12_answer1': result12_answer1,
    'result12_answer2': result12_answer2,
    'result12_answer3': result12_answer3,
    'result12_answer4': result12_answer4,

    'result13_city': result13_city,
    'result13_countryside': result13_countryside,
    
    'result14_single': result14_single,
    'result14_married': result14_married,
    'result14_divorced': result14_divorced,
    'result14_widow': result14_widow,

    'result15_illiterate': result15_illiterate,
    'result15_read': result15_read,
    'result15_middle': result15_middle,
    'result15_high': result15_high,

    'result16_educated': result16_educated,
    'result16_uneducated': result16_uneducated,

    'result17_zerotothree': result17_zerotothree,
    'result17_threetofive': result17_threetofive,
    'result17_fivetoseven': result17_fivetoseven,
    'result17_morethan': result17_morethan,

    'result18_physicalviolence': result18_physicalviolence,
    'result18_psychologicalviolence': result18_psychologicalviolence,
    'result18_verbalviolence': result18_verbalviolence,
    'result18_otherviolence': result18_otherviolence,
}
    return render(request, 'blog/result.html', results)




def information(request):
    
    return render(request, 'blog/information.html')

    