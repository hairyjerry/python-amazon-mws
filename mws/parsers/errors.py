from base import first_element, BaseResponseMixin, BaseElementWrapper


class ErrorResponse(ValueError, BaseElementWrapper, BaseResponseMixin):

    def __init__(self, element):
        BaseElementWrapper.__init__(self, element)
        ValueError.__init__(self, self.message)

    @property
    @first_element
    def type(self):
        return self.element.xpath('//Error/Type/text()')

    @property
    @first_element
    def code(self):
        return self.element.xpath('//ErrorResponse/Error/Code/text()')

    @property
    @first_element
    def message(self):
        return self.element.xpath('//ErrorResponse/Error/Message/text()')

    @property
    @first_element
    def request_id(self):
        return self.element.xpath('//ErrorResponse/RequestID/text()')
