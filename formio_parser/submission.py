# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import json

from builder import Builder


class Submission:

    def __init__(self, submission_json, builder=None, builder_schema_json=None, lang='en'):
        """
        @param submission
        @param builder Builder
        @param builder_schema
        """
        self.submission = json.loads(submission_json)
        
        self.builder = builder
        self.builder_schema_json = builder_schema_json
        self.lang = lang

        if self.builder and self.builder_schema_json:
            raise Exception("Constructor accepts either builder or builder_schema_json.")

        if self.builder:
            assert isinstance(self.builder, Builder)
        elif self.builder_schema_json:
            assert isinstance(self.builder_schema_json, str)
        else:
            raise Exception("Provide either the argument: builder or builder_schema_json.")

        if self.builder is None and self.builder_schema_json:
            self.set_builder_by_builder_schema_json()

        self.components = {}
        self.init_components()

    def set_builder_by_builder_schema_json(self):
        self.builder = Builder(self.builder_schema_json, self.lang)

    def init_components(self):
        for key, component in self.builder.components.items():
            # Rather lazy check, but sane.
            if not self.submission.get(key):
                continue
            
            component_submission = self.submission.get(key)

            # Instantiate the compoent class
            component_class = globals()[component.__class__.__name__]
            component_obj = component_class(self.builder, component_submission)

            if component_obj is not None:
                component_obj.init_submission_attrs(component_submission)
                self.components[key] = component_obj


# class SubmissionStore:
#
#     def __init__(self, submission):
#         self._submission = submission
#
#     def _getattr__(self, key):
#         if self._submission.builder.components.get(key):
#             return self._submission.component.get(key)
#         else:
#             return None