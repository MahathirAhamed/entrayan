from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import (
                                          require_GET,
                                          require_POST,
                                          require_http_methods
                                         )
from django.http import (
                         JsonResponse
                        )
from django.template import Context
import logging
import json
from jsonschema import (
                        validate,
                        ValidationError,
                        FormatChecker
                       )
from schema import CREATE_COURSE_SCHEMA


from models import (
                   CourseInfo,
                   SubscriberInfo,
                   AlertInfo,
                   User
                   )

logger = logging.getLogger('custom')
logger.setLevel(logging.INFO)

@staff_member_required
@require_http_methods(['GET', 'POST'])
@csrf_exempt
def subscribe_courses(request):
    logger.info('requested course details page') 
    try:
        if request.method == 'GET':
            courses = []
            course_details = CourseInfo.objects.filter().all()
            if course_details:
                courses = [model_to_dict(course) for course in course_details]
                return render_to_response('coursedetails.html', {"courses":courses},
                        context_instance=RequestContext(request))
        if request.method == 'POST':
            logger.info('called subscribe_course function') 
            course_ids = json.loads(request.body.decode('utf-8')).get('course_ids', [])
            user = User.objects.get(pk=request.user.id)
            for crse_id in course_ids:
                course_info = CourseInfo.objects.filter(pk=int(crse_id)).first().as_dict()
                if course_info:
                    subcriber_info = {'course_subscribed':course_info.get('course_name'),
                            'course':course_info.get('course_id'),
                            'subscriber':user,
                            'course_date':course_info.get('course_date')
                            }
                    sub_info = SubscriberInfo(**subcriber_info)
                    sub_info.save()
            return JsonResponse({"message":'Data Saved'},status=200)
    except Exception as e:
        return JsonResponse({"message": e}, status=500)

@staff_member_required
@require_http_methods(['GET', 'POST'])
@csrf_exempt
def create_course(request):
    try:
        if request.method == 'GET':
            return render_to_response('createcourse.html',{},context_instance=RequestContext(request))
        if request.method == 'POST':
            json_body = json.loads(request.body.decode('utf-8'))
            validate(json_body, CREATE_COURSE_SCHEMA, format_checker=FormatChecker())
            user = User.objects.get(username=json_body['author_name'].lower())
            json_body['author'] = user
            course_info = CourseInfo(**json_body)
            course_info.save()
            return JsonResponse({"message":'Data Saved'},status=200)
    except ValidationError as e:
        return JsonResponse({"message": e.message}, status=400)
    except Exception as e:
        return JsonResponse({"message": e}, status=500)
