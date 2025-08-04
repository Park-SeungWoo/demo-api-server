# /hello GET
from django.http import HttpResponse
from rest_framework.decorators import api_view

from main_app_name.core.decorators.deserialize_decorator import deserialize
from main_app_name.core.decorators.multi_method_decorator import multi_methods
from main_app_name.dtos.request_dtos.sample_request_dtos import SampleRequestDto
from main_app_name.dtos.resopnse_dtos.sample_response_dto import SampleResponseDto
from main_app_name.exceptions.request_exceptions import MissingFieldError
from main_app_name.exceptions.type_exceptions import NotDtoClassError
from main_app_name.responses.dto_response import DtoResponse
from main_app_name.responses.error_response import ErrorResponse


def pong(request) -> HttpResponse:
    try:
        response = SampleResponseDto('Hello, Django!')
        return DtoResponse.response(response)
    except MissingFieldError as e:
        return ErrorResponse.response(e, 400)
    except NotDtoClassError as e:
        return ErrorResponse.response(e, 500)
    except Exception as e:
        return ErrorResponse.response(e, 500)

@deserialize
def pingpong(request, ping: SampleRequestDto) -> HttpResponse:
    try:
        response = SampleResponseDto(f'Hello, {ping.ping}')
        return DtoResponse.response(response)
    except MissingFieldError as e:
        return ErrorResponse.response(e, 400)
    except NotDtoClassError as e:
        return ErrorResponse.response(e, 500)
    except Exception as e:
        return ErrorResponse.response(e, 500)


@api_view(['GET', 'POST'])
@multi_methods(GET=pong, POST=pingpong)
def pingpong_multi_method_acceptor():
    pass