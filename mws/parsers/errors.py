from base import first_element, BaseResponseMixin, BaseElementWrapper


class ErrorResponse(ValueError, BaseElementWrapper, BaseResponseMixin):

    namespaces = {
        'a': 'http://mws.amazonservices.com/schema/Products/2011-10-01'
    }

    def __init__(self, element):
        BaseElementWrapper.__init__(self, element)
        ValueError.__init__(self, self.message)

    @property
    @first_element
    def type(self):
        return self.element.xpath('//a:ErrorResponse/a:Error/a:Type/text()', namespaces=self.namespaces)

    @property
    @first_element
    def code(self):
        return self.element.xpath('//a:ErrorResponse/a:Error/a:Code/text()', namespaces=self.namespaces)

    @property
    @first_element
    def message(self):
        return self.element.xpath('//a:ErrorResponse/a:Error/a:Message/text()', namespaces=self.namespaces)

    @property
    @first_element
    def request_id(self):
        return self.element.xpath('//a:ErrorResponse/a:RequestID/text()', namespaces=self.namespaces)
