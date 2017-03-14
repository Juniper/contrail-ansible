# inidata is used to manage ini
#
# Example usage
# - name: configure contrailctl configuration
#  ini_file:
#    dest: /etc/xyz.conf     # an ini file
#    section: "{{ item.section }}"
#    option: "{{ item.option }}"
#    value: "{{ item.value }}"
#    backup: yes
#    create: yes
#  with_inidata:
#    DEFAULTS:
#        opt1: val1
#        opt2: val2
#        opt3: val3
#    SECT1:
#        sec_opt1: val1
#        sec_opt2: val2
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
import ansible.errors as errors


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        if not isinstance(terms, dict):
            raise errors.AnsibleError("inidata lookup expects dictionary , got '%s'" %terms)
        ret = []
        for item0 in terms:
            if not isinstance(terms[item0], dict):
                raise errors.AnsibleError("inidata lookup expects a dictionary, got '%s'" %terms[item0])
            for item1 in terms[item0]:
                ret.append({'section': item0, 'option': item1, 'value': terms[item0][item1]})
        return ret
