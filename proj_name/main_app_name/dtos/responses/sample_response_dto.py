from main_app_name.dtos.abstract_dto import Dto


class SampleResponseDto(Dto):
    def __init__(self, pong: str):
        self.pong: str = pong