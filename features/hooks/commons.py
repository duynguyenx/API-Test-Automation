from hamcrest import assert_that, has_entries
import json
from jsonpath_rw import *


class Commons(object):
    @staticmethod
    def create_payload_from_template(original_payload, **kwargs):
        payload = original_payload
        for k, v in kwargs.iteritems():
            if k in payload:
                original_payload[k] = v
            else:
                raise KeyError("The key " + k + "does not exist in the original payload template " + original_payload)

        return payload

    @staticmethod
    def get_path(match):
        '''return an iterator based upon MATCH.PATH. Each item is a path component,
        start from outer most item.'''
        if match.context is not None:
            for path_element in Commons.get_path(match.context):
                yield path_element
            yield str(match.path)

    @staticmethod
    def update_json(json, path, value):
        '''Update JSON dictionnary PATH with VALUE. Return updated JSON'''
        try:
            first = next(path)
            # check if item is an array
            if first.startswith('[') and first.endswith(']'):
                try:
                    first = int(first[1:-1])
                except ValueError:
                    pass
            json[first] = Commons.update_json(json[first], path, value)
            return json
        except StopIteration:
            return value

    @staticmethod
    def modify_json_by_path(json_to_modify, explicit_json_paths):
        new_json = ''
        default_value = 'DEFAULTED'
        for k in explicit_json_paths:
            path = parse(k)
            matches = path.find(json_to_modify)

            for match in matches:
                new_json = Commons.update_json(json_to_modify, Commons.get_path(match), default_value)

        return new_json

    @staticmethod
    def assert_without_dynamic_fields(expected_response_from_constant, actual_response, explicit_json_paths):
        expected_response_modified = Commons.modify_json_by_path(json.loads(expected_response_from_constant),
                                                                 explicit_json_paths)
        actual_response_modified = Commons.modify_json_by_path(actual_response, explicit_json_paths)
        assert_that(expected_response_modified, has_entries(actual_response_modified))

    @staticmethod
    def get_casted_value(value):
        if "[integer]" in value:
            value = int(value[:value.index('[integer]')])
            return value
        elif "[float]" in value:
            value = float(value[:value.index('[float]')])
            return value
        else:
            return value


