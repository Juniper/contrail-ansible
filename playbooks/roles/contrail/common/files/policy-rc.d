#!/bin/bash
if [ "${1}" = "--quiet" ]; then
  name="$2"
else
  name="$1"
fi
sensitive_services_list=/etc/sensitive_services
if [ -e $sensitive_services_list ]; then
    grep -x "$name" "$sensitive_services_list" && exit 101
fi
exit 0
