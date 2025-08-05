from django.http import HttpResponse
from rest_framework.decorators import api_view

from ..core.decorators.deserialize_decorator import deserialize
from ..core.decorators.multi_method_decorator import multi_methods
from ..dtos.requests.sample_request_dtos import SampleRequestDto
from ..dtos.responses.sample_response_dto import SampleResponseDto
from ..exceptions.request_exceptions import MissingFieldError
from ..exceptions.type_exceptions import NotDtoClassError
from ..responses.dto_response import DtoResponse
from ..responses.error_response import ErrorResponse


# /hello GET
def pong(request) -> HttpResponse:
    try:
        response = SampleResponseDto('Hello, Django!')
        return DtoResponse.response(response, 200)
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
        return DtoResponse.response(response, 201)
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
